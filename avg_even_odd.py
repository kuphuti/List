elements= [23,14,56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
    else:
	    sum1=sum1+elements[i]
    i=i+1    
avg_even=sum/i
avg_odd=sum1/i
print("aveg of even=",avg_even)
print("aveg of odd=",avg_odd)