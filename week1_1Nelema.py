l=[]
def packages(l):
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if(l[j]<l[min]):
                min=j
            l[i],l[min]=l[min],l[i]
    return l
n=int(input())
for i in range(0,n):
    m=int(input())
    l.append(m)
print(packages(l))



