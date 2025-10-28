import gen_sudoku as gsdk

N = 9

class Sudoku:
    def __init__(self):
        self.tabuleiro = [[0 for _ in range(N)] for _ in range(N)]
        self.solucao = [[0 for _ in range(N)] for _ in range(N)]
        self.vidas = 5
