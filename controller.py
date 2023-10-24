from model import *
from random import*

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        l = 0
        while l == 0:
            try:
                self.tarefa = tarefa
                id = randint(1000,9999)
                cont = -1
                if len(todo.listarTarefas()) > 1:
                    for tarefas in todo.listarTarefas():
                        cont += 1
                        if cont >= 1:
                            tarefas = tarefas [:4]
                            tarefas = int(tarefas)
                            if id != tarefas:
                                if self.tarefa == "":
                                    print("Informe uma tarefa valida")
                                    l = 1
                                else:
                                    if todo.adicionarTarefa(self.tarefa, id) == True:
                                        print("Tarefa adicionada.")
                                        l = 1
                                    else:
                                        print("Algum problema foi encontrado.")
                                        l = 1
                            else:
                                id = randint(1000,9999)
                else:
                    if self.tarefa == "":
                        print("Informe uma tarefa valida")
                        l = 1
                    else:
                        if todo.adicionarTarefa(self.tarefa, id) == True:
                            print("Tarefa adicionada.")
                            l = 1
                        else:
                            print("Algum problema foi encontrado.")
                            l = 1
            except Exception:
                print("Valor invalido")
                l = 1

class ControllerListarTarefa():
    def __init__(self):
        cont = -1
        for tarefas in todo.listarTarefas():
            cont += 1
            if cont >= 1:
                tarefas = tarefas[5:-1]
                print(f"{cont} - {tarefas}")
                

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        n = 0
        while n == 0:
            try:
                x = int(excluir)
                self.excluir = x- 1
                
                if todo.excluirTarefa(self.excluir) == True:
                    print("Tarefa excluida.")
                    n = 1
                else:
                    print("Algum problema foi encontrado.")

            except Exception:
                print("Valor invalido")
                excluir = input("Qual o indice da tarefa você deseja excluir: ")

