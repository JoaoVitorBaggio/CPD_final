
from hash       import Tabela_hash, NaoEncontrado
from leitura    import Carregavel
from jogadores  import Tabela_Jogadores, Jogador

from pandas     import Series
from typing     import Self
from pathlib    import Path

class Tag:
    def __init__(self, texto:str, ids:list[int]=[]) -> None:
        self.text = texto
        self.ids = ids
        return
    
    def filtrar(self, lista:list[Jogador]) -> list[Jogador]:
        lista_filtrada = []
        for jogador in lista:
            if jogador.sofifa_id in self.ids:
                lista_filtrada.append(jogador)
        return lista_filtrada
    
    def obter_jogadores(self, tabela_jogadores:Tabela_Jogadores) -> list[Jogador]:
        jogadores = [tabela_jogadores[i] for i in self.ids]
        return jogadores
    
    def imprimir_jogadores(self, tabela_jogadores:Tabela_Jogadores) -> Self:
        jogadores = self.obter_jogadores(tabela_jogadores)
        tabela_jogadores.imprimir_jogadores(jogadores)

        return self

class Tabela_Tags(Tabela_hash[Tag, str], Carregavel):
    def __init__(self, tamanho: int = 720007, caminho : Path | None = None) -> None:
        super().__init__(tamanho)

        if caminho:
            self.carregar_arquivo(caminho)

        return

    def carregar_item(self, linha: Series) -> Self:
        # user_id     = linha['user_id']
        sofifa_id   = linha['sofifa_id']
        texto       = str(linha['tag'])

        try:
            tag = self[texto]
        except NaoEncontrado as Erro:
            tag = Tag(texto, [sofifa_id])
            Erro.linha.append(tag)

        if not(sofifa_id in tag.ids):
            tag.ids.append(sofifa_id)

        return self

    def get_comentarios_by_user(self, user_id):
        # Retorna a lista de comentários do usuário pelo ID
        return self.hash_table.get(user_id, [])

    def hash(self, chave: str) -> int:
        return ord(chave[0]) % self.tamanho
    
    def get_chave(self, item: Tag) -> str:
        return item.text

    def intersect(self, tags:list[str], tabela_jogadores:Tabela_Jogadores) -> list[Jogador]:
        tag0str = tags.pop(0)
        tag0 = self[tag0str]
        jogadores = tag0.obter_jogadores(tabela_jogadores)
        for tagstr in tags:
            tag = self[tagstr]
            jogadores = tag.filtrar(jogadores)
        return jogadores