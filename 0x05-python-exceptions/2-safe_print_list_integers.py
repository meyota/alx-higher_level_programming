#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        elem = my_list[i]
        try:
            print("{:d}".format(elem), end="")
            num += 1
        except Exception:
            continue
    print()
    return (num)
