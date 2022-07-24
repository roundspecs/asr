import json
import os
from typing import List
from models.task import Task


DB_DIR = "db"

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
        return cls(*data)
    
    @classmethod
    def from_json_file(cls):
        with open(cls.filepath, "r") as file:
            data = json.load(file)
        return cls.from_py_obj(data)
    
    def save(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.to_py_obj, file)
    
    def add_task_as_emmet(self, emmet_abbr: str):
        #TODO
        pass