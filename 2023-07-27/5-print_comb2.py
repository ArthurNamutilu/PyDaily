#!/usr/bin/python3
for i in range(00, 100):
    if i == 99:
        print(i)
    else:
        print(f"{str(i).zfill(2)}, ", end="")
