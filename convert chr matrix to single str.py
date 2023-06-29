chr=[["g","f","g"],["i","s"],["b","e","s","t"]]
list=[]
i=0
while i<len(chr):
    j=0
    while j<len(chr[i]):   
        list.append(chr[i][j])
        j=j+1
    i=i+1
a=0
sum=""
while a<len(list):
    sum=sum+(list[a])
    a=a+1
print(sum)