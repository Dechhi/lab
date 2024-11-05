import time
import math

def recursive_F(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (-1)**n * (2 * recursive_F(n - 1) / math.factorial(n) + recursive_F(n - 2))

def iterative_F(n):
    if n == 0 or n == 1:
        return 1

    F = [0] * (n + 1)  # Список для хранения значений F(n)
    F[0], F[1] = 1, 1  # Начальные условия

    for i in range(2, n + 1):
        F[i] = (-1)**i * (2 * F[i - 1] / math.factorial(i) + F[i - 2])

    return F[n]

# Таблица для хранения результатов
results = []

# Определяем диапазон значений n
n_values = list(range(1, 21))  # Измените диапазон по мере необходимости

for n in n_values:
    # Измеряем время для рекурсивного подхода
    start_time = time.time()
    recursive_result = recursive_F(n)
    recursive_time = time.time() - start_time

    # Измеряем время для итеративного подхода
    start_time = time.time()
    iterative_result = iterative_F(n)
    iterative_time = time.time() - start_time

    # Сохранение результатов в таблице
    results.append((n, recursive_result, recursive_time, iterative_result, iterative_time))

# Печатаем результаты в виде таблицы
print(" n | Recursive Result | Recursive Time (s) | Iterative Result | Iterative Time (s)")
print("-" * 70)
for result in results:
    print(f"{result[0]:>2} | {result[1]:<16} | {result[2]:<19.6f} | {result[3]:<16} | {result[4]:<19.6f}")