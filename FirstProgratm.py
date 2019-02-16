
def printHello():
    print("Hello Functions")
printHello()

def printHi(name="John"):
    print("Hi, " +name)

printHi("Kasani")
printHi("Anil")

def sum(a,b,c):
    print(a+b+c)
sum(1,2,3)

def returnSum(a,b):
    return (a+b)

x =returnSum(20,40)
print ("Sum of a and b vasle is : ", x)
