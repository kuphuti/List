marks=[[78,76,94,86,88],[91,71,98,65],[95,45,78],[87,67,49,68,88]]
sum=0
i=0
while i<len(marks):
    a=0
    while a<len(marks[i]):
        k=marks[i][a]
        sum=sum+k
        a=a+1
    i=i+1
print("total marks=",sum)        