import random

def game(comp , you):
    if comp==you:
        return None


    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False


    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True


    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

comp=input("Computer Turn: Rock(r) , Paper(p) , Scissor(s) : ?")
randNum=random.randint(1,3)
if randNum==1:
    comp='r'
elif randNum==2:
    comp='p'
else:
    comp='s'

you=input("Your Turn: Rock(r) , Paper(p) , Scissor(s) : ")
a=game(comp,you)

print(f"Computer Chooses :  {comp}")
print(f"You Chooses : {you} ")

if a == None:
    print("Its a Draw.")
elif a:
    print(" You Win.")
else:
    print(" You Lose.")




