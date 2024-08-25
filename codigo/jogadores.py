
from hash       import Tabela_hash
from leitura    import Tabela_carregada
from pandas     import Series
from typing     import Self
from pathlib    import Path

class Jogador:
    """ Dados de um jogador"""

    def __init__(
            self
            , sofifa_id     :int
            , nome_curto    :str
            , nome_longo    :str
            , posicoes      :str
            , nacionalidade :str
            , nome_clube    :str
            , nome_liga     :str
            ) -> None:
        
        """
        Conforme o cabeçalho:
            sofifa_id,short_name,long_name,player_positions,nationality,club_name,league_name
        """

        self.sofifa_id     = sofifa_id     
        self.nome_curto    = nome_curto    
        self.nome_longo    = nome_longo    
        self.posicoes      = posicoes      
        self.nacionalidade = nacionalidade 
        self.nome_clube    = nome_clube    
        self.nome_liga     = nome_liga     

        return

    def __str__(self) -> str:
        # Imprime os dados do jogador
        return f"""
        sofifa_id           {self.sofifa_id    } \n
        short_name          {self.nome_curto   } \n
        long_name           {self.nome_longo   } \n
        player_positions    {self.posicoes     } \n
        nationality         {self.nacionalidade} \n
        club_name           {self.nome_clube   } \n
        league_name         {self.nome_liga    } \n
        """

class Tabela_Jogadores (
    Tabela_hash[Jogador, int],
    Tabela_carregada[Jogador]
    ):
    
    """ Tabela que busca os jogadores pelo id"""

    def __init__(self, caminho: Path, tamanho: int) -> None:
        super().__init__(caminho, tamanho)
        self.carregar_tabela(caminho)
        return

    def hash(self, chave: int) -> int:
        return chave % self.tamanho

    def get_chave(self, item: Jogador) -> int:
        return item.sofifa_id

    def carregar_item(self, linha: Series) -> Self:
        self.inserir(Jogador(*linha))
        return self
