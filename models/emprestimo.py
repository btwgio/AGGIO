from datetime import datetime
import json

class Emprestimo:
    def __init__ (self,  id:int,  valor:float, duracao:int, data:datetime,juros:float):
        self.__id = id                          #número ID do empréstimo 
        #self.__solicitado = solicitado
        #self.__aprovado = aprovado
        #self.__quitado = quitado           #se a pessoa quitou o empréstimo ou não 
        #self.__cobrado = cobrado
        self.__valor = valor
        self.__data = data
        self.__duracao = duracao
        self.__juros = juros
        #self.__id_agiota = id_agiota
        #self.__id_cliente = id_cliente
        #self.__id_cobrador = id_cobrador

    def get_id(self):
        return self.__id
    '''def get_solicitado(self):
        return self.__solicitado
    def get_aprovado(self):
        return self.__aprovado
    def get_quitado(self):
        return self.__quitado'''
    def get_valor(self): 
        return self.__valor 
    '''def get_cobrado(self):
        return self.__cobrado'''
    def get_data(self):
        return self.__data
    def get_duracao(self):
        return self.__duracao
    def get_juros(self):
        return self.__juros
    
    def set_id(self, id:int):
        self.__id = id 
    '''def set_solicitado(self, solicitado:bool):
        self.__solicitado = solicitado
    def set_aprovado(self, aprovado: bool):
        self.__aprovado = aprovado
    def set_quitado(self, quitado: bool):
        self.__quitado = quitado'''
    def set_valor(self, valor:float): 
        self.__valor = valor 
    '''def set_cobrado(self, cobrado:bool):
        self.__cobrado = cobrado'''
    def set_data(self, data:datetime):
        self.__data = data
    def set_duracao(self, duracao: int):
        self.__duracao = duracao
    def set_juros(self, juros: float):
        self.__juros = juros

    def __str__(self):
        return f"{self.__id} - {self.__valor} - {self.__data} - {self.__duracao} - {self.__juros}"

class Emprestimos:
    emprestimos = []
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
            x.valor = obj.valor
            x.data = obj.data
            x.duracao = obj.duracao
            x.juros = obj.juros
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) 
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def salvar(cls):    
        with open("emprestimos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        with open("emprestimos.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Emprestimo(obj["id"], obj["valor"], obj["data"], obj["duracao"], obj["juros"])
                cls.objetos.append(c)       
