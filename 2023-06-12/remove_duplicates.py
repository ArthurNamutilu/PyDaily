#!/usr/bin/python3
def remove_duplicates(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

my_list = [1, 2, 3, 3, 4, 5]
print(remove_duplicates(my_list))
