import time

def algorithmic_even_numbers(n):
    result = []
    for number in range(2, n + 1, 2):  # Перебираем четные числа
        if int(str(number)[0]) <= 5:  # Проверяем первую цифру
            result.append(number)
    return result
def functional_even_numbers(n):
    return [number for number in range(2, n + 1) if number % 2 == 0 and int(str(number)[0]) <= 5]
def algorithmic_even_numbers_limited(n):
    result = []
    for number in range(2, n + 1, 2):
        if int(str(number)[0]) <= 5 and number < 1000:  # Ограничение на количество цифр
            result.append(number)
    return result

def functional_even_numbers_limited(n):
    return [number for number in range(2, n + 1) if number % 2 == 0 and int(str(number)[0]) <= 5 and number < 1000]

# Сравнение времени выполнения с учетом ограничений
# Задаем значение n
n = 1000

# Алгоритмический подход
start_time = time.time()
algorithmic_result_limited = algorithmic_even_numbers_limited(n)
algorithmic_time_limited = time.time() - start_time

# Функциональный подход
start_time = time.time()
functional_result_limited = functional_even_numbers_limited(n)
functional_time_limited = time.time() - start_time

# Вывод результатов с ограничениями
print("Algorithmic Result with Limitations:", algorithmic_result_limited)
print("Algorithmic Time with Limitations (s):", algorithmic_time_limited)

print("Functional Result with Limitations:", functional_result_limited)
print("Functional Time with Limitations (s):", functional_time_limited)