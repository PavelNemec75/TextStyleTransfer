import pickle
from pathlib import Path
from typing import Any, Union


class Helpers:
    @classmethod
    def read_pickle_file(cls, path: Path) -> Any:  # noqa: ANN401
        with Path(path).open("rb") as f:
            return pickle.load(f)  # noqa: S301

    @classmethod
    def save_to_pickle_file(cls, path: Path, content: Union[str, list, dict, tuple]) -> None:  # noqa: UP007
        with Path(path).open("wb") as f:
            pickle.dump(content, f)
