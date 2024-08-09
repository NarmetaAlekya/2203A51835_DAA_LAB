l = []
def arrange_books():
  for i in range(0,len(l)-1):
      for j in range(0,len(l)-1):
          if(l[j]>l[j+1]):
              temp=l[j]
              l[j]=l[j+1]
              l[j+1]=temp
  return l
print("enter the number of books")
n=int(input())
print("enter the books price")
for i in range(0, n):
    m = int(input())
    l.append(m)
print(arrange_books())
