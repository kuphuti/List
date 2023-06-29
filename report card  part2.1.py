marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
year=1
while i<len(marks):
    a=0
    sum=0
    while a<len(marks[i]):
        k=marks[i][a]
        sum=sum+k
        a=a+1
    b=sum//len(marks[i])
    i=i+1
    print("evg of",year,"year=",b)       
    year=year+1