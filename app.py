import os, json
from datetime import datetime


class manage_task:
    def __init__(self, file_path, file_name, status, default_data_structure):
        self.file_path = file_path
        self.file_name = file_name
        self.complete_path = f"{file_path}{file_name}"
        self.status = status
        self.structure = default_data_structure

    def validate_file(self):
        file_is_valid = os.path.exists(self.complete_path)
        if not file_is_valid:
            print("file not exist")
            self.create_file()

    # TODO: I need to create a .json file
    def create_file(self):
        status = ["todo", "in-progress", "done"]
        print("date", datetime.today())
        data = {
            "id": 0,
            "description": "lorem",
            "status": status[0],
            "createdAt": "asd",
            "updatedAt": "updatedAt",
        }
        print("data", data)
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print(f"File was created with name: {self.file_name} {json_obj}")


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


if __name__ == "__main__":
    main()
