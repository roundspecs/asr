import datetime
from typing import List
from typing_extensions import Self

TIME_FORMAT = "%H:%M:%S"


class Activity:
    def __init__(self, name: str, start: datetime.time, end: datetime.time | None = None) -> None:
        self.name = name
        self.start = start
        self.end = end

    @property
    def to_py_obj(self) -> List[str | int]:
        data = self.__dict__.copy()
        data.update(
            {
                "start": self.start.strftime(TIME_FORMAT),
                "end": self.end.strftime(TIME_FORMAT) if self.end else None,
            }
        )

        return data

    @classmethod
    def from_py_obj(cls, data: List[str | int]) -> Self:
        data.update(
            {
                "start": datetime.datetime.strptime(data["start"], TIME_FORMAT).time(),
                "end": datetime.datetime.strptime(data["end"], TIME_FORMAT).time() if data["end"] else None,
            }
        )
        return cls(**data)
