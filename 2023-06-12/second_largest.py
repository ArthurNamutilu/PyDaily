#!/usr/bin/python3
def find_second_largest(numbers):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest

numbers = [5, 12, 8, 17, 3, 10]
print(find_second_largest(numbers))
