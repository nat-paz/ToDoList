from dao import *
class ToDo():
    def adicionarTarefa(self, tarefa):
        add = DaoAdicionarTarefa()
        return add.adicionar(tarefa)

    # def excluirTarefa(self, excluir):
    #     self.lista.pop(excluir)
    #     return True

    def listarTarefas(self):
        listar = DaoListarTarefa()
        return listar.listar()

todo = ToDo()