from view import View

class UIa:
    @staticmethod
    def menu():
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UIa.menu()
            if op == 1: UIa.cliente_inserir()
            if op == 2: UIa.cliente_listar()
            if op == 3: UIa.cliente_atualizar()
            if op == 4: UIa.cliente_excluir()
    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        endereco = input("Informe o endereço: ")
        fone = input("Informe o fone: ")
        View.cliente_inserir(nome, endereco, fone)
    @staticmethod
    def cliente_listar():
        for cliente in View.cliente_listar(): 
            print(cliente)
    @staticmethod
    def cliente_atualizar():
        UIa.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        View.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        UIa.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

UIa.main()


class UIc:
    @staticmethod
    def menu():
        print("Clientes")
        print("  1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UIc.menu()
            if op == 1: UIc.cliente_inserir()
            if op == 2: UIc.cliente_listar()
            if op == 3: UIc.cliente_atualizar()
            if op == 4: UIc.cliente_excluir()
    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        View.cliente_inserir(nome, email, fone)
    @staticmethod
    def cliente_listar():
        for cliente in View.cliente_listar(): 
            print(cliente)
    @staticmethod
    def cliente_atualizar():
        UIc.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        View.cliente_atualizar(id, nome, email, fone)
    @staticmethod
    def cliente_excluir():
        UIc.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

UIc.main()
