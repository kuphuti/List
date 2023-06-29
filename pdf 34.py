n=[34.67,12,-94.89,"python","c#"]
i=0
list=[]
while i<len(n):
    if type(n[i])==float:
        list.append(n[i])
    i=i+1
print(list)