# list=[20,37,20,21]
# i=0
# list1=[]
# while i<len(list):
#     if list[i] not in list1:
#        list1.append(list[i])
#     i=i+1
# print(list1)


list=[1,1,1,1]
i=0
b=[]
while i<len(list):
    j=i+1
    a=list[i]
    count=0
    while j<len(list):
        c=list[j]
        if count<=2 and a==c:
            count=count+1
            if count==2:
                b.append(a)
        j=j+1
    i=i+1
print(b)