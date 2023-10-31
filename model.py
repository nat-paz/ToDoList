from dao import *
class ToDo():
    def adicionarTarefa(self, tarefa ,x):
        add = DaoAdicionarTarefa(tarefa)
        return add.adicionar(x)


    def listarTarefas(self):
        listar = DaoListarTarefa()
        return listar.listar()
    
    def alterarTarefa(self, tarefa_A, nova_tarefa):
        alterar = DaoAlterar()
        return alterar.alterarTarefa(tarefa_A, nova_tarefa)
    
    def ConcluirExcluirTarefa(self, statusA, statusN):
        daoconcluirexcluir = DAO_ConcluirExcluirTarefa()
        return daoconcluirexcluir.ConcluirExcluirTarefa(statusA, statusN)

todo = ToDo()