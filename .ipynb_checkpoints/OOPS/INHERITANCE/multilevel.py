class grandparent:
    def home(self):
        print("home from gp")
class parent(grandparent):
    def home(self):
        print("from parent class")
        super().home()
class child(parent):
    def home(self):
        print("home from child")
        super().home() 

obj = child()
obj.home()