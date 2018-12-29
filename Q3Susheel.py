class Library:
    def choice(self):
        n = 0
        while n == 0:
            print("""
            1.Add Book Information
            2.Display Book Information
            3.list all book of given Author
            4.list the count of book in the library
            5.exit""")
            ch = int(input("enter your choice"))
            if ch == 1:
                print("enter the book information")
                n = 0
            elif ch == 2:
                print(" enter the book name ")
                n = 0
            elif ch == 3:
                print("enter the author name ")
            elif ch == 4:
                print("count of the book in lib is ***")
                n = 0
            elif ch == 5:
                print(" successfully exited from the library portal ")
                n = 1
            else:
                print("sorry.....!!!!! wrong choice")


library = Library()
library.choice()
