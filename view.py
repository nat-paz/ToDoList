from controller import *
import os

sair = 0
while sair == 0:

    print("Software de To-Do List")
    print("[1] Adicionar tarefa \n[2] Listar tarefas\n[3] Alterar tarefa \n[4] Concluir tarefa \n[5] Listar tarefas concluidas \n[6] Excluir tarefa \n[7] Sair")
    menu = input("Informe a opção desejada: ")

    os.system("cls")

    match menu:
        case "1": 
            print ("Adicionar tarefas \n")     
            tarefa = input("Qual tarefa você deseja adicionar: ")
            adicionarTarefa = ControllerAdicionarTarefa(tarefa)
            os.system("pause")
            os.system("cls")
        
        case "2":
            print ("Listar tarefas \n")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")

        case "3":
            print ("Alterar tarefas \n")
            print("Essas são suas tarefas:")
            listarTarefa = ControllerListarTarefa()
            print("")
            indice = input("Qual o indice da tarefa que você deseja alterar: ")
            nova_tarefa = input("Qual será a nova tarefa: ")
            print("")
            alterar = ContollerAlterarTarefa(indice,nova_tarefa)
            listarTarefa = ControllerListarTarefa()
            os.system("pause")
            os.system("cls")

            
        case "4":
            os.system("cls")
            print ("Concluir tarefas \n")
            print ("Sua lista de tarefas:")
            listarTarefa = ControllerListarTarefa()
            print (" ")
            indiceAlt = input ("Qual a tarefa que deseja concluir? Adicione o índice: ")
            alterar = ControllerConcluirTarefa(indiceAlt)
            print(" ")
            listarTarefa = ControllerListarTarefa()
            print (" ")
            os.system("pause")

        case "5":
            os.system("cls")
            print ("Lista de tarefas concluídas:")
            listarTarefa = ControllerListarTarefaC()
            print (" ")
            os.system("pause")

        case "6":
            os.system("cls")
            print ("Excluir tarefas \n")
            print ("Lista de tarefas:")
            listarTarefa = ControllerListarTarefa()
            print(" ")
            excluir = input ("Qual o índice da tarefa que deseja excluir? ")
            excluirTarefa = ControllerExcluirTarefa(excluir)
            print(" ")
            print ("Lista de tarefas:")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")

        case "7":
            break

        case _:
            print("Opção invalida")
