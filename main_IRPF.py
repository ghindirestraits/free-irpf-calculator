'''
    IRPF - Cálculo do IR para PF nas modalidades Simplificada e Completa
    
    Este código foi desenvolvido em formato de atividade avaliativa para a cadeira
    de Engenharia de Software, ministrada pelo professor Michael da Costa Mora

    por Gabriel Heberle, Lucas Loureiro Kosciuk, Raup Sessim da Silva
'''

# Inicialização de variáveis globais
nome = ""
idade = 0
cpf = 0
numDepend = 0
contPrev = 0
totalRend = 0
base = 0
Base_IRPF = 0
IRPF = 0
salliq = 0

# Função para cálculo do IRPF Simplificado
def cadastroSimples():
    
    global nome
    global cpf
    global contPrev
    global totalRend
    global base
    global Base_IRPF
    global IRPF
    global salliq

    nome = input("\n Nome: ")

    cpf = input("\n CPF: ")

    contPrev = input("\n Contr. Previd.: R$")

    totalRend = input("\n Total Rend.: R$")
    
    base = int(totalRend) - int(contPrev)
    Base_IRPF = base * 0.95

    if Base_IRPF <= 12000:
        print("\nIsento de Imposto de Renda")
        IRPF = 0

    if Base_IRPF >= 12000 and Base_IRPF <= 24000:
        IRPF = Base_IRPF * 0.15

    if Base_IRPF >= 24000:
        IRPF = Base_IRPF * 0.275

    salliq = int(totalRend) - int(contPrev)

    print("\nValor do IRPF: R$" + str(IRPF))
    print("\nSalario Liquido: " + str(salliq))
    print("\n\n\n\n\n")

# Função para cálculo do IRPF Completo
def cadastroCompleto():

    global nome
    global idade
    global cpf
    global numDepend
    global contPrev
    global totalRend
    global base
    global Base_IRPF
    global IRPF
    global salliq

    nome = input("\n Nome: ")

    idade = input("\n Idade: ")

    cpf = input("\n CPF: ")

    numDepend = input("\n Num Dependentes: ")

    contPrev = input("\n Contr. Previd.: R$")

    totalRend = input("\n Total Rend.: R$")

    Base_IRPF = int(totalRend) - int(contPrev)

    if int(idade) < 65 :
        if int(numDepend) <= 2:
            Base_IRPF = Base_IRPF * 0.98

        if int(numDepend) >= 3 and int(numDepend) <= 5:
            Base_IRPF = Base_IRPF * 0.965

        if int(numDepend) > 5:
            Base_IRPF = Base_IRPF * 0.95

    if int(idade) >= 65:
        if int(numDepend) <= 2:
            Base_IRPF = Base_IRPF * 0.97

        if int(numDepend) >= 3 and int(numDepend) <= 5:
            Base_IRPF = Base_IRPF * 0.955

        if int(numDepend) > 5:
            Base_IRPF = Base_IRPF * 0.94

    if Base_IRPF <= 12000:
        print("\nIsento de Imposto de Renda")
        IRPF = 0

    if Base_IRPF >= 12000 and Base_IRPF <= 24000:
        IRPF = Base_IRPF * 0.15

    if Base_IRPF >= 24000:
        IRPF = Base_IRPF * 0.275

    salliq = int(totalRend) - int(contPrev)
    
    print("\nValor do IRPF: R$" + str(IRPF))
    print("\nSalario Liquido: R$" + str(salliq))
    print("\n\n\n\n\n")

# Definição da função de interface gráfica
def menu():

    while(1):
        print("\n  ******************************************** ")
        print("\n  *                                          * ")
        print("\n  *  SISTEMA DE DECLARACAO IMPOSTO DE RENDA  * ")
        print("\n  *                                          * ")
        print("\n  ******************************************** ")

        print("\n\n        *** OPCOES CADASTRAMENTO ***     ")
        print("\n  -------------------------------------------")
        print("\n         ( 1 ) DECLARACAO SIMPLIFICADA")
        print("\n         ( 2 ) DECLARACAO COMPLETA")
        print("\n         ( 0 ) SAIR")

        escolha = input()

        if int(escolha) == 1:
            cadastroSimples()

        elif int(escolha) == 2:
            cadastroCompleto()

        else:
            break

menu()
