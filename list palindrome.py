list=input("enter")
rev=-len(list)
i=-1
sum=""
while i>=rev:
    sum=sum+list[i]
    i=i-1
if list==sum:
    print("palindrome")
else:
    print(" not palindrome")
            
# str=input("enter str")
# for i in range(0,(len(str))):
#     if str[i]==str[len(str)-i-1]:
#         print(" not palindrome")
#         print(" palindrome")
