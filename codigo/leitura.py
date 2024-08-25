
from pandas     import read_csv, Series
from pathlib    import Path
from typing     import Self

class Tabela_carregada[T]:
    """ Tabela que carrega os itens de um arquivo csv
    I: Tipo de um item da tabela"""

    def carregar_tabela(
            self
            , caminho_arquivo   : Path
            ) -> Self:

        with read_csv(caminho_arquivo) as tabela:

            for linha in tabela:
                self.carregar_item(linha)

        return self

    def carregar_item(self, linha:Series) -> Self:
        """ Dada uma liha da tabela, inicializa um item 
        e insere na tabela"""
        # A forma que um item é carregado é definida pela tabela
        ...
