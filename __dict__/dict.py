#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return '[{}] ({}) <{}>'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.created_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        for key, value in obj_dict.items():
            print(f"Key is '{key}' value is: {value}")
        # print(obj_dict)


newModel = BaseModel()
# newModel.to_dict()
print(newModel.__str__())
