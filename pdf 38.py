list=['.com', '.edu', '.tv'] 
i=0 
l=".edu/https://www.w3resource/python-exercises/list/"
while i<len(list): 
    if (list[i]) in l: 
        match="true"
    else: 
        match="false" 
    i=i+1
print(match)


