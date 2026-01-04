#HIGHER ORDER FUNCTION-------------------------
# A. MAP-------------------------------
# Q.add
# l1 = eval(input("enter a value:"))
# l2 = eval(input("enter a value:"))
# l3 = eval(input("enter a value:"))
# def add(x,y,z):
#     return x+y+z
# res = map(add,l1,l2,l3)
# print(res)
# print(tuple(res))

# Q.square
# l1 = eval(input("enter a value:"))
# def square(n):
#     return n**2
# res = map(square,l1)
# print(res)
# print(tuple(res))

# Q.square root
# l1 = eval(input("enter a value:"))
# def sqrt(n):
#     return n**0.5
# res = map(sqrt,l1)
# print(res)
# print(tuple(res))



def show():
    x = 10
    def display():
        nonlocal x
        x = x+5
        print(x)
    display()

show()