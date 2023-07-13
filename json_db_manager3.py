import os
import json


class ContexManager:
    json_id = 0

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if not self.__file.closed:
            self.__file.close()

    def creat_obj(self, id_obj, data):
        with ContexManager(self.filename, "r") as f:
            json_data = json.load(f)
            if id_obj not in json_data:
                json_data[id_obj] = data
            else:
                print("Объект уже существует")
        with ContexManager(self.filename, "w") as f:
            json.dump(json_data, f)

    def read(self, id_obj):
        with ContexManager(self.filename, "r") as f:
            json_data = json.load(f)
            data = json_data[id_obj]
            return data

    def update(self, id_obj, data):
        with ContexManager(self.filename, "r") as f:
            json_data = json.load(f)
            if id_obj in json_data:
                json_data[id_obj] = data
            else:
                print("Объекта не существует")
        with ContexManager(self.filename, "w") as out_f:
            json.dump(json_data, out_f)

    def delete_obj(self, id_obj):
        with ContexManager(self.filename, "r") as f:
            json_data = json.load(f)
            del json_data[id_obj]
        with ContexManager(self.filename, "w") as f:
            json.dump(json_data, f)


if not os.path.isfile("json_db.json"):
    with ContexManager("json_db.json", "w") as f:
        f.write(json.dumps({}))

file = ContexManager("json_db.json", "w")
# file.creat_obj("text1", 123)
# file.read("text2")
# file.update("text2", 666)
# file.delete_obj("text2")
