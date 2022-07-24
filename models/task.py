from typing import Any, Dict, List, Tuple
from datetime import datetime
from typing_extensions import Self

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class Task:
    def __init__(
        self,
        name: str,
        parent: Self | None = None,
        children: List[Self] | None = None,
        time_frames: List[Tuple[datetime, datetime | None]] = None,
        isDone: bool = False,
    ) -> None:
        self.name = name
        self.parent: Task | None = parent
        self.children: List[Task] = children or []
        self.time_frames: List[Tuple[datetime, datetime | None]] = time_frames or []
        self.isDone: bool = isDone

    @property
    def to_py_obj(self) -> Dict[str, Any]:
        data = self.__dict__.copy()
        data.update(
            {
                "time_frames": [
                    (
                        i.strftime(DATETIME_FORMAT),
                        j.strftime(DATETIME_FORMAT) if j else None,
                    )
                    for i, j in self.time_frames
                ],
                "children": [i.to_py_obj for i in self.children],
            }
        )
        return data

    @classmethod
    def from_py_obj(cls, data: Dict[str, Any]) -> Self:
        data.update(
            {
                "time_frames": [
                    (
                        datetime.strptime(i, DATETIME_FORMAT),
                        datetime.strptime(j, DATETIME_FORMAT) if j else None,
                    )
                    for i, j in data["time_frames"]
                ],
                "children": [cls.from_py_obj(i) for i in data["children"]],
            }
        )
        return cls(**data)

    def tree_str(self):
        return f"{'🗹' if self.isDone else '☐'} {self.name}"