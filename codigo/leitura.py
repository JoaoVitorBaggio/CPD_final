
from pandas     import read_csv, Series
from pathlib    import Path
from typing     import Self

from icecream   import ic

class Tabela_carregada[T]:
    """ Tabela que carrega os itens de um arquivo csv
    I: Tipo de um item da tabela"""

    def carregar_tabela(
            self
            , caminho_arquivo   : Path
            ) -> Self:

        tabela = read_csv(caminho_arquivo)

        i = 0
        controle = True
        while controle:
            try:
                linha = tabela.iloc[i, :]
                self.carregar_item(linha)
                i += 1
            except IndexError:
                controle = False

        return self

    def carregar_item(self, linha:Series) -> Self:
        """ Dada uma liha da tabela, inicializa um item 
        e insere na tabela"""
        # A forma que um item é carregado é definida pela tabela
        ...
