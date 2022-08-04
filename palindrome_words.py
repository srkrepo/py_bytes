# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'

# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import re


def palindrome(sentence):
    # for i in (",.'?/><}{{}}'"):
    #     sentence = sentence.replace(i, "")

    sentence = re.sub('[^a-zA-Z0-9 \n]', '', sentence)

    # palindrome = []
    words = sentence.split(' ')
    print(words)
    # for word in words:
    #     word = word.lower()
    #     if word == word[::-1]:
    #         palindrome.append(word)
    palindrome = [word.lower() for word in words if word.lower() == word.lower()[::-1]]
    return palindrome


print(palindrome('Madam, my mother tongue is malayalam'))
