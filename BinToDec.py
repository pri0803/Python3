#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Binary to decimal
#
# Author:      aarus
#
# Created:     09-09-2022
# Copyright:   (c) aarus 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    num = int(input("Enter a binary number   "))
    n = num
    s = 0
    c = 0
    while(n!=0):
        r = n%10
        s = s + r*(2**c)
        n = n//10
        c+=1
    print("Decimal number is : ",s)

if __name__ == '__main__':
    main()
