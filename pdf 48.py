a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
list=[]
while i<len(a):
    list.append(a[i:i+3])
    i=i+3
print(list)