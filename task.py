from typing import List


class Task:
    def __init__(self, parent, children: List) -> None:
        self.parent: Task = parent
        self.children: List[Task] = children
