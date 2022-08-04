# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Count Frequency
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def count_frequency(arr, n):
    """

    :param arr:
    :param n:
    :return:
    """

    for i in range(0, n):
        arr[i] -= 1

    for i in range(0, n):
        # print(i, arr[i] % n, '::', arr[arr[i] % n])
        arr[arr[i] % n] = n + arr[arr[i] % n]
        # print(arr, '-2-')

    for i in range(0, n):
        print('>>', i + 1, '   -> ', arr[i] // n)


if __name__ == '__main__':
    ARR = [5, 2, 7, 7, 5, 5, 2]
    N = len(ARR)
    count_frequency(ARR, N)

    items = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'C'], ['R', 'M'], ['S'], ['P'], ['A']]
    result = dict()
    for item in items:
        if item[0] not in result.keys():
            result[item[0]] = len(item) - 1
        elif item[0] in result.keys():
            result[item[0]] += len(item) - 1

    print(result)
