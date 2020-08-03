

def user_input():
    game_range=[1,2,3,4,5,6,7,8,9]
    choice=0
    while(choice==0):
        choice=input("Enter your choice from 1-10: ")
        choice=int(choice)
        if choice not in game_range:
            print("Not in range")
            choice= 0
    return choice



def marker_assign():
    p1=''
    while p1 !='X' and p1 != 'O':
        p1=input("Player 1, are you X/O: ")
        if p1=='X':
            p2='O'
        else:
            p2='X'
    print(f"Player 1: {p1} and Player 2: {p2}")
    return (p1,p2)


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']



def display_board():   
    print(row1[0]+'|'+row1[1]+'|'+row1[2])
    print("__ __")
    print(row2[0]+'|'+row2[1]+'|'+row2[2])
    print("__ __")
    print(row3[0]+'|'+row3[1]+'|'+row3[2])
    print("__ __")


display_board()
p1,p2=marker_assign()
ct=1
stat='con'
while stat=='con':
    if row1[0]==row1[1]==row1[2]=='X' or row2[0]==row2[1]==row2[2]=='X' or row3[0]==row3[1]==row3[2]=='X' or row1[0]==row2[1]==row3[2]=='X' or row1[2]==row2[1]==row3[0]=='X'or row1[0]==row1[1]==row1[2]=='O' or row2[0]==row2[1]==row2[2]=='O' or row3[0]==row3[1]==row3[2]=='O' or row1[0]==row2[1]==row3[2]=='O' or row1[2]==row2[1]==row3[0]=='O'or row1[0]==row2[0]==row3[0]=='X' or row1[1]==row2[1]==row3[1]=='X' or row1[2]==row2[2]==row3[2]=='X' or row1[0]==row2[0]==row3[0]=='O' or row1[0]==row2[0]==row3[0]=='O' or row1[0]==row2[0]==row3[0]=='O' or ct==10 :
        stat='brek'
    elif ct%2 !=0:
        print('Player 1, Your chance now!')
        choice=user_input()
        choice=choice
        if choice in range(1,4):
            row1[choice-1]=p1
        elif choice in range(4,7):
            row2[choice-4]=p1
        else:
            row3[choice-7]=p1
        ct=ct+1
        display_board()
    else:
        print('Player 2, Your chance now!')
        choice=user_input()
        choice=choice
        if choice in range(1,4):
            row1[choice-1]=p2
        elif choice in range(4,7):
            row2[choice-4]=p2
        else:
            row3[choice-7]=p2
        ct=ct+1
        display_board()
    
print(ct)
if ct !=10:
    if ct%2==0:
        print("Congrats, Player 1 has won,\n Player 2 better luck next time")
    else:
        print("Congrats, Player 2 has won,\n Player 1 better luck next time")
elif ct==10:
    print("This game is a draw!!")





    

    
   
    
    

