#!/usr/bin/env python3

def return_evens(num_list):
    even = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
    return even


def make_exclamation(sentence_list):
    exclaimed = []
    for sentence in sentence_list:
        exclaimed.append(sentence + '!')
    return exclaimed
