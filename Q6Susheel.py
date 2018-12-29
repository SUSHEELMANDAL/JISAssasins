class Sorting:
    def takeInputInt(self):
        n = int(input("Enter the number of names you want to insert"))
        j = []
        for i in range(0, n):
            num = input("enter the name \n")
            j.append(num)
        return j

    def sortInput(self,k):
        k.sort()
        print(" The sorted list for the given input is ", k)
sorting = Sorting()
num=sorting.takeInputInt()
sorting.sortInput(num)


