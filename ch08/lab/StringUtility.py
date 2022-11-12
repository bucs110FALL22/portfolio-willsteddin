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

    def fixStart(self):
        repetitions = 0
        newstr = ""
        if len(self.string) <= 1:
            return self.string
        charOne = self.string[0]
        for char in self.string:
            if char == charOne:
                if repetitions == 0:
                    newstr += char
                    repetitions += 1
                else:
                    newstr += "*"
            else: newstr += char
        return newstr

    def asciiSum(self):
        sum = 0
        for char in self.string:
            sum += ord(char)
        return sum

    def cipher(self):
        newstr = ""
        shift = len(self.string)
        for char in self.string:
            if ord(char) == 32:
                newstr += char
            if char.isupper() and ord(char) != 32:
                newstr += chr((ord(char) + shift-65) % 26 +65)
            elif char.islower() and ord(char) != 32:
                newstr += chr((ord(char) + shift-97) % 26 +97)
        return newstr

