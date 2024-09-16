from models.cliente import Cliente, Clientes
from models.agiota import Agiota, Agiotas
from models.cobrador import Cobrador, Cobradores
#from models.emprestimo import Emprestimo, Emprestimos
#from models.parcela import Parcela, Parcelas

class View:
    #CLIENTE
    @staticmethod
    def cliente_inserir(nome, celular, endereco):
        c = Cliente(0, nome, celular, endereco)
        Clientes.inserir(c)
    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_atualizar(id, nome, celular, endereco):
        c = Cliente(id, nome, celular, endereco)
        Clientes.atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

    #AGIOTA
    @staticmethod
    def inserir_agiota(nome, celular, endereco, credito):
        a = Agiota(0, nome, celular, endereco, credito)
        Agiotas.inserir(a)
    
    

        
