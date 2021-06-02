def invalid():
    print("\n\t!!!!!!!!!!!!!!!!!!!invalid choice!!!!!!!!!!!!!!!!!!!!\n")
import random
PL=[]
CL=[]
RL=[]
x=0
y=0
print("----------Rock Paper Sissor ML Game By Kunal Upadhyay----------")
while True:
    if y==0:
        if x!=0:
            print("\t\t\t<1> Play again ")
        else:
            print("\t\t\t<1> Play Game")
        print("\t\t\t  <2> Exit")
        c=input("Enter your choice : ")
    if c=='1':
        L=["R","P","S"]
        y=1
        print("\t\t\t< R > Rock \n\t\t\t< P > Paper \n\t\t\t< S > Sissor")
        print(PL,CL,RL)
        player=input("Enter Your choice : ")
        if player!="R" and player!="P"and player!="S" :
            invalid()
            continue
        PL.append(player)
        for i in range(0,len(RL)):
            if player==PL[i] and RL[i]=="W":
                L.remove(CL[i])
            if player==CL[i] and RL[i]=="W":
                L=[]
                L.append(PL[i])
            if player==PL[i] and RL[i]=="L":
                L=[]
                L.append(CL[i])
            print(L)
        computer=random.choice(L)
        CL.append(computer)
        print("Computer : ",computer)
        if (player=="P" and computer=="R")or(player=="S" and computer=="P")or(player=="R" and computer=="S"):
            print("You Win")
            RL.append("W")
        elif(player==computer):
            print("Tie")
            RL.append("W")
        else:
            print("You Lose")
            RL.append("L")
    elif c=='2':
        break;
    else:
        invalid()
        continue
    x=1
    y=0
    
