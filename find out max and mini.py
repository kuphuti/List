list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=[0]
min=[0]
while i<len(list):   
  if len(list[i])>len(max):
    max=list[i]
  elif len(list[i])<len(min):
    min=list[i] 
  i=i+1    
print("maximum=",len(max),max)
print("miximum=",len(min),min)
      