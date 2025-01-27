from collections import defaultdict
from typing import List, Tuple, Iterable

import torch
import networkx as nx


def nonzero_1d(values):
    output = torch.nonzero(values, as_tuple=False).squeeze()
    if output.dim() == 1:
        return output
    return output.view(-1)


def as_numpy(val: torch.Tensor):
    return val.cpu().detach().numpy()


def _bucketing(val: torch.Tensor) -> Tuple[torch.Tensor, callable]:
    """Internal function to create groups on the values.

    Parameters
    ----------
    val : Tensor
        Value tensor.

    Returns
    -------
    unique_val : Tensor
        Unique values.
    bucketor : callable[Tensor -> list[Tensor]]
        A bucketing function that splits the given tensor data as the same
        way of how the :attr:`val` tensor is grouped.
    """
    sorted_values, sorted_indices_in_original = torch.sort(val)
    unique_values = as_numpy(torch.unique(sorted_values))
    bucket_indices = []
    for value in unique_values:
        value_indices = nonzero_1d(sorted_values == value).long()
        selected = torch.index_select(sorted_indices_in_original, 0, value_indices)
        bucket_indices.append(selected.long())

    def bucketor(data) -> List[torch.Tensor]:
        buckets = [torch.index_select(data, 0, idx) for idx in bucket_indices]

        return buckets

    return unique_values, bucketor


def _batch_nx_graphs(graphs):
    import torch
    import networkx as nx
    from openff.nagl.molecule._graph._batch import FrameDict

    if not len(graphs):
        raise ValueError("Cannot batch empty graphs")

    for graph in graphs:
        assert all(
            key in graph.graph for key in ["node_data", "graph_data", "edge_data"]
        )

    joined_graph = nx.disjoint_union_all(graphs)

    framedict_keys = ["node_data", "graph_data"]
    if isinstance(graphs[0].graph["edge_data"], FrameDict):
        framedict_keys.append("edge_data")
    else:
        new_edge_data = defaultdict(FrameDict)
        for edge_direction in graphs[0].graph["edge_data"].keys():
            for key in graphs[0].graph["edge_data"][edge_direction].keys():
                tensors = []
                for graph in graphs:
                    tensors.append(graph.graph["edge_data"][edge_direction][key])
                new_edge_data[edge_direction][key] = torch.cat(tensors, dim=0)
        joined_graph.graph["edge_data"] = new_edge_data

    for key in framedict_keys:
        joined_graph.graph[key] = FrameDict()
        for feature_key in graphs[0].graph[key].keys():
            tensors = []
            for graph in graphs:
                if feature_key not in graph.graph[key]:
                    raise ValueError(
                        f"Graphs are missing feature {feature_key} in {key}"
                    )
                tensors.append(graph.graph[key][feature_key])
            joined_graph.graph[key][feature_key] = torch.cat(tensors, dim=0)
    return joined_graph


def _unbatch_nx_graphs(
    graph: nx.Graph,
    n_representations_per_molecule: Iterable[int],
) -> List[nx.Graph]:
    import networkx as nx
    from openff.nagl.molecule._graph._batch import FrameDict

    unbatched_graphs = []
    start = 0
    for n_representations in n_representations_per_molecule:
        end = start + n_representations
        subgraph = nx.subgraph(graph, range(start, end))

        for data_name in ["node_data", "graph_data"]:
            if data_name in graph.graph:
                node_data = FrameDict()
                for k, v in graph.graph[data_name].items():
                    node_data[k] = v[start:end]
                subgraph.graph[data_name] = node_data

        if "edge_data" in graph.graph:
            old_edge_data = graph.graph["edge_data"]
            if isinstance(old_edge_data, defaultdict):
                edge_data = defaultdict(FrameDict)
                for direction in old_edge_data.keys():
                    for k, v in old_edge_data[direction].items():
                        edge_data[direction][k] = v[start:end]
            else:
                edge_data = FrameDict()
                for k, v in old_edge_data.items():
                    edge_data[k] = v[start:end]
            subgraph.graph["edge_data"] = edge_data

        unbatched_graphs.append(subgraph)
        start = end
    return unbatched_graphs