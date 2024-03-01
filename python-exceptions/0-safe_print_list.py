#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")  # Print element without any space
            count += 1
        except IndexError:
            break
    print("")  # Print a newline after printing all elements
    return count
