import json
import os
from typing import List
from typing_extensions import Self
from models.task import Task


DB_DIR = "/home/seven89/Documents/asr-db"


class TaskList:
    filepath = os.path.join(DB_DIR, "tasks.json")

    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks

    @property
    def to_py_obj(self):
        return [t.to_py_obj for t in self.tasks]

    @classmethod
    def from_py_obj(cls, data: List):
        data = [Task.from_py_obj(d) for d in data]
        return cls(data)

    @classmethod
    def from_json_file(cls):
        if not os.path.exists(DB_DIR):
            os.makedirs(DB_DIR)
        if not os.path.exists(cls.filepath):
            with open(cls.filepath, "w") as file:
                json.dump([], file)
        with open(cls.filepath, "r") as file:
            data = json.load(file)
        return cls.from_py_obj(data)

    def save(self):
        with open(self.filepath, "w") as file:
            json.dump(self.to_py_obj, file, indent=2)

    def add_task_as_emmet(self, emmet_abbr: str) -> Self:
        self.tasks.append(Task(emmet_abbr))
        added_task_list = TaskList([Task(emmet_abbr)])
        self.save()
        return added_task_list

    def tree_str(self):
        return "\n".join([t.tree_str() for t in self.tasks])

    def remove_task_as_emmet(self, emmet_abbr: str) -> Self:
        self.tasks = [t for t in self.tasks if t.name != emmet_abbr]
        self.save()
        return TaskList([Task(emmet_abbr)])
