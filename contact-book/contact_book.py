import sys

from Crud.file import criar_arquivo
from Crud.interface import menu, cabecalho, cor, pausar
from Crud.contact import adicionar_contato, ver_contatos, excluir_contato

criar_arquivo('agenda.txt')
opcoes = ['Adicionar Contato', 'Ver Contatos', 'Deletar Contato', 'Sair']

while True:
    cabecalho(cor('Menu Principal'.center(30), 36))
    menu(opcoes)

    while True:
        try:
            opcao = int(input('Digite o que deseja fazer: ').strip())
            if 1 <= opcao <= len(opcoes):
                break
            else:
                print(cor('ERRO, Digite apenas uma das opções válida!', 31))
        except ValueError:
            print(cor('ERRO, Digite apenas números!', 31))
        except KeyboardInterrupt:
            print(cor('Encerrando programa...',31))
            sys.exit()

    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        ver_contatos()
    elif opcao == 3:
        excluir_contato()
    elif opcao == 4:
        print(cor('Até logo!', 36))
        break

    pausar()
