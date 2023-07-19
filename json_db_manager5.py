import os
import json
from pathlib import Path


class ContexManager:

    def __init__(self, filename, mode="r+"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.__file = open(self.filename, self.mode)
        # self.__file.read()
        global json_data
        json_data = JsonData(self.__file, json.load(self.__file))
        # self.__file.write("")
        return json_data

    def __exit__(self, exc_type, exc_value, exc_traceback):
        json.dump(json_data.data, json_data.file, indent=0)
        if not self.__file.closed:
            self.__file.close()


class JsonData:

    def __init__(self, file, data):
        self.file = file
        self.data = data

    def get_data(self):
        return self.file

    def set_obj(self, id_obj, content_obj):
        if id_obj not in self.data:
            self.data[id_obj] = content_obj
        else:
            print("Объект уже существует")
        return self.data

    def read_obj(self, id_obj):
        return self.data[id_obj]

    def update_obj(self, id_obj, content_obj):
        if id_obj in self.data:
            self.data[id_obj] = content_obj
        else:
            print("Объекта не существует")
        return self.data

    def del_obj(self, id_obj):
        if id_obj in self.data:
            del self.data[id_obj]
        else:
            print("Объекта не существует")
        return self.data


with ContexManager("json_db.json") as f:
    # print(f.read_obj("test2"))
    f.set_obj("sobaka", 123)