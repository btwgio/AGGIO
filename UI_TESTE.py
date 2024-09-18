from view import View
from datetime import datetime

class UI:
    @staticmethod
    def menu():
        print("Olá! Tudo bem? Quem é você no sistema?")
        print("1-Cliente\n2-Agiota\n3-Cobrador\n4-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            print("==============================================================================")
            if op == 1: # Cliente
                op1 = 0 
                while op1 != 6:
                    op1 = UI.cliente_menu()
                    if op1 == 1: # Criar conta cliente
                        UI.cliente_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta cliente
                        UI.cliente_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Solicitar empréstimo
                        UI.emprestimo_inserir()
                        print("==============================================================================")
                    if op1 == 4: # Ver minhas parcelas
                        UI.parcela_listar_cliente()
                        print("==============================================================================")
                    if op1 == 5: # Pagar parcela
                        UI.parcela_pagar()
                        print("==============================================================================")
                    if op1 == 6: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 7: # Sair
                        print("==============================================================================")
                        op = 4
                        break
                    else: print("Opção inválida")
            if op == 2:  # Agiota
                op1 = 0 
                while op1 != 12:
                    op1 = UI.agiota_menu()
                    if op1 == 1: # Criar conta agiota
                        UI.agiota_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta agiota
                        UI.agiota_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Atualizar cliente
                        UI.cliente_atualizar()
                        print("==============================================================================")
                    if op1 == 4: # Atualizar cobrador
                        UI.cobrador_atualizar()
                        print("==============================================================================")
                    if op1 == 5: # Listar agiotas
                        UI.agiota_listar()
                        print("==============================================================================")
                    if op1 == 6: # Listar clientes
                        UI.cliente_listar()
                        print("==============================================================================")
                    if op1 == 7: # Listar cobradores
                        UI.cobrador_listar()
                        print("==============================================================================")
                    if op1 == 8: # Ver empréstimos
                        UI.emprestimo_listar()
                        print("==============================================================================")
                    if op1 == 9: # Ver parcelas
                        UI.parcela_listar()
                        print("==============================================================================")
                    if op1 == 10: # Aceitar empréstimo
                        UI.emprestimo_aceitar()
                        print("==============================================================================")
                    if op1 == 11: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 12: # Sair
                        op = 4
                        break
                    else: print("Opção inválida")
            if op == 3: #Cobrador
                op1 = 0 
                while op1 != 12:
                    op1 = UI.cobrador_menu()
                    if op1 == 1: # Criar conta cobrador
                        UI.cobrador_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta cobrador
                        UI.cobrador_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Ver parcelas não pagas
                        UI.parcelas_listar_nao_pago()
                        print("==============================================================================")
                    if op1 == 4: # Cobrar parcelas
                        UI.emprestimo_cobrar()
                        print("==============================================================================")
                    if op1 == 5: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 6: # Sair
                        op = 4
                        break
            if op == 4: # Fim
                print("Obrigado por usar AGGIO!")
                break
            else: print("Opção inválida")
    
    def cliente_menu():
        print("Seja bem-vindo senhor(a) cliente, o que deseja?")
        print("1-Criar uma conta\n2-Editar minha conta\n3-Solicitar empréstimo\n4-Ver minhas parcelas\n5-Pagar parcela\n6-Voltar\n7-Sair")
        return int(input("Escolha uma opção: "))
    
    def agiota_menu():
        print("Seja bem-vindo senhor(a) agiota, o que deseja?")
        print("1-Criar uma conta\n2-Atualizar agiotas\n3-Atualizar clientes\n4-Atualizar cobradores\n5-Ver agiotas\n6-Ver clientes\n7-Ver cobradores\n8-Ver empréstimos\n9-Ver parcelas\n10-Aceitar empréstimo\n11-Voltar\n12-Sair")
        return int(input("Escolha uma opção: "))
    
    def cobrador_menu():
        print("Seja bem-vindo senhor(a) cobrador(a), o que deseja?")
        print("1-Criar uma conta\n2-Editar minha conta\n3-Ver parcelas não pagas\n4-Cobrar parcela\n5-Voltar\n6-Sair")
        return int(input("Escolha uma opção: "))
    
    def cliente_inserir():
        nome = input("Informe o nome do cliente: ")
        celular = input("Informe o celular do cliente: ")
        endereco = input("Informe o endereço do cliente: ")
        saldo = float(input("Informe o saldo do cliente: "))
        View.cliente_inserir(nome, celular, endereco, saldo)
        
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome do cliente: ")
        celular = input("Informe o novo celular do cliente: ")
        endereco = input("Informe o novo endereco do cliente: ")
        saldo = float(input("Informe o novo saldo do cliente: "))
        View.cliente_atualizar(id, nome, celular, endereco, saldo)
    
    def cliente_listar():
        print("Lista de clientes:")
        for cliente in View.cliente_listar(): 
            print(cliente)
        
    def agiota_inserir():
        nome = input("Informe o nome do agiota: ")
        celular = input("Informe o celular do agiota: ")
        endereco = input("Informe o endereço do agiota: ")
        credito = float(input("Informe o crédito do agiota: "))
        View.agiota_inserir(nome, celular, endereco, credito)
        
    def agiota_atualizar():
        UI.agiota_listar()
        id = int(input("Informe o id do agiota a ser atualizado: "))
        nome = input("Informe o novo nome do agiota: ")
        celular = input("Informe o novo celular do agiota: ")
        endereco = input("Informe o novo endereco do agiota: ")
        credito = float(input("Informe o novo credito do agiota: "))
        View.agiota_atualizar(id, nome, celular, endereco, credito)
        
    def agiota_listar():
        print("Lista de agiotas:")
        for agiota in View.agiota_listar(): 
            print(agiota)
    
    def cobrador_inserir():
        nome = input("Informe o nome do cobrador: ")
        celular = input("Informe o celular do cobrador: ")
        endereco = input("Informe o endereço do cobrador: ")
        placa = input("Informe a placa do veículo do cobrador: ")
        UI.agiota_listar()
        id_agiota = int(input("Informe o ID de para qual agiota o cobrador trabalha: "))
        View.cobrador_inserir(nome, celular, endereco, placa, id_agiota)
        
    def cobrador_atualizar():
        UI.cobrador_listar()
        id = int(input("Informe o id do cobrador a ser atualizado: "))
        nome = input("Informe o novo nome do cobrador: ")
        celular = input("Informe o novo celular do cobrador: ")
        endereco = input("Informe o novo endereco do cobrador: ")
        placa = input("Informe a nova placa do veículo do cobrador: ")
        UI.agiota_listar()
        id_agiota = int(input("Informe o ID de para qual agiota o cobrador trabalha agora: "))
        View.cobrador_atualizar(id, nome, celular, endereco, placa, id_agiota)
        
    def cobrador_listar():
        print("Lista de cobradores:")
        for cobrador in View.cobrador_listar(): 
            print(cobrador)
    
    def emprestimo_inserir():
        UI.cliente_listar()
        id_cliente = int(input("Qual o ID do cliente que pediu o emprestimo: "))
        valor = float(input("Digite qual valor você quer pegar emprestado: "))
        print("Lista de agiotas disponíveis: ")
        qtd = 0
        for a in View.agiota_listar():
            if a.get_credito() >= valor:
                print(a)
                qtd = qtd + 1
        if qtd == 0: 
            print("Não tem agiotas disponíveis")
            return None
        id_agiota = int(input("Escolha o ID do agiota que você quer pegar o emprestimo: "))   
        for c in View.cobrador_listar():
            if c.get_id_agiota() == id_agiota:
                id_cobrador = c.get_id()
                break
        data = datetime.today()
        duracao = int(input("Quantos meses de emprestimo: "))
        juros = float(input("Quanto de juros: "))
        View.emprestimo_inserir(id_agiota, id_cliente, id_cobrador, valor, data, duracao, juros)
        
    def emprestimo_aceitar():
        print("Lista de emprestimos:")
        for e in View.emprestimo_listar():
            if e.get_aprovado == False:
                print(e)
        id = int(input("Informe o ID de qual emprestimo você quer aprovar: "))
        aux = View.emprestimo_listar_id(id)
        View.emprestimo_atualizar(aux.get_id(),aux.get_id_agiota(),aux.get_id_cliente(),aux.get_id_cobrador(),aux.get_solicitado(),True,aux.get_quitado(),aux.get_cobrado(),aux.get_valor(),aux.get_duracao(),aux.get_data(),aux.get_juros())
        print("Emprestimo aceito")
        
    def emprestimo_listar():
        print("Lista de emprestimos:")
        for emprestimo in View.emprestimo_listar():
            print(emprestimo)
    
    def emprestimo_cobrar():
        UI.emprestimo_listar()
        id = int(input("Qual emprestimo você quer cobrar: "))
        
        aux = View.emprestimo_listar_id(id)
        View.emprestimo_atualizar(aux.get_id(),aux.get_id_agiota(),aux.get_id_cliente(),aux.get_id_cobrador(),aux.get_solicitado(),aux.get_aprovado(),aux.get_quitado(),True,aux.get_valor(),aux.get_duracao(),aux.get_data(),aux.get_juros())
        print("Emprestimo cobrado!")
    
    def parcela_listar():
        print("Lista de parcelas:")
        for parcela in View.parcela_listar():
            print(parcela)
            
    def parcela_listar_cliente():
        UI.cliente_listar()
        id = int(input("Qual o id do cliente quer ver as parcelas: "))
        for e in View.emprestimo_listar():
            if e.get_id_cliente == id:
                print(e)
        id = int(input("De qual emprestimo são as parcelas: "))
        for p in View.emprestimo_listar():
            if p.get_id_emprestimo == id:
                print(p)
                
    def parcela_pagar():
        UI.parcela_listar_cliente()
        id = int(input("Qual o ID da parcela que você quer pagar: "))
        
        aux = View.parcela_listar_id(id)
        View.parcela_atualizar(aux.get_id(), aux.get_id_emprestimo(), aux.get_data_vencimento(), aux.get_valor(), True)
    
    def parcelas_listar_nao_pago():
        for p in View.parcela_listar():
            if p.get_pago() == False:
                print(p)
    
        
UI.main()