from dao import *
class ToDo():
    def adicionarTarefa(self, tarefa ,x):
        add = DaoAdicionarTarefa(tarefa)
        return add.adicionar(x)


    def listarTarefas(self):
        listar = DaoListarTarefa()
        return listar.listar()
    
    def alterarTarefa(self, antigo, novo):
        alterar = DaoAlterar()
        return alterar.alterarTarefa(antigo, novo)
    
    def ConcluirExcluirTarefa(self, antigo, novo):
        daoconcluirexcluir = DaoAlterar()
        return daoconcluirexcluir.alterarTarefa(antigo, novo)

todo = ToDo()