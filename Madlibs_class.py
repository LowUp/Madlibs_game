class madlibs_class:

    def __init__(self, missingWords):
        self.missingWords = missingWords

    def get_missing_word(self, num):
        return self.missingWords[num]

    def set_missing_word(self, num, word):
       self.missingWords.insert(num, word)