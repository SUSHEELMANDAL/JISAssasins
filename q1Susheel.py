class Input:
    def takeInputInt(self):
        n = int(input("Enter the number of number you want to insert"))
        j = []
        for i in range(0, n):
            num = int(input("enter the number \n"))
            j.append(num)
        return j

    def checkInput(self,k):
        count_zero = 0
        count_even = 0
        count_odd = 0
        for i in k:
            if i == 0:
                count_zero += 1
            elif i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        print("the count of zeros are {}\nthe count of even number is {}\nthe count of odd number are {}".format(count_zero,count_even,count_odd))

it = Input()
num = it.takeInputInt()
it.checkInput(num)
