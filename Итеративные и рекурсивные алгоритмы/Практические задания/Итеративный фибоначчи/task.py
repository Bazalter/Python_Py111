def fib_iterative(n: int) -> int:
    """
    Вычислить n-е число последовательности Фибоначчи, используя итеративный алгоритм.

    :param n: Номер числа последовательности Фибоначии. Нумерация чисел с 0
    :return: n-е число последовательности Фибоначчи
    """
    if n < 0:
        raise ValueError()
    a, b = 0, 1
    if n == 0:
        return a

    if n == 1:
        return b

    for _ in range(2, n+1):
        c = a + b
        a, b = b, c
    return c


