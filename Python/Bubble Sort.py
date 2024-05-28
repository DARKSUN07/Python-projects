def sort(l):
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

list=[22,98,76,54,10,90,96,7]
sort(list)
print(list)

