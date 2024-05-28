n = int(input("Enter no of choclates: "))
cnt = 0
i = 1
while i<n:
    cnt+=1
    i = i + 2*cnt + 1
if n <= (i-cnt-1):
    print(cnt*2)
else:
    print(cnt*2+1)
    
