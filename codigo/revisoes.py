
from leitura    import Carregavel
from hash       import Tabela_hash, NaoEncontrado
from jogadores  import Tabela_Jogadores, Jogador
from quicksort  import quick_sort

from pandas     import Series
from pathlib    import Path
from typing     import Self

class Revisao:
    def __init__(
            self,
            sofifa_id   :int,
            rating      :float,
            ) -> None:
        self.sofifa_id   = sofifa_id
        self.rating      = rating
        pass

class Usuario:
    def __init__(
            self,
            user_id:int,
            revisoes:list[Revisao] = [],
            ) -> None:
        self.user_id    = user_id
        self.revisoes   = revisoes
        pass

    class ordenar_revisoes(quick_sort[Revisao, float]):
        def criterio(self, elemento: Revisao) -> float:
            return -elemento.rating
        
    def get_top_n(self, n:int) -> list[Revisao]:
        paragrafo = "user_id, sofifa_id, rating"
        self.ordenar_revisoes(self.revisoes)
        
        top_n = self.revisoes[:20]

        return top_n

class Tabela_Usuarios(Tabela_hash[Usuario, int], Carregavel):
    def __init__(
            self,
            tabela_jogadores    : Tabela_Jogadores,
            caminho             : Path | None = None,
            tamanho             : int = 20000,
            periodo             : int = 10000
            ) -> None:
        self.total_palavras = 24188078
        self.periodo = periodo
        self.tempo = periodo
        self.lidas = 0

        super().__init__(tamanho)

        self.tabela_jogadores = tabela_jogadores

        if caminho:
            self.carregar_arquivo(caminho=caminho)

        return

    def hash(self, chave: int) -> int:
        return chave % self.tamanho

    def get_chave(self, item: Usuario) -> int:
        return item.user_id

    def carregar_item(self, linha: Series) -> Self:

        user_id     = int(linha["user_id"])
        sofifa_id   = int(linha["sofifa_id"])
        rating      = linha["rating"]

        revisao = Revisao(
            sofifa_id,
            rating,
        )
        
        try:
            # Tenta encontrar o usuário e acrescentar a revisão
            usuario = self[user_id]
            usuario.revisoes.append(revisao)

        except NaoEncontrado as Erro:
            # Se não encontrar, cadastra o usuário na tabela, com a revisão
            usuario = Usuario(
                user_id,
                revisoes=[revisao]
                )
            linha = Erro.linha
            linha.append(usuario)

        jogador = self.tabela_jogadores[sofifa_id]
        jogador.avaliar(rating)

        return self

    class ordenar_pares_jogador_nota(quick_sort[tuple[Jogador, float], float]):
        def criterio(self, elemento: tuple[Jogador, float]) -> float:
            return -elemento[0].media()

    def imprimir_top(self, n:int, user_id:int) -> Self:
        print("sofifa_id, short_name, long_name, global_rating, count, rating")

        usuario = self[user_id]
        revisoes = usuario.get_top_n(n)
        pares = []

        for revisao in revisoes:
            sofifa_id = revisao.sofifa_id
            nota = revisao.rating
            jogador:Jogador = self.tabela_jogadores[sofifa_id]
            pares.append((jogador, nota))

        self.ordenar_pares_jogador_nota(pares)

        for par in pares:
            jogador, rating = par
            sofifa_id       = jogador.sofifa_id
            short_name      = jogador.nome_curto
            long_name       = jogador.nome_longo
            global_rating   = jogador.media()
            count           = jogador.avaliacoes
            print(f"{sofifa_id}, {short_name}, {long_name}, {global_rating}, {count}, {rating}")

        return self