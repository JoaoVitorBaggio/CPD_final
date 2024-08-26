import csv

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
    
    def _collect_words_with_prefix(self, node, current_word, prefix, results):
        """Coleta palavras que começam com o prefixo a partir de um nó."""
        if node is None:
            return
        
        # Verifica se o nó é relevante para a coleta
        if node.character == prefix[len(current_word)]:
            # Se o prefixo está completo, coletar todas as palavras na subárvore
            if len(current_word) == len(prefix):
                if node.is_end_of_string:
                    results.append((current_word, node.id))
                self._collect_words_with_prefix(node.middle, current_word, prefix, results)
            else:
                # Se ainda precisamos de mais caracteres para completar o prefixo
                self._collect_words_with_prefix(node.middle, current_word + node.character, prefix, results)
        
        # Explora a subárvore da esquerda e direita apenas se necessário
        if node.character > prefix[len(current_word)]:
            self._collect_words_with_prefix(node.left, current_word, prefix, results)
        if node.character < prefix[len(current_word)]:
            self._collect_words_with_prefix(node.right, current_word, prefix, results)
    
    def search_for_prefix(self, prefix):
        """Coleta todas as palavras que começam com o prefixo."""
        results = []
        self._collect_words_with_prefix(self.root, "", prefix, results)
        return results

def carregar_colunas_tst(arquivo_csv):
    tst = TST()
    
    # Abrir o arquivo CSV e ler a primeira e terceira colunas
    with open(arquivo_csv, newline='') as csvfile:
        leitor_csv = csv.reader(csvfile)
        for linha in leitor_csv:
            if len(linha) >= 3:  # Garantir que a linha tenha pelo menos 3 colunas
                id_valor = linha[0].strip()  # Primeira coluna (ID)
                valor_coluna = linha[2].strip()  # Terceira coluna (nome ou cidade)
                
                # Inserir o valor na TST com o ID associado
                tst.insert(valor_coluna, id_valor)

    return tst

def main():
    # Carregar a TST a partir do arquivo CSV
    arquivo_csv = 'dados\players.csv'  # Substitua pelo nome do seu arquivo CSV
    tst = carregar_colunas_tst(arquivo_csv)
    
    # Perguntar ao usuário qual prefixo ele quer procurar
    while True:
        prefixo = input("Informe o prefixo a ser pesquisado (ou 'sair' para terminar): ").strip()
        if prefixo.lower() == 'sair':
            break
        
        # Coletar e exibir todas as palavras que começam com o prefixo, junto com seus IDs
        resultados = tst.search_for_prefix(prefixo)
        
        if resultados:
            print(f'Palavras encontradas com o prefixo "{prefixo}":')
            for palavra, id_valor in resultados:
                print(f'Nome: {palavra}, ID: {id_valor}')
        else:
            print(f'Nenhuma palavra encontrada com o prefixo "{prefixo}".')

# Executar o programa
if __name__ == "__main__":
    main()
