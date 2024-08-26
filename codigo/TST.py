
# import csv
from pandas     import read_csv, Series
from caminhos   import pasta_dados
from leitura    import Carregavel
from typing     import Self

class TSTNode:
    def __init__(self, character):
        self.character = character
        self.is_end_of_string = False
        self.left = None
        self.middle = None
        self.right = None
        self.id = None  # Armazena o ID associado ao fim da palavra

class TST(Carregavel):
    def __init__(self, caminho = None):
        self.root = None
        if caminho:
            self.carregar_arquivo(caminho)
    
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

    def carregar_item(self, linha:Series) -> Self:
        self.insert(
            word        = linha["long_name"],
            word_id     = linha["sofifa_id"],
        )
        return self
