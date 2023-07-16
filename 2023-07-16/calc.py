#!/usr/bin/python3

op_list = ['+', '-', '*', '/']

num1 = float(input("Enter first number: "))
op = input(f"Enter one of this operators {op_list} : ")
num2 = float(input("Enter second number: "))

if op not in op_list:
    print('Invalid operator')
elif op == op_list[0]:
    result = num1 + num2
    print(f'{num1} {op} {num2} is: {result}')
elif op == op_list[1]:
    result = num1 - num2
    print(f'{num1} {op} {num2} is: {result}')
elif op == op_list[2]:
    result = num1 * num2
    print(f'{num1} {op} {num2} is: {result}')
elif op == op_list[3]:
    result = num1 / num2
    print(f'{num1} {op} {num2} is: {result}')
