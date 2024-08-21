import os, json, argparse
from datetime import datetime


class manage_task:
    def __init__(self, file_path, file_name, status, command):
        self.file_path = file_path
        self.file_name = file_name
        self.complete_path = f"{file_path}{file_name}"
        self.status = status
        self.counter = 0
        self.command = command

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
        data.append(current_data)
        self.write(data)
        print(
            f"✅ Task add with ID: {current_data['id']} || Text: {current_data['description']}"
        )

    def delete(self, task_id: int) -> None:
        data = self.read()
        clean_list = [item for item in data if item["id"] != int(task_id)]
        self.write(clean_list)
        print(f"✅ Task deleted ID: {task_id}")

    # TODO: Create a update method
    def update(self, task_id: int, update_value: str) -> None:
        data = self.read()
        for item in data:
            if int(item["id"]) == int(task_id):
                item["description"] = update_value
                item["updatedAt"] = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        self.write(data)
        print(f"✅ Task updated to ID: {task_id} || Text: {update_value}")

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

    def shootgun_cli(self) -> None:
        match self.command.command:
            case "add":
                self.create(self.command.text)
            case "update":
                self.update(self.command.task_id, self.command.task_text_updated)
            case "delete":
                self.delete(self.command.task_id)
            case "mark-todo":
                self.change_status(self.command.task_id, self.status[1])
            case "mark-in-progress":
                self.change_status(self.command.task_id, self.status[1])
            case "mark-done":
                self.change_status(self.command.task_id, self.status[2])
            case "list":
                self.list_tasks()


def arg_setup():

    # setup to recibe arguments
    parser = argparse.ArgumentParser(description="This is a CLI to manage your tasks.")

    sub_parser = parser.add_subparsers(
        dest="command", help="List of commands aviable to use."
    )

    # crating the commands
    #  add   task command
    add_parser = sub_parser.add_parser(
        "add",
        help="Command for add a task, pass a str with this command. ex. add 'this is a text'",
    )
    add_parser.add_argument("text", default="", help="Text to update")

    #  update task command
    update_parser = sub_parser.add_parser(
        "update",
        help="Command for update a task, pass a str with this command. ex. add 'this is a text'",
    )
    update_parser.add_argument("task_id", default="", help="Id to update")
    update_parser.add_argument(
        "task_text_updated", default="", help="Text to update the task"
    )
    #  delete task command
    delete_parser = sub_parser.add_parser(
        "delete",
        help="Command for delete a task",
    )
    delete_parser.add_argument("task_id", default="", help="Id to delete")

    #  mark_in_progress task command
    mark_in_progress_parser = sub_parser.add_parser(
        "mark-in-progress",
        help="Command for mark-in-progress a task",
    )
    mark_in_progress_parser.add_argument(
        "task_id", default="", help="Id to mark-in-progress"
    )

    #  mark_done task command
    mark_done = sub_parser.add_parser(
        "mark-done",
        help="Command for mark-done a task",
    )
    mark_done.add_argument("task_id", default="", help="Id to mark-done")

    #  mark_todo task command
    mark_todo = sub_parser.add_parser(
        "mark-todo",
        help="Command for mark-todo a task",
    )
    mark_todo.add_argument("task_id", default="", help="Id to mark-todo")

    # list tasks by status command
    list_parser = sub_parser.add_parser(
        "list",
        help="Command to list tasks by status",
    )
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["done", "todo", "in-progress"],
        help="Status of tasks to list",
    )

    return parser.parse_args()


def main():
    command = arg_setup()
    file_path = "./"
    file_name = "data.json"
    status = ["TODO", "IN-PROGRESS", "DONE"]
    data = manage_task(file_path, file_name, status, command)
    data.validate_file()
    data.shootgun_cli()

    # initialize the data

    # TODO: We only accept existing commands
    # Shootgun commands
    # data.shootgun_cli()

    # data.find_by_status(status[0])
    # data.update(3, "Complete Tor Ragnarok")

    # data.change_status(3, status[2])

    # data.list_tasks()
    # data.create("Complete The Lengend of Zelda: Ocarina of time")
    # data.create("Complete The Lengend of Zelda: Majoras Mask")
    # data.create("Complete The Lengend of Zelda: Minish Cap")

    # conditional action
    transfer_data = {"id": 0, "text": ""}


if __name__ == "__main__":
    main()
