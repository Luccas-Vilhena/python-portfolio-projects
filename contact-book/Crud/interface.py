import os
def linha(tamanho=30):
    print('-' * tamanho)

def cabecalho(texto):
    linha()
    print(texto)
    linha()

def cor(texto, codigo):
    return f'\033[{codigo}m{texto}\033[m'

def menu(opcoes):
    for i, opcao in enumerate(opcoes, 1):
        print(cor(f'{i}| {opcao}',37))

def pedir_input(mensagem, validador, mensagem_erro):
    while True:
        valor = input(mensagem).strip()
        if validador(valor):
            return valor
        print(cor(mensagem_erro,31))

def confirmar(mensagem):
    resposta = input(f'{mensagem} (S/N): ').strip().upper()
    return resposta == 'S'

def pausar():
    input('\nPressione ENTER para continuar...')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')