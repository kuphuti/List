n=[[0],[1,3],[5,7],[9,11],[13,15,17]]
length=len(n)
i=0
min=n[0]
max=n[0]
while (i<length):
    if (len(n[i])<len(min)):
        min=n[i]
    if (len(n[i])>len(max)):
        max=n[i]
    i=i+1
print(len(min),min)
print(len(max),max)