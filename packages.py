import numpy as np

l = []
print("Enter time to reach the destination")
n = int(input())


def Time():
  for i in range(0, n):
    m = int(input())
    l.append(m)
  arr= np.array(l)
  for i in range(0,len(arr)-1):
      for j in range(0,len(arr)-1):
          if(arr[j]>arr[j+1]):
              temp=arr[j]
              arr[j]=arr[j+1]
              arr[j+1]=temp
  return arr
print(Time())

