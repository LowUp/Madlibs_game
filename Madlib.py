from Madlibs_class import madlibs_class
from itertools import repeat

missing_word = []

missing_word += list(repeat("__", 14))

words = madlibs_class(missing_word)


def Text():
    text = [
        ["It was " + words.get_missing_word(0) + ", cold November day. "],
        ["I woke up to the " + words.get_missing_word(1)],
        ["smell of " + words.get_missing_word(2)],
        ["roasting in the " + words.get_missing_word(3) + " dowstairs."],
        ["I " + words.get_missing_word(4) + " down the stairs to see if I could help"],
        [words.get_missing_word(5) + " the dinner."],
        ["My mom said, 'See if '" + words.get_missing_word(6)],
        ["needs a fresh" + words.get_missing_word(7)],
        ["So I carried a tray of glasses full of " + words.get_missing_word(8)],
        ["into the " + words.get_missing_word(9) + " room."],
        ["When I got there, I couldn't believe my " + words.get_missing_word(10) + " !"],
        ["There were " + words.get_missing_word(11)],
        [words.get_missing_word(12) + " on the"],
        [words.get_missing_word(13) + " !"]
    ]
    return text


def display_text(text):
    for sentence in text:
        print(sentence)


def input_words(text):
    print("Fill the blanks !")

    counter = 0

    for sentence in text:
        print(sentence)
        words.set_missing_word(counter, input("- "))
        counter += 1


input_words(Text())

display_text(Text())





