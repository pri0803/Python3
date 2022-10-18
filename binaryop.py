#-------------------------------------------------------------------------------
# Purpose:  To see working of eval() function
# eval() is used to evaluate the expression inside input or print function
#-------------------------------------------------------------------------------

def main():
    #Bitwise operations
    a = int(input("Enter a no."))
    b = int(input("Enter another no."))
    print("Binary sum: ",(a&b))
    print("Binary or: ",(a | b))
    print("Binary XOR: ",(a^b))
    print("Binary right shift: ",(a>>b))
    print("Binary left shift: ",(a<<b))



if __name__ == '__main__':
    main()
