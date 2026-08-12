import os

def limpar_tela():
    os.system('cls')

def pausar():
    print('\n' + '─' * 42)
    input('  Pressione [ENTER] para continuar...')

def verificar_senha(senha):
    if senha == senha_adm:
        return True
    return False

senha_adm = '4321'

while True:
    limpar_tela()
    print('┌────────────────────────────────────────┐')
    print('│          SISTEMA DE BIBLIOTECA         │')
    print('├────────────────────────────────────────┤')
    print('│  [1] - ACESSO ADM                      │')
    print('│  [2] - ACESSO ESTUDANTE                │')
    print('│  [0] - SAIR                            │')
    print('└────────────────────────────────────────┘')
    op = input('\n> Digite a opção desejada: ')

    if op == '1':
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│             AUTENTICAÇÃO               │')
        print('└────────────────────────────────────────┘')
        senha = input('  Digite a senha de administrador: ')
        
        if verificar_senha(senha):
            limpar_tela()
            print('┌────────────────────────────────────────┐')
            print('│               ACESSO ADM               │')
            print('├────────────────────────────────────────┤')
            print('│  [1] - Novo Empréstimo                 │')
            print('│  [2] - Controle de Estudantes          │')
            print('│  [3] - Controle de Livros              │')
            print('│  [0] - Voltar para o Menu              │')
            print('└────────────────────────────────────────┘')
            sub_op = input('\n> Opção: ')

            if sub_op == '1':
                limpar_tela()
                print('┌────────────────────────────────────────┐')
                print('│            NOVO EMPRÉSTIMO             │')
                print('└────────────────────────────────────────┘')
                cliente = input('  ID do Cliente: ')
                livro = input('  ID do Livro: ')
                data = input('  Data do Empréstimo: ')
                pausar()

            elif sub_op == '2':
                limpar_tela()
                print('┌────────────────────────────────────────┐')
                print('│         CONTROLE DE ESTUDANTES         │')
                print('├────────────────────────────────────────┤')
                print('│  [1] - Cadastrar Estudante             │')
                print('│  [2] - Pesquisar Estudante             │')
                print('│  [3] - Editar Estudante                │')
                print('│  [4] - Excluir Estudante               │')
                print('│  [0] - Voltar                          │')
                print('└────────────────────────────────────────┘')
                pausar()

            elif sub_op == '3':
                limpar_tela()
                print('┌────────────────────────────────────────┐')
                print('│           CONTROLE DE LIVROS           │')
                print('├────────────────────────────────────────┤')
                print('│  [1] - Cadastrar Livro                 │')
                print('│  [2] - Ver Livros Disponíveis          │')
                print('│  [3] - Ver Estoque Completo            │')
                print('│  [0] - Voltar                          │')
                print('└────────────────────────────────────────┘')
                pausar()
        else:
            print('\n[!] Senha incorreta! Acesso negado.')
            pausar()

    elif op == '2':
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│            ACESSO ESTUDANTE            │')
        print('└────────────────────────────────────────┘')
        cpf = input('  Digite seu CPF: ')
        
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│             PAINEL ESTUDANTE           │')
        print('├────────────────────────────────────────┤')
        print('│  [1] - Verificar Empréstimos           │')
        print('│  [2] - Ver Meus Dados                  │')
        print('│  [0] - Voltar                          │')
        print('└────────────────────────────────────────┘')
        pausar()

    elif op == '0':
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│      Encerrando o sistema... Até já!   │')
        print('└────────────────────────────────────────┘\n')
        break
        
    else:
        print('\n[!] Opção inválida. Escolha uma das opções do menu.')
        pausar()