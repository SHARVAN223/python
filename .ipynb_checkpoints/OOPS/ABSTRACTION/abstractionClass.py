from abc import ABC , abstractclassmethod
class A(ABC):
    def dashboard(self):
        print("welcome dashboard")
    @abstractclassmethod
    def login(self):
        pass
class B(A):
    def login(self):
        print("login sucessful")
    pass


obj = B()
obj.dashboard()
obj.login()