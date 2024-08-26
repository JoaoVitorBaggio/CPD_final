import csv

class TSTNode:
    def __init__(self, character):
        self.character = character
        self.is_end_of_string = False
        self.left = None
        self.middle = None
        self.right = None

class TST:
    def __init__(self):
        self.root = None
    
    def insert(self, word):
        self.root = self._insert(self.root, word, 0)
    
    def _insert(self, node, word, index):
        char = word[index]
        
        if node is None:
            node = TSTNode(char)
        
        if char < node.character:
            node.left = self._insert(node.left, word, index)
        elif char > node.character:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 == len(word):
                node.is_end_of_string = True
            else:
                node.middle = self._insert(node.middle, word, index + 1)
        
        return node
    
    def search(self, word):
        return self._search(self.root, word, 0)
    
    def _search(self, node, word, index):
        if node is None:
            return False
        
        char = word[index]
        
        if char < node.character:
            return self._search(node.left, word, index)
        elif char > node.character:
            return self._search(node.right, word, index)
        else:
            if index + 1 == len(word):
                return node.is_end_of_string
            return self._search(node.middle, word, index + 1)

### Função para Ler a Terceira Coluna e Inserir na TST

def carregar_terceira_coluna_tst(arquivo_csv):
    tst = TST()
    
    # Abrir o arquivo CSV e ler a terceira coluna
    with open(arquivo_csv, newline='') as csvfile:
        leitor_csv = csv.reader(csvfile)
        for linha in leitor_csv:
            if len(linha) >= 4:  # Garantir que a linha tenha pelo menos 3 colunas
                valor_terceira_coluna = linha[3].strip()  # Terceira coluna (índice 2)
                tst.insert(valor_terceira_coluna)
    
    return tst

# Exemplo de uso
arquivo_csv = 'dados\players.csv'  # Substitua pelo nome do seu arquivo CSV
tst = carregar_terceira_coluna_tst(arquivo_csv)

# Verificando se um valor da terceira coluna está na TST
valor_para_buscar = "Lio"
encontrado = tst.search(valor_para_buscar)
print(f'Valor "{valor_para_buscar}" encontrado?', "Sim" if encontrado else "Não")
