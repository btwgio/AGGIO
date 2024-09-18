from models.cliente import Cliente, Clientes
from models.agiota import Agiota, Agiotas
from models.cobrador import Cobrador, Cobradores
from models.emprestimo import Emprestimo, Emprestimos
from models.parcela import Parcela, Parcelas

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
    
    @staticmethod
    def listar_agiota():
        return Agiotas.listar()
    
    @staticmethod
    def atualizar_agiota(id, nome, celular, endereco, credito):
        c = Agiota(id, nome, celular, endereco, credito)
        Agiotas.atualizar(c)
    @staticmethod
    def excluir_agiota(id):
        c = (id, "", "", "","")
        Agiotas.excluir(c)
    
    #COBRADOR
    @staticmethod
    def inserir_cobrador(nome, celular, endereco, placa):
        a = Cobrador(0, nome, celular, endereco, placa)
        Cobradores.inserir(a)
    
    @staticmethod
    def listar_cobrador():
        return Cobradores.listar()
    
    @staticmethod
    def atualizar_Cobrador(id, nome, celular, endereco, placa):
        c = Cobrador(id, nome, celular, endereco, placa)
        Cobradores.atualizar(c)

    @staticmethod
    def excluir_cobrador(id):
        c = (id, "", "", "","")
        Cobradores.excluir(c)
    
    #EMPRESTIMO
    @staticmethod
    def inserir_emprestimo(valor, data, duracao, juros):
        a = Emprestimo(0, valor, data, duracao, juros)
        Emprestimos.inserir(a)
    
    @staticmethod
    def listar_emprestimo():
        return Emprestimos.listar()
    
    @staticmethod
    def atualizar_emprestimo(id, valor, data, duracao, juros):
        c = Emprestimo(id, valor, data, duracao, juros)
        Emprestimos.atualizar(c)
        
    @staticmethod
    def excluir_emprestimo(id):
        c = (id, "", "", "","")
        Emprestimos.excluir(c)
    
    #PARCELA
    @staticmethod
    def inserir_parcela(data_vencimento, valor):
        a = Parcela(0, data_vencimento, valor)
        Parcelas.inserir(a)
    
    @staticmethod
    def listar_parcela():
        return Parcelas.listar()
    
    @staticmethod
    def atualizar_parcela(data_vencimento, valor):
        c = Parcela(id, data_vencimento, valor)
        Parcelas.atualizar(c)
        
    @staticmethod
    def excluir_parcela(id):
        c = (id, "", "")
        Parcelas.excluir(c)
    
    
    

        
