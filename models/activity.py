import datetime
from typing import List
from typing_extensions import Self


class Activity:
    def __init__(self, name: str, time_spent: datetime.timedelta) -> None:
        self.name = name
        self.time_spent = time_spent

    @property
    def to_py_obj(self) -> List[str | int]:
        return [self.name, self.time_spent.total_seconds()]

    @classmethod
    def from_py_obj(cls, data: List[str | int]) -> Self:
        return cls(*data)
