print("Enter orders Priority Number:")
n=int(input())
def priority_numbers(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l
l=[]
for i in range(0,n):
  m=int(input())
  l.append(m)

print(priority_numbers(l))
