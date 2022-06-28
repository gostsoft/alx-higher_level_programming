#!/usr/bin/python3
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

for let in letters:
    if let == "e" or let == "q":
        continue
    else:
        print(let)
