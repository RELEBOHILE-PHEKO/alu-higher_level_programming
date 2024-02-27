#!/usr/bin/python3
for first_number in range(0, 10):
    for second_number in range(first_number + 1, 10):
        if first_number == 8 and second_number == 9:
            print("{:02d}".format(first_number * 10 + second_number))
        else:
            print("{:02d},".format(first_number * 10 + second_number), end='')
