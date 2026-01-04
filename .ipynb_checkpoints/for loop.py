# Q. pattern

# n = int(input("enter a value:"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(i,end = ' ')
#     print()


# n = int(input("enter a value:"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(i*2,end = ' ')
#     print()


# n = int(input("enter a value:"))
# y = 1
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(y,end = ' ')
#         y = y+1
#     print()

# n = int(input("enter a value:"))
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(2*i-1,end = ' ')
#     print()

# prime
# num = 7
# cout = 0
# for i in range (1,num+1):
#     if(num%i== 0):
#         cout+=1
# if(cout==2):
#     print("prime")
# else:
#     print("not prime")

# or
# num = int(input("enter a number:"))
# ans = True
# for i in range(2, num):
#     if (num%i == 0):
#         print("not prime")
#         ans = False
#         break
# if (ans == True):
#     print("prime")


# Q.give list of all factors of any number
# n = int(input("enter a number:"))

# factorial= []

# for i in range(1 , n+1):
#     if n% i ==0:
#         factorial.append(i)

# print("factorial is ", factorial)


# Q. arrange all item from list in assending order
# n = int(input("enter a number:"))
# sum = 0
# for i in range(1, n):
#     if n%i == 0:
#         sum = sum+i
# if n == sum :
#     print(f'given number {n} is perfect number')
# else :
#     print(f'given number {n} is not perfect number')


# n= int(input("enter a number:"))
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print(j,end ='')
#     print()