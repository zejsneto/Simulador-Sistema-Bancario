import os

from datetime import datetime
dataHoraAtuais = datetime.now()
dataHoraTexto = dataHoraAtuais.strftime('%d/%m/%Y %H:%M')

def criarNovo():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    conta = input("Digite o tipo de conta (s: Salário, c: Comum ou p: Plus): ")
    senha = input("Digite a senha: ")
    valorInicial = input("Digite o valor inicial: ")
    if os.path.isfile(cpf+".txt"):
        print("Cliente já registrado.")    
    else:
        arquivo = open(cpf+".txt", "a")
        arquivo.write("Nome: %s\n" % nome)
        arquivo.write("CPF: %s\n" % cpf)
        if conta == "s":
            arquivo.write("Conta: Salário\n")
        elif conta == "c":
            arquivo.write("Conta: Comum\n")
        elif conta == "p":
            arquivo.write("Conta: Plus\n")
        arquivo.write("Senha: %s\n" % senha)
        arquivo.write("Inicio: %s\n" % valorInicial)
        arquivo.close()
        print("Cliente criado.")

def apagarCliente():
    cpfVerificar = input("Digite o CPF: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Digite a senha: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        if senhaVerificar == senha[3][1]:
            os.remove(cpfVerificar+".txt")
            print("Conta apagada.")
        if senhaVerificar != senha[3][1]:
            print("A senha está incorreta.")
            return
    
    else: 
        print("O CPF está incorreto/não existe.")
        return

def debitar():
    cpfVerificar = input("Digite o CPF: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Digite a senha: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        if senhaVerificar == senha[3][1]:
            if senha[2][1] == "Salario":
                valorDebitado = float(input("Digite o valor a ser debitado: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.05*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= 0:
                    arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("Foi debitado um valor de R$ %.2f com tarifa de R$ %.2f" %(valorDebitado, tarifa))
                else:
                    print("Saldo insuficiente para completar a transação")

            elif senha[2][1] == "Comum":
                valorDebitado = float(input("Digite o valor a ser debitado: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.03*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= -500:
                    arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("Foi debitado um valor de R$ %.2f com tarifa de R$ %.2f" %(valorDebitado, tarifa))
              
                else:
                    print("Saldo insuficiente para completar a transação")

            elif senha[2][1] == "Plus":
                valorDebitado = float(input("Digite o valor a ser debitado: "))
                arquivo = open(cpfVerificar+".txt", "a")
                tarifa = (0.01*valorDebitado)
                novoSaldo = float(senha[-1][-1]) - valorDebitado - tarifa
                if novoSaldo >= -5000:
                    arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(dataHoraTexto, valorDebitado, tarifa, novoSaldo))
                    arquivo.close()
                    print("Foi debitado um valor de R$ %.2f com tarifa de R$ %.2f" %(valorDebitado, tarifa))

                else:
                    print("Saldo insuficiente para completar a transação")

        if senhaVerificar != senha[3][1]:
            print("A senha está incorreta.")
            return
            
    else: 
        print("O CPF está incorreto/não existe.")
        return

def depositar():
    cpfVerificar = input("Digite o CPF: ")
    if  os.path.exists(cpfVerificar+".txt"):
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()
        valorDepositado = float(input("Digite o valor que deseja depositar: "))
        arquivo = open(cpfVerificar+".txt", "a")
        novoSaldo = float(senha[-1][-1]) + valorDepositado
        arquivo.write("Data: %s + %.2f Tarifa: 0.00 Saldo: %.2f\n" %(dataHoraTexto, valorDepositado, novoSaldo))
        arquivo.close()
        print("Foi depositado um valor de R$ %.2f." %valorDepositado)
            
    else: 
        print("O CPF está incorreto/não existe.")
        return

def verSaldo():
    cpfVerificar = input("Digite o CPF: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Digite a senha: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()

        if senhaVerificar == senha[3][1]:
            print("Seu saldo é de R$ %s." %senha[-1][-1])
            
        if senhaVerificar != senha[3][1]:
            print("A senha está incorreta.")
            return
            
    else: 
        print("O CPF está incorreto/não existe.")
        return

def verExtrato():
    cpfVerificar = input("Digite o CPF: ")
    if  os.path.exists(cpfVerificar+".txt"):
        senhaVerificar = input("Digite a senha: ")
        arquivo = open(cpfVerificar+".txt", "r")
        senha = []
        for i in arquivo.readlines():
            senha.append(i.strip().split())
        arquivo.close()

        if senhaVerificar == senha[3][1]:
            senha.pop(3)
            senha.pop(3)
            for i in range(len(senha)):
                   print(*senha[i])
            
        else:
            print("A senha está incorreta.")
            return
            
    else: 
        print("O CPF está incorreto/não existe.")
        return

def main():
    while True:
        print()
        print("-----Menu-----")
        print()
        print("1. Criar Novo Cliente")
        print("2. Apagar Cliente")
        print("3. Debitar")
        print("4. Depositar")
        print("5. Ver Saldo")
        print("6. Ver Extrato")
        print()
        print("0. Sair")
        print()
        print("--------------")

        opcao = input("Escolha uma das opções: ")

        if opcao == "1":
            criarNovo()
        
        if opcao == "2":
            apagarCliente()

        if opcao == "3":
            debitar()  

        if opcao == "4":
            depositar()  

        if opcao == "5":
            verSaldo()  

        if opcao == "6":
            verExtrato()  

        if opcao == "0":
            break  

main()