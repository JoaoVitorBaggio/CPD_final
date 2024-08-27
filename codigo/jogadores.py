
from hash       import Tabela_hash
from leitura    import Carregavel
from quicksort  import quick_sort

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
        self.valor_media    = -1
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

    def imprimir(self) -> str:
        # Imprime os dados em várias linhas
        print(f"""{""
        }sofifa_id          {self.sofifa_id     }{"\n"
        }short_name         {self.nome_curto    }{"\n"
        }long_name          {self.nome_longo    }{"\n"
        }player_positions   {self.posicoes      }{"\n"
        }nationality        {self.nacionalidade }{"\n"
        }club_name          {self.nome_clube    }{"\n"
        }league_name        {self.nome_liga     }{"\n"
        }rating             {self.media()       }{"\n"
        }count              {self.avaliacoes    }
        """)

    def __str__(self) -> str:
        # Imprime os dados do jogador em uma linha
        return f"""{""
        }{self.sofifa_id     }{", "
        }{self.nome_curto    }{", "
        }{self.nome_longo    }{", "
        }{self.posicoes      }{", "
        }{self.nacionalidade }{", "
        }{self.nome_clube    }{", "
        }{self.nome_liga     }{", "
        }{self.media()       }{", "
        }{self.avaliacoes    }{""
        }"""

class Tabela_Jogadores (
    Tabela_hash[Jogador, int],
    Carregavel
    ):

    """ Tabela que busca os jogadores pelo id"""

    def __init__(
            self
            , tamanho: int = 36007
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

    def imprimir_jogadores(self, jogadores:list[Jogador]):
        string_de_formato = "{:<10} {:<20} {:<40} {:<18} {:<20} {:<30} {:<40} {:<10} {:<10}"
        if jogadores:
            print(string_de_formato.format(
                "sofifa_id",
                "short_name",
                "long_name",
                "player_positions",
                "nationality",
                "club_name",
                "league_name",
                "rating",
                "count",
                ))
            for jogador in jogadores:            
                print(string_de_formato.format(
                jogador.sofifa_id,
                jogador.nome_curto,
                jogador.nome_longo,
                jogador.posicoes,
                jogador.nacionalidade,
                jogador.nome_clube,
                jogador.nome_liga,
                jogador.media(),
                jogador.avaliacoes,
                ))
        else:
            print("Nenhum resultado satisfatório.")

    def melhores_posicao(self, n:int, posicao:str, minimo:int = 1000) -> list[Jogador]:
        jogadores_selecionados = []
        for linha in self.linhas:
            for jogador in linha:
                jogador:Jogador
                posicoes = jogador.posicoes.replace(",",'').split()
                if (posicao in posicoes) and (jogador.avaliacoes >= minimo):
                    jogadores_selecionados.append(jogador)
        ordenar_jogadores_por_medias(jogadores_selecionados)
        jogadores_selecionados = jogadores_selecionados[:n]

        return jogadores_selecionados

class ordenar_jogadores_por_medias(quick_sort[Jogador, float]):
    def criterio(self, elemento: Jogador) -> float:
        return -elemento.media()
