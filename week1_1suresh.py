import numpy as np
print("enter the books price")
n=int(input())
l=[]
def arrange_books(arr):
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if(arr[j]<arr[min]):
        min=j
    arr[i],arr[min]=arr[min],arr[i]
  return arr

for i in range(0,n):
  m=int(input())
  l.append(m)
arr=np.array(l)
print(arrange_books(arr))



