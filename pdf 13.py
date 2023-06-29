list=[1,1,2,3,4,4,5,1]
# a="aabcdeefghii"
# list=str(a)
i=0
list1=[]
while i<len(list):
    sum=0
    k=list[i]
    while i<len(list) and k==list[i]:
        sum=sum+1
        i=i+1
    if sum>1:
        list1.append([sum,k])
    else:
        list1.append(k)
print(list1)