import os
from time import sleep
import datetime

Livros = ['O Poder do Hábito', 'Mais Esperto que o Diabo', 'As Coisas que Você só Vê', 'Steve Jobs', 'Minha História', 'Malcolm X', 'O Senhor dos Anéis', 'Harry Potter', 'O Hobbit', 'O Iluminado', 'It: A Coisa', 'Drácula', 'VIVA', 'Orgulho e Preconceito', 'A Culpa é das Estrelas', 'O Código Da Vinci', 'A Garota no Trem', 'Garota Exemplar', 'O Exorcista', 'O Cemitério', 'Bird Box']

Generos_cadastrados = ['Autoajuda', 'Autoajuda', 'Autoajuda', 'Biografia', 'Biografia', 'Biografia', 'Fantasia', 'Fantasia', 'Fantasia', 'Horror', 'Horror', 'Horror', 'Romance', 'Romance', 'Romance', 'Suspense', 'Suspense', 'Suspense', 'Terror', 'Terror', 'Terror']

Quantidade = [5, 3, 4, 2, 6, 3, 4, 10, 7, 3, 2, 5, 2, 8, 4, 6, 3, 5, 4, 2, 3]

Generos_Base = ['Autoajuda', 'Biografia', 'Fantasia', 'Horror', 'Romance', 'Suspense', 'Terror']

Estudantes = [] 

Emprestimos_ativos = []

Historico_emprestimos = [] 

# Estudantes para testar o código

estudante_01 = ["Mychel", '202601']
Estudantes.append(estudante_01)

estudante_02 = ["Albert", '202602']
Estudantes.append(estudante_02)

estudante_03 = ["Wesley", '202603']
Estudantes.append(estudante_03)

estudante_04 = ["Paulo", '202604']
Estudantes.append(estudante_04)

# Índices para facilitar a leitura do código
NOME = 0
MATRICULA = 1

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    print('\n' + '─' * 42)
    input('  Pressione [ENTER] para continuar...')

def verificar_senha(senha):
    if senha == senha_adm:
        return True
    return False

def cadastra_emprestimo():
    print('Digite a Data. Exemplo DD/MM/AAAA')
    data = input('> ')
    estudante_emprstimo=[]
    matricula = input("Digite a matrícula: ")
    estudante = buscar_estudantes(matricula)
    print(f'Nome: {estudante[0]}')
    print(f'Matrícula: {estudante[1]}')

    livro = buscar_por_nome() 

    try:
        Quantidade[livro]-=1
        nome_estudante = estudante[0]
        matricula_estudante = estudante[1]
        esc = Livros[livro]
        estudante_emprstimo.append(nome_estudante )
        estudante_emprstimo.append(matricula_estudante )
        estudante_emprstimo.append(esc )
        estudante_emprstimo.append(data )
        Emprestimos_ativos.append(estudante_emprstimo)
    
        print('Informações')
    
        print(f'Nome: {nome_estudante} - Matrícula: {matricula_estudante} - Livro: {esc} - Data: {data}')
        
        print(f'Finalizado!')
    except TypeError: 
        print('Tente novamente')    

    

def ver_emprestimos():
    for i in Emprestimos_ativos:
        print(i)
        

#============================================ MYCHEL ======================================================

def cadastrar_estudante(): #MYCHEL
    while True:
        nome = input("Digite seu nome completo: ")
        matricula = int(input("Digite o número de sua matrícula: "))

        matricula_disponivel = True
        for estudante in Estudantes:
            if matricula == estudante[MATRICULA]:
                matricula_disponivel = False
                break

        if matricula_disponivel:
            estudante = [nome, matricula]
            Estudantes.append(estudante)
            print(f'Estudante {nome.capitalize()} cadastrado com sucesso!')

        else:
            print("Estudante com matrícula igual já registrado. Voltando ao cadastro...")
            sleep(1)

        continuar = input("Você deseja continuar? [S/N]")
        if continuar.lower() != "s":
            break

def exibir_estudantes(): #MYCHEL
    #limpar_tela()
    for estudante in Estudantes:
        print(f"Nome: {estudante[NOME]}")
        print(f"Matrícula: {estudante[MATRICULA]}")
        print('--------------------------------------')

def buscar_estudantes(matricula): #MYCHEL
    for estudante in Estudantes:
        if estudante[MATRICULA] == matricula:
            return estudante

def editar_estudante():
    while True:
        matricula = input("Digite a matrícula: ")
        estudante = buscar_estudantes(matricula)
        print(f'Nome: {estudante[0]}')
        print(f'Matrícula: {estudante[1]}')
        if estudante:
            novo_nome = input("Digite o novo nome: ")
            nova_matricula = input("Digite a nova matrícula: ")
            equal = False

            if nova_matricula != matricula:
                for estd in Estudantes:
                    if estd[MATRICULA] == nova_matricula:
                        equal = True

                if equal:
                    option = input("Estudante com matrícula equivalente encontrado, impossível prosseguir com a alteração. Deseja tentar novamente? [S/N]")
                    if option.lower() != "s":
                        break

                else:
                    estudante[MATRICULA] = nova_matricula
                    estudante[NOME] = novo_nome
                    print("Alteração concluída com sucesso. Retornando...")
                    sleep(2)
                    break
            else:
                estudante[NOME] = novo_nome
                print("Alteração concluída com sucesso. Retornando...")
                sleep(2)
                break

        else:
            option = input("Matrícula não encontrada. Tentar novamente? [S/N]")
            if option.lower() != "s":
                break

def remover_estudante(): #MYCHEL
    matricula = int(input("Digite a matrícula do estudante que deseja remover: "))

    estudante_encontrado = False
    for estudante in Estudantes:
        if estudante[MATRICULA] == matricula:
            confirmacao = input(f"Confirma a remoção de {estudante[NOME]}? [S/N]: ")
            if confirmacao.lower() == "s":
                Estudantes.remove(estudante)
                print(f"Estudante {estudante[NOME]} removido com sucesso!")
            else:
                print("Remoção cancelada.")
            estudante_encontrado = True
            break

    if not estudante_encontrado:
        print("Nenhum estudante encontrado com essa matrícula.")

#=============================================================================================================

#=============================================== ALBERT ======================================================

def exibir_generos():
    print('\nLISTA DE GÊNEROS')
    for i in range(len(Generos_Base)):
        print(f'{i + 1}. {Generos_Base[i]}', end = ' ')



def cadastrar_livro():
    while True:
        nome = input('DIGITE O NOME DO LIVRO: ')
        quantidade = int(input('QUANTIDADE: '))
        
        if nome in Livros:
            posicao = Livros.index(nome) 
            Quantidade[posicao] += quantidade  
            print(f'\nLivro já existente! Foram adicionadas {quantidade} unidades ao estoque.')
        
        else:
            exibir_generos()
            print()
            escolha = int(input('ESCOLHA O GÊNERO: ')) 
            pos = escolha - 1
            genero_escolhido = Generos_Base[pos]
            
            Generos_cadastrados.append(genero_escolhido)
            Livros.append(nome)
            Quantidade.append(quantidade)
            print('\nLivro cadastrado com sucesso!')
        opcao = input('\nDigite [1] para cadastrar outro livro ou [0] para sair: ')
        if opcao == '0':
            break

def ver_genero():
    exibir_generos()
    print() 
    
    escolha = int(input('\nDIGITE O NÚMERO DO GÊNERO QUE DESEJA VER: '))
    pos = escolha - 1
    genero_procurado = Generos_Base[pos]
    
    print(f'\n=== LIVROS DO GÊNERO: {genero_procurado} ===')
    print('-----------------------------------------')
    if genero_procurado not in Generos_cadastrados:
        print('  Nenhum livro cadastrado neste gênero.')
    else:
        for i in range(len(Livros)):       
            if Generos_cadastrados[i] == genero_procurado:
                print(f'-> {Livros[i]} | Quantidade: {Quantidade[i]}')

def buscar_por_nome():
    print('\n   === BUSCAR LIVRO POR NOME ===')
    print('-----------------------------------------')
    
    nome_busca = input('Digite o nome do livro que deseja buscar: ')
    
    print(f'\n--- Resultado da busca por: {nome_busca} ---')
    encontrou = False
    
    for i in range(len(Livros)):
        
        if Livros[i] == nome_busca:
            
            print(f'-> Livro: {Livros[i]} | Gênero: {Generos_cadastrados[i]} | Qtd: {Quantidade[i]}')
            encontrou = True

            return i
            
    if not encontrou:
        print('  Nenhum livro encontrado com este nome.')
        
    print('-----------------------------------------')

def ver_estoque_geral():
    print('\n   === ESTOQUE GERAL DE LIVROS ===')
    print('-----------------------------------------')
    if len(Livros) == 0:
        print('  Nenhum livro cadastrado no estoque.')
    else:
        for i in range(len(Livros)):
            
            nome_do_livro = Livros[i]
            genero_do_livro = Generos_cadastrados[i]
            quantidade_do_livro = Quantidade[i]
            
            print(f'  -> Livro: {nome_do_livro} | Gênero: {genero_do_livro} | Qtd: {quantidade_do_livro}')


#================================================================================================================

#=============================================== PAULO ==========================================================
def emprestimos_ativos(matricula):
    limpar_tela()
    print('=== Empréstimos Ativos ===')
    encontrou = False

    for emprestimo in Emprestimos_ativos:
        if emprestimo[0] == matricula:
            print(f"Livro: {emprestimo[1]}")
            print(f"Data do empréstimo: {emprestimo[2]}")
            print("-" * 40)
            encontrou = True

    if not encontrou:
        print("Você não possui empréstimos ativos.")
    pausar()



def historico_emprestimos(matricula):
    limpar_tela()
    print('=== Histórico de Empréstimos ===')
    encontrou = False

    for emprestimo in Historico_emprestimos:
        if emprestimo[0] == matricula:
            print(f"Livro: {emprestimo[1]}")
            print(f"Data do empréstimo: {emprestimo[2]}")
            print("-" * 40)
            encontrou = True

    if not encontrou:
        print("Você ainda não possui histórico de empréstimos.")
    pausar()


def dados_estudante(matricula):
    limpar_tela()
    print('=== Dados do Estudante ===')
    estudante = buscar_estudantes(matricula)

    print("\n=== MEUS DADOS ===")

    if estudante:
        print(f"Nome: {estudante[NOME]}")
        print(f"Matrícula: {estudante[MATRICULA]}")
    else:
        print("Estudante não encontrado.")
    pausar()

#================================================================================================================
senha_adm = '4321'

#============================================= SISTEMA PRINCIPAL ================================================

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
            while True:
                limpar_tela()
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
                    limpar_tela()
                    print('┌────────────────────────────────────────┐')
                    print('│            NOVO EMPRÉSTIMO             │')
                    print('└────────────────────────────────────────┘')
                    """
                    cliente = input('  Matrícula do Cliente: ')
                    livro = input('  Nome do Livro: ')
                    data = input('  Data do Empréstimo: ')
                    """
                    cadastra_emprestimo()
                    pausar()

                elif sub_op == '2':
                    while True:
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
                        op = int(input('\n> Opção: '))
                        if op == 1:
                            cadastrar_estudante()
                        elif op == 2:
                            matricula = input("Digite a matrícula do estudante que deseja pesquisar: ")
                            dados_estudante(matricula)
                        elif op == 3:
                            editar_estudante()
                            
                        elif op == 4:
                            remover_estudante()
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            pausar()

                elif sub_op == '3':
                    while True:
                        limpar_tela()
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
                            cadastrar_livro()
                            pausar()
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│         VER ESTOQUE COMPLETO           │')
                            print('├────────────────────────────────────────┤')
                            ver_estoque_geral()
                            pausar()

                        elif op == 3:
                            print('┌────────────────────────────────────────┐')
                            print('│            BUSCAR POR GÊNERO           │')
                            print('├────────────────────────────────────────┤')
                            ver_genero()
                            pausar()

                        elif op == 4:
                            print('┌────────────────────────────────────────┐')
                            print('│             BUSCAR POR NOME            │')
                            print('├────────────────────────────────────────┤')
                            buscar_por_nome()
                            pausar()
                        elif op == 0:
                            break

                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            pausar()
                elif sub_op == '4':
                    while True:
                        limpar_tela()
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
                            ver_emprestimos()
                            pausar()
                            #AGUARDAR FUNÇÃO DE VER EMPRÉSTIMOS ATIVOS
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│       HISTÓRICO DE EMPRÉSTIMOS         │')
                            print('├────────────────────────────────────────┤')
                            pausar()
                            historico_emprestimos(matricula)
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            pausar()

                elif sub_op == '5':
                    while True:
                        limpar_tela()
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
                            pausar()
                            print('Em breve, função de registrar devolução estará disponível.')
                        elif op == 2:
                            print('┌────────────────────────────────────────┐')
                            print('│       HISTÓRICO DE DEVOLUÇÕES          │')
                            print('├────────────────────────────────────────┤')
                            pausar()
                            print('Em breve, função de histórico de devoluções estará disponível.')
                        elif op == 0:
                            break
                        else:
                            print('\n[!] Opção inválida. Escolha uma das opções do menu.')
                            pausar()

        else:
            print('\n[!] Senha incorreta! Acesso negado.')
            pausar()

    elif op == '2':
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│            ACESSO ESTUDANTE            │')
        print('└────────────────────────────────────────┘')
        mat = input('  Digite sua Matricúla: ')
        if mat in Estudantes:
            limpar_tela()
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
                    emprestimos_ativos(mat)
                elif op == 2:
                    print('┌────────────────────────────────────────┐')
                    print('│       HISTÓRICO DE EMPRÉSTIMOS         │')
                    print('├────────────────────────────────────────┤')
                    historico_emprestimos(mat)
                    
                elif op == 0:
                    print('┌────────────────────────────────────────┐')
                    print('│             VOLTANDO AO MENU           │')
                    print('└────────────────────────────────────────┘')
                    pausar()
                
            elif sup_op == 2:
                print('┌────────────────────────────────────────┐')
                print('│           VER MEUS DADOS               │')
                print('├────────────────────────────────────────┤')
                dados_estudante(mat)
            elif sup_op == 3:
                print('┌────────────────────────────────────────┐')
                print('│            BUSCAR POR GÊNERO           │')
                print('├────────────────────────────────────────┤')
                ver_genero()
                pausar()

            elif sup_op == 4:
                print('┌────────────────────────────────────────┐')
                print('│             BUSCAR POR NOME            │')
                print('├────────────────────────────────────────┤')
                buscar_por_nome()
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