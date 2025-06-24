from random import randint
import time, math, tracemalloc

# até 12 queens ele resolve super rápido
# 13 queens demora, mas resolve
# 14 demorou alguns bons minutos e não tive resultado
N_QUEENS = 8
grid = [[0 for x in range(N_QUEENS)] for y in range(N_QUEENS)]
# matriz de zeros
current_score = 0

# posições aleatórias para as rainhas
def random_queen():
    queenlist = [randint(0, N_QUEENS-1) for i in range(N_QUEENS)]
    return queenlist

# posiciona as rainhas na matriz (tabuleiro)
def populate_grid(grid, queenlist):
    for linha, coluna in enumerate(queenlist):
        grid[linha][coluna] = 1

# 10 de score para cada conflito
# menor é melhor
def evaluate_solution(grid):
    main_diags = [0] * (2 * N_QUEENS - 1) # diagonais principais
    anti_diags = [0] * (2 * N_QUEENS - 1) # anti diagonais

    score = 0
    for j in range(len(grid[0])): # colunas
        count = 0
        for i in range(len(grid)): # pra cada lista
            if grid[i][j] == 1:
                count += 1
        if count > 1: # se tiver mais de uma rainha por coluna, conflito vertical!
            penalty = (count - 1) * 10
            score += penalty
            # print(f"Vertical conflict in column {j+1}, Vertical conflict count: {count - 1}") # DEBUG

    # checando direita e esquerda diagonais
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                main_index = i - j + (N_QUEENS - 1)  # direita
                anti_index = i + j # esquerda
                main_diags[main_index] += 1
                anti_diags[anti_index] += 1

    for count in main_diags:
        if count > 1: # se tiver mais que uma na sua diagonal principal, conflito na diagonal principal!
            score += (count - 1) * 10
            # print(f"Main diagonal conflict, Main diagonal conflict count: {count - 1}") # DEBUG

    for count in anti_diags:
        if count > 1: # igual o de cima
            score += (count - 1) * 10
            # print(f"Anti-diagonal conflict, Anti-diagonal conflict count: {count - 1}") # DEBUG

    return score # retorna o score calculado

def neighbor_state(grid, score_to_beat):
    best_grid = None
    best_score = score_to_beat

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 1:
                continue

            for delta_j in [-1, 1]:
                new_j = j + delta_j

                if 0 <= new_j < len(grid[0]) and grid[i][new_j] == 0:
                    # Copia apenas a linha modificada (mais leve que copiar o grid inteiro)
                    new_grid = [row[:] for row in grid]
                    new_grid[i][j] = 0
                    new_grid[i][new_j] = 1

                    result = evaluate_solution(new_grid)

                    if result < best_score:
                        best_grid = new_grid
                        best_score = result

                        if result == 0:
                            return new_grid  # early stop ao encontrar solução perfeita

    if best_grid:
        return neighbor_state(best_grid, best_score)

    # Removido print para acelerar
    return 0


def solve():
    tracemalloc.start()
    start = time.time()
    while True: # loop infinito pra forçar a testagem até encontrar
        # limpar grid
        for i in range(N_QUEENS):
            for j in range(N_QUEENS):
                grid[i][j] = 0

        populate_grid(grid, random_queen()) # preenche a grid com as rainhas
        current_score = evaluate_solution(grid) # score da grid formada

        climbing = neighbor_state(grid, current_score) # testa possibilidades buscando uma solução

        if climbing != 0: # a função acima retorna 0 se não encontrar solução melhor do que atual, resultado em um pedido
            # de uma nova grid para testar
            print("Solution found!")
            for x in climbing: print(x)
               # estatisticas
            end = time.time()

            print(f"\nTotal de rainhas {N_QUEENS}\nTempo total: {end - start:.4f} segundos\nTotal de possibilidades: {math.factorial(N_QUEENS)}")
            # interessante, nessa solução a quantidade de boards possívels é sempre NQUEENS fatorial, pois só pode existir 1 rainha
            # por row,

            current, peak = tracemalloc.get_traced_memory()
            print(f"RAM pico: {peak / (1024 * 1024):.2f} MB")
            tracemalloc.stop()
            return climbing

def encontrar_92_solucoes_hillclimbing():
    tracemalloc.start()
    start = time.time()

    solucoes = []
    solucoes_set = set()

    tentativas = 0
    max_tentativas = 500000  # aumentei para dar mais chances de achar soluções

    while len(solucoes) < 92 and tentativas < max_tentativas:
        tentativas += 1
        # limpa grid
        for i in range(N_QUEENS):
            for j in range(N_QUEENS):
                grid[i][j] = 0

        populate_grid(grid, random_queen())
        current_score = evaluate_solution(grid)
        climbing = neighbor_state(grid, current_score)

        if climbing != 0:
            sol = tuple([row.index(1) for row in climbing])
            if sol not in solucoes_set:
                solucoes_set.add(sol)
                solucoes.append(sol)
                print(f"Solução {len(solucoes)}: {sol}")

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\nForam encontradas {len(solucoes)} soluções únicas em {end - start:.2f} segundos.")
    print(f"Memória atual usada no final: {current} bytes")
    print(f"Pico de uso de memória: {peak} bytes")

    return solucoes
