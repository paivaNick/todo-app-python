from rich import print
from rich.console import Console
from rich.table import Table
import json
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("ID")
table.add_column("Titulo")
table.add_column("Data", style="dim", width=12)
table.add_column("Status", style="dim", width=12)
table.add_column("Description")

class Todo():

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, *tasks):
        for task in tasks:
            self.tasks.append(task._body)
        print('[bold magenta]task adicionada[bold magenta]')

    def list_tasks(self):
        for indice, task in enumerate(self.tasks):
            task["id"] = indice
            table.add_row(str(task["id"]), task["name"], str(task["date"]),
                          str(task["status"]), task["desc"])

        console.print(table)

    def remove_task(self, id):
        for indice, task in enumerate(self.tasks):
            print(indice, task)
            if indice == id:
                self.tasks.pop(id)

    def gravar_json(self):
        with open(".data_file.json", "w") as write_file:
            json.dump(self.tasks, write_file)









