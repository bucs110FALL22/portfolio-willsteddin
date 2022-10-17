def percentageToLetter(grade):
    if grade >= 90:
        return("A")
    elif grade >= 80 and grade < 90:
        return("B")
    elif grade >= 70 and grade < 80:
        return("C")
    elif grade >= 60 and grade < 70:
        return("D")
    else:
        return("F")

def isPassing(letter):
    if letter == "A" or letter == "B" or letter == "C":
        return(True)
    else:
        return(False)



gradeNumber = int(input("Enter the grade you received on the exam: "))
gradeLetter = percentageToLetter(gradeNumber)
print(isPassing(gradeLetter))
