import json


class ContexManager:

    def __init__(self, filename, mode="r+"):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.__file = open(self.filename, self.mode)
        json_data = JsonData(json.load(self.__file))
        return json_data

    def __exit__(self, exc_type, exc_value, exc_traceback):
        #json.dumps(JsonData.get_data())
        if not self.__file.closed:
            self.__file.close()


class JsonData:

    def __init__(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_obj(self, id_obj, content_obj):
        if id_obj not in self.data:
            self.data[id_obj] = content_obj
        else:
            print("Объект уже существует")

    def read_obj(self, id_obj):
        return self.data[id_obj]

    def update_obj(self, id_obj, content_obj):
        if id_obj in self.data:
            self.data[id_obj] = content_obj
        else:
            print("Объекта не существует")

    def del_obj(self, id_obj):
        if id_obj in self.data:
            del self.data[id_obj]
        else:
            print("Объекта не существует")


with ContexManager("json_db.json") as f:
    # f.read_obj("text2")
    f.set_obj("kot", "boris")
