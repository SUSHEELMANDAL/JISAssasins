import random


class Count:
    def __init__(self):
        self.count = 0

    def takeInput(self):
        self.num = int(input("enter a 6 digit number "))

    def genValue(self):
        self.num1 = random.randint(100000, 999999)


    def checkInput(self):
        while(self.num!=self.num1):
            self.count = self.count + 1
            self.genValue()
        print("the random took this number of time find the perecft match",self.count)


count = Count()
count.takeInput()
count.genValue()
count.checkInput()
