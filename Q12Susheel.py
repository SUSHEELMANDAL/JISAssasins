class Test:
    def takeInput(self):
        myText =input("enter the string")
        return myText

    def reversTxt(self, msg):
        take=msg.split(" ")
        take.reverse()
        print(" ".join(take))


test = Test()
word = test.takeInput()
test.reversTxt(word)
