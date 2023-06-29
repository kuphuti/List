question_list = [
"How many continents are there?", # pehla question
"What is the capital of India?",# doosra question
"NG mei kaun se course padhaya jaata hai?"# teesra question
]

options_list = [
#pehle question ke liye options
["1.Four", "2.Nine", "3.Seven", "4.Eight"],
#second question ke liye options
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
#third question ke liye options
["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)

solution_list = [3, 4, 1]
_5050=[["1.Four","3.Seven"],["2.Bhopal","4.Delhi"],["1.Software Engineering","3.Tourism"]]
i=0
m=0
money=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(options_list[i][j])
        j=j+1
    k=m
    while k<1:
       life_line=input("enter life_line yes or no")
       k=k+1
       if life_line=="yes":
           h=0
           while h<len(_5050[i]): 
               print(_5050[i][h])
               m=m+1
               h=h+1
    a=int(input("enter one option"))
    if a==solution_list[i]:
        money=money+1000
        print("congrats you got right answer you won=",money)
    else:
        print("sorry you miss the chance wrong answer")
    i=i+1