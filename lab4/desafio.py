
"""
    ATENÇÃO
    Esse é o arquivo enviado para o site da Beecrowd para validação,
    por isso possui cópias do conteúdo de outros arquivos.
    Para ler o código desenvolvido exclusivamente para o desafio, vá
    para o final do arquivo, após a divisória "DESAFIO".
    Parte do código pode ter sido apagada por ser incompatível ou desnecessária.
"""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 H A S H   H A S H   H A S H   H A S H   H A S H   H A S H   H A S H   H A S H  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Tabela_hash:
    """ Tabela Hash de itens do tipo I, com chave do tipo C"""

    # Métodos especiais

    def __init__(
            self
            , tamanho:int
            ) -> None:
        # Inicialização da tabela vazia
        self.linhas = [list() for i in range(tamanho)]
        self.tamanho = tamanho
        self.ultima_linha_consultada = []
        return

    def __getitem__(self, chave):
        """ Dada uma chave, retorna o item que a contém"""
        linha = self.get_linha(chave)
        for item in linha:
            if self.compara_chaves(item, chave):
                return item
        raise NaoEncontrado(chave)

    def __str__(self) -> str:
        return super().__str__()

    # Métodos proprios

    def compara_chaves(self, item, chave):
        return chave == self.get_chave(item)

    def get_linha(self, chave):
        """ Dada uma chave, retorna a linha na qual o item pode estar"""
        indice = self.hash(chave)
        linha = self.linhas[indice]
        self.ultima_linha_consultada = linha
        return linha
    
    def get_linha_item(self, item) -> list[str]:
        """ Dada um item, retorna a linha na qual ele pode ficar"""
        chave = self.get_chave(item)
        linha = self.get_linha(chave)
        return linha

    def inserir(self, item):
        """ Dado o item, insere ele na tabela"""
        linha = self.get_linha_item(item)
        linha.append(item)
        return linha

    # Métodos abstratos

    def hash(self, chave) -> int:
        """ Dada uma chave, retorna o índice da linha na qual o item fica"""
        # Essa função varia para cada tabela
        ...

    def get_chave(self, item):
        """ Dado um item, retorna a chave contida nele"""
        # Essa função varia para cada tabela
        ...

class NaoEncontrado(Exception):
    def __init__(self, chave) -> None:
        self.chave = chave
        return
    
    def __str__(self) -> str:
        chave = self.chave
        return f"Erro: Item de chave {chave} nao encontrado."

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 D E S A F I O   D E S A F I O   D E S A F I O   D E S A F I O   D E S A F I O
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Hash_int(Tabela_hash):
    # Tabela hash simples com inteiros

    def hash(self, chave: int) -> int:
        return chave % self.tamanho

    def get_chave(self, item: int) -> int:
        return item

    def carregar_por_str(self, linha:str):
        itens = linha.split()
        for item in itens:
            self.inserir(int(item))

    def __str__(self) -> str:
        impressao = ""
        i = 0
        for linha in self.linhas:
            impressao += f"{i} ->"
            for numero in linha:
                impressao += f" {numero} ->"
            impressao += f" \\\n"
            i += 1
        return impressao

# Recebe os dados
quantidadede_de_tabelas = int(input())

tabelas = []

# Inicializa as tabelas
for i in range(quantidadede_de_tabelas):
    # Recebe os dois parâmetros em uma linha
    tamanho_tabela, quantidade_elementos = input().split()
    # Converte os parâmetros
    tamanho_tabela = int(tamanho_tabela)
    quantidade_elementos = int(quantidade_elementos)
    # Inicializa a tabela
    tabela = Hash_int(tamanho=tamanho_tabela)
    tabelas.append(tabela)
    # Recebe os elementos em uma linha
    linha = input()
    # Insere os elementos na tabela
    tabela.carregar_por_str(linha)

print(*tabelas, sep="\n", end="")
