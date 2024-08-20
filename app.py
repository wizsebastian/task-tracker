import os, json, argparse
from datetime import datetime


class JsonAction:
    def __init__(self, obj, file_name):
        self.data = obj
        self.file_name = file_name

    def read(self):
        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def write(self, data):
        current_data = self.read()
        current_data.append(data)
        with open(self.file_name, "w", encoding="UTF-8") as file:
            json.dump(current_data, file, indent=4)
        print("Task added")

    # def delete(self, item_id):
    #     current_data = self.read()
    #     current_data.find()

    def search_by(self, search_type, val) -> list:
        current_data = self.read()
        # selected_item
        selected_item = [item for item in current_data if item[search_type] == val]
        return selected_item


class manage_task:
    def __init__(self, file_path, file_name, status):
        self.file_path = file_path
        self.file_name = file_name
        self.complete_path = f"{file_path}{file_name}"
        self.status = status
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
        print("date", datetime.today())
        data = []
        print("data", data)
        with open(self.file_name, "w") as json_file:
            json.dump(data, json_file, indent=4)
            print(f"File was created with name: {self.file_name}")

    def read(self):
        with open(self.file_name, "r") as file:
            data = json.load(file)
        return data

    def write(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
            print("READY")

    # def add(self, text):
    #     data = self.read()
    #     new_item = {
    #         "id": self.counter + 1,
    #         "description": text,
    #         "status": self.status[0],
    #         "createdAt": str(datetime.today()),
    #         "updatedAt": str(
    #             datetime.today(),
    #         ),
    #     }
    #     # data.append(new_item)
    #     self.write(data)

    def find_by_status(self, status):
        data = self.read()
        current_search = [
            item for item in data if item["status"].lower() == status.lower()
        ]
        print(f"Task with status: {status}")
        print(current_search)

    def create(self, text) -> None:
        data = self.read()
        current_data = {
            "id": len(data) + 1,
            "description": text,
            "status": self.status[0],
            "createdAt": datetime.now().strftime("%y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.now().strftime("%y-%m-%d %H:%M:%S"),
        }
        print(data)
        data.append(current_data)
        self.write(data)
        print(f"✅ Task add with ID: {data}")

    def delete(self, task_id: int) -> None:
        data = self.read()
        clean_list = [item for item in data if item["id"] != task_id]
        self.write(clean_list)

    # TODO: Create a update method
    def update(self, task_id: int, update_value: str) -> None:
        data = self.read()
        # item_to_update =
        for item in data:
            if item["id"] == task_id:
                item["description"] = update_value
                item["updatedAt"] = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        print(data)
        self.write(data)

    def change_status(self, task_id, status_updated) -> None:
        list_task = self.read()
        for item in list_task:
            if item["id"] == task_id:
                item["status"] = status_updated
        self.write(list_task)

    def list_tasks(self):
        list_task = self.read()
        print("Your tasks list:")
        for task in list_task:
            print(
                f"ID: {task['id']} || NAME: {task['description']} || STATUS: {task['status']} "
            )


def main():
    file_path = "./"
    file_name = "data.json"
    status = ["TODO", "IN-PROGRESS", "DONE"]

    # setup to recibe arguments
    # parser = argparse.ArgumentParser(description="Task tracker...")
    # parser.add_argument("command", help="The command to run")
    # parser.add_argument("--optional", type=str, help="This is an optional argument.")
    # arg = parser.parse_args()

    # initialize the data
    data = manage_task(file_path, file_name, status)
    data.validate_file()

    data.find_by_status(status[0])
    # data.update(3, "Complete Tor Ragnarok")

    # data.change_status(3, status[2])

    # data.list_tasks()
    # data.create("Complete The Lengend of Zelda: Ocarina of time")
    # data.create("Complete The Lengend of Zelda: Majoras Mask")
    # data.create("Complete The Lengend of Zelda: Minish Cap")

    # conditional action
    # match arg.command:
    #     case "list":
    #         print("rosiut")
    #     case "create":
    #         print("case 2, crearte")

    # print("Works...", arg.command)
    return
    # data.add("Primera vez")


if __name__ == "__main__":
    main()
