class StringUtility():
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        count = 0
        for i in self.string:
            if i in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                count += 1
        if count < 5:
            return str(count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            newstr = self.string[0] + self.string[1] + self.string[len(self.string)-2] + self.string[len(self.string)-1]
            return newstr