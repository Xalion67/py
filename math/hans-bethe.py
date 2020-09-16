# Вычисление квадратов чисел по Гансу Бете
# Метод работает до пятидесяти включительно


def trick_Hans_Bethe(num_to_power):
    limit_calculate_extent = 50

    # Разность между пятьюдесятью и числом для возведения в квадрат
    difference = limit_calculate_extent - num_to_power

    # Из 50² вычитаем разность сто раз
    result_calculated = 50 ** 2 - difference * 100

    # Для точного ответа к результату вычитания прибавляем квадрат разности
    result_calculated += difference ** 2
    return result_calculated
