from modules.Task import Task
from modules.Todo import Todo

__version__ = "0.0.1"
__author__ = "nicolas paiva"
__license__ = "Unlicense"

todo = Todo("dia")
task1 = Task("limpar a casa", "obrigaçao")
task2 = Task("assistir o curso", "prioridade" )
task3 = Task("dormir")
task4 = Task("estudar CLI")
task5 = Task("teste", )
todo.add_task(task1, task2, task3, task4, task5)
todo.remove_task(2)
todo.gravar_json()

todo.list_tasks()
