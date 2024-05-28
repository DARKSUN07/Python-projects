print("This programe is to convert temperature in either fahrenheit or celsius")
temp=int(input("If you want to enter temp in fahrenheit press 0\nIf you want to enter temp in celsius press 1: "))
if(temp==0):
    a=int(input("Enter temp in fahrenheit: "))
    b=(a-32)*(5/9)
    print("Your temp in celsius is",b)
elif(temp==1):
    a=int(input("Enter temp in celsius: "))
    b=(a*(9/5))+32
    print("Your temp in fahrenheit is",b)
else:
    print("Invalid Input")
    
    
