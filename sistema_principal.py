
from time import sleep
import listas
import funcoes

# Índices para facilitar a leitura do código
NOME = 0
MATRICULA = 1


#================================================================================================================

#============================================= SISTEMA PRINCIPAL ================================================

while True:
    funcoes.limpar_tela()
    print('┌────────────────────────────────────────┐')
    print('│          SISTEMA DE BIBLIOTECA         │')
    print('├────────────────────────────────────────┤')
    print('│  [1] - ACESSO ADM                      │')
    print('│  [2] - ACESSO ESTUDANTE                │')
    print('│  [0] - SAIR                            │')
    print('└────────────────────────────────────────┘')
    op = input('\n> Digite a opção desejada: ')

    if op == '1':
        funcoes.limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│             AUTENTICAÇÃO               │')
        print('└────────────────────────────────────────┘')
        senha = input('  Digite a senha de administrador: ')
        
        if funcoes.verificar_senha(senha):
            while True:
                funcoes.limpar_tela()
                print('┌────────────────────────────────────────┐')
                print('│               ACESSO ADM               │')
                print('├────────────────────────────────────────┤')
                print('│  [1] - Novo Empréstimo                 │')
                print('│  [2] - Controle de Estudantes          │')
                print('│  [3] - Controle de Livros              │')
                print('│  [4] - Controle de Empréstimos         │')
                print('│  [5] - Controle de Devoluções          │')
                print('│  [0] - Voltar para o Menu              │')
                print('└────────────────────────────────────────┘')
                sub_op = input('\n> Opção: ')

                if sub_op == '1':
                    funcoes.limpar_tela()
                    print('┌────────────────────────────────────────┐')
                    print('│            NOVO EMPRÉSTIMO             │')
                    print('└────────────────────────────────────────┘')
                    """
                    cliente = input('  Matrícula do Cliente: ')
                    livro = input('  Nome do Livro: ')
                    data = input('  Data do Empréstimo: ')
                    """
                    funcoes.cadastra_emprestimo()
                    funcoes.pausar()

                elif sub_op == '2':
                    while True:
                        funcoes.limpar_tela()
                        print('┌────────────────────────────────────────┐')
                        print('│         CONTROLE DE ESTUDANTES         │')
                        print('├────────────────────────────────────────┤')
                        print('│  [1] - Cadastrar Estudante             │')
                        print('│  [2] - Pesquisar Estudante             │')
                        print('│  [3] - Editar Estudante                │')
                        print('│  [4] - Excluir Estudante               │')
                        print('│  [0] - Voltar                          │')
                        print('└────────────────────────────────────────┘')
                        op = int(input('\n> Opção: '))
                        if op == 1:
                            funcoes.cadastrar_estudante()
                        elif op == 2:
                            matricula = input("Digite a matrícula do estudante que deseja pesquisar: ")
                            funcoes.dados_estudante(matricula)
                        elif op == 3:
                            funcoes.editar_estudante()
                            
                        elif op == 4:
                            funcoes.remover_estudante()
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            funcoes.pausar()

                elif sub_op == '3':
                    while True:
                        funcoes.limpar_tela()
                        print('┌────────────────────────────────────────┐')
                        print('│          CONTROLE DE LIVROS            │')
                        print('├────────────────────────────────────────┤')
                        print('│  [1] - Cadastrar Novo Livro            │')
                        print('│  [2] - Ver Estoque Geral               │')
                        print('│  [3] - Buscar Livro por Gênero         │')
                        print('│  [4] - Buscar Livro por Nome           │')
                        print('│  [0] - Voltar                          │')
                        print('└────────────────────────────────────────┘')
                        op = int(input('\n> Opção: '))
                        if op == 1:
                            print('┌────────────────────────────────────────┐')
                            print('│           CADASTRO DE LIVROS           │')
                            print('└────────────────────────────────────────┘')
                            funcoes.cadastrar_livro()
                            funcoes.pausar()
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│         VER ESTOQUE COMPLETO           │')
                            print('├────────────────────────────────────────┤')
                            funcoes.ver_estoque_geral()
                            funcoes.pausar()

                        elif op == 3:
                            print('┌────────────────────────────────────────┐')
                            print('│            BUSCAR POR GÊNERO           │')
                            print('├────────────────────────────────────────┤')
                            funcoes.ver_genero()
                            funcoes.pausar()

                        elif op == 4:
                            print('┌────────────────────────────────────────┐')
                            print('│             BUSCAR POR NOME            │')
                            print('├────────────────────────────────────────┤')
                            funcoes.buscar_por_nome()
                            funcoes.pausar()
                        elif op == 0:
                            break

                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            funcoes.pausar()
                elif sub_op == '4':
                    while True:
                        funcoes.limpar_tela()
                        print('┌────────────────────────────────────────┐')
                        print('│         CONTROLE DE EMPRÉSTIMOS        │')
                        print('├────────────────────────────────────────┤')
                        print('│  [1] - Ver Empréstimos Ativos          │')
                        print('│  [2] - Histórico de Empréstimos        │')
                        print('│  [0] - Voltar                          │')
                        print('└────────────────────────────────────────┘')
                        op = int(input('\n> Opção: '))
                        if op == 1:
                            print('┌────────────────────────────────────────┐')
                            print('│         EMPRÉSTIMOS ATIVOS             │')
                            print('├────────────────────────────────────────┤')
                            funcoes.ver_emprestimos()
                            funcoes.pausar()
                            #AGUARDAR FUNÇÃO DE VER EMPRÉSTIMOS ATIVOS
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│       HISTÓRICO DE EMPRÉSTIMOS         │')
                            print('├────────────────────────────────────────┤')
                            funcoes.pausar()
                            funcoes.historico_emprestimos(matricula)
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            funcoes.pausar()

                elif sub_op == '5':
                    while True:
                        funcoes.limpar_tela()
                        print('┌────────────────────────────────────────┐')
                        print('│         CONTROLE DE DEVOLUÇÕES         │')
                        print('├────────────────────────────────────────┤')
                        print('│  [1] - Registrar Devolução             │')
                        print('│  [2] - Histórico de Devoluções         │')
                        print('│  [0] - Voltar                          │')
                        print('└────────────────────────────────────────┘')
                        op = int(input('\n> Opção: '))
                        if op == 1:
                            print('┌────────────────────────────────────────┐')
                            print('│          REGISTRAR DEVOLUÇÃO           │')
                            print('├────────────────────────────────────────┤')
                            funcoes.pausar()
                            #AGUARDAR FUNÇÃO DE REGISTRAR DEVOLUÇÃO
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│       HISTÓRICO DE DEVOLUÇÕES          │')
                            print('├────────────────────────────────────────┤')
                            funcoes.pausar()
                            #AGUARDAR FUNÇÃO DE VER HISTÓRICO DE DEVOLUÇÕES
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            funcoes.pausar()

        else:
            print('\n[!] Senha incorreta! Acesso negado.')
            funcoes.pausar()

    elif op == '2':
        funcoes.limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│            ACESSO ESTUDANTE            │')
        print('└────────────────────────────────────────┘')
        mat = input('  Digite sua Matricúla: ')
        if mat in listas.Estudantes:
            funcoes.limpar_tela()
            print('┌────────────────────────────────────────┐')
            print('│             PAINEL ESTUDANTE           │')
            print('├────────────────────────────────────────┤')
            print('│  [1] - Verificar Empréstimos           │')
            print('│  [2] - Ver Meus Dados                  │')
            print('│  [3] - Buscar livro por Gênero         │')
            print('│  [4] - Buscar livro por Nome           │')
            print('│  [0] - Voltar                          │')
            print('└────────────────────────────────────────┘')
            sup_op = int(input('>: '))

            if sup_op == 1:
                print('┌────────────────────────────────────────┐')
                print('│         VERIFICAR EMPRÉSTIMOS          │')
                print('├────────────────────────────────────────┤')
                print('│  [1] - Empréstimos Ativos              │')
                print('│  [2] - Histórico de Empréstimos        │')
                print('│  [0] - Voltar                          │')
                print('└────────────────────────────────────────┘')
                op = int(input('>: '))
                #pausar()
                if op == 1:
                    print('┌────────────────────────────────────────┐')
                    print('│         EMPRÉSTIMOS ATIVOS             │')
                    print('├────────────────────────────────────────┤')
                    funcoes.emprestimos_ativos(mat)
                elif op == 2:
                    print('┌────────────────────────────────────────┐')
                    print('│       HISTÓRICO DE EMPRÉSTIMOS         │')
                    print('├────────────────────────────────────────┤')
                    funcoes.historico_emprestimos(mat)
                    
                elif op == 0:
                    print('┌────────────────────────────────────────┐')
                    print('│             VOLTANDO AO MENU           │')
                    print('└────────────────────────────────────────┘')
                    funcoes.pausar()
                
            elif sup_op == 2:
                print('┌────────────────────────────────────────┐')
                print('│           VER MEUS DADOS               │')
                print('├────────────────────────────────────────┤')
                funcoes.dados_estudante(mat)
            elif sup_op == 3:
                print('┌────────────────────────────────────────┐')
                print('│            BUSCAR POR GÊNERO           │')
                print('├────────────────────────────────────────┤')
                funcoes.ver_genero()
                funcoes.pausar()

            elif sup_op == 4:
                print('┌────────────────────────────────────────┐')
                print('│             BUSCAR POR NOME            │')
                print('├────────────────────────────────────────┤')
                funcoes.buscar_por_nome()
                funcoes.pausar()


        elif op == '0':
            funcoes.limpar_tela()
            print('┌────────────────────────────────────────┐')
            print('│      Encerrando o sistema... Até já!   │')
            print('└────────────────────────────────────────┘\n')
            break
            
        else:
            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
            funcoes.pausar()