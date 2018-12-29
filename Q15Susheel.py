class Power:
    def __init__(self):
        self.x = int(input("Enter the value of base"))
        self.y = int(input("Enter the value of power y= "))
        self.z = int(input("Enter the value of power z= "))


    def calPower(self):
            self.x=(self.x**self.y)*(self.x**self.z)


    def printPow(self):
        print("The value is",self.x)

power=Power()
power.calPower()
power.printPow()