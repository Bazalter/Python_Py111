def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    if n < 0:
        raise ValueError()
    res = 1
    for i in range(n+1):
        if i == 0:
            res = 1
        else:
            res *= i

    return res

# print(factorial_iterative(5))
