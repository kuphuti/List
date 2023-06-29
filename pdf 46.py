a=['0', '1', '2', '3', '4']
b=['red', 'green', 'black', 'blue', 'white']
c=['100', '200', '300', '400', '500']
i=0
list=[]
while i<len(a):
    k=a[i]+b[i]+c[i]
    list.append(k)
    i=i+1
print(list)
