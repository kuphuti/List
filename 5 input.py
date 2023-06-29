i=0
list=[]
even_sum=0
odd_sum=0
while i<5:
    num=int(input("enter num"))
    list.append(num)
    if list[i]%2==0:
        even_sum=even_sum+list[i]
    else:
        odd_sum=odd_sum+list[i] 
    i=i+1
print("even=",even_sum)
print("odd=",odd_sum)