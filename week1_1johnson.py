import numpy as np
print("Enter the Time to reach destination")
n=int(input())
l=[]
def Destination(arr):
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if(des[j]<des[min]):
        min=j
    des[i],des[min]=des[min],des[i]
  return arr

for i in range(0,n):
  m=int(input())
  l.append(m)
des=np.array(l)
print(Destination(des))


