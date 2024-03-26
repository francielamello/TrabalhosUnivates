import time
import random

# Função para ordenação usando o algoritmo Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Troca os elementos se estiverem fora de ordem
    return arr

# Função para ordenação usando o algoritmo Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]  # Divide a lista em duas metades
        R = arr[mid:]

        merge_sort(L)  # Chama a função recursivamente para ordenar a metade esquerda
        merge_sort(R)  # Chama a função recursivamente para ordenar a metade direita

        i = j = k = 0

        # Combina as duas metades ordenadas
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes de L e R
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Função para medir o tempo de execução de um algoritmo de ordenação
def measure_time(algorithm, arr):
    start_time = time.time()  # Marca o tempo de início
    algorithm(arr)  # Executa o algoritmo de ordenação
    end_time = time.time()  # Marca o tempo de fim
    return end_time - start_time  # Retorna o tempo de execução em segundos

# Tamanhos dos arrays que serão testados
array_sizes = [100, 1000, 10000]

print("Teste de Desempenho:\n")

# Para cada tamanho de array, execute os testes de desempenho
for size in array_sizes:
    # Gera um array de números aleatórios
    arr = [random.randint(0, 1000) for _ in range(size)]

    # Teste de desempenho para o Bubble Sort
    bubble_sort_time = measure_time(bubble_sort, arr.copy())

    # Teste de desempenho para o Merge Sort
    merge_sort_time = measure_time(merge_sort, arr.copy())

    # Exibe os resultados
    print(f"Tamanho do array: {size}")
    print(f"Tempo Bubble Sort: {bubble_sort_time} s")
    print(f"Tempo Merge Sort: {merge_sort_time} s")
    print("----------------------------------")
