def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        return [list(map(int, line.split())) for line in file]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print()

def transpose(matrix):
    N = len(matrix)
    return [[matrix[j][i] for j in range(N)] for i in range(N)]

def calculate_matrix_F(A):
    N = len(A)
    F = [row[:] for row in A]  # Копируем матрицу A в F

    # Находим минимальный элемент в нечетных столбцах
    min_odd_columns = float('inf')
    for i in range(N):
        if i % 2 == 0:  # нечетные столбцы (0, 2, ...)
            for j in range(N):
                if A[j][i] < min_odd_columns:
                    min_odd_columns = A[j][i]

    # Считаем сумму чисел в нечетных строках
    sum_odd_rows = 0
    for i in range(N):
        if i % 2 == 0:  # нечетные строки (0, 2, ...)
            sum_odd_rows += sum(A[i])

    # Меняем области в F
    if min_odd_columns < sum_odd_rows:
        # Поменять симметрично области 3 и 2
        for i in range(N):
            if i % 2 == 1:  # четные столбцы
                for j in range(N):
                    if j % 2 == 0:  # нечетные строки
                        F[j][i], F[i][j] = F[i][j], F[j][i]
    else:
        # Поменять несимметрично области 2 и 3
        for i in range(N):
            if i % 2 == 0:  # нечетные строки
                for j in range(N):
                    if j % 2 == 1:  # четные столбцы
                        F[i][j], F[j][i] = F[j][i], F[i][j]

    return F

def matrix_operations(K, A, F):
    N = len(A)

    # Вычисляем K * F
    KF = [[K * F[i][j] for j in range(N)] for i in range(N)]

    # Вычисляем A^T
    AT = transpose(A)

    # Вычисляем K * A^T
    KAT = [[K * AT[i][j] for j in range(N)] for i in range(N)]

    # Вычисляем (K * F) * A
    KFA = [[0] * N for _ in range(N)]  # Инициализируем результирующую матрицу
    for i in range(N):
        for j in range(N):
            KFA[i][j] = sum(KF[i][k] * A[k][j] for k in range(N))

    # Вычисляем (K * F) * A - K * A^T
    result_matrix = [[KFA[i][j] - KAT[i][j] for j in range(N)] for i in range(N)]

    return result_matrix

def main():
    # Считываем K и N
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    # Считываем матрицу A из файла
    A = read_matrix_from_file('matrix.txt')
    print("Матрица A:")
    print_matrix(A)

    # Формируем матрицу F
    F = calculate_matrix_F(A)
    print("Матрица F:")
    print_matrix(F)

    # Выполняем матричные операции
    result = matrix_operations(K, A, F)
    print("Результат (K * F * A - K * A^T):")
    print_matrix(result)

if __name__ == "__main__":
    main()