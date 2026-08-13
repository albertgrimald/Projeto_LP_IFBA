import os

Livros = ['O Poder do Hábito', 'Mais Esperto que o Diabo', 'As Coisas que Você só Vê', 'Steve Jobs', 'Minha História', 'Malcolm X', 'O Senhor dos Anéis', 'Harry Potter', 'O Hobbit', 'O Iluminado', 'It: A Coisa', 'Drácula', 'VIVA', 'Orgulho e Preconceito', 'A Culpa é das Estrelas', 'O Código Da Vinci', 'A Garota no Trem', 'Garota Exemplar', 'O Exorcista', 'O Cemitério', 'Bird Box']

Generos_cadastrados = ['Autoajuda', 'Autoajuda', 'Autoajuda', 'Biografia', 'Biografia', 'Biografia', 'Fantasia', 'Fantasia', 'Fantasia', 'Horror', 'Horror', 'Horror', 'Romance', 'Romance', 'Romance', 'Suspense', 'Suspense', 'Suspense', 'Terror', 'Terror', 'Terror']

Quantidade = [5, 3, 4, 2, 6, 3, 4, 10, 7, 3, 2, 5, 2, 8, 4, 6, 3, 5, 4, 2, 3]

Generos_Base = ['Autoajuda', 'Biografia', 'Fantasia', 'Horror', 'Romance', 'Suspense', 'Terror']

def limpar_tela():
    os.system('cls')

def pausar():
    print('\n' + '─' * 42)
    input('  Pressione [ENTER] para continuar...')

def verificar_senha(senha):
    if senha == senha_adm:
        return True
    return False

def exibir_generos():
    print('\nLISTA DE GÊNEROS')
    for i in range(len(Generos_Base)):
        print(f'{i + 1}. {Generos_Base[i]}', end = ' ')

def cadastrar_livro():
    nome = input('DIGITE O NOME DO LIVRO: ')
    quantidade = int(input('QUANTIDADE: '))
    exibir_generos()
    print()
    escolha = int(input('ESCOLHA O GÊNERO: ')) 
    pos = escolha - 1
    genero_escolhido = Generos_Base[pos]
    Generos_cadastrados.append(genero_escolhido)
    Livros.append(nome)
    Quantidade.append(quantidade)

def ver_genero():
    # 1. Usa a função que você já tem para mostrar os gêneros na tela
    exibir_generos()
    print() # Apenas pula uma linha
    
    # 2. Pergunta qual gênero a pessoa quer olhar
    escolha = int(input('\nDIGITE O NÚMERO DO GÊNERO QUE DESEJA VER: '))
    pos = escolha - 1
    genero_procurado = Generos_Base[pos]
    
    print(f'\n=== LIVROS DO GÊNERO: {genero_procurado} ===')
    print('-----------------------------------------')
    
    # 3. Faz um loop para olhar os livros cadastrados (da posição 0 até o final)
    for i in range(len(Livros)):
        
        # Se o gênero do livro na posição 'i' for igual ao que o usuário escolheu
        if Generos_cadastrados[i] == genero_procurado:
            # Mostra o livro e a quantidade que estão na mesma posição 'i'
            print(f'-> {Livros[i]} | Quantidade: {Quantidade[i]}')

def buscar_por_nome():
    print('\n   === BUSCAR LIVRO POR NOME ===')
    print('-----------------------------------------')
    
    # 1. Pede para o usuário digitar o nome (ou parte do nome) do livro
    nome_busca = input('Digite o nome do livro que deseja buscar: ')
    
    print(f'\n--- Resultado da busca por: {nome_busca} ---')
    encontrou = False
    
    # 2. Passa por todas as posições das listas
    for i in range(len(Livros)):
        
        # 3. Compara se o nome cadastrado é igual ao que o usuário digitou
        if Livros[i] == nome_busca:
            
            # 4. Mostra as informações do livro encontrado
            print(f'-> Livro: {Livros[i]} | Gênero: {Generos_cadastrados[i]} | Qtd: {Quantidade[i]}')
            encontrou = True
            
    # 5. Se não encontrar nenhum livro com esse nome exato
    if not encontrou:
        print('  Nenhum livro encontrado com este nome.')
        
    print('-----------------------------------------')

def ver_estoque_geral():
    print('\n   === ESTOQUE GERAL DE LIVROS ===')
    print('-----------------------------------------')
    
    # 1. Faz um loop que passa por todas as posições (0, 1, 2...) das listas
    for i in range(len(Livros)):
        
        # 2. Pega as informações de cada lista usando a mesma posição 'i'
        nome_do_livro = Livros[i]
        genero_do_livro = Generos_cadastrados[i]
        quantidade_do_livro = Quantidade[i]
        
        # 3. Mostra a linha completa na tela
        print(f'  -> Livro: {nome_do_livro} | Gênero: {genero_do_livro} | Qtd: {quantidade_do_livro}')


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
            elif sub_op == '3':
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
        sup_op = int(input('>: '))
        if sup_op == 1:
            print('┌────────────────────────────────────────┐')
            print('│         VERIFICAR EMPRÉSTIMOS          │')
            print('├────────────────────────────────────────┤')
            print('│  [1] - Empréstimos Ativos              │')
            print('│  [2] - Histórico de Empréstimos        │')
            print('│  [0] - Voltar                          │')
            print('└────────────────────────────────────────┘')
            pausar()
            op = int(input('>: '))
            if op == 1:
                print('┌────────────────────────────────────────┐')
                print('│         EMPRÉSTIMOS ATIVOS             │')
                print('├────────────────────────────────────────┤')
                #AGUARDAR FUNÇÃO DE VER EMPRÉSTIMOS ATIVOS
            elif op == 2:
                print('┌────────────────────────────────────────┐')
                print('│       HISTÓRICO DE EMPRÉSTIMOS         │')
                print('├────────────────────────────────────────┤')
                #AGUARDAR FUNÇÃO DE VER HISTÓRICO DE EMPRÉSTIMOS
            elif op == 0:
                print('┌────────────────────────────────────────┐')
                print('│             VOLTANDO AO MENU           │')
                print('└────────────────────────────────────────┘')
                pausar()
        elif sup_op == 2:
            print('┌────────────────────────────────────────┐')
            print('│           VER MEUS DADOS               │')
            print('├────────────────────────────────────────┤')
            #AGUARDAR FUNÇÃO DE VER DADOS DO ESTUDANTE


    elif op == '0':
        limpar_tela()
        print('┌────────────────────────────────────────┐')
        print('│      Encerrando o sistema... Até já!   │')
        print('└────────────────────────────────────────┘\n')
        break
        
    else:
        print('\n[!] Opção inválida. Escolha uma das opções do menu.')
        pausar()