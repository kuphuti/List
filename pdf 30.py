# list=[-12,14,95,3]
# i=0
# b=0
# a=-0
# while i<len(list):
#     if list[i]>0:
#         b=b+1
#     else:
#         a=a+1
#     i=i+1
# print("positive=",b)
# print("negative=",a)

l=[1,2,5,4]
i=7
b=3
a=b
while a<len(l):
    l.insert(a,i)
    a=a+1+b
print(l)