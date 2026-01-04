# x = [1,2,3,4]
# y = [1,2,3,4,]
# print(x is not y)


# s = 'i love python'
# print(s.index('love'))


# l = (1,2,3,[1,2,5])
# print(l.index(3))

# s = 'this is python'
# print(s[8:2:-2])

# print(s[5:5 : 4])

# s = 'this is python class'
# print(s.split('i' , 1))

# s = 'python'
# print(' '.join(s))

# s1 = 'python'
# print('+'.join(s1))

# l = [200, 300 , 400 , 5000]
# l.sort(reverse=True)
# print(l)

# l= ['x' , 'y', 'z', 1, 2, 3]
# d1= dict.fromkeys(l,50)
# print(d1)

# s1 = {1,2,3,4}
# s2 = {5,6,7,8}
# print(s1.isdisjoint(s2))

# n = int(input("enter a number:"))
# i = 1
# sum = 0
# while(i<=n):
#     sum = sum+i
#     if(i<n):
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     i = i+1
# print(sum)


# n = int(input("enter a number:"))
# i = 1
# while(i<=n):
#     print('*'* n)
#     i = i+1

# n = int(input("enter a number:"))
# i = 1
# while(i<=n):
#     print('* '*i + '' *(n-i))
#     i = i+1


# n = int(input("enter a number:"))
# i = 1
# while(i<=n):
#     print(''*(n-i) + '*'*i)
#     i = i+1

# n = int(input("enter a number:"))
# i = 0
# while(i<=n):
#     print(''*i + '*'*(n-i))
#     i = i+1


# n = int(input("enter a number:"))
# i = 0
# while(i<=n):
#     print(''*i + '*'*(n-i))
#     i = i+1
# i = i-2
# while(i>=0):
#     print(''*i + '*'*(n-i))
#     i = i-1


# n = int(input("enter a number:"))
# i =1
# while(i<=n):
#     ch='A'
#     j=1
#     while(j<=n):
#         print(ch , end=' ')
#         ch = chr(ord(ch)+1)
#         j = j+1
#     print()
#     i = i+1


# n = int(input("enyter a vavbn"))
# i =1
# while(i<=n):
#     ch = 'A'
#     j = 1
#     while(j<=i):
#         print(ch, end =' ')
#         ch = chr(ord(ch)+1)
#         j = j+1
#     print()
#     i = i+1


# n = int(input("enter a number:"))
# i =1
# while(i<=n):
#     ch='A'
#     j=1
#     while(j<=n):
#         print(ch , end=' ')
#         ch = chr(ord(ch)+1)
#         j = j+1
#     print()
#     i = i+1


# n = int(input("enyter a vavbn"))
# i =1
# while(i<=n):
#     ch = 'A'
#     j = 1
#     while(j<=i):
#         print(ch, end =' ')
#         ch = chr(ord(ch)+1)
#         j = j+1
#     print()
#     i = i+1


# n = int(input("enyter a number:"))
# i =1
# while(i<=n):
#     j = 1
#     while(j<=i):
#         print(i,end =' ')
#         j = j+2
#     print()
#     i = i+2


# def add(*n):
#     sum = 0
#     li = {}
#     li.append(n)
#     return li
# x = add(*eval(input("enter a number:")))
# print(x)

# class parent:
#     x = 10
#     def home(self):
#         print("hello")
# class child(parent):
#     print("hello world")

# obj = child()
# print(obj.x)
# obj.home()

# class Grandparnet:
#     x = 10
#     def home(self):
#         print("home for gparent")
# class parent(Grandparnet):
#     def home(self):
#         print("home for parnt")
#         super().home()
# class child(parent):
#     def home(self):
#         print("home for child")
#         super().home()

# obj = child()
# obj.home()






