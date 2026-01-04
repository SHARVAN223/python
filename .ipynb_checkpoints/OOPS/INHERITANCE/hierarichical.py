class A:
    def home(self):
        print("from class A")
class B(A):
    def home(self):
        print("from class b")
        # super().home()
        C().home()

class C(A):
    def home(self):
        print("from class c")
        # super().home()



obj = C()
obj.home()
