import os

def limpar_tela():
    os.system('cls')

def pausar():
    input('[ENTER] para continuar...')

def verificar_senha(senha):
    if senha == senha_adm:
        return True
    return False


senha_adm = '4321'

while True:
    limpar_tela()
    print('    SISTEMA DA BIBLIOTECA     ')
    print(' [1] - ACESSO ADM             ')
    print(' [2] - ACESSO ESTUDANTE       ')
    print(' [0] - SAIR                   ')
    op = input('DIGITE A OPÇÃO DE ACESSO: ')

    if op == '1':
        senha = input('DIGITE A SENHA: ')
        verificar = verificar_senha(senha)
        if verificar == True:
            print(' ACESSO ADM  ')
            print('[1]- CONTROLE DE ESTUDANTES')
            print('[2]- CONTROLE DE LIVROS')
            print('[3]- NOVO EMPRÉSTIMO')
            print('[0]- VOLTAR PARA O MENU')
            pausar()

    elif op == '2':
        cpf = int(input('DIGITE SEU CPF: '))
        print(' ACESSO ESTUDANTE ')
        print('[1]- VERIFICAR EMPRÉSTIMOS' )
        print('[2]- VER MEUS DADOS')
        print('[0]- VOLTAR PARA O MENU')
        pausar()
        
    elif op == '0':
        print('SAINDO DO SISTEMA')
        break
    else:
        print('OPÇÃO INVÁLIDA! DIGITE UMA DAS OPÇÕES ACIMA!')
        pausar()
    