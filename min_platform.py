# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_min_platform_01(arr, dep, num):
    """

    :param arr:
    :param dep:
    :param num:
    :return:
    """

    i, j, ocu_pltf, max_plft = 0, 0, 0, 0

    while (i < num and j < num):
        if arr[i] < dep[j]:
            ocu_pltf += 1
            i += 1
            if ocu_pltf > max_plft:
                max_plft = ocu_pltf
        else:
            ocu_pltf -= 1
            j += 1

    return ocu_pltf, max_plft


def get_min_platform_02(arr, dep, num):
    """

    :param arr:
    :param dep:
    :param n:
    :return:
    """

    # plat_needed indicates number of platforms
    # needed at a time
    result = 1

    # run a nested loop to find overlap
    for i in range(num):
        # minimum platform needed
        plat_needed = 1
        print('\n------------------')
        for j in range(i + 1, num):
            # check for overlap
            print(arr[i], arr[j], '----', dep[i], dep[j])
            if (max(arr[i], arr[j]) <= min(dep[i], dep[j])):
                plat_needed += 1
                print('\t\t-------', arr[i], arr[j], '----', dep[i], dep[j])
                print('\t\t-------', max(arr[i], arr[j]), '----', min(dep[i], dep[j]))

        # update result
        result = max(result, plat_needed)

    return result


arr = [100, 140, 150, 200, 215, 400]
dep = [110, 300, 220, 230, 315, 600]

# arr = [900, 940, 950, 1100, 1500, 1800]
# dep = [910, 1200, 1120, 1130, 1900, 2000]

n = len(arr)

print(get_min_platform_01(arr, dep, n))
print(get_min_platform_02(arr, dep, n))
