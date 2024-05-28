pos=-1

def search(list,n):
    a=0
    for i in list:
        a+=1
        globals()["pos"]=a
        if i==n:
            return True
            break
    
   

l=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter the no. you want to search: "))
if search(l,n):
    print("element found at",pos)
else:
    print("element not found")
