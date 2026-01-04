# f = open('n2.txt','a+')
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.encoding)
# print(f.closed)



#WRITELINE
# f = open('n2.txt','a+')
# data = 'this is python classs\n'
# f.write(data)
# f.close()

#WRITELINES
# f = open('n2.txt','a+')
# data = ['python\n', 'java\n', 'php\n']
# f.writelines(data)
# f.close()


#READ
# f = open('n2.txt', 'r+')
# data = f.read()
# print(data)
# data = f.read(5)
# print(data)
# f.close()


#READ(N)
# f = open('n2.txt', 'r+')
# data = f.read(10)
# print(data)
# data = f.read(5)
# print(data)
# f.close()


#READLINE
# f = open('n2.txt', 'r+')
# data = f.readline()
# print(data)
# f.close()


#READLINES
f = open('n2.txt', 'r+')
data = f.readlines()
print(data)
f.close()