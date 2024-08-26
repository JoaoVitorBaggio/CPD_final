
import csv
from caminhos import pasta_dados

class TSTNode:
    def __init__(self, character):
        self.character = character
        self.is_end_of_string = False
        self.left = None
        self.middle = None
        self.right = None
        self.id = None  # Armazena o ID associado ao fim da palavra

class TST:
    def __init__(self):
        self.root = None
    
    def insert(self, word, word_id):
        self.root = self._insert(self.root, word, word_id, 0)
    
    def _insert(self, node, word, word_id, index):
        char = word[index]
        
        if node is None:
            node = TSTNode(char)
        
        if char < node.character:
            node.left = self._insert(node.left, word, word_id, index)
        elif char > node.character:
            node.right = self._insert(node.right, word, word_id, index)
        else:
            if index + 1 == len(word):
                node.is_end_of_string = True
                node.id = word_id  # Armazena o ID quando a palavra termina
            else:
                node.middle = self._insert(node.middle, word, word_id, index + 1)
        
        return node
    
    def _search_node(self, node, prefix, index):
        """Busca o nó correspondente ao final do prefixo."""
        if node is None:
            return None
        
        char = prefix[index]
        
        if char < node.character:
            return self._search_node(node.left, prefix, index)
        elif char > node.character:
            return self._search_node(node.right, prefix, index)
        else:
            if index + 1 == len(prefix):
                return node
            return self._search_node(node.middle, prefix, index + 1)
    
    def collect_words_with_prefix(self, prefix):
        """Coleta todas as palavras que compartilham o mesmo prefixo."""
        node_at_prefix = self._search_node(self.root, prefix, 0)
        if node_at_prefix is None:
            return []  # Prefixo não encontrado
        
        # Coleta todas as palavras a partir do nó do prefixo
        words_with_ids = []
        self._collect_words(node_at_prefix.middle, prefix, words_with_ids)
        
        # Inclui o próprio prefixo se ele for uma palavra completa
        if node_at_prefix.is_end_of_string:
            words_with_ids.append((prefix, node_at_prefix.id))
        
        return words_with_ids
    
    def _collect_words(self, node, current_word, words_with_ids):
        """Recursivamente coleta palavras a partir de um nó."""
        if node is None:
            return
        
        # Coletar na subárvore da esquerda
        self._collect_words(node.left, current_word, words_with_ids)
        
        # Se o nó atual marca o fim de uma palavra, adicionamos a palavra completa e o ID
        if node.is_end_of_string:
            words_with_ids.append((current_word + node.character, node.id))
        
        # Continuar na subárvore do meio
        self._collect_words(node.middle, current_word + node.character, words_with_ids)
        
        # Coletar na subárvore da direita
        self._collect_words(node.right, current_word, words_with_ids)

### Função para Ler a Terceira Coluna de um CSV e Inserir na TST

def carregar_terceira_coluna_tst(arquivo_csv):
    tst = TST()
    
    # Abrir o arquivo CSV e ler a primeira e terceira colunas
    with open(arquivo_csv, newline='') as csvfile:
        leitor_csv = csv.reader(csvfile)
        for linha in leitor_csv:
            if len(linha) >= 3:  # Garantir que a linha tenha pelo menos 3 colunas
                id_valor = linha[0].strip()  # Primeira coluna (ID)
                valor_terceira_coluna = linha[2].strip()  # Terceira coluna (cidade ou nome)
                
                # Inserir o valor na TST com o ID associado
                tst.insert(valor_terceira_coluna, id_valor)

    return tst

### Função Principal para Interagir com o Usuário

def main():
    # Carregar a TST a partir da terceira coluna de um arquivo CSV
    arquivo_csv = pasta_dados / "players.csv"  # Substitua pelo nome do seu arquivo CSV
    tst = carregar_terceira_coluna_tst(arquivo_csv)
    
    # Perguntar ao usuário qual prefixo ele quer procurar
    while True:
        prefixo = input("Informe o prefixo a ser pesquisado (ou 'sair' para terminar): ").strip()
        if prefixo.lower() == 'sair':
            break
        
        # Coletar e exibir todas as palavras que compartilham o prefixo, junto com seus IDs
        palavras_com_ids = tst.collect_words_with_prefix(prefixo)
        
        if palavras_com_ids:
            for palavra, id_valor in palavras_com_ids:
                print(f'ID: {id_valor}, Palavra: {palavra}')
        else:
            print(f'Nenhuma palavra encontrada com o prefixo "{prefixo}".')

# Executar o programa
if __name__ == "__main__":
    main()
