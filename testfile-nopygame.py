from random import randint

N_QUEENS = 4
grid = [[0 for x in range(N_QUEENS)] for y in range(N_QUEENS)]

current_score = 0

def random_queen():
    queenlist = [randint(0, N_QUEENS-1) for i in range(N_QUEENS)]
    return queenlist

def populate_grid(grid, queenlist):
    for linha, coluna in enumerate(queenlist):
        grid[linha][coluna] = 1

# 10 SCORE FOR EACH CONFLICT
# LOWER IS BETTER
def evaluate_solution(grid):
    main_diags = [0] * (2 * N_QUEENS - 1)
    anti_diags = [0] * (2 * N_QUEENS - 1)

    score = 0
    for j in range(len(grid[0])): # colunas
        count = 0
        for i in range(len(grid)): # pra cada lista
            if grid[i][j] == 1:
                count += 1
        if count > 1:
            penalty = (count - 1) * 10
            score += penalty
            print(f"Vertical conflict in column {j+1}")

    # checando direita e esquerda diagonais
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                main_index = i - j + (N_QUEENS - 1)  # direita
                anti_index = i + j # esquerda
                main_diags[main_index] += 1
                anti_diags[anti_index] += 1

    for idx, count in enumerate(main_diags):
        if count > 1:
            score += (count - 1) * 10
            print(f"Main diagonal conflict")

    for idx, count in enumerate(anti_diags):
        if count > 1:
            score += (count - 1) * 10
            print(f"Anti-diagonal conflict")
    return score


def main():
    populate_grid(grid, random_queen())
    current_score = evaluate_solution(grid)
    for x in grid: print(x)
    print(f"Current score: {current_score}")

if __name__ == "__main__":
    main()