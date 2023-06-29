num=[2,7,9,11]
t=9
i=0
list=[]
while i<len(num):
    j=0
    while j<len(num):
        a=num[i]+num[j]
        if a==t:
            list.append(num[i])
        j=j+1
    i=i+1 
print(list)