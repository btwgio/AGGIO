from models.cliente import Cliente, Clientes
from models.agiota import Agiota, Agiotas
from models.cobrador import Cobrador, Cobradores
from models.emprestimo import Emprestimo, Emprestimos
from models.parcela import Parcela, Parcelas
from datetime import datetime

class View:
    #CLIENTE
    @staticmethod
    def cliente_inserir(nome:str, celular:str, endereco:str, saldo:float):
        c = Cliente(0, nome, celular, endereco, saldo)
        Clientes.inserir(c)
    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_listar_id(id:int):
        return Clientes.listar_id(id)
    @staticmethod
    def cliente_atualizar(id:int, nome:str, celular:str, endereco:str, saldo:float):
        c = Cliente(id, nome, celular, endereco, saldo)
        Clientes.atualizar(c)
    @staticmethod
    def cliente_excluir(id:int):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    #AGIOTA
    @staticmethod
    def agiota_inserir(nome:str, celular:str, endereco:str, credito:float):
        a = Agiota(0, nome, celular, endereco, credito)
        Agiotas.inserir(a)
    @staticmethod
    def agiota_listar():
        return Agiotas.listar()
    @staticmethod
    def agiota_listar_id(id:int):
        return Agiotas.listar_id(id)
    @staticmethod
    def agiota_atualizar(id:int, nome:str, celular:str, endereco:str, credito:float):
        a = Agiota(id, nome, celular, endereco, credito)
        Agiotas.atualizar(a)
    @staticmethod
    def agiota_excluir(id:int):
        a = Agiota(id, "", "", "","")
        Agiotas.excluir(a)
    
    #COBRADOR
    @staticmethod
    def cobrador_inserir(nome:str, celular:str, endereco:str, placa:str, id_agiota:int):
        c = Cobrador(0, nome, celular, endereco, placa, id_agiota)
        Cobradores.inserir(c)
    @staticmethod
    def cobrador_listar():
        return Cobradores.listar()
    @staticmethod
    def cobrador_listar_id(id:int):
        return Cobradores.listar_id(id)
    @staticmethod
    def cobrador_atualizar(id:int, nome:str, celular:str, endereco:str, placa:str, id_agiota):
        c = Cobrador(id, nome, celular, endereco, placa, id_agiota)
        Cobradores.atualizar(c)
    @staticmethod
    def cobrador_excluir(id:int):
        c = Cobrador(id, "", "", "", "", "")
        Cobradores.excluir(c)
    
    #EMPRESTIMO
    @staticmethod
    def emprestimo_inserir(id_agiota, id_cliente, id_cobrador, valor, data, duracao, juros):
        e = Emprestimo(0, id_agiota, id_cliente, id_cobrador, True, False, False, False, valor, duracao, data, juros)
        Emprestimos.inserir(e)
    @staticmethod
    def emprestimo_listar():
        return Emprestimos.listar()
    @staticmethod
    def emprestimo_listar_id(id:int):
        return Emprestimos.listar_id(id)
    @staticmethod
    def emprestimo_atualizar(id:int, id_agiota:int, id_cliente:int, id_cobrador:int, solicitado:bool, aprovado:bool, quitado:bool, cobrado:bool, valor:float, duracao:int, data:datetime, juros:float):
        e = Emprestimo(id, id_agiota, id_cliente, id_cobrador, solicitado, aprovado, quitado, cobrado, valor, duracao, data, juros)
        Emprestimos.atualizar(e)
    @staticmethod
    def emprestimo_excluir(id:int):
        e = Emprestimo(id, "", "", "", "", "", "", "", "", "", "", "")
        Emprestimos.excluir(e)

    #PARCELA
    @staticmethod
    def parcela_inserir(id_emprestimo:int, data_vencimento:datetime, valor:float):
        p = Parcela(0, id_emprestimo, data_vencimento, valor, False)
        Parcelas.inserir(p)
    @staticmethod
    def parcela_listar():
        return Parcelas.listar()
    @staticmethod
    def parcela_listar_id(id:int):
        return Parcelas.listar_id(id)
    @staticmethod
    def parcela_atualizar(id: int, id_emprestimo:int, data_vencimento:datetime, valor:float, pago:bool):
        p = Parcela(id, id_emprestimo, data_vencimento, valor, pago)
        Parcelas.atualizar(p)
    @staticmethod
    def parcela_excluir(id:int):
        p = Parcela(id, "", "", "", "")
        Parcelas.excluir(p)
    
    
    

        
