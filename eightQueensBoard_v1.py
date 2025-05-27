import pygame
import sys
from random import randint

# Configurações
TAM_CELULA = 60  # Tamanho de cada célula do tabuleiro
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS

# Solução fixa para as 8 rainhas (linha por coluna)
# Cada valor representa a linha da rainha na respectiva coluna
# solucao = [0, 4, 7, 5, 2, 6, 1, 3]
temp_board = [randint(0, 7) for x in range(0,8)]
solucao = list()

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Problema das 8 Rainhas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

grid = [[0 for x in range(NUM_RAINHAS)] for y in range(NUM_RAINHAS)]

def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            if (linha + coluna) % 2 == 0:
                cor = BRANCO
            else:
                cor = PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

# demonstração visual da aleatoriedade
def random_rainhas():
    for coluna, linha in enumerate(temp_board):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y = linha * TAM_CELULA + TAM_CELULA // 2
        radius = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)

def desenhar_rainhas_solucao():
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y =  linha * TAM_CELULA + TAM_CELULA // 2
        radius   = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)

# preencher na matriz quais espaços possuem uma rainha
def populate_grid(grid):
    for coluna, linha in enumerate(temp_board):
        grid[coluna][linha] = 1




# For each pair of queens (i, j), check if they are:
# in the same row
# on the same diagonal
def evaluation(grid):
    pass



def main():
    populate_grid(grid)
    desenhar_tabuleiro()
    random_rainhas()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()