a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b*b-4*a*c
deno=2*a
if(d>0):
    print("Real and distinct roots")
    r1=(-b+d**0.5)/deno
    r2=(-b-d**0.5)/deno
    print("roots are:",r1,"and",r2)
elif(d==0):
    print("Equal roots")
    r=-b/deno
    print("Roots are:",r,r)
else:
    print("Imaginary roots")
