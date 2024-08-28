import json 

class Cobrador:
    def __init__ (self, id:int, nome:str, celular:str, placa_carro:str, arma:str, id_agiota:int):
        self.__id = id 
        self.__nome = nome
        self.__celular = celular 
        self.__placa_carro = placa_carro
        self.__arma = arma
        self.__id_agiota = id_agiota

    def get_id(self):
        return self.__id 
    def get_nome(self): 
        return self.__nome 
    def get_celular(self):
        return self.__celular
    def get_placa_carro(self):
        return self.__placa_carro 
    def get_arma(self):
        return self.__arma
    def get_id_agiota(self):
        return self.__id_agiota 
    
    def set_id(self, id:int):
        self.__id = id
    def set_nome(self, nome:str): 
        self.__nome = nome 
    def set_celular(self, celular:str):
        self.__celular = celular 
    def set_placa_carro(self, placa_carro:str):
        self.__placa_carro = placa_carro
    def set_arma(self, arma:str):
        self.__arma = arma
    def set_id_agiota(self, id_agiota:int):
        self.__id_agiota = id_agiota

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__celular} - {self.__placa_carro} - {self.__arma} - {self.__id_agiota}"

class Cobradores:
    cobradores = []
    
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de objetos do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.cobradores:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)          # novo objeto recebe o id calculado
        cls.cobradores.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo
    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.cobradores  
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.cobradores:   # percorre a lista procurando o objeto com o id informado
            if x.get_id() == id: return x
        return None      
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            x.set_nome(obj.get_nome())
            x.set_celular(obj.get_celular())
            x.set_placa_carro(obj.get_placa_carro())
            x.set_arma(obj.get_arma())
            x.set_id_agiota(obj.get_id_agiota())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.cobradores.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("cobradores.json", mode="w") as arquivo:
            json.dump(cls.cobradores, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.cobradores = []
        with open("cobradores.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cobrador(obj["id"], obj["nome"], obj["celular"], obj["placa_carro"], obj["arma"], obj["id_agiota"])
                cls.cobradores.append(c)  
