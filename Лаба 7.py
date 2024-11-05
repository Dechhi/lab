import tkinter as tk
from tkinter import scrolledtext
import time

def algorithmic_even_numbers_limited(n):
    result = []
    for number in range(2, n + 1, 2):
        if int(str(number)[0]) <= 5 and number < 1000:
            result.append(number)
    return result

def run_algorithm():
    try:
        n = int(entry.get())
        if n < 1:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Введите натуральное число больше 0.")
            return

        start_time = time.time()
        result = algorithmic_even_numbers_limited(n)
        elapsed_time = time.time() - start_time

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Четные числа до {n}, крайняя левая цифра которых не превышает 5:\n")
        result_text.insert(tk.END, f"{result}\n")
        result_text.insert(tk.END, f"Время выполнения: {elapsed_time:.6f} секунд")
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Введите корректное натуральное число.")

# Создание основного окна
root = tk.Tk()
root.title("Поиск четных чисел")

# Метка для ввода значения n
label = tk.Label(root, text="Введите значение n:")
label.pack()

# Поле для ввода
entry = tk.Entry(root)
entry.pack()

# Кнопка для запуска алгоритма
button = tk.Button(root, text="Найти четные числа", command=run_algorithm)
button.pack()

# Поле для вывода результатов
result_text = scrolledtext.ScrolledText(root, width=50, height=15)
result_text.pack()

# Запуск основного цикла
root.mainloop()