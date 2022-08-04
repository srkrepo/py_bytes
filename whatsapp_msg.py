# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pywhatkit

# syntax: phone number with country code, message, hour and minutes
pywhatkit.sendwhatmsg('+91xxxxxxxx', 'Your Message', 12, 1)

import pywhatkit

# syntax: group link, message, hour and minutes
pywhatkit.sendwhatmsg_to_group("group-link", "Your Message", 12, 1)

# import pytube
# link = input('Enter The Youtube Video URL')
# dn = pytube.Youtube(link)
# dn.streams.first().download()
# print('Your Video Has Been Downloaded', link)
