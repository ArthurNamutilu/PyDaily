#!/usr/bin/python3
my_list = [1, 2, 'Gg', 3, 4, 5]
x = 4
printed_integers = 0
for i in range(x):
    try:
        print(f"{my_list[i]:d}", end="")
        printed_integers += 1
    except ValueError:
        pass
print()
print(f"printed integers: {printed_integers:d}")
