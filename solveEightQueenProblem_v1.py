import pygame
import sys
import random

# Configurações
TAM_CELULA = 60
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS + 50  # espaço extra para o botão

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Problema das 8 Rainhas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)

# Fonte para o botão
font = pygame.font.SysFont(None, 36)

# Variável que armazena a solução atual
solucao = []

def existe_conflict(col, row, solucao):
    # Verifica conflitos com rainhas já colocadas
    for c in range(col):
        r = solucao[c]
        # mesmo linha ou diagonais
        if r == row or abs(r - row) == abs(c - col):
            return True
    return False

def gerar_solucao_recursive(col, solucao_atual):
    if col == NUM_RAINHAS:
        return solucao_atual[:]
    options = [row for row in range(NUM_RAINHAS) if not existe_conflict(col, row, solucao_atual)]
    random.shuffle(options)
    for row in options:
        solucao_atual.append(row)
        resultado = gerar_solucao_recursive(col + 1, solucao_atual)
        if resultado:
            return resultado
        solucao_atual.pop()
    return None

def gerar_solucao():
    return gerar_solucao_recursive(0, [])

def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

def desenhar_rainhas():
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y = linha * TAM_CELULA + TAM_CELULA // 2
        radius = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)

'''def desenhar_botao():
    botao_rect = pygame.Rect(10, ALTURA - 40, 220, 30)
    pygame.draw.rect(screen, AZUL, botao_rect)
    texto = font.render("Gerar Nova Solução", True, BRANCO)
    screen.blit(texto, (20, ALTURA - 35))
    return botao_rect
'''
def desenhar_botao():
    # a largura do botão deve ser o suficiente para cobrir o texto
    botao_largura = 250
    botao_altura = 40
    botao_x = 10
    botao_y = ALTURA - 50  # ajustado para ficar visualmente mais bonito
    botao_rect = pygame.Rect(botao_x, botao_y, botao_largura, botao_altura)
    pygame.draw.rect(screen, AZUL, botao_rect)

    # Centralizar o texto no botão
    texto = font.render("Gerar Nova Solução", True, BRANCO)
    texto_rect = texto.get_rect(center=botao_rect.center)
    screen.blit(texto, texto_rect)

    return botao_rect

def main():
    global solucao
    clock = pygame.time.Clock()
    solucao = gerar_solucao()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if pygame.Rect(10, ALTURA - 40, 220, 30).collidepoint(mouse_pos):
                    solucao = gerar_solucao()

        desenhar_tabuleiro()
        desenhar_rainhas()
        desenhar_botao()
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()