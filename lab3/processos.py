"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from util      import *
from radixsort import radix_sort
from quicksort import *
# from icecream  import ic

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Contagem:
    def  __init__(self, palavra:str, quantidade:int=0) -> None:
        self.palavra = palavra
        self.quantidade = quantidade
        return

    def __str__(self) -> str:
        linha = f"{self.palavra} {self.quantidade}"
        return linha

    def contar(self, palavra:str) -> bool:
        if palavra == self.palavra:
            self.quantidade += 1
            return True
        else:
            return False

class qs_quantidade(quick_sort[Contagem, int]):
    # Ordena contagen com base no atributo quantidade
    def criterio(self, elemento: Contagem) -> int:
        return - elemento.quantidade

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç Õ E S   F U N Ç 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def criar_sorted(nome):
    """
    Lê um aquivo na pasta de entrada e cria uma
    versão em ordem alfabética, na pasta de saída.
    """

    # Caminhos
    caminho_entrada = f"entradas/{nome}.txt"
    caminho_saida   = f"saidas/{nome}_sorted.txt"

    # Lê a entrada
    palavras = ler_lista(caminho_entrada)

    # Ordena
    radix_sort(palavras)

    # Imprime a saída no arquivo
    imprimir_linhas(palavras, caminho_saida)

def criar_counted(nome):
    """
    Lê um aquivo _sorted e cria uma versao _counted.
    """

    # Caminhos
    caminho_entrada = f"saidas/{nome}_sorted.txt"
    caminho_saida   = f"saidas/{nome}_counted.txt"

    # Lê a entrada
    palavras = ler_lista(caminho_entrada)

    # Conta
    contagens = []
    contador = Contagem(palavras[0])
    for palavra in palavras:
        # Se a palavra for diferente
        if not contador.contar(palavra):
            # Salva o contador no array
            contagens.append(contador)
            # Inicia um novo contador
            contador = Contagem(palavra, quantidade=1)

    # Imprime a saída no arquivo
    imprimir_linhas(contagens, caminho_saida)

def criar_ranked(nome):
    """
    Lê um aquivo _counted e cria uma versao _ranked.
    """

    # Caminhos
    caminho_entrada = f"saidas/{nome}_counted.txt"
    caminho_saida   = f"saidas/{nome}_ranked.txt"

    # Lê a entrada
    with open(caminho_entrada) as arquivo:
        linhas = arquivo.readlines()

    # Transforma em contagens
    contagens = []
    for linha in linhas:
        par = linha.split()
        palavra = par[0]
        quantidade = int(par[1])
        contador = Contagem(palavra, quantidade=quantidade)
        contagens.append(contador)

    # Ordena
    qs_rank(contagens, 2000)

    # Imprime a saída no arquivo
    imprimir_linhas(contagens, caminho_saida)

def qs_rank(fonte: list[Contagem], comprimento_final:int):
    # Ordena com base no atributo quantidade
    qs_quantidade(fonte)

    # Corta os elemntos fora do ranking
    comprimento_inicial = len(fonte)
    while len(fonte) > comprimento_final:
        fonte.pop()

    return
