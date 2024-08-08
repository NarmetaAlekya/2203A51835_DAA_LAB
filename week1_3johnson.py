import numpy as np
print("Enter the number of orders:")
n=int(input())
print("Enter orders Priority Number:")
def orders(priority_num):
    for i in range(1, len(priority_num)):
        key = priority_num[i]
        j = i - 1
        while j >= 0 and key < priority_num[j]:
            priority_num[j + 1] = priority_num[j]
            j -= 1
        priority_num[j + 1] = key
    return priority_num
l=[]
for i in range(0,n):
  m=int(input())
  l.append(m)
priority_num=np.array(l)
print(orders(priority_num))

