class parent:
    x = 10
    def home(self):
        print("from parent class")
class child(parent):
    def home(self):
        print("home from child")
        super().home() 

obj = child()
obj.home()
