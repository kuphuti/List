magic_square=[[8,3,4],[1,5,9,],[6,7,2]]
i=0
while i<len(magic_square):
    j=0
    r=0
    while j<len(magic_square[i]):
        r+=magic_square[i][j]
        j=j+1
    print(r)
    i=i+1

i=0
a=1
while i<len(magic_square):
    c_sum=0
    j=0
    while j<len(magic_square[i]):
        c_sum+=magic_square[j][i]
        j=j+1
    i=i+1
    print(c_sum)
    a=a+1

i=0
di_sum=0
while i<len(magic_square):
    j=i
    while j<len(magic_square[i]):
        n=magic_square[j][j]
        di_sum=di_sum+n
        j=j+len(magic_square[i])
    i=i+1
print(di_sum)
i=0
di_sum1=0
while i<len(magic_square):
        j=i+1
        l=magic_square[i][-j]
        di_sum1=di_sum1+l
        i=i+1
print(di_sum1)

if r==c_sum and di_sum==15:
    print("magic_square")
else:
    print("not magic_square")

