class father:
    def home(self):
        print("home from father")
        # mother().home() or
        mother.home(self)
class mother:
    def home(self):
        print("home from mother")
class child(father, mother):
    def home(self):
        print("home from child")
        super().home()

obj = child()
obj.home()