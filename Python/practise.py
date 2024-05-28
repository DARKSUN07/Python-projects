n=int(input("Enter no of elements you want to put: "))
l=[]
for i in range(n):
    val=int(input("Enter list elements(Only integers): "))
    l.append(val)
print("Your list: ",l)

#selection sort
def sort(l):
    for i in range(len(l)-1):
        min=i
        for j in range(i+1,len(l)):
            if l[j]<l[min]:
                min=j
        if min!=i:
            temp=l[i]
            l[i]=l[min]
            l[min]=temp
    

'''#bubble sort
def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp'''
        
sort(l)
print("Sorted list is: ",l)
ele=int(input("Enter element you want to search: "));

'''#linear search
def search(l,n):
    for i in l:
        if i==n:
            return True
            break'''

#binary search
def search(list,n):
    f=0
    l=len(list)-1
    while f<=l:
        mid=(f+l)//2
        if list[mid]==n:
            return True
        elif list[mid]<n:
            f=mid
        else:
            l=mid
if search(l,ele):
    print("element found")
else:
    print("element not found")
#[1,2,3,4,5]
