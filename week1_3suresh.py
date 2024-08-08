import numpy as np

l = []
print("Enter the unique barcode")
n = int(input())

def package():
  for i in range(0, n):
    m = int(input())
    l.append(m)
  numbers= np.array(l)
  for i in range(0,len(numbers)-1):
      for j in range(0,len(numbers)-1):
          if(numbers[j]>numbers[j+1]):
              temp=numbers[j]
              numbers[j]=numbers[j+1]
              numbers[j+1]=temp
  return numbers
print(package())


