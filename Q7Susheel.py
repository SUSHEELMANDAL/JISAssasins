class Sum:
    def __init__(self):
        self.Sum = 0
        self.Number = int(input("Please Enter any Number: "))
    def check(self):
        while (self.Number > 0):
            Reminder = self.Number % 10
            self.Sum = self.Sum + Reminder
            self.Number = self.Number // 10
        print("\n Sum of the digits of Given Number = %d" % self.Sum)
su= Sum()
su.check()





