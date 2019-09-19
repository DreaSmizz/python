print("Hello World")
print("This line will be printed")
x = 1
if x == 1:
    print("x is 1")
myint = 7
print(myint)
myfloat = 7.0
print(myfloat)
mystring = "hello"
print(mystring)
mystring = "Hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])
for x in mylist:
    print(x)

