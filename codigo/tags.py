import csv

class HashTable:
    def __init__(self):
        # Dicionário para armazenar os dados (tabela hash)
        self.hash_table = {}

    def load_from_csv(self, csv_file):
        # Carrega os dados do arquivo CSV e os insere na tabela hash
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                user_id = row[0]  # Coluna 0: ID do usuário
                jogador_id = row[1]  # Coluna 1: ID do jogador
                comentario = row[2]  # Coluna 2: Comentário

                # Verifica se o user_id já existe na tabela hash
                if user_id not in self.hash_table:
                    self.hash_table[user_id] = []

                # Adiciona a tupla (jogador_id, comentario) à lista correspondente ao user_id
                self.hash_table[user_id].append((jogador_id, comentario))

    def get_comentarios_by_user(self, user_id):
        # Retorna a lista de comentários do usuário pelo ID
        return self.hash_table.get(user_id, [])

hash_table = HashTable()
hash_table.load_from_csv("dados/tags.csv")

# Consultando comentários de um usuário
print(hash_table.get_comentarios_by_user("17800"))  # Saída: [('101', 'Ótimo jogador!'), ('102', 'Precisa melhorar.')]