list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# list=[1,2,3,4,5]
a=20
l=4 
i=l
while i<len(list):
    list.insert(i,a)
    i=i+1+l
print(list)

