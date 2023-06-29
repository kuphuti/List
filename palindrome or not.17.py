names=input("enter names")
i=0
while i<len(names):
    a=names[i]
    i=i+1
b=-1
c=-len(names)   
while b>=c:
    d=names[b]
    print(d) 
    b=b-1
if a==d:
    print("palindome hai")
else:
    print("palindrome nahi hai")    
