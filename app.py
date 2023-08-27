from functools import wraps
from rich import print
from rich.console import Console
from rich.table import Table


class Task():

    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.status = False
        self._body = {
            "name": self.name,
            "date": self.date,
            "status": self.status
        }


console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Titulo")
table.add_column("Data", style="dim", width=12)
table.add_column("Status", style="dim", width=12)


class Todo():

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, *tasks):
        for task in tasks:
            print(task._body)
            self.tasks.append(task._body)
        print('[bold magenta]task adicionada[bold magenta]')

    def list_tasks(self):
        print(self.tasks)
        for task in self.tasks:
            print(task)
            table.add_row(task["name"], task["date"], str(task["status"]))

        console.print(table)


# def change_status(selfkkk)

todo = Todo("dia")
task1 = Task("limpar a casa", "2023-10-03")
task2 = Task("assistir o curso", "2023-08-26")
todo.add_task(task1, task2)
todo.list_tasks()
