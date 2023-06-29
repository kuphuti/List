# a=[4,6,4,3,3,4,3,4,3,8]
# k=3
# i=0
# list=[]
# for i in a:
#    b=a.count(i)
#    if b>k and i not in list:
#        list.append(i)
#    i=i+1
# print(list)

list=[4,6,4,3,3,4,3,4,3,8]
k=3
i=0
a=[]
while i<len(list):
    j=i+1
    sum=0
    while j<len(list):
        sum=sum+1
        if list[i]==list[j] and k<sum and list[i] not in a:
            a.append(list[i])
        j=j+1
    i=i+1
print(a)
