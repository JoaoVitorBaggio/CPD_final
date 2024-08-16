"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from util import *

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def radix_sort          (
        linhas: list[str],  # Lista de linhas a ser ordenada, sem prefixo
        indice: int = 0,    # Índice a ser usado para separar as linhas
        ) ->    None:
    """
    Ordena a lista de strings apontada por "linhas"
    A partir do caractere de índice "indice", í.e:
        Pressupõe que os caracteres anteriores
        são iguais para todas as linhas, ex.:
            índice = 6
            linhas = [
                dddeeeaab,
                dddeeebbb,
                dddeeeaac,
                dddeeebba]
    """

    """
    Ordem das variáveis:
        Quantos índices são necessários indexar
            para que se obtenha um char.
        Sequências de evolução de ordem:
            O(0)    O(1)    O(2)        O(3)
            char    str     list[str]   list[list[str]]
            letra   linha   linhas
                            fila        filas
        Operações permitidas se N>0:
            O(N-1) = O(N)[i]        # Leitura
            O(N+1)[i] = O(N)        # Escrita
            O(N) = O(N) + O(N)      # Concatenação
            O(N) += O(N)            # Autoconcatenação
            O(N) = O(N+1).pop(i)    # Pop
            O(N+1).append(O(N))     # Append
    """

    # Inicia as filas
    # 256 filas vazias, uma para cada caractere ascii
    filas = []
    for i in range(256):
        filas.append([])

    # Coloca cada linha na fila certa
    while linhas:
        # Pega a primeira linha
        linha = linhas.pop(0)
        # Se houver letra
        if indice < len(linha):
            # Caractere indexado da linha
            letra = linha[indice]
            # Ascii do caractere
            codigo = ord(letra)
        # Senão
        else:
            codigo = 0
        # Adiciona à fila
        fila = filas[codigo]
        fila.append(linha)

    # Linhas está vazia

    # Remove a primeira fila
    # Pois essas linhas já foram completamente lidas
    fila0 = filas.pop(0)
    linhas += fila0

    # Ordena cada uma das filas e adiciona às linhas
    for fila in filas:
        match len(fila):
            case 0:
                pass
            case 1:
                # Adiciona às linhas
                linhas += fila
            case _:
                # Ordena as filas a partir do proximo indice
                radix_sort(fila, indice = indice + 1)
                # Adiciona às linhas
                linhas += fila
    return