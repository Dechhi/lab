import numpy as np
import matplotlib.pyplot as plt


def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        return np.array([list(map(int, line.split())) for line in file])


def generate_random_matrix(N):
    return np.random.randint(-10, 11, (N, N))


def print_matrix(matrix, name):
    print(f"Матрица {name}:")
    for row in matrix:
        print(" ".join(map(str, row)))
    print()


def swap_symmetric(matrix, area1, area2):
    for i in range(area1.shape[0]):
        for j in range(area1.shape[1]):
            area1[i, j], area2[i, j] = area2[i, j], area1[i, j]


def swap_non_symmetric(matrix, area1, area2):
    area1[:, :], area2[:, :] = area2, area1


def calculate_matrix_F(A, K):
    N = A.shape[0]
    n = N // 2

    B = A[:n, :n]
    C = A[n:, :n]
    E = A[:n, n:]
    D = A[n:, n:]

    F = np.copy(A)

    # Условие для изменения F
    count_greater_than_K = np.sum(E[:, ::2] > K)
    sum_odd_rows = np.sum(C[::2, :])

    if count_greater_than_K > sum_odd_rows:
        swap_symmetric(F, C, E)
    else:
        swap_non_symmetric(F, B, C)

    return F


def plot_matrices(F):
    plt.figure(figsize=(10, 5))

    # Гистограмма по элементам матрицы F
    plt.subplot(131)
    plt.hist(F.flatten(), bins=21, color='blue', alpha=0.7)
    plt.title("Гистограмма элементов F")
    plt.xlabel("Значение")
    plt.ylabel("Частота")

    # Тепловая карта матрицы F
    plt.subplot(132)
    plt.imshow(F, cmap='viridis', interpolation='nearest')
    plt.title("Тепловая карта матрицы F")
    plt.colorbar()

    # Линейный график по строкам
    plt.subplot(133)
    for i in range(F.shape[0]):
        plt.plot(F[i], label=f"Строка {i + 1}")
    plt.title("Линейный график строк F")
    plt.xlabel("Индекс столбца")
    plt.ylabel("Значение")
    plt.legend()

    plt.tight_layout()
    plt.show()


def main():
    # Считываем K и N
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    # Считываем или генерируем матрицу A
    if N <= 4:
        A = read_matrix_from_file('fixed_matrix.txt')
    else:
        A = generate_random_matrix(N)

    print_matrix(A, 'A')

    # Формируем матрицу F
    F = calculate_matrix_F(A, K)
    print_matrix(F, 'F')

    # Определитель матрицы A
    det_A = np.linalg.det(A)
    print(f"Определитель матрицы A: {det_A}")

    # Сумма диагональных элементов матрицы F
    sum_diag_F = np.trace(F)
    print(f"Сумма диагональных элементов матрицы F: {sum_diag_F}")

    # Выбор операции в зависимости от условий
    if det_A > sum_diag_F:
        # A * A^T - K * F^T
        result = np.dot(A, A.T) - K * F.T
    else:
        # (A^T + G^-1 - F^-1) * K
        G = np.tril(A)
        try:
            G_inv = np.linalg.inv(G)
            F_inv = np.linalg.inv(F)
            result = (A.T + G_inv - F_inv) * K
        except np.linalg.LinAlgError:
            print("Невозможно вычислить инверсию G или F.")
            return

    print_matrix(result, 'Результат')

    # Построение графиков
    plot_matrices(F)


if __name__ == "__main__":
    main()