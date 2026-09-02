
def criar_arquivo(nome):
    try:
        with open(nome, 'x'):
            pass
    except FileExistsError:
        pass
    except OSError:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'r')
        for linha in arquivo:
            dados = linha.strip().split(';')
            nome_contato = dados[0]
            sobrenome_contato = dados[1]
            telefone_contato = dados[2]
            print(f'Nome: {nome_contato}')
            print(f'Sobrenome: {sobrenome_contato if sobrenome_contato else "-"}')
            print(f'Telefone: {telefone_contato}')
            print('-' * 30)
        arquivo.close()
    except Exception as e:
        print('Houve um erro ao ler o arquivo!')

def adicionar_arquivo(nome, texto):
    with open(nome, 'a') as arquivo:
        arquivo.write(texto + '\n')

def deletar_contato(caminho, telefone):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    linhas_restantes = []
    encontrado = False
    for linha in linhas:
        dados = linha.strip().split(';')
        if len(dados) == 3 and dados[2] == telefone:
            encontrado = True
            continue
        linhas_restantes.append(linha)
    if not encontrado:
        return False
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas_restantes)
    return True

def contar_contatos(caminho='agenda.txt'):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return sum(1 for linha in f if linha.strip())
    except FileNotFoundError:
        return 0

def telefone_existe(caminho, telefone):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(';')
                if len(dados) == 3 and dados[2] == telefone:
                    return True
    except FileNotFoundError:
        return False
    return False