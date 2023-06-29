list=[[1,2,4],[2,4,4],[1,2]]
i=0
b=[]
while i<len(list):
    j=0
    sum=0
    while j<len(list):
        if i<len(list[j]):
            a=list[j][i]
            sum=sum+a
        j=j+1
    i=i+1
    b.append(sum)
print(b)
