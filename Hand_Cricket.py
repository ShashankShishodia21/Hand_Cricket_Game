import random
a = 0
user_score = 0
comp_score=0
print('Let the toss begins')
print("---------------------------------------------------")
user_value = int(input('Choose a number b/w 1-6 = '))
comp_value = random.choice([1,2,3,4,5,6])
print ("computer choose" , comp_value)
sum = user_value + comp_value
if user_value % 2 == 0:
       print('You choose even')
       print('computer choose odd')
       if sum%2==0:
           print('You won the toss')
           print("---------------------------------------------------")
           a=a+1
       else:
           print('computer won the toss')   
else:
    print('You choose odd ')
    print('computer choose even ')
    if sum%2==0:
          print('computer won the toss')
          print("---------------------------------------------------")
    else:
          print('You won the toss')
          a=a+1
if a>0:
    #whom will win the toss will bat first
    print("You'll Bat first")
    your_turn = int(input("enter a number b/w 1 to 6 = "))
    comp_turn=random.choice([1,2,3,4,5,6])
    print("computer choose = ",comp_turn)
    if your_turn == comp_turn:
        print("You are out !!!")
    else:
        user_score = user_score +your_turn
        print("User Score = ",user_score)
    print("---------------------------------------------------")
    print("Computer will Bat now")
    your_turn = int(input("enter a number b/w 1 to 6 = "))
    comp_turn=random.choice([1,2,3,4,5,6])
    print("computer choose = ",comp_turn)
    if your_turn == comp_turn:
        print("Computer is  out !!!")
    else:
        comp_score = comp_score +comp_turn;
        print("computer score = ",comp_score)
        
    if comp_score>user_score:
        print("Computer won")
    elif comp_score<user_score :
        print("User won")
    else:
        print("Match draw")
    print("---------------------------------------------------")  
if a==0:
    #whom will win the toss will bat first
    print("Computer Bat first")
    your_turn = int(input("enter a number b/w 1 to 6 = "))
    comp_turn=random.choice([1,2,3,4,5,6])
    print("computer choose = ",comp_turn)
    if your_turn == comp_turn:
        print("Computer is  out !!!")
    else:
        comp_score = comp_score +comp_turn;
        print("computer score = ",comp_score)
    print("---------------------------------------------------")
    print("You'll Bat now")
    your_turn = int(input("enter a number b/w 1 to 6 = "))
    comp_turn=random.choice([1,2,3,4,5,6])
    print("computer choose = ",comp_turn)
    if your_turn == comp_turn:
        print("You are out !!!")
    else:
        user_score = user_score +your_turn
        print("User Score = ",user_score)
    if comp_score>user_score:
        print("Computer won")
    elif comp_score<user_score :
        print("User won")
    else:
        print("Match draw")