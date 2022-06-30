#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    print(f"{len(sys.argv)} argument:")
    for n in range(len(sys.argv)):
        print(f"{n+1}: {sys.argv[n+1]}")
