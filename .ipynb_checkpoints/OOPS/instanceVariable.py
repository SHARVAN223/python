class student:
    def __init__(self,name,contact):
        self.n = name 
        self.c = contact
        print(self.n, self.c)

    def addnew(self, roll):
        self.r = roll
        print(self.r)

    def display(self):
        print(self.n, self.c, self.r, self.email)

obj=student('sharvan',12345)
obj.addnew(101)
obj.email = "sharvan705@gmail.com"
obj.display()
print(obj.n, obj.c, obj.r,obj.email)




