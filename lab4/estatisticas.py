
from pathlib    import Path
from hash       import *
from typing     import Self

class Estatisticas:
    def __init__(self, tamanho_hash:int) -> None:
        # Estatisticas da tabela
        self.tamanho_hash       = tamanho_hash
        self.numero_ocupadas    = 0
        self.tamanho_maximo     = 0
        self.numero_itens       = 0

        # Estatisticas das consultas
        self.testes_maximo      = 0
        self.testes_totais      = 0
        self.itens_encontrados  = 0
        # Ultima consulta
        self.testes_ultima      = 0

        return
    
    # Estatísticas derivadas dos dados coletados

    def tamanho_medio(self) -> float:
        return self.numero_itens     / self.numero_ocupadas
    
    def taxa_ocupacao(self) -> float:
        return self.numero_ocupadas  / self.tamanho_hash

    def testes_media(self) -> float:
        return self.testes_totais    / self.itens_encontrados

class Hash_estatistica[I, C](Tabela_hash[I, C]):
    """ Classe de tabela hash que calcula as estatísticas pedidas no experimento.
    Em todos metodos, chama o metodo da superclasse e faz registros"""

    def __init__(self, caminho: Path, tamanho: int):
        # Inicializa as estatisticas e a tabela
        self.estatisticas = Estatisticas(tamanho)
        super().__init__(tamanho=tamanho, caminho=caminho)

    def __getitem__(self, chave: C) -> I:
        # Nova consulta, zera o numero de testes
        self.estatisticas.testes_ultima = 0
        try:
            # Encontra um item
            item = super().__getitem__(chave)
            # Um item encontrado
            self.estatisticas.itens_encontrados += 1
            # Registra numero de testes
            numero_de_testes = self.estatisticas.testes_ultima
            # Incrementa o total de testes
            self.estatisticas.testes_totais += numero_de_testes
            # Testa para o maximo de testes
            if numero_de_testes > self.estatisticas.testes_maximo:
                self.estatisticas.testes_maximo = numero_de_testes
            # Retorna o item encontrado
            return item
        except NaoEncontrado as excecao:
            # Propaga a exceção
            raise excecao

    def compara_chaves(self, item: I, chave: C):
        # Cada teste de chave, incrementa o numero de testes nesta consulta
        self.estatisticas.testes_ultima += 1
        return super().compara_chaves(item, chave)

    def inserir(self, item: I) -> Self:
        super().inserir(item)
        linha = self.ultima_linha_consultada
        # Se acabamos de inserir o primeiro elemento de uma lista
        if len(linha) == 1:
            # O número de listas ocupadas aumentou
            self.estatisticas.numero_ocupadas += 1
        # Se a linha lida foi a maior já criada
        if len(linha) > self.estatisticas.tamanho_maximo:
            # Registra o comprimento dela
            self.estatisticas.tamanho_maximo = len(linha)
        # Número de itens aumentou
        self.estatisticas.numero_itens += 1
        return linha
