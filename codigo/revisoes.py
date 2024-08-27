
from leitura    import Carregavel
from hash       import Tabela_hash, NaoEncontrado
from pandas     import Series
from pathlib    import Path
from typing     import Self

class Revisao:
    def __init__(
            self,
            user_id     :int,
            sofifa_id   :int,
            rating      :float,
            ) -> None:
        pass

class Usuario:
    def __init__(
            self,
            user_id:int,
            revisoes:list[Revisao] = []
            ) -> None:
        self.user_id = user_id
        self.revisoes = revisoes
        pass

class Tabela_Usuarios(Tabela_hash[Usuario, int], Carregavel):
    def __init__(
            self,
            caminho: Path | None = None,
            tamanho: int = 20000
            ) -> None:
        super.__init__(tamanho)

        if caminho:
            self.carregar_arquivo(caminho=caminho)

        return

    def hash(self, chave: int) -> int:
        return chave % 2000

    def get_chave(self, item: Usuario) -> int:
        return item.user_id

    def carregar_item(self, linha: Series) -> Self:
        user_id     = linha["user_id"]
        sofifa_id   = linha["sofifa_id"]
        rating      = linha["rating"]

        revisao = Revisao(
            user_id,
            sofifa_id,
            rating,
        )

        try:
            usuario = self[user_id]
        except NaoEncontrado:
            usuario = Usuario(
                user_id, 
                revisoes=[revisao]
                )
            self.inserir(usuario)

        return self
