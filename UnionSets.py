
A = [1,2,3]
B = [2,4,6]
    #Union and intersection
A = set(A)
B = set(B)
Z = list(A.intersection(B))
Q = list(A.symmetric_difference(B))
Q.extend(Z)
print("Set  A is : ",A)
print("Set B is : ",B)
print("Interesection is :",Z)
print("Union is :",Q)

