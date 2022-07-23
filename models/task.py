from typing import Any, Dict, List, Tuple
from datetime import datetime
from typing_extensions import Self

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

class Task:
    def __init__(
        self,
        name: str,
        parent: Self,
        children: List[Self],
        time_frames=None,
        isDone=False,
    ) -> None:
        self.name = name
        self.parent: Task | None = parent
        self.children: List[Task] = children
        self.time_frames: List[Tuple[datetime, datetime | None]] = time_frames or []
        self.isDone=isDone

    @property
    def to_json_dict(self) -> Dict[str, Any]:
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
                "children": [i.to_json_dict for i in self.children]
            }
        )
        return data

    @classmethod
    def from_json_dict(cls, data: Dict[str, Any]) -> Self:
        data.update(
            {
                "time_frames": [
                    (
                        datetime.strptime(i, DATETIME_FORMAT),
                        datetime.strptime(j, DATETIME_FORMAT) if j else None,
                    )
                    for i, j in data["time_frames"]
                ],
                "children": [cls.from_json_dict(i) for i in data["children"]]
            }
        )
        return cls(**data)
