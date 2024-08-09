l = []
print("Enter the unique barcode")
def package():
  for i in range(0,len(l)-1):
      for j in range(0,len(l)-1):
          if(l[j]>l[j+1]):
              temp=l[j]
              l[j]=l[j+1]
              l[j+1]=temp
  return l
n=int(input())
for i in range(0, n):
    m = int(input())
    l.append(m)
print(package())


