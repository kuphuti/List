list=[[1,2], [2, 4]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        j=j+1
    i=i+1
print(i,j)