import random

def play():
    a=input("Rock Paper Scissors \n r for rock\n s for scissors\n p for paper\n")
    c = random.choice(['r','s','p'])
    
    if(a==c):
        print("Tie")
    
    if win(a,c):
        return 'you win!'
    
    return 'You lost!'

# r > s & s > p & p > r
def win(a,c):
    if( a=='r' and c=='s') or ( a=='s' and c=='p') or ( a=='p' and c=='r'):
        return True  

print(play())