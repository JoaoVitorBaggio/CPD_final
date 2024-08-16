
from caminhos   import *
from jogador    import *
from hash       import NaoEncontrado
from time       import time

class Experimento:
    def __init__(
            self
            , tamanho_tabela    : int
            , caminho_jogadores : Path = pasta_entrada / "players.csv"
            , caminho_consultas : Path = pasta_entrada / "consultas.csv"
            ) -> None:
        self.linhas_impressao = []
        self.linhas_consultas = []

        self.construir_tabela(tamanho_tabela, caminho_jogadores)
        self.realizar_consultas(caminho_consultas)
        self.imprimir_linhas()
        return

    def construir_tabela(self, tamanho_tabela, caminho_jogadores) -> None:
        # Inicializa uma tabela e cronometra
        tempo_inicial = tempo()
        self.tabela = Tabela_Jogadores(caminho_jogadores, tamanho_tabela)
        self.estatisticas = self.tabela.estatisticas
        self.tempo_construcao = tempo() - tempo_inicial
        self.imprimir_construcao()
        return

    def realizar_consultas(self, caminho_consultas) -> None:
        # Marca o tempo inicial
        tempo_inicial = tempo()
        # Abre o aruivo de consultas
        arquivo = open(caminho_consultas, 'r')
        # Carrega id para consultar
        sofifa_id = int(arquivo.readline())
        # Lê todas consultas
        while not(sofifa_id is None):
            self.tentar_consultar(sofifa_id)
            # Imprime os dados da consulta
            self.imprimir_ultima_consulta()
            # Lê a próxima linha
            try:
                ##FIX
                sofifa_id = int(arquivo.readline())
            except ValueError:
                break
        # Calcula o tempo
        self.tempo_consultas = tempo() - tempo_inicial
        # Imprime os dados das consultas
        self.imprimir_consultas()
        return
    
    def tentar_consultar(self, sofifa_id:int) -> None:
        try:
            # Se encontrar jogador
            self.ultimo_jogador = self.tabela[sofifa_id]
        except NaoEncontrado:
            # Se não encontrar jogador
            self.ultimo_jogador = Jogador(sofifa_id, "NAO ENCONTRADO", "")

    def imprimir_construcao(self) -> None:
        self.linhas_impressao = [
            "PARTE1: ESTATISTICAS DA TABELA HASH"
            , f"TEMPO DE CONSTRUCAO DA TABELA {self.tempo_construcao}"
            , f"TAXA DE OCUPACAO {self.estatisticas.taxa_ocupacao()}"
            , f"TAMANHO MAXIMO DE LISTA {self.estatisticas.tamanho_maximo}"
            , f"TAMANHO MEDIO DE LISTA {self.estatisticas.tamanho_medio()}"
            , ""
        ]
        return

    def imprimir_ultima_consulta(self) -> None:
        jogador = self.ultimo_jogador
        consultas = self.estatisticas.testes_ultima
        linha = f"{jogador} {consultas}"
        self.linhas_consultas.append(linha)
        return

    def imprimir_consultas(self) -> None:
        primeiras_linhas = [
            "PARTE 2: ESTATISTICAS DAS CONSULTAS"
            , f"TEMPO PARA REALIZACAO DE TODAS CONSULTAS {self.tempo_consultas}"
        ]
        ultimas_linhas = [
            f"MAXIMO NUMERO DE TESTES POR NOME ENCONTRADO {self.estatisticas.testes_maximo}"
            , f"MEDIA NUMERO DE TESTES POR NOME ENCONTRADO {self.estatisticas.testes_media()}"
        ]
        self.linhas_impressao +=  primeiras_linhas + self.linhas_consultas + ultimas_linhas
        return

    def imprimir_linhas(self) -> None:
        arquivo = open(pasta_saida / f"experimento{self.tabela.tamanho}.txt", 'w')
        for linha in self.linhas_impressao:
            print(linha, file = arquivo)

def tempo() -> int:
    return int(1000 * time())
