# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# import re


def ip_address(address):
    """

    :param address:
    :return:
    """
    # One linear solution
    # new_address = re.sub("[.]", "[.]", address)

    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address


ipaddress = ip_address("1.1.2.3")
print(ipaddress)
