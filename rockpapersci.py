import random

def play():
    player=str(input("r for rock,p for paper,s for scisor: "))
    choose=["r","p","s"]
    computer=random.choice(choose)
    print(f'your choice {player} == {computer}')
    if (player==computer):
     print("game is over")
    elif (player=='r' and computer=='s')or (player=='p' and computer=="r") or (player=='s' and computer=="p"):
        print("you are winning")
    else:
        print("you are losing,try again later")

play()
