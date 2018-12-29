class SumLast:
    def __init__(self):
        self.num = int(input("Enter the number"))
        self.sum=0

    def calSum(self):
        ld = self.num % 10
        fd = self.num
        while (self.num >= 10):
            self.num = self.num // 10
        fd = self.num
        self.sum = fd + ld

    def printSum(self):
        print("The sum of first and last digit of the number is", self.sum)


sumLast = SumLast()
sumLast.calSum()
sumLast.printSum()
