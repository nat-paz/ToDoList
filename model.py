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
    
    def alterarTarefa(self, tarefa_A, nova_tarefa):
        alterar = DaoAlterar()
        return alterar.alterarTarefa(tarefa_A, nova_tarefa)

todo = ToDo()