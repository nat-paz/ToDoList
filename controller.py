from model import *
from random import*

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
            try:
                self.tarefa = tarefa
                id = randint(1000,9999)
                cont = -1
                if len(todo.listarTarefas()) > 1:
                    for tarefas in todo.listarTarefas():
                        cont += 1
                        if cont >= 1:
                            tarefas = tarefas.split()
                            tarefasId = int(tarefas[1])
                            if id != tarefasId:
                                if self.tarefa == "":
                                    print("Informe uma tarefa valida")
                                    break
                                else:
                                    if todo.adicionarTarefa(self.tarefa, id) == True:
                                        print("Tarefa adicionada.")
                                        break
                                    else:
                                        print("Algum problema foi encontrado.")
                                        break
                            else:
                                id = randint(1000,9999)
                else:
                    if self.tarefa == "":
                        print("Informe uma tarefa valida")
                    else:
                        if todo.adicionarTarefa(self.tarefa, id) == True:
                            print("Tarefa adicionada.")
                        else:
                            print("Algum problema foi encontrado.")
            except Exception:
                print("Valor invalido")

class ControllerListarTarefa():
    def __init__(self):
        cont = 0
        if len(todo.listarTarefas()) > 1:
            for tarefas in todo.listarTarefas():
                tarefas = tarefas.split()
                tarefasA = tarefas[0]
                if tarefasA == "A":
                    cont += 1
                    print(f"{cont} - {tarefas[2]}")


class ContollerAlterarTarefa():
    def __init__(self, indice, nova_tarefa):
        self.indice = indice
        self.nova_tarefa = nova_tarefa
        indices = {}
        indiceInt = int(indice)

        if nova_tarefa == "":
            print("Algo deu errado ao alterar a atrefa. Tente novamente.")

        else:
            cont = 0
            if len(todo.listarTarefas()) > 1:
                for tarefas in todo.listarTarefas():
                    tarefas = tarefas.split()
                    tarefasA = tarefas[0]
                    if tarefasA == "A":
                        cont += 1
                        indices[cont] = tarefas[2]

            for chave, valor in indices.items():
                if chave == indiceInt:
                    if todo.alterarTarefa(valor, nova_tarefa) == True:
                        print("Tarefa alterada com sucesso!")
                    else:
                        print("Algum problema foi encontrado. Tente novamente!")

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

