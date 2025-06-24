import random, time, tracemalloc

##### Defs iniciais - cada processo de algoritmo genetico

######################## 1 - Gera Individuo 

def gerar_individuo():
    return random.sample(range(8), 8) 

######################## 2 - Avalia individuos (conflitos)

def avaliar(individuo):
    conflitos = 0

    for i in range(len(individuo)):
        for j in range(i + 1, len(individuo)):
            ## i e j são as linhas
            ## individuo[i] e individuo[j] são as colunas

            ## Se estão na mesma diagonal principal
            if i - individuo[i] == j - individuo[j]:
                conflitos = conflitos + 1

            ## Se estão na mesma diogonal secundaria
            if i + individuo[i] == j + individuo[j]:
                conflitos = conflitos + 1

    return conflitos

######################### 3 - Gera população

def gerar_populacao(n):
    populacao = []

    for p in range(n):
        populacao.append(gerar_individuo())
        
    return populacao

######################## 4 - Seleção

def selecionar(qtd_pais, populacao):
    pais = []

    for s in range(qtd_pais): 
        ## escolhe dois inidividuos aleatorios da população
        a = random.choice(populacao)
        b = random.choice(populacao)

        ## Compara os dois e aciona
        if avaliar(a) < avaliar(b):
            pais.append(a)
        else:
            pais.append(b)

    return pais

######################## 5 - Cruzamento (crossover) - pais geram filhos

def cruzar(pai1, pai2):
    ponto = random.randint(1, 6) ## Ponto de corte aleatorio entre 1 e 6
    filho = pai1[:ponto] ## Para a primeira parte copia o pai até o indice[:ponto]

    for valor in pai2: ## Percorre pai2
        if valor not in filho: ## Analise os valores de pai2 que não estão no filho
            filho.append(valor) ## Adiciona esses valores ao filho

    return filho

######################## 6 - Mutação - Adiciona variedade genética

def mutar(filho, taxa_mutacao=0.1):
    ## random.random retorna um numero de 0.0 a 1.0
    ## se o número for menor que a taxa de mutação, a mutação acontece
    if random.random() < taxa_mutacao: 
        ## escolhe dois indices diferentes entre 0 e 7 pra trocar
        i, j = random.sample(range(8), 2)
        ## troca o valor de i por j, e o de j por i
        filho[i], filho[j] = filho[j], filho[i]
    return filho

#
# #####################################################################################
# ##########################    TESTES     ############################################
# #####################################################################################
#
#
# operacao_teste = input("Deseja realizar algum teste antes? (s/n) ").lower()
# if operacao_teste == "s":
#     print("- Digite 1 para testar Geração de individuo")
#     print("- Digite 2 para testar a Avaliação de individuo")
#     print("- Digite 3 para testar a Geração de população")
#     print("- Digite 4 para testar a Seleçao de individuos")
#     print("- Digite 5 para testar o Cruzamento de individuos")
#     print("- Digite 6 para testar a Mutação de individuos")
#     teste_desejado = int(input())
#     print("")
#
#     if teste_desejado == 1:
#         ######################### Teste 1 - Gerar individuo
#
#         print("- Teste 1 - Gerar individuo: ", gerar_individuo())
#         print("")
#
#     if teste_desejado == 2:
#         ######################### Teste 2 - Avaliar individuo
#
#         individuo_teste2 = gerar_individuo()
#
#         print("- Teste 2 - Avaliação:")
#         print("Individuo: ", individuo_teste2)
#         print("Conflitos: ", avaliar(individuo_teste2))
#         print("")
#
#     if teste_desejado == 3:
#         ########################## Teste 3 - Gerar população
#
#         print("- Teste 3 - Gerar população: (Gerando uma população de 5 como exemplo)")
#         populacao_teste1 = gerar_populacao(5)
#
#         for z, individuo in enumerate(populacao_teste1):
#             print("Individuo ", z+1, " : ", individuo)
#         print("")
#
#     if teste_desejado == 4:
#         ######################### Teste 4 - Seleciona individuos
#
#         print("- Teste 4 - Seleciona individuos da população: (Exemplo: População de 10 e selecionando 4 pais)")
#
#         populacao_teste2 = gerar_populacao(10)
#
#         pais_teste = selecionar(4, populacao_teste2)
#
#         print("População antes da seleção: ")
#         for z, individuo in enumerate(populacao_teste2):
#             print(f"Indivíduo {z+1}: {individuo} - Conflitos: {avaliar(individuo)}")
#
#         print("Pais depois da seleção: ")
#         for i, individuo in enumerate(pais_teste): ## Percorre a lista pais (i = indice)
#             print(f"Pai {i+1}: {individuo} - Conflitos: {avaliar(individuo)}")
#         print("")
#
#     if teste_desejado == 5:
#         ######################### Teste 5 - Cruzamento
#
#         print("- Teste 5 - Cruzamento:")
#
#         pai1_teste = gerar_individuo()
#         pai2_teste = gerar_individuo()
#
#         print("Pai 1 : ", pai1_teste)
#         print("Pai 2: ", pai2_teste)
#
#         filho_teste = cruzar(pai1_teste, pai2_teste)
#
#         print("Filho", filho_teste)
#         print("")
#
#     if teste_desejado == 6:
#         ######################### Teste 6 - Teste mutação
#
#         individuo_teste6 = [3, 1, 4, 7, 0, 6, 2, 5]
#
#         print("- Teste 6 - Mutação:")
#         print("Individuo antes da mutação: ", individuo_teste6)
#         mutado = mutar(individuo_teste6, taxa_mutacao=1.0)
#         print("Individuo depois de mutar: ", mutado)
#         print("")
#
# input("Pressione Enter para iniciar o algoritmo genético...")


############################### Loop principal

def algoritmo_genetico(qtd_populacao=100, qtd_pais=20, taxa_mutacao=0.1, max_geracoes=1000):

    inicio_tempo = time.time() ## Marca o tempo inicial

    populacao = gerar_populacao(qtd_populacao)

    for geracao in range(max_geracoes):
        print(f"Geração {geracao+1}")

        ## Avalia e ordena a população
        populacao = sorted(populacao, key=avaliar) 

        melhor_individuo = populacao[0] ## Após ordenação pega o primeiro e melhor individuo
        conflitos = avaliar(melhor_individuo)

        print("")
        print(f"Melhor individuo: {melhor_individuo} - Conflitos: {conflitos}")

        ## Verifica se o individuo possui 0 conflitos
        if conflitos == 0:
            fim_tempo = time.time() ## Marca o fim do tempo se sucesso
            tempo_execucao = fim_tempo - inicio_tempo ## Calcula o tempo total se sucesso
            print("")
            print("Solução encontrada!")
            print(f"Tempo necessário: {tempo_execucao:.4f} segundos")
            return melhor_individuo

        ## Seleciona os pais
        pais = selecionar(qtd_pais, populacao) 

        print("Pais selecionados: ")
        for i, pai in enumerate(pais):
            print(f"Pai {i+1}: {pai} - Conflitos: {avaliar(pai)}")

        ## Gera nova população via cruzamento e mutação
        filhos = []

        for s in range(len(populacao)):
            pai1, pai2 = random.sample(pais, 2)
            filho = cruzar(pai1, pai2) ## Cruzamento dos pais
            filho = mutar(filho, taxa_mutacao) ## Adiciona mutação cm taxa de 10%
            filhos.append(filho)
            print(f"Filho {s+1}: {filho} - Conflitos: {avaliar(filho)}")

        ## Atualizaçã a população com os filhos
        populacao = filhos
    
    fim_tempo = time.time() ## Marca o fim do tempo se fracasso
    tempo_execucao = fim_tempo - inicio_tempo ## Calcula o tempo total se fracasso

    print("")
    print("Número máximo de gerações atingido. Nenhuma solução perfeita encontrada.")
    return "Nenhuma solução encontrada"

############################### Encontrar 92 soluções únicas ###############################

def encontrar_92_solucoes_genetico(qtd_populacao=300, qtd_pais=80, taxa_mutacao=0.3, max_geracoes=10000):
    tracemalloc.start()
    inicio_tempo = time.time()
    populacao = gerar_populacao(qtd_populacao)

    solucoes = []
    geracoes = 0
    tentativas = 0

    while len(solucoes) < 92 and geracoes < max_geracoes:
        tentativas += 1
        populacao = sorted(populacao, key=avaliar)
        melhor = populacao[0]
        if avaliar(melhor) == 0 and melhor not in solucoes:
            solucoes.append(melhor)
            print(f"Solução {len(solucoes)}: {melhor}")

        pais = selecionar(qtd_pais, populacao)
        filhos = []
        for _ in range(len(populacao)):
            pai1, pai2 = random.sample(pais, 2)
            filho = cruzar(pai1, pai2)
            filho = mutar(filho, taxa_mutacao)
            filhos.append(filho)
        populacao = filhos
        geracoes += 1

    fim_tempo = time.time()
    mem_atual, mem_pico = tracemalloc.get_traced_memory()  # Captura o uso de memória
    tracemalloc.stop()

    print(f"\nForam encontradas {len(solucoes)} soluções únicas em {fim_tempo - inicio_tempo:.2f} segundos.")
    print(f"Memória atual usada no final: {mem_atual} bytes")
    print(f"Pico de uso de memória: {mem_pico} bytes")
    return solucoes
