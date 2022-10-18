
var = 10
print(hex(id(var)))
print(var)

def func():
    myT = tuple()         #my tuple
    y = list(myT)
    n = int(input("Enter number of elements to be in tuple"))
    print("Enter inputs or elements")
    for j in range(0,n):
        y.append(int(input()))
    c = 0
    revT = list()   #temporary list
    myT = tuple(y)
    i  = n-1
    while i >= 0:
        a = myT[i]
        revT.append(a)
        c += 1
        i -= 1
    print("Orignal turple : ",myT)
    print("Reversed tuple : ", tuple(revT))     #reversed tuple printing

func()







