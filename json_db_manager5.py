import json
from pathlib import Path
from typing import Optional, Any


class JsonDataLoader:
    def __init__(self, filename: str) -> None:
        self.filename = Path(filename)
        self.data: dict[str, Any] | None = None

    def __enter__(self) -> dict[str, Any]:
        if not self.filename.exists():
            self.filename.touch()
            self.data = {}
            return self.data

        with open(self.filename, 'r') as f:
            data = f.read()
            self.data = json.loads(data if len(data) > 0 else '{}')
            return self.data

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.data))


class DataRepository:
    def __init__(self, loader: Optional[JsonDataLoader] = None):
        if loader is None:
            self.loader = JsonDataLoader("database.json")
        else:
            self.loader = loader

    def create(self, id_obj: int, content_obj: dict, override: bool = False) -> None:
        with self.loader as data:
            if id_obj in data and not override:
                print("Объект уже существует")
                return
            data[str(id_obj)] = content_obj

    def get(self, id_obj: int) -> dict | None:
        with self.loader as data:
            return data.get(str(id_obj), None)

    def update(self, id_obj: int, content_obj: dict) -> None:
        with self.loader as data:
            if str(id_obj) not in data:
                print("Объекта не существует")
                return

            data[str(id_obj)] = content_obj

    def delete(self, id_obj: int) -> dict | None:
        with self.loader as data:
            if id_obj not in data:
                print("Объекта не существует")

            data = data.pop(str(id_obj))
            return data


def main():
    repo = DataRepository()

    repo.create(1, {"jopa": "jopa"})

    obj: dict[str, str] | None = repo.get(1)
    if obj is not None:
        print(f"Object :{obj}")
    obj["new_jopa"] = "new_jopa"
    repo.update(1, obj)
    if obj is not None:
        print(f"Object :{obj}")

    repo.delete(1)
    obj = repo.get(1)
    if obj is None:
        print("Object deleted!")


if __name__ == "__main__":
    main()
