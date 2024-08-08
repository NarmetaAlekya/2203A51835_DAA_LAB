import numpy as np
print("Enter orders Priority Number:")
n=int(input())
def priority_numbers(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
l=[]
for i in range(0,n):
  m=int(input())
  l.append(m)
arr=np.array(l)
print(priority_numbers(arr))
