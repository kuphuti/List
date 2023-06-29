n=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
k=3
i=k
while i<len(n):
    n.pop()
    i=i+k+1
print(n)
