from Madlibs_class import madlibs_class
from itertools import repeat

missing_word = []

missing_word += list(repeat("__", 8))

words = madlibs_class(missing_word)

Text = [
    ["It was " + words.get_missing_word(0) + ", cold November day. "]
   # ["I woke up to the __ smell of __ roasting in the __ dowstairs."]
]


def display(T):
    print("Fill the blanks !")

    counter = 0

    for sentence in T:
        print(sentence)
        words.set_missing_word(counter, input("- "))
        counter += 1


display(Text)


