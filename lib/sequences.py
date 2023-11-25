#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if (length == 0):
        print([])
    elif (length == 1):
        print('[0]')
    elif (length == 2):
        print('[0,1]\n')
    else:
        fib_sequence = [0, 1]
        for _ in range(2, length):
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)

        for number in fib_sequence:
            print(number)