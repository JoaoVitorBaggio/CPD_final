
from csv        import reader
from pathlib    import Path
from typing     import Self

class Tabela_carregada:
    """ Tabela que carrega os itens de um arquivo csv
    I: Tipo de um item da tabela"""

    def carregar_tabela(
            self
            , caminho_arquivo   : Path
            , remover_cabeçalho : bool = True
            ) -> Self:

        with open(caminho_arquivo, 'r') as arquivo_csv:
            leitor = reader(arquivo_csv)
            ## FIX
            """if remover_cabeçalho:
                # Remove o cabeçalho
                leitor = leitor[1:]"""

            for linha in leitor:
                try:
                    self.carregar_item(linha)
                except ValueError:
                    ...

        return self

    def carregar_item(self, linha:list[str]) -> Self:
        """ Dada uma liha da tabela, inicializa um item 
        e adiciona à tabela"""
        # A forma que um item é carregado é definida pela tabela
        ...
