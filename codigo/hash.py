
from leitura    import Tabela_carregada
from pathlib    import Path

class Tabela_hash[I, C] (Tabela_carregada):
    """ Tabela Hash de itens do tipo I, com chave do tipo C"""

    # Métodos especiais

    def __init__(
            self
            , tamanho:int
            , caminho:Path  | None = None
            ) -> None:
        # Inicialização da tabela vazia
        self.linhas = [list() for i in range(tamanho)]
        self.tamanho = tamanho
        self.ultima_linha_consultada = []
        if caminho:
            # Inicialização da tabela com um arquivo
            self.carregar_tabela(caminho)
        return

    def __getitem__(self, chave:C) -> I:
        """ Dada uma chave, retorna o item que a contém"""
        linha = self.get_linha(chave)
        for item in linha:
            if self.compara_chaves(item, chave):
                return item
        raise NaoEncontrado(chave)

    def __str__(self) -> str:
        return super().__str__()

    # Métodos proprios

    def compara_chaves(self, item:I, chave:C):
        return chave == self.get_chave(item)

    def get_linha(self, chave:C):
        """ Dada uma chave, retorna a linha na qual o item pode estar"""
        indice = self.hash(chave)
        linha = self.linhas[indice]
        # Salva a linhas
        self.ultima_linha_consultada = linha
        return linha
    
    def get_linha_item(self, item:I) -> list[str]:
        """ Dada um item, retorna a linha na qual ele pode ficar"""
        chave = self.get_chave(item)
        linha = self.get_linha(chave)
        return linha

    def inserir(self, item:I) -> list[I]:
        """ Dado o item, insere ele na tabela"""
        linha = self.get_linha_item(item)
        linha.append(item)
        return linha

    # Métodos abstratos

    def hash(self, chave:C) -> int:
        """ Dada uma chave, retorna o índice da linha na qual o item fica"""
        # Essa função varia para cada tabela
        ...

    def get_chave(self, item:I) -> C:
        """ Dado um item, retorna a chave contida nele"""
        # Essa função varia para cada tabela
        ...

class NaoEncontrado[C](Exception):
    def __init__(self, chave:C) -> None:
        self.chave = chave
        return
    
    def __str__(self) -> str:
        chave = self.chave
        return f"Erro: Item de chave {chave} nao encontrado."
