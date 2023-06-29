# binary=[1,0,1,0,1]
# i=-1
# length=0-len(binary)
# p=0
# dec=0
# while i>=length:
#     if binary[i]==1:
#         a=binary[i]
#         p=2**p
#         b=a*p
#         dec=dec+b
#     else:
#       pass
#     i=i-1
#     p=p+1
# print(dec)

bin=int(input("enter bin"))
dec=0
p=1
while bin!=0:
    rev=bin%10
    bin=bin//10
    dec=dec+rev*p
    p=p*2
print(dec)