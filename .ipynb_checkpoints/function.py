# def xyz():
#     print("hello")
# xyz()
# xyz()


# def add(x,y):
#     print(x+y)
#     return(x+y)
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# res = add(p,q)
# print(res)


# def add(x,y):
#     z = x+y
#     return z
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# res = add(p,q)
# print(res)


# def add(x,y):
#     print(x+y)
#     return (x+y)
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# res = add(p,q)
# print(res)
# print(add(p,q))




# USER DEFINE FUNCTION------------------------------

#A. with argument without return-------------------------
# def fun_name(x,y):
#     print(x+y)
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# fun_name(a,b)


#B. with argument with return-------------------------
# def fun_name(x,y):
#     z = x-y
#     return z
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# print(fun_name(a,b))


# c. without argument with return---------------------------
# def fun_name():
#    x = a
#    y = b
#    z = x*y
#    return z
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# print(fun_name())


# D. without argument without return
# def fun_name():
#    x = a
#    y = b
#    print(x//y)
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# fun_name()



# POSTIONAL ARUMENT---------------------------------
# def add(x,y,z):
#     return x+y+z
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# r = int(input("enter a number:"))
# res = add(p,q,r)
# print(res)

# res = add() - error (add() missing 3 required postional arument x,y,z)
# res = add(p)
# res= add(p,q)

# DEFAULT POSTIONAL ARGUMENT--------------------------------
# def add(x = 0, y=0, z=0):
#     return(x+y+z)
# print(add(10,20,30))
# print(add())
# print(add(10))
# print(add(10,20))
# print(add(10,20,30,40))    error--    (add() takes from 0 to 3 positional argument but 4 were given)

# VARIABLE LENGTH POSTIONAL ARUMENT----------------------------------
# def add(*args):
#     print(args)
#     print(type(args))
# add(1,2,3,4,5,6,7,8,9,10)

# Q.
# def add(*n):
#     sum = 0
#     for i in n:
#         sum = sum +i
#     return sum
# x = add(1,2,3,4,5,6)
# print(x)


# def add(*n):
#     print(n)
#     print(type(n))
# x = add(eval(input("enter a value:")))
# print(x)

# def add(*n):
#     print(n)
#     print(type(n))
# x = add(*eval(input("enter a number:")))
# print(x)

# def add(*n): convet tuple to list
#     li = []
#     li.append(n)
#     return li
#     print(type(n))
# x = add(*eval(input("enter a number:")))
# print(x)

# KEYWORD - ARGUMENT------------------------------------
# def fun_name(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# r = int(input("enter a number:"))
# fun_name(z = p, y = q,x = r)
# fun_name()
# fun_name(z = p, y = q, x = r)

# DEFAULT KEYWORD ARGUMENT-------------------------------
# def fun_name(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# p = int(input("enter a number:"))
# q = int(input("enter a number:"))
# r = int(input("enter a number:"))
# fun_name(z = p, y = q,x = r)
# fun_name()
# fun_name(z = p, y = q, x = r)

# VARIBALE LENGTH KEYWORD ARUMENT-----------------------------

  
# def fun_name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fun_name(**eval(input("enter any dist:")))


# ex :
# def fun_name(**kwargs):
    # for i in kwargs.keys():
    #     print(i)
    
    # for i in kwargs.values():
    #     print(i)
    
#     for i ,j in kwargs.items():
#         print('key=',i , 'values =' ,j)

# fun_name(x = 10 , y = 20, z = 67, p = 67, q = 45)




# ALL ARGUMENT PARAMETER
# def fun_name(x,y = 0,*z, p , **q):
#     print(x)
#     print(y)
#     print(z)
#     print(p)
#     print(q)

# fun_name(10, 20, 30, 40, 50, p = 5, r = 2, s = 1, t = 3)


# Q.
# def natural_num(n):
#     for i in range(1, n+1):
#         print(i)

# n = int(input("enter a number:"))
# natural_num(n)

# Q.
# def natural_sum(a):
#     ans = 0
#     for i in range(1,a+1):
#         ans+=i
#     return ans
# num = int(input("enter a number:")) 
# print(natural_sum(num))

# Q.
# def even(n):
#     for i in range(2 , n+1 , 2):
#         print(i)
# n = int(input("enter a value:"))
# even(n)


# Q
# def factorial(a):
#     ans = 1
#     for i in range(1,a+1):
#         ans*=i
#     return ans
# num = int(input("enter a number:")) 
# print(factorial(num))

# Q
# def print_1_to_10():
#     li = []
#     for i in range(11):
#         li.append(i)
#     return li
# ans = print_1_to_10()
# print(ans)

# def num(**n):
#     li = []
#     for i in n.values():
#         li.append(i)
#     return li
# print(num(**eval(input("enter a values:"))))


# Q.prime number
# def prime(num):
#     cout = 0
#     for i in range(1, num+1):
#         if(num%i ==0):
#             cout+=1
                 
#     if (cout == 2):
#         return "prime"
#     else:
#         return"not prime"

# ans = int(input("enter an number:"))
# print(prime(ans))


