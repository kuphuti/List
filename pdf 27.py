n=int(input("enter n"))
list=[1,2,3]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and k!=i:
                print(list[i],list[j],list[k])