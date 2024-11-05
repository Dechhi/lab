def number_to_words(number):
    digit_to_word = {
        '0': 'ноль',
        '1': 'один',
        '2': 'два',
        '3': 'три',
        '4': 'четыре',
        '5': 'пять',
        '6': 'шесть',
        '7': 'семь',
        '8': 'восемь',
        '9': 'девять'
    }
    return ' '.join(digit_to_word[digit] for digit in str(number))


def process_sequences():
    try:
        # Чтение данных из файла input.txt
        with open('input.txt', 'r', encoding='utf-8') as file:
            content = file.read().strip()

        # Разбиение ввода на отдельные элементы
        numbers = content.split()
        current_sequence = []
        results = []

        for number_str in numbers:
            # Проверка, что элемент является натуральным числом
            if not number_str.isdigit() or int(number_str) == 0:
                continue

            number = int(number_str)
            # Составление последовательности чисел в порядке возрастания
            if not current_sequence or number > current_sequence[-1]:
                current_sequence.append(number)
            else:
                # Если последовательность завершена, обрабатываем минимальное число
                if len(current_sequence) > 1:
                    min_number = min(current_sequence)
                    min_number_words = number_to_words(min_number)
                    sequence_rest = [str(num) for num in current_sequence if num != min_number]
                    results.append(f"{min_number_words} {' '.join(sequence_rest)}")
                current_sequence = [number]

        # Обработка последней последовательности
        if len(current_sequence) > 1:
            min_number = min(current_sequence)
            min_number_words = number_to_words(min_number)
            sequence_rest = [str(num) for num in current_sequence if num != min_number]
            results.append(f"{min_number_words} {' '.join(sequence_rest)}")

        # Вывод результатов
        for result in results:
            print(result)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Вызов функции для обработки последовательностей
process_sequences()