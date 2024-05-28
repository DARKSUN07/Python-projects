divisor_found=False
n=int(input("Enter a positive integer:"))
divisor_limit= (n//2+1)
for divisor in range(2, divisor_limit):
    if n % divisor == 0:
        divisor_found = True
        break
if divisor_found:
    print(n,"is not prime as it has a divisor",divisor)
else:
    print(n,"is a prime number")
