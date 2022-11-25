import random
import time 
def play():
  while True :   
    user = input('Choise "R" for rock "P" for papier and "S" for seccoirs ')
    time.sleep(1)
    computer =random.choice(['r','p','s'])
    if user == computer :
        print("It's Tie")
    elif win(user,computer):
         print("You win ")
    else :
         print('You lose')
    play_again =input('play again ? y/n ')
    if  play_again !='y' :
         break
            
def win(player,adverse):
     if (player == 'r' and adverse == 's') or (player == 's' and adverse == 'p') \
     or (player == 'p' and adverse =='s') :
         return True   
         
play()