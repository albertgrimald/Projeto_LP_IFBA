import listas
from time import sleep
import os

def limpar_tela():
    os.system('cls')

def pausar():
    print('\n' + '─' * 42)
    input('  Pressione [ENTER] para continuar...')

def verificar_senha(senha):
    if senha == listas.senha_adm:
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
        listas.Quantidade[livro]-=1
        nome_estudante = estudante[0]
        matricula_estudante = estudante[1]
        esc = listas.Livros[livro]
        estudante_emprstimo.append(nome_estudante )
        estudante_emprstimo.append(matricula_estudante )
        estudante_emprstimo.append(esc )
        estudante_emprstimo.append(data )
        listas.Emprestimos_ativos.append(estudante_emprstimo)
    
        print('Informações')
    
        print(f'Nome: {nome_estudante} - Matrícula: {matricula_estudante} - Livro: {esc} - Data: {data}')
        
        print(f'Finalizado!')
    except TypeError: 
        print('Tente novamente')    

    

def ver_emprestimos():
    for i in listas.Emprestimos_ativos:
        print(i)
        

#============================================ MYCHEL ======================================================

def cadastrar_estudante(): #MYCHEL
    while True:
        nome = input("Digite seu nome completo: ")
        matricula = int(input("Digite o número de sua matrícula: "))

        matricula_disponivel = True
        for estudante in listas.Estudantes:
            if matricula == estudante[listas.MATRICULA]:
                matricula_disponivel = False
                break

        if matricula_disponivel:
            estudante = [nome, matricula]
            listas.Estudantes.append(estudante)
            print(f'Estudante {nome.capitalize()} cadastrado com sucesso!')

        else:
            print("Estudante com matrícula igual já registrado. Voltando ao cadastro...")
            sleep(1)

        continuar = input("Você deseja continuar? [S/N]")
        if continuar.lower() != "s":
            break

def exibir_estudantes(): #MYCHEL
    #limpar_tela()
    for estudante in listas.Estudantes:
        print(f"Nome: {estudante[listas.NOME]}")
        print(f"Matrícula: {estudante[listas.MATRICULA]}")
        print('--------------------------------------')

def buscar_estudantes(matricula): #MYCHEL
    for estudante in listas.Estudantes:
        if estudante[listas.MATRICULA] == matricula:
            return estudante

def editar_estudante():
    while True:
        matricula = input("Digite a matrícula: ")
        estudante = buscar_estudantes(matricula)
        print(f'Nome: {estudante[listas.NOME]}')
        print(f'Matrícula: {estudante[listas.MATRICULA]}')
        if estudante:
            novo_nome = input("Digite o novo nome: ")
            nova_matricula = input("Digite a nova matrícula: ")
            equal = False

            if nova_matricula != matricula:
                for estd in listas.Estudantes:
                    if estd[listas.MATRICULA] == nova_matricula:
                        equal = True

                if equal:
                    option = input("Estudante com matrícula equivalente encontrado, impossível prosseguir com a alteração. Deseja tentar novamente? [S/N]")
                    if option.lower() != "s":
                        break

                else:
                    estudante[listas.MATRICULA] = nova_matricula
                    estudante[listas.NOME] = novo_nome
                    print("Alteração concluída com sucesso. Retornando...")
                    sleep(2)
                    break
            else:
                estudante[listas.NOME] = novo_nome
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
    for estudante in listas.Estudantes:
        if estudante[listas.MATRICULA] == matricula:
            confirmacao = input(f"Confirma a remoção de {estudante[listas.NOME]}? [S/N]: ")
            if confirmacao.lower() == "s":
                listas.Estudantes.remove(estudante)
                print(f"Estudante {estudante[listas.NOME]} removido com sucesso!")
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
    for i in range(len(listas.Generos_Base)):
        print(f'{i + 1}. {listas.Generos_Base[i]}', end = ' ')



def cadastrar_livro():
    while True:
        nome = input('DIGITE O NOME DO LIVRO: ')
        quantidade = int(input('QUANTIDADE: '))
        
        if nome in listas.Livros:
            posicao = listas.Livros.index(nome) 
            listas.Quantidade[posicao] += quantidade  
            print(f'\nLivro já existente! Foram adicionadas {quantidade} unidades ao estoque.')
        
        else:
            exibir_generos()
            print()
            escolha = int(input('ESCOLHA O GÊNERO: ')) 
            pos = escolha - 1
            genero_escolhido = listas.Generos_Base[pos]
            
            listas.Generos_cadastrados.append(genero_escolhido)
            listas.Livros.append(nome)
            listas.Quantidade.append(quantidade)
            print('\nLivro cadastrado com sucesso!')
        opcao = input('\nDigite [1] para cadastrar outro livro ou [0] para sair: ')
        if opcao == '0':
            break

def ver_genero():
    exibir_generos()
    print() 
    
    escolha = int(input('\nDIGITE O NÚMERO DO GÊNERO QUE DESEJA VER: '))
    pos = escolha - 1
    genero_procurado = listas.Generos_Base[pos]
    
    print(f'\n=== LIVROS DO GÊNERO: {genero_procurado} ===')
    print('-----------------------------------------')
    if genero_procurado not in listas.Generos_cadastrados:
        print('  Nenhum livro cadastrado neste gênero.')
    else:
        for i in range(len(listas.Livros)):       
            if listas.Generos_cadastrados[i] == genero_procurado:
                print(f'-> {listas.Livros[i]} | Quantidade: {listas.Quantidade[i]}')

def buscar_por_nome():
    print('\n   === BUSCAR LIVRO POR NOME ===')
    print('-----------------------------------------')
    
    nome_busca = input('Digite o nome do livro que deseja buscar: ')
    
    print(f'\n--- Resultado da busca por: {nome_busca} ---')
    encontrou = False
    
    for i in range(len(listas.Livros)):
        
        if listas.Livros[i] == nome_busca:
            
            print(f'-> Livro: {listas.Livros[i]} | Gênero: {listas.Generos_cadastrados[i]} | Qtd: {listas.Quantidade[i]}')
            encontrou = True

            return i
            
    if not encontrou:
        print('  Nenhum livro encontrado com este nome.')
        
    print('-----------------------------------------')

def ver_estoque_geral():
    print('\n   === ESTOQUE GERAL DE LIVROS ===')
    print('-----------------------------------------')
    if len(listas.Livros) == 0:
        print('  Nenhum livro cadastrado no estoque.')
    else:
        for i in range(len(listas.Livros)):
            
            nome_do_livro = listas.Livros[i]
            genero_do_livro = listas.Generos_cadastrados[i]
            quantidade_do_livro = listas.Quantidade[i]
            
            print(f'  -> Livro: {nome_do_livro} | Gênero: {genero_do_livro} | Qtd: {quantidade_do_livro}')


#================================================================================================================

#=============================================== PAULO ==========================================================
def emprestimos_ativos(matricula):
    limpar_tela()
    print('=== Empréstimos Ativos ===')
    encontrou = False

    for emprestimo in listas.Emprestimos_ativos:
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

    for emprestimo in listas.Historico_emprestimos:
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
        print(f"Nome: {estudante[listas.NOME]}")
        print(f"Matrícula: {estudante[listas.MATRICULA]}")
    else:
        print("Estudante não encontrado.")
    pausar()