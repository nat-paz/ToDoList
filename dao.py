from random import randint



Arquivo = "ToDo.txt"
ids = []

class DaoAdicionarTarefa():
    def adicionar(self, tarefa):
        self.id = randint(1000,9999)
        ids.append(self.id)
        with open(Arquivo, "a") as arquivo:
            id = randint(1000,9999)
            if id in ids:
                return False
            else:
                arquivo.write(f"{id}\t{tarefa}\n")
                return True


class DaoListarTarefa():
    def listar(self):
        with open(Arquivo,"r") as arquivo:
            linhas = arquivo.readlines()
        return linhas