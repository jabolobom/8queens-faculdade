import pygame, sys
import alg_genetico as genetico
import alg_hillclimbing as hillclimbing

# Configurações
TAM_CELULA = 60
NUM_RAINHAS = 8
LARGURA = TAM_CELULA * NUM_RAINHAS
ALTURA = TAM_CELULA * NUM_RAINHAS + 100
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)


# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Problema das 8 Rainhas")

def desenhar_tabuleiro():
    for linha in range(NUM_RAINHAS):
        for coluna in range(NUM_RAINHAS):
            cor = BRANCO if (linha + coluna) % 2 == 0 else PRETO
            rect = pygame.Rect(coluna * TAM_CELULA, linha * TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(screen, cor, rect)

def desenhar_rainhas(solucao):
    for coluna, linha in enumerate(solucao):
        center_x = coluna * TAM_CELULA + TAM_CELULA // 2
        center_y = linha * TAM_CELULA + TAM_CELULA // 2
        radius = TAM_CELULA // 3
        pygame.draw.circle(screen, VERMELHO, (center_x, center_y), radius)


class botao:
    def __init__(self, width, height, posx, posy, color, textcolor, text, algo):
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy

        self.text = text
        self.color = color
        self.textcolor = textcolor
        self.font = pygame.font.SysFont('arial', 24)
        self.rect = pygame.Rect(posx, posy, width, height)

        self.algo = algo

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        buttontext = self.font.render(self.text, True, self.textcolor)
        text_rect = buttontext.get_rect(center=self.rect.center)
        screen.blit(buttontext, text_rect)

    def handle_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.algo()

def main():
    solucao_atual = []
    clock = pygame.time.Clock()
    clock.tick(60)
    screen.fill(BRANCO)

    botao_genetico = botao(200, 40, 10, ALTURA - 50, AZUL, BRANCO, "GENETICO (1)", genetico.algoritmo_genetico)
    botao_hillclimbing = botao(200, 40, 250, ALTURA - 50, VERMELHO, BRANCO, "HILLCLIMBING (1)", hillclimbing.solve)
    botao_genetico_92 = botao(200, 40, 10, ALTURA - 100, CINZA, PRETO, "GENÉTICO (92)", genetico.encontrar_92_solucoes_genetico)
    botao_hillclimbing_92 = botao(200, 40, 250, ALTURA - 100, (100,100,100), (255,255,255), "HILLCLIMBING (92)", hillclimbing.encontrar_92_solucoes_hillclimbing)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                resposta1 = botao_genetico.handle_click(event)
                resposta2 = botao_hillclimbing.handle_click(event)
                resposta3 = botao_genetico_92.handle_click(event)
                resposta4 = botao_hillclimbing_92.handle_click(event)



                if resposta1:
                    solucao_atual = resposta1
                elif resposta2:
                    solucao_atual = [next(i for i in range(len(resposta2)) if resposta2[i][col] == 1) for col in range(NUM_RAINHAS)]
                elif resposta3:
                    if isinstance(resposta3, list) and len(resposta3) > 0:
                        solucao_atual = list(resposta3[0])  # Mostra a primeira das 92 soluções
                elif resposta4:
                    if isinstance(resposta4, list) and len(resposta4) > 0:
                        solucao_atual = list(resposta4[0])  # Mostra a primeira solução encontrada pelo hill climbing

        desenhar_tabuleiro()
        desenhar_rainhas(solucao_atual)
        botao_genetico.draw()
        botao_hillclimbing.draw()
        botao_genetico_92.draw()
        botao_hillclimbing_92.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()
