#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        return my_string.translate({ord("c"): None, ord("C"): None})
    return my_string
