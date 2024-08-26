
from leitura    import Carregavel
from hash       import Tabela_hash
from pandas     import Series
from pathlib    import Path
from typing     import Self

class Revisao:
    ...

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
    def __init__(self, caminho: Path | None = None) -> None:
        if caminho:
            self.carregar_arquivo(caminho=caminho)
            return
        
    def hash(self, chave: int) -> int:
        ...
        return super().hash(chave)
    
    def get_chave(self, item: Usuario) -> int:
        ...
        return super().get_chave(item)
    
    def carregar_item(self, linha: Series) -> Self:
        ...
        return super().carregar_item(linha)
