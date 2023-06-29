a=['Red', 'Maroon', 'Yellow', 'Olive']
i=0
list=[]
while i<len(a):
    j=0
    k=[]
    while j<len(a[i]):
        k.append(a[i][j])
        j=j+1
    i=i+1
    list.append(k)
print(list)

# b=['red','maroon','yellow','olive']
# a=[]
# for i in b:
#     b=list(i)
#     a.append(b)
# print(a)