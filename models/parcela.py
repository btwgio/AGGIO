from datetime import datetime
import json

class Parcela:
    def __init__(self, id:int, data_vencimento:datetime, valor: float):
        self.__id = id
        self.__data_vencimento = data_vencimento
        self.__valor = valor
        #self.__pago = pago
        #self.__id_emprestimo = id_emprestimo
    
    def set_id(self, id: int):
        self.__id = id
    def set_data_vencimento(self, data: str):
        self.__data_vencimento = data
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_id(self):
        return self.__id
    def get_data_vencimento(self):
        return self.__data_vencimento
    def get_valor(self):
        return self.__valor
    def __str__(self):
        return f'{self.__id} - {self.__set_data_vencimento} - {self.__valor}R$'

class Parcelas:
    parcelas = []
    @classmethod
    def inserir(cls, obj):     
        cls.abrir()            
        id = 0                  
        for x in cls.objetos:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id             
        cls.objetos.append(obj) 
        cls.salvar()            
    
    @classmethod
    def listar(cls):            
        cls.abrir()
        return cls.objetos  
    
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.objetos:  
            if x.id == id: return x
        return None   
       
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id) 
        if x != None:
            x.data = obj.data
            x.valor = obj.valor
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) 
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):    
        with open("parcelas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("parcelas.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Parcela(obj["id"], obj["data"], obj["valor"])
                cls.objetos.append(c)       


