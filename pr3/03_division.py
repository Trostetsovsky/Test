# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b, c = 179, 37, 0
copy_a = a
while a >= b:
    a -= b
    c += 1
print("Целочисленное деление", copy_a, "на", b, "даёт", c)