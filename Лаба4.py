import re
import random


def generate_file(filename, num_count=20, upper_limit=100):
    with open(filename, 'w') as file:
        numbers = [str(random.randint(1, upper_limit)) for _ in range(num_count)]
        file.write(' '.join(numbers))


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def number_to_words(number):
    digit_to_word = {
        '0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
        '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'
    }
    return ' '.join(digit_to_word[digit] for digit in str(number))


def find_sequences(numbers):
    sequences = []
    current_sequence = []

    for num in numbers:
        if not current_sequence or num > current_sequence[-1]:
            current_sequence.append(num)
        else:
            if len(current_sequence) > 1:
                sequences.append(current_sequence)
            current_sequence = [num]

    if len(current_sequence) > 1:
        sequences.append(current_sequence)

    return sequences


def main():
    filename = 'data.txt'

    # Генерируем файл с случайными числами
    generate_file(filename)

    # Считываем данные из файла
    text = read_file(filename)

    # Находим все натуральные числа в тексте
    numbers = list(map(int, re.findall(r'\b\d+\b', text)))

    # Находим последовательности натуральных чисел
    sequences = find_sequences(sorted(numbers))

    # Выводим последовательности
    for sequence in sequences:
        min_number = min(sequence)
        sequence_str = ' '.join(map(str, sequence))
        print(f"Последовательность: {sequence_str}")
        print(f"Минимальное число в последовательности: {min_number} ({number_to_words(min_number)})")


if __name__ == "__main__":
    main()