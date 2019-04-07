#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
# Единичная функция
#
# Написать функцию, возвращающую свой аргумент
#
# identity("a") -> "a"
def identity(x):
    return x


###############################################################################
# Инфляция
#
# Написать функцию, вычисляющую стоимость объекта через
# несколько лет. Каждый год стоимость растет на определенный процент.
#
# orig - начальная стоимость
# ir - значение роста стоимости в процентах
# n - количество лет
#orig=float(input())
#n=float(input())
#ir=float(input())
def inflation(orig, ir, n):
    for i in range(n):
        orig=orig*(1+ir/100)
    return orig


###############################################################################
# Делимость
# Написать предикат (функцию, возвращающую логическое значение), проверяющий
# делиться ли одно число на другое
def is_divisor(dividend, divisor):
    if dividend%divisor==0:
        return True
    else:
        return False


###############################################################################
# Простое число
#
# Задание: написать предикат (функцию, возвращающую логическое значение),
# проверяющие является ли аргумент простым числом
def is_prime(n):
    for i in range(2,n+1):
        if n%i==0 and i<n:
            return False
        else:
            return True

#
#
#
###############################################################################
###############################################################################
###############################################################################
###### Набор тестов
######
###### Запускать из коммандной строки python task2.py
######
def test(got, expected):
    if got == expected:
        print("      ok: for {}".format(expected))
    else:
        print("=========")
        print("    neok:")
        print("получено:")
        print(got)
        print("ожидаемо:")
        print(expected)
        print("=========")


def main():
    print("identitiy")
    test(identity("a"), "a")
    test(identity(len), len)

    print("\ninflation")
    test(inflation(100.0, 0, 10), 100.0)
    test(inflation(1.0, 100, 5),  32.0)

    print("\nis_divisor")
    test(is_divisor(4, 2), True)
    test(is_divisor(32, 3), False)
    test(is_divisor(999, 9), True)
    test(is_divisor(256, 16), True)

    print('\nis_prime')
    test(is_prime(2), True)
    test(is_prime(3), True)
    test(is_prime(2017), True)
    test(is_prime(39916801), True)
    test(is_prime(4), False)
    test(is_prime(1443), False)
    test(is_prime(10201), False)


if __name__ == '__main__':
    main()
