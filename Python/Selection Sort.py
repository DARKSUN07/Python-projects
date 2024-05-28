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
                           

list=[12,99,71,7,100,69,26,25]
sort(list)
print(list)
