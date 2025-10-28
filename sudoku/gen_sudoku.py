import random

N = 9 

def pode_colocar(tabuleiro, linha, coluna, num):
    for i in range(N):
        if tabuleiro[linha][i] == num or tabuleiro[i][coluna] == num:
            return False
        
        startLinha = linha - linha % 3
        startColuna = coluna - coluna % 3

        for i in range(3):
            for j in range(3):
                if tabuleiro[i + startLinha][j + startColuna] == num:
                    return False
                
    return True

def gerar_completo(tabuleiro):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for linha in range(N):
        for coluna in range(N):
            if tabuleiro[linha][coluna] == 0:
                random.shuffle(nums)
                for i in range(N):
                    num = nums[i]
                    if pode_colocar(tabuleiro, linha, coluna, num):
                        tabuleiro[linha][coluna] = num
                        if gerar_completo(tabuleiro):
                            return True
                        tabuleiro[linha][coluna] = 0
                return False
    return True

def copiar_tabuleiro(origem, destino):
    for i in range(N):
        for j in range(N):
            destino[i][j] = origem[i][j]

def criar_desafio(tabuleiro, holes):
    while holes > 0:
        linha = random.randint(0,8)
        coluna = random.randint(0,8)
        if tabuleiro[linha][coluna] == 0:
            while tabuleiro[linha][coluna] == 0:
                linha = random.randint(0,8)
                coluna = random.randint(0,8)
            tabuleiro[linha][coluna] = 0
            holes -= 1
        elif tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            holes -= 1