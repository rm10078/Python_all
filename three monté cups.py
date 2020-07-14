from random import shuffle
def input_guess():
    guess=input("Enter the number 0,1,2 : ")
    guess=int(guess)
    return guess

def shuffle_list():
    mlist=['','','O']
    import random
    random.shuffle(mlist)
    return mlist

def check_guess(guess,mlist):
    if mlist[guess]=='O':
     print("Correct")
    else:
     print("Wrong")
     print(mlist1)

guess1=input_guess()
mlist1=shuffle_list()
check_guess(guess1,mlist1)







