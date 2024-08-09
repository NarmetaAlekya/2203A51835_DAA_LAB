
n=int(input())
arr=[]
def Destination(arr):
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if(arr[j]<arr[min]):
        min=j
   arr[i],arr[min]=arr[min],arr[i]
  return arr
for i in range(0,n):
  m=int(input())
  arr.append(m)

print(Destination(arr))


