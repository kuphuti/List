a="(",")","[","]","{","}"
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
       if a[i]=="(" and a[i]==")" and a[i]=="[" and a[i]=="]" and a[i]=="{" and a[i]=="}":
        print("true") 
else:
    print("invalid")
i=i+1
    
