import numpy as np
print("Enter the price of the products:")
n=int(input())
def products_order(price):
    for i in range(1, len(price)):
        key = price[i]
        j = i - 1
        while j >= 0 and key < price[j]:
            price[j + 1] = price[j]
            j -= 1
        price[j + 1] = key
    return price
l=[]
for i in range(0,n):
  m=int(input())
  l.append(m)
price=np.array(l)
print("prices in order:");
print(products_order(price))

