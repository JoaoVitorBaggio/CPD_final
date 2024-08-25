
from hash       import Tabela_hash
from typing     import Self
from pathlib    import Path

class Jogador:
    """ Dados de um jogador"""

    def __init__(
            self
            , sofifa_id :int | str
            , nome      :str
            , posicoes  :str
            ) -> None:
        self.sofifa_id  = int(sofifa_id)
        self.nome       = nome
        self.posicoes   = posicoes
        return

    def __str__(self) -> str:
        # Imprime os dados do jogador
        return f"{self.sofifa_id} {self.nome}"

class Tabela_Jogadores (Tabela_hash[Jogador, int]):
    """ Tabela que busca os jogadores pelo id"""

    def __init__(self, caminho: Path, tamanho: int) -> None:
        super().__init__(caminho, tamanho)
        self.carregar_tabela(caminho, remover_cabeçalho=True)
        return

    def hash(self, chave: int) -> int:
        return chave % self.tamanho

    def get_chave(self, item: Jogador) -> int:
        return item.sofifa_id

    def carregar_item(self, linha: list[str]) -> Self:
        self.inserir(Jogador(*linha))
        return self
