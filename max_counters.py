# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def max_counter(max_number, lst_values):
    """

    :param max_number:
    :param lst_values:
    :return:
    """

    counters = [0] * max_number
    start_line = 0
    current_max = 0

    for i in lst_values:
        x = i - 1

        if i > max_number:
            start_line = current_max
        elif counters[x] < start_line:
            counters[x] = start_line + 1
        else:
            counters[x] += 1

        if i <= max_number and counters[x] > current_max:
            current_max = counters[x]

    print(counters, '--------\n')
    for i in range(len(counters)):
        if counters[i] < start_line:
            print(i, start_line)
            counters[i] = start_line

    return counters


print(max_counter(5, [3, 4, 4, 6, 1, 4, 4]))
