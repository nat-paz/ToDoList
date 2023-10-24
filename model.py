from dao import *
class ToDo():
    def adicionarTarefa(self, tarefa ,x):
        add = DaoAdicionarTarefa(tarefa)
        return add.adicionar(x)

    # def excluirTarefa(self, excluir):
    #     self.lista.pop(excluir)
    #     return True

    def listarTarefas(self):
        listar = DaoListarTarefa()
        return listar.listar()

todo = ToDo()