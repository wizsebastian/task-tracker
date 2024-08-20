import os, json
from datetime import datetime


class manage_task:
    def __init__(self, file_path, file_name, status, default_data_structure):
        self.file_path = file_path
        self.file_name = file_name
        self.complete_path = f"{file_path}{file_name}"
        self.status = status
        self.structure = default_data_structure
        self.counter = 0

    def validate_file(self):
        file_is_valid = os.path.exists(self.complete_path)
        if not file_is_valid:
            print("file not exist")
            self.create_file()
        else:
            data = self.read()
            self.counter = len(data)
            print(self.counter)

    # TODO: I need to create a .json file
    def create_file(self):
        status = ["todo", "in-progress", "done"]
        print("date", datetime.today())
        data = {
            "id": 0,
            "description": "lorem",
            "status": self.status[0],
            "createdAt": "asd",
            "updatedAt": "updatedAt",
        }
        print("data", data)
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print(f"File was created with name: {self.file_name}")

    def read(self):
        with open(self.file_name, "r") as file:
            data = json.load(file)
        return data

    def write(self, data):
        print("on write", data)
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
            print("READY")

    def add(self, text):
        data = self.read()
        new_item = {
            "id": self.counter + 1,
            "description": text,
            "status": self.status[0],
            "createdAt": datetime.today(),
            "updatedAt": datetime.today(),
        }
        data.append(new_item)
        self.write(data)


def main():
    file_path = "./"
    file_name = "data.json"
    status = ["todo", "in-progress", "done"]
    default_data_structure = {
        "id": 0,
        "description": "lorem",
        "status": status[0],
        "createdAt": datetime.today(),
        "updatedAt": "updatedAt",
    }

    print("Works...")
    data = manage_task(file_path, file_name, status, default_data_structure)
    data.validate_file()
    data.add("Primera vez")


if __name__ == "__main__":
    main()
