import json

class Cliente:
    def __init__ (self, id, nome, celular, endereco):
        self.id = id              #id do cliente. por ex.: nathan tem o ID 40 e esse nome o identifica no sistema
        self.nome = nome          #nome do cliente
        self.celular = celular    #celular do cliente 
        self.endereco = endereco  #endereco do cliente
        #self.saldo = saldo  

    def get_id(self):
        return self.id 
    def get_nome(self): 
        return self.nome 
    def get_celular(self):
        return self.celular
    def get_endereco(self):
        return self.endereco  
    '''def get_saldo(self):
        return self.saldo'''
    
    def set_id(self, id):
        self.id = id
    def set_nome(self, nome): 
        self.nome = nome 
    def set_celular(self, celular):
        self.celular = celular 
    def set_endereco(self, endereco):
        self.endereco = endereco 
    '''def set_saldo(self, saldo:int):
        self.saldo = saldo'''

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.celular} - {self.endereco}R$"

class Clientes:
    clientes = []
    
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de objetos do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.clientes:
            if x.id > id: id = x.id
        id += 1    
        obj.id = id          # novo objeto recebe o id calculado
        cls.clientes.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo
    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.clientes 
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.clientes:   # percorre a lista procurando o objeto com o id informado
            if x.id == id: return x
        return None      
    @classmethod
    def atualizar(cls, c):
        x = cls.listar_id(c.id)
        if x != None:
            x.desc = c.desc
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.clientes.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        with open("clientes.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Cliente(obj["id"], obj["nome"], obj["celular"], obj["endereco"])
                cls.clientes.append(c)

