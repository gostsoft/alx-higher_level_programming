#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition_result = 0
    for n in sys.argv:
        if n != sys.argv[0]:
            addition_result += int(n)
    print(addition_result)
