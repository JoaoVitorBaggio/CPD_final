
from hash       import Tabela_hash
from leitura    import Carregavel
from pandas     import Series
from typing     import Self
from pathlib    import Path

class Jogador:
    """ Dados de um jogador"""

    def __init__(
            self
            , sofifa_id     :int | None = None
            , nome_curto    :str | None = None
            , nome_longo    :str | None = None
            , posicoes      :str | None = None
            , nacionalidade :str | None = None
            , nome_clube    :str | None = None
            , nome_liga     :str | None = None
            ) -> None:

        self.sofifa_id      = sofifa_id
        self.nome_curto     = nome_curto
        self.nome_longo     = nome_longo
        self.posicoes       = posicoes
        self.nacionalidade  = nacionalidade
        self.nome_clube     = nome_clube
        self.nome_liga      = nome_liga

        self.avaliacoes     = 0
        self.nota_total     = 0
        self.valor_media    = None
        self.media_correta  = True

        return

    def avaliar(self, nota:float) -> Self:
        self.nota_total += nota
        self.avaliacoes += 1
        self.media_correta = False
        return Self

    def media(self) -> float:
        if not self.media_correta:
            self.recalcula_media()
        return self.valor_media

    def recalcula_media(self) -> Self:
        try:
            self.valor_media = self.nota_total / self.avaliacoes
        except ZeroDivisionError:
            self.valor_media = None
        return Self

    def __str__(self) -> str:
        # Imprime os dados do jogador
        return f"""{""
        }sofifa_id           {self.sofifa_id     }{"\n"
        }short_name          {self.nome_curto    }{"\n"
        }long_name           {self.nome_longo    }{"\n"
        }player_positions    {self.posicoes      }{"\n"
        }nationality         {self.nacionalidade }{"\n"
        }club_name           {self.nome_clube    }{"\n"
        }league_name         {self.nome_liga     }{"\n"
        }rating              {self.media()       }{""
        }
        """

class Tabela_Jogadores (
    Tabela_hash[Jogador, int],
    Carregavel
    ):

    """ Tabela que busca os jogadores pelo id"""

    def __init__(
            self
            , tamanho: int
            , caminho: Path | None = None
            ) -> None:
        
        super().__init__(tamanho)

        if caminho:
            self.carregar_arquivo(caminho)

        return

    def hash(self, chave: int) -> int:
        return chave % self.tamanho

    def get_chave(self, item: Jogador) -> int:
        return item.sofifa_id

    def carregar_item(self, linha: Series) -> Self:
        self.inserir(Jogador(
            sofifa_id      = linha["sofifa_id"],
            nome_curto     = linha["short_name"],
            nome_longo     = linha["long_name"],
            posicoes       = linha["player_positions"],
            nacionalidade  = linha["nationality"],
            nome_clube     = linha["club_name"],
            nome_liga      = linha["league_name"],
        ))
        return self
