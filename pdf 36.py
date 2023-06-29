# list=["1","2","3","4","5","6","7","8"]
# i=0
# list1=[]
# b=0
# while i<len(list):
#     b=list[i]+list[i+1]
#     list1.append(b)
#     i=i+2
# print(list1)

a=input("enter a")
b=a
i=-1
length=0-len(a)
sum=""
while i>=length:
    sum=sum+b[i]
    i=i-1
if b==sum:
    print("true")
else:
    print("false")