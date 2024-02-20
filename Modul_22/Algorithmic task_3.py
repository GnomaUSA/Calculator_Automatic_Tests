# Напишите функцию replace_duplicates, которая принимает на вход произвольную строку s.
# Функция должна заменять две одинаковые буквы на следующую по алфавиту букву.
# Несколько важных моментов:
# буквы не обязаны быть смежными (смежные - стоящие рядом;
# в строке 'abc' буквы a и b, а также b и c - являются смежными, в то время как a и c - нет)
# zz заменяем на a
# строка s состоит из букв английского алфавита в строчном регистре
# Повторяйте операцию, пока не останется никаких возможных замен.
# Функция должна вернуть строку с оставшимися буквами в любом порядке.

def replace_duplicates(s):
    from collections import Counter
    from string import ascii_lowercase

    # Создание словаря для сопоставления букв со следующими буквами в алфавите
    letter_map = {letter: ascii_lowercase[(i + 1) % 26] for i, letter in enumerate(ascii_lowercase)}

    # Считаем количество каждой буквы в строке
    letter_count = Counter(s)

    # Повторяем процесс замены, пока есть дубликаты
    changes = True
    while changes:
        changes = False
        for letter, count in list(letter_count.items()):
            # Если буква встречается более одного раза
            if count > 1:
                changes = True
                # Уменьшаем количество текущей буквы на 2
                letter_count[letter] -= 2
                # Увеличиваем количество следующей буквы в алфавите на 1
                next_letter = letter_map[letter]
                letter_count[next_letter] += 1

                # Удаляем букву из словаря, если она больше не встречается
                if letter_count[letter] == 0:
                    del letter_count[letter]

    # Формируем итоговую строку из оставшихся букв
    return ''.join(letter * count for letter, count in letter_count.items())

# Тестовый пример
test_string = "abbcc"
replace_duplicates(test_string)

