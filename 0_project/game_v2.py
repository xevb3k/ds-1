"""
Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

# интервал загадываемого/угадываемого числа
a = 1
b = 100

import numpy as np

def predict(number: int = 1) -> int:
    """Угадываем число бинарным поиском

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    x1 = a
    x2 = b

    predict_number = (x2-x1+1) // 2    # предполагаем что число в середине
    count = 1                          # минимум одна попытка точно нужна

    while True:        
        if (number == predict_number):
            break
        if number < predict_number:
            x2 = predict_number - 1
        else:
            x1 = predict_number + 1
        if x1 == x2:
            predict_number = x1
        else:
            predict_number = np.random.randint(x1, x2)  # предполагаемое число
        count += 1
    return count


def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(a, b, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
   score_game(predict)
