class Intr:
    def takeInputInt(self):
        n = int(input("Enter the number of number you want to insert"))
        j = []
        for i in range(0, n):
            num = int(input("enter the number \n"))
            j.append(num)
        return j

    def checkMinMax(self, k):
        print("the max value  is ", max(k))
        print(" the min value is ", min(k))



it = Intr()
num = it.takeInputInt()
it.checkMinMax(num)

