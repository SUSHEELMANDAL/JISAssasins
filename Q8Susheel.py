class Swap:
    def __init__(self):
        self.num1 = input("enter the value of num1:")
        self.num2 = input("enterrhe value of num2:")

    def swapItSelf(self):
        temp = self.num1
        self.num1 = self.num2
        self.num2 = temp

    def printAll(self):
        print('num1 after swapping: {}'.format(self.num1))
        print('num2 after swapping: {}'.format(self.num2))


swap =Swap()
swap.swapItSelf()
swap.printAll()

