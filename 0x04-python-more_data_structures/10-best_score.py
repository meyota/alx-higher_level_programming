#!/usr/bin/python3
def best_score(a_dictionary):
    keymax = max(a_dictionary, key= lambda x: a_dictionary[x])
    print(keymax)
