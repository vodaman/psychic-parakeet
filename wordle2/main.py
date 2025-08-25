# import necessary libraries
from random import choice
from english_dictionary.scripts.read_pickle import get_dict
from time import sleep

dictionary = list(filter(lambda w: len(w) == 5, map(str.lower, get_dict())))
word = choice(dictionary)
attemptCount = 0
attempt = ""

print(len(dictionary))
sleep(1)

print(word)

while attemptCount <= 5:
    attempt = input()
    if len(attempt) == 5:
        for i in range(len(attempt)):
            if attempt[i] == word[i]:
                print("{" + attempt[i] + "}", end="")
            elif attempt[i] in word:
                print("[" + attempt[i] + "]", end="")
            else:
                print(attempt[i], end="")
    elif len(attempt) < 5:
        print("too few letters")
        continue
    else:
        print("too many letters")
        continue
    print("")
    attemptCount += 1
