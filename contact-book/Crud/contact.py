
from Crud.file import adicionar_arquivo, ler_arquivo, contar_contatos, deletar_contato, telefone_existe
from Crud.interface import linha, cor,confirmar


def adicionar_contato():
    linha()
    print(cor('Adicionar Contato'.center(30), 32))
    linha()
    while True:
        nome = input('Digite o nome: ').strip().capitalize()
        if nome:
            break
        print(cor('ERRO, o nome não pode ficar vazio!', 31))
    sobre = input('Digite o sobrenome: ').strip().capitalize()
    while True:
        telefone = input('Digite o número do contato: ').strip()
        if not (telefone.isdigit() and len(telefone) == 11):
            print(cor('ERRO, digite um telefone com 11 números!', 31))
        elif telefone_existe('agenda.txt', telefone):
            print(cor('ERRO, já existe um contato com esse número!', 31))
        else:
            adicionar_arquivo('agenda.txt', f'{nome};{sobre};{telefone}')
            print(f'O contato de {nome} foi salvo com sucesso.')
            break

def ver_contatos():
    total = contar_contatos('agenda.txt')
    linha()
    print(cor(f'Contatos Salvos [{total}]'.center(35), 35))
    linha()
    if total == 0:
        print(cor('Nenhum contato cadastrado ainda', 33))
    else:
        ler_arquivo('agenda.txt')

def excluir_contato():
    linha()
    print(cor('Deletar Contato'.center(30), 36))
    linha()
    if contar_contatos('agenda.txt') == 0:
        print(cor('Nenhum contato cadastrado para deletar.', 33))
    else:
        ler_arquivo('agenda.txt')
        telefone = input('Digite o telefone do contato a deletar: ').strip()
        if confirmar(f'Tem certeza que deseja deletar o contato com telefone {telefone}?'):
            if deletar_contato('agenda.txt', telefone):
                print(cor('Contato deletado com sucesso!', 32))
            else:
                print(cor('Telefone não encontrado!', 31))
        else:
            print(cor('Operação Cancelada.', 33))