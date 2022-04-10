class date():
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    def valid_date(self):
        if self.d<32:
            if self.m<13:
                return True
            else:
                return False
        else:
            return False
    def isleap(self):
        if self.y%4==0 or self.y%400==0:
            return True
        else:
            return False
    def Feb_check(self):
        if self.isleap()==True and self.d<29:
            print(self.d+1,self.m,self.y)
        elif self.isleap()==False and self.d<28:
            print(self.d+1,self.m,self.y)
        elif self.d== 28 and self.isleap()==False:
            print(1,self.m+1,self.y)
        elif self.isleap()==True and self.d== 29:
            print(1,self.m+1,self.y)
    def odd_month(self):
        if self.m==12 and self.d == 31:
            print(1,1,self.y+1)
        elif  self.d == 31:
            print(1,self.m+1,self.y)
        elif self.d<31:
            print(self.d+1,self.m,self.y)
    def even_month(self):
        if self.d == 30:
            print(1,self.m+1,self.y)
        elif self.d<30:
            print(self.d+1,self.m,self.y)
    def get_date(self):
        odd=[1,3,5,7,8,10,12]
        even=[4,6,9,11]
        if self.valid_date():
            if self.m==2:
                self.Feb_check()
            elif self.m in even:
                self.even_month()
            elif self.m in odd:
                self.odd_month()
        else:
            print("invalid input")
d=int(input("enter the day"))
m=int(input("enter the month"))
y=int(input("enter the year"))
a=date(d,m,y)
a.get_date()