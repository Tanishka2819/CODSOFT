import random


options = ("rock" , "paper" , "scissors")
player_score = 0
computer_score = 0


while True:
    player= ""
    computer = random.choice(options)
    

    while player not in options:
      player = input(" Enter a choice ( rock , paper, scissors): ").lower()

      print(f"Player: {player}")
      print(f"Computer: {computer}")

    if player == computer:
      print(f"Computer: {computer}")

    elif player == "rock" and computer == "scissors" :
      print("You Win!")
      player_score+=1

    elif player == "paper" and computer =="rock" :
      print("You Win!")
      player_score+=1

    elif player == "scissors" and computer =="paper" :
      print("You Win!")
      player_score+=1
    else:
      print("You lose!")
      computer_score+=1

    print(f"Score -> You: {player_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no):").lower()
    if play_again != "yes":
      print("\nThanks for playing!")
      print(f"Final score -> You:{player_score}|Computer:{computer_score}")
      break
