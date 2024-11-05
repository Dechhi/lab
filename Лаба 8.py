
import tkinter as tk
from tkinter import filedialog
import csv
from math import radians, sin, cos

class Pentagon:
    def __init__(self, center_x, center_y, size, color):
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
        self.color = color

    def segment(self):
        """Разделение на сегменты (в данном случае просто возвращает координаты пятого угольника)"""
        angles = [radians(i * 72) for i in range(5)]
        return [(self.center_x + self.size * cos(angle),
                 self.center_y + self.size * sin(angle)) for angle in angles]

    def visualize(self, canvas):
        """Визуализация пятиугольника на заданном канвасе"""
        coords = self.segment()
        for i in range(len(coords)):
            x0, y0 = coords[i]
            x1, y1 = coords[(i + 1) % len(coords)]
            canvas.create_line(x0, y0, x1, y1, fill=self.color)

    def colorize(self, new_color):
        """Изменение цвета пятиугольника"""
        self.color = new_color

    def move(self, dx, dy):
        """Перемещение пятиугольника по плоскости"""
        self.center_x += dx
        self.center_y += dy

class PentagonApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.pentagons = []

        # Кнопка для загрузки данных
        load_button = tk.Button(root, text="Загрузить данные", command=self.load_data)
        load_button.pack()

        # Пример перемещения и раскрашивания
        self.example_operations()

    def load_data(self):
        """Загрузка данных из CSV файла"""
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')  # Используем ';' как разделитель
                for row in reader:
                    if len(row) != 4:  # Проверка на количество элементов
                        print(f"Ошибка: ожидается 4 значения, но получено {len(row)}. Строка: {row}")
                        continue
                    try:
                        x, y, size, color = [item.strip() for item in row]  # Удаление пробелов
                        pentagon = Pentagon(float(x), float(y), float(size), color)
                        self.pentagons.append(pentagon)
                        pentagon.visualize(self.canvas)
                    except ValueError as e:
                        print(f"Ошибка в данных: {e}. Строка: {row}")

    def example_operations(self):
        """Пример использования методов перемещения и раскраски"""
        pentagon = Pentagon(200, 200, 50, "blue")
        pentagon.visualize(self.canvas)
        pentagon.move(20, 20)
        pentagon.colorize("red")
        self.canvas.delete("all")
        pentagon.visualize(self.canvas)

if __name__ == "__main__":
    root = tk.Tk()
    app = PentagonApp(root)
    root.mainloop()
