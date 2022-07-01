#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print(f"{len(sys.argv)} argument:")
    for n in range(len(sys.argv)):
        if n != 0:
            print(f"{n}: {sys.argv[n]}")
