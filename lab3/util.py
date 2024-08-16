"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from typing import Protocol, Self

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Comparavel(Protocol):
    " Pode ser comparado."

    def __lt__(self, outro: Self) -> bool:
        ...

    def __gt__(self, outro: Self) -> bool:
        ...

    def __le__(self, outro: Self) -> bool:
        ...

    def __ge__(self, outro: Self) -> bool:
        ...

type Ordenavel[C:Comparavel] = list[C]
" Lista modificável de componentes comparáveis."

class Printavel(Protocol):
    def __str__(self) -> str:
        ...

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Básicos de ordenamento

def swap            (
        lista:  list,   # Lista a ser modificada
        i:      int,    # Índice de troca
        j:      int,    # Índice de troca
        ) ->    None:
    """ Troca o conteúdo da lista nos índices i e j """

    # Troca os elementos de lugar
    segura   = lista[i]
    lista[i] = lista[j]
    lista[j] = segura

    # Retorna a lista modificada
    return

def inserir         [C:Comparavel](
        fonte:      C,
        destino:    Ordenavel[C]
        ) ->        None:

    # Faixa de busca da inserção
    min = 0
    max = len(destino) - 1

    while min != max:
        mid = (min + max) // 2
        if fonte > destino[mid]:
            min = mid
        else:
            max = mid
    
    destino.insert(min, fonte)

    return

def insertion_sort  (
        lista   :Ordenavel
        ) ->    None:

    # Separa a lista em parte ordenada e desordenada
    desordenada = lista
    ordenada = []

    # Remove os elementos da desordenada
    # Insere na ordenada, mantendo a ordem
    # Até a desordenada estar vazia
    while desordenada:
        elemento = desordenada.pop(0)
        inserir(elemento, ordenada)

    # Aplica
    lista = ordenada

    return

# Leitura de arquivos e tokenização

def remover_vazios  (
        lista   :list
        ) ->    None:
    " Remove todas strings vazias de uma lista "

    ok = True
    while ok:
        try:
            lista.remove('')
        except:
            ok = False

    return

def ler_lista       (
        nome_arquivo    :str
        ) ->            list[str]:
    """
    Lê  um arquivo e separa em uma lista de strings, usando qualquer caractere de separação.
    """

    with open(nome_arquivo, 'r') as arquivo:
        palavras = arquivo.read().split()

    return palavras

def ler_matriz      (
        nome_arquivo    :str
        ) ->            list[list[str]]:
    """
    Lê o arquivo, separando por linhas e colunas de acordo com espaços e linhas do arquivo.
    """

    matriz = []

    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                # Remover espaços em branco extras e dividir a linha em elementos
                elementos = linha.strip().split()
                matriz.append(elementos)

        for lista in matriz:
            lista.pop(0)

        return matriz

    except FileNotFoundError:

        raise Exception(f'Arquivo "{nome_arquivo}" não foi encontrado.')

def imprimir_linhas (fonte:list[Printavel], destino:str):
    with open(destino, 'w') as arquivo:

        while len(fonte) > 1:
            linha = fonte.pop(0)
            print(linha, file=arquivo)

        # Imprime a última linha sem criar nova linha
        linha = fonte.pop(0)
        print(linha, file=arquivo, end='')

        return