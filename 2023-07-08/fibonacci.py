#!/usr/bin/python3

def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize with the first two Fibonacci number

  # Generate Fibonacci numbers up to the desired count
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

myno = int(input('Input value to get its fibonacci values: '))
fib_nums = fibonacci(myno)
print(fib_nums)

