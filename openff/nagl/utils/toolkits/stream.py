from typing import Optional

__all__ = [
    "Streamer",
]


class Streamer:
    def __init__(
        self,
        filename: str,
        file_format: Optional[str] = None,
        zipped: Optional[bool] = None,
    ):
        if file_format is None:
            file_format = self.get_file_format(filename)

        self.filename = filename
        self.file_format = file_format

    @staticmethod
    def get_file_format(file: str):
        if file.endswith("sdf") or file.endswith("sdf.gz"):
            file_format = "sdf"
        elif file.endswith("smi") or file.endswith("smiles"):
            file_format = "smi"
        else:
            raise NotImplementedError(f"Do not recognize format of {file}")
        return file_format

    def to_file():
        ...

    def from_file(as_smiles: bool = True, unsafe: bool = False):
        ...
