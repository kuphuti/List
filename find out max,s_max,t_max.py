n=[60,70,80,90,10,20,30]
i=0
max=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i=i+1
j=0
s_max=0
while j<len(n):
    if n[j]>s_max and n[j]!=max:
        s_max=n[j]
    j=j+1
k=0
t_max=0
while k<len(n):
    if n[k]>t_max and s_max>n[k] and n[k]!=max:
        t_max=n[k]
    k=k+1
print("max=",max)
print("second max=",s_max)
print("third max=",t_max)