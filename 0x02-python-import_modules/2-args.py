#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(f"{len(sys.argv)-1} arguments.")
    elif len(sys.argv) == 2:
        print(f"{len(sys.argv)-1} argument:")
        for n in range(len(sys.argv)):
            if n != 0:
                print(f"{n}: {sys.argv[n]}")
    else:
        print(f"{len(sys.argv)-1} arguments:")
        for n in range(len(sys.argv)):
            if n != 0:
                print(f"{n}: {sys.argv[n]}")
