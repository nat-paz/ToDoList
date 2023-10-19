from controller import *
import os

sair = 0
while sair == 0:

    print("Software de To-Do List")
    print("[1] Adicionar tarefa \n[2] Listar tarefas \n[3] Excluir tarefa \n[4] Sair")
    menu = input("Informe a opção desejada: ")
    os.system("pause")
    os.system("cls")

    match menu:
        case "1":
            tarefa = input("Qual tarefa você deseja adicionar: ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")
        
        case "2":
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")
            
        case "3":
            listarTarefa = ControllerListarTarefa()
            excluir = input("Qual o indice da tarefa você deseja excluir: ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")

        case "4":
            break

        case _:
            print("Opção invalida")
