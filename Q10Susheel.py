class Name:
    def __init__(self):
        self.string = input("Enter a string: ")
        self.array = []

    def removeVowel(self):
        for i in self.string:
            # print(i)
            if i not in "aeiouAEIOU":
                self.array.append(i)

    def printString(self):
        print("".join(self.array))


name = Name()
name.removeVowel()
name.printString()








