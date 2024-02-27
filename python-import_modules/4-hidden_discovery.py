#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    alif = dir()
    for i in range(0, len(alif)):
        if alif[i][:2] !="__":
            print("{:s}".format(alif[i]))
