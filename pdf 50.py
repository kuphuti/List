a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
list=[]
while i<len(a):
    k=a[i]+b[i]
    list.append(k)
    i=i+1
print(list)