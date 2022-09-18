import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='p':
            return False
        elif you=='c':
            return True
    elif comp=='p':
        if you=='s':
            return True
        elif you=='c':
            return False
    elif comp=='c':
        if you=='s':
            return False
        elif you=='p':
            return True
print("Comp Turn: Stone(s) Paper(p) or Scissor(c)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='c'

you=input("Your Turn:Stone(s) Paper(p) or Scissor(c)?")
a=gameWin(comp,you)
print(f"Computer chose {comp} ")
print(f"you chose {you} ")

if a==None:
    print("The game is a tie")
elif a:
    print("You Win!!")
else:
    print("You Lose!!")
