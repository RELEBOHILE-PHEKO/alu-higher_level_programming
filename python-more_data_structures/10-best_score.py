#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum_value = 0
    maximum_key = None
    for key, value in a_dictionary.items():
        if value > maximum_value:
            maximum_value = value
            maximum_key = key
    return maximum_key
