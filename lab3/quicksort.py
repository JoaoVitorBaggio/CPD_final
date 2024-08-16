"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O R T S   I M P O
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from util       import Comparavel

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S   C L A S S E S   T I P O S
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class quick_sort[T, C:Comparavel]:
    " Variante com listas encadeadas do python."

    def __init__  (
            self,
            fonte:  list[T],    # Lista a ser ordenada
            )->     None:       # Ordena a lista

        # Salva a fonte
        self.fonte = fonte

        # Filtra e resolve casos triviais
        if self.trivial():
            return

        # Menores que o pivo
        self.esquerda   = []
        # Iguais ao pivo
        self.meio       = []
        # Maiores que pivo
        self.direita    = []

        # Escolhe o pivô
        self.selecionar()

        # Faz a separação dos maiores e menores que o pivô
        self.separar()

        # Resolve as partes
        self.resolver()

        # Recombina as partes
        self.recombinar()

        return

    def trivial(self) -> bool:
        return len(self.fonte) <= 1

    def selecionar(self) -> None:
        elemento = self.fonte.pop(0)
        self.meio.append(elemento)
        self.pivo = self.criterio(elemento)
        return

    def criterio(self, elemento:T) -> C:
        return elemento

    def separar(self) -> None:
        # Enquanto tiver fonte
        while self.fonte:
            # Remove o último elemento da fonte
            elemento = self.fonte.pop(0)
            chave = self.criterio(elemento)
            # Coloca ele no grupo correto
            if chave < self.pivo:
                self.esquerda.append(elemento)
            elif chave > self.pivo:
                self.direita.append(elemento)
            else:
                self.meio.append(elemento)
        return

    def resolver(self) -> None:
        self.__class__(self.esquerda)
        self.__class__(self.direita)
        return

    def recombinar(self) -> None:
        self.fonte += self.esquerda + self.meio + self.direita
        return
