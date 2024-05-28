n = int(input("Enter the number up to which Fibonacci sequence is to be printed:"))
result=[ ] 
a=0
b=1
while a<=n:
    result.append(a)
    t=a
    a=b
    b=t+b
print("The Fibonacci sequence up to",n,"is:",result)
