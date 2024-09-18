from datetime import datetime
import json
from models.modelo import Modelo

class Emprestimo:
    def __init__(self, id:int, id_agiota:int, id_cliente:int, id_cobrador:int, solicitado:bool, aprovado:bool, quitado:bool, cobrado:bool, valor:float, duracao:int, data:datetime, juros:float):
        self.id = id   
        self.id_agiota = id_agiota
        self.id_cliente = id_cliente
        self.id_cobrador = id_cobrador 
        
        self.solicitado = solicitado
        self.aprovado = aprovado
        self.quitado = quitado           
        self.cobrado = cobrado
        
        self.valor = valor
        self.data = data       
        self.duracao = duracao 
        self.juros = juros     
        
    def get_id(self):
        return self.id
    def get_id_agiota(self):
        return self.id_agiota
    def get_id_cliente(self):
        return self.id_cliente
    def get_id_cobrador(self):
        return self.id_cobrador
    def get_solicitado(self):
        return self.solicitado
    def get_aprovado(self):
        return self.aprovado
    def get_quitado(self):
        return self.quitado
    def get_cobrado(self):
        return self.cobrado
    def get_valor(self): 
        return self.valor 
    def get_data(self):
        return self.data
    def get_duracao(self):
        return self.duracao
    def get_juros(self):
        return self.juros
    
    def set_id(self, id:int):
        self.id = id 
    def set_id_agiota(self, id:int):
        self.id_agiota = id
    def set_id_cliente(self, id:int):
        self.id_cliente = id
    def set_id_cobrador(self, id:int):
        self.id_cobrador = id
    def set_solicitado(self, solicitado:bool):
        self.solicitado = solicitado
    def set_aprovado(self, aprovado: bool):
        self.aprovado = aprovado
    def set_quitado(self, quitado: bool):
        self.quitado = quitado
    def set_cobrado(self, cobrado:bool):
        self.cobrado = cobrado
    def set_valor(self, valor:float): 
        self.valor = valor 
    def set_data(self, data:datetime):
        self.data = data
    def set_duracao(self, duracao: int):
        self.duracao = duracao
    def set_juros(self, juros: float):
        self.juros = juros

    def __str__(self):
        return f"ID: {self.id} - ID_AGIOTA: {self.id_agiota} - ID_CLIENTE: {self.id_cliente} - ID_COBRADOR: {self.id_cobrador} - SOLICITADO: {self.solicitado} - APROVADO: {self.aprovado} - QUITADO: {self.quitado} - COBRADO: {self.cobrado} - VALOR DO EMPRÉSTIMO: {self.valor} - DURAÇÃO EM MESES: {self.duracao} - DATA DO EMPRÉSTIMO: {self.data.strftime('%d/%m/%Y')} - JUROS: {self.juros}"

class Emprestimos(Modelo):
    @classmethod
    def salvar(cls):    
        with open("./emprestimos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("./emprestimos.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  e = Emprestimo(obj["id"], obj["id_agiota"], obj["id_cliente"], obj["id_cobrador"], obj["solicitado"], obj["aprovado"], obj["quitado"], obj["cobrado"], obj["valor"], obj["duracao"], datetime.strptime(obj["data"], "%d/%m/%Y"), obj["juros"])
                  cls.objetos.append(e)
        except FileNotFoundError:
          pass 
