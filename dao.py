from random import *

Arquivo = "ToDo.txt"


class DaoAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def adicionar(self, x):
        with open(Arquivo, "a") as arquivo:
            tarefa_formatada = f"{x}\t{self.tarefa}"
            
            with open(Arquivo, "r") as arquivo:
                ler = arquivo.read()

            with open(Arquivo, "a") as arquivo:
                if "ID: \tTarefa:" not in ler:
                    arquivo.write(f"ID: \tTarefa:\n")
                arquivo.write(f"{tarefa_formatada}\n")
                return True


class DaoListarTarefa():
    def listar(self):
        with open(Arquivo,"r") as arquivo:
            linhas = arquivo.readlines()
        return linhas