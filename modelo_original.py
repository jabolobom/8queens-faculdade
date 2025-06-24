import time
import tracemalloc

NUM_RAINHAS = 8

def existe_conflict(col, row, solucao):
    for c in range(col):
        r = solucao[c]
        if r == row or abs(r - row) == abs(c - col):
            return True
    return False

def backtracking_todas_solucoes(col, solucao_atual, todas_solucoes):
    if col == NUM_RAINHAS:
        todas_solucoes.append(solucao_atual[:])
        return

    for row in range(NUM_RAINHAS):
        if not existe_conflict(col, row, solucao_atual):
            solucao_atual.append(row)
            backtracking_todas_solucoes(col + 1, solucao_atual, todas_solucoes)
            solucao_atual.pop()

def encontrar_92_solucoes_backtracking():
    tracemalloc.start()
    start = time.time()

    todas_solucoes = []
    backtracking_todas_solucoes(0, [], todas_solucoes)

    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    for i, sol in enumerate(todas_solucoes, 1):
        print(f"Solução {i}: {sol}")

    print(f"\nForam encontradas {len(todas_solucoes)} soluções únicas em {end - start:.2f} segundos.")
    print(f"Memória atual usada no final: {current} bytes")
    print(f"Pico de uso de memória: {peak} bytes")

if __name__ == "__main__":
    encontrar_92_solucoes_backtracking()
