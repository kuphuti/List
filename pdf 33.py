#list=[12,67,98,34]
#a=[]
#for i in list:
  #sum=0
  #for j in str(i):
   # sum+=int(j)
  #a.append(sum)
#print(a)
list=[12,67,98,34]
a=[]
i=0
while i<len(list):
  j=0
  b=str(list[i])
  while j<len(b):
    d=str(b)
    e=0
    c=0
    while e<len(d):
      c=int(d[e])+c
      e+=1
      j+=1
    a.append(c)
  i=i+1
print(a)