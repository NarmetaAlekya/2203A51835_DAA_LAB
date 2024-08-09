print("Enter the number of products")
n=int(input())
print("Enter the product IDS")
product_ids=[]
def arrange_products(product_ids):
  for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
      if(product_ids[j]<product_ids[min]):
        min=j
    product_ids[i],product_ids[min]=product_ids[min],product_ids[i]
  return product_ids

for i in range(0,n):
  m=int(input())
  product_ids.append(m)
print(arrange_products(product_ids))




