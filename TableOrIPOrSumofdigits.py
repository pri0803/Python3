
import socket
def main():
    hostnm = socket.gethostname()
    ipad = socket.gethostbyname(hostnm)
    print("Device name : ",hostnm)
    print("IP address : ",ipad)
    print("Enter a number\n\n")
    num = int(input())
    print("Table of ", num)
    table(num,1)
    print("\n Sum of natural numbers till ,",num)
    sum(num)

def table(n ,i):
    if i>10:
        return

    print(n,"*",i,"=",n*i)
    return table(n , i+1)

def sum(n):
    s = 0
    S = 0
    for i in range(1,n+1):
        s = s + i
    print("Sum = ",s)

    while s!= 0:
        r = s%10
        S = S +r
        s //= 10
    print("Sum of digits of sum =",S)



if __name__ == '__main__':
    main()
