# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Candy distribution
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def distribute_candy(arr, n):
    """

    :param arr:
    :param n:
    :return:
    """

    # Default 1 is required for all
    dis = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            dis[i] = dis[i - 1] + 1
        # print(arr[i], "-", arr[i - 1], ': ', dis[i])

    print(dis,'\n\n')
    for j in range(n - 2, -1, -1):
        if arr[j] > arr[j + 1]:
            dis[j] = dis[j + 1] + 1
        # print(arr[j], "-", arr[j + 1], ': ', dis[j])

    print(dis)


if __name__ == '__main__':
    # ARR = [1, 0, 2]
    ARR = [1, 5, 2, 5]
    N = len(ARR)
    required_candy = distribute_candy(ARR, N)
