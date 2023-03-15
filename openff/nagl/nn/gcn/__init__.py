"Architectures for convolutional layers"

from ._base import BaseGCNStack
from ._sage import SAGEConvStack
from ._gin import GINConvStack


__all__ = ["BaseGCNStack", "SAGEConvStack", "GINConvStack"]

# TODO: eventually migrate out DGL?
