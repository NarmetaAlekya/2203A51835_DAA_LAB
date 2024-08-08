import numpy as np
print("Enter the number of products")
n=int(input())
print("Enter the product IDS")
l=[]
def arrange_products(arr):
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if(product_ids[j]<product_ids[min]):
        min=j
    product_ids[i],product_ids[min]=product_ids[min],product_ids[i]
  return product_ids

for i in range(0,n):
  m=int(input())
  l.append(m)
product_ids=np.array(l)
print(arrange_products(product_ids))




