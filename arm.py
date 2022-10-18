n=int(input("Enter the number"))
#order=len(str(n))
temp=n
s=0
while(n>0):
    r=n%10
    s=s+(r**3)
    n=n//10
if s==temp:
    print("Armstrong number")
else:
    print("Not an armstrong number")
