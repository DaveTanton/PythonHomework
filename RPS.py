mport random as r
print ("Rock, paper, scissor game")

result = ""
choices = ("rock","paper","scissors","SHOTGUN")


while True: #whats this "error"
  computer = choices[r.randint (0,3)]
  user=input("\nRock, Paper or Scissors? make your choice :").lower()

  if user == "shotgun":
    result="STOP CHEATING! TRY AGAIN!!"  
  elif user == computer:
    result = "IT'S A DRAW"
  elif user == "rock":
    if computer == "scissors":
      result = "YOU WIN"
    if computer == "paper":
      result = "YOU LOSE"
    if computer == "SHOTGUN":
      result ="SHOTGUN!! I WIN! YOU LOSE. HA HA!"
  elif user == "paper":
    if computer == "rock": 
      result = "YOU WIN"
    if computer == "scissors":
      result = "YOU LOSE"
    if computer == "SHOTGUN":
      result ="SHOTGUN!! I WIN! YOU LOSE. HA HA!"
  elif user == "scissor":
    if computer == "paper":
      result = "YOU WIN"
    if computer == "rock": 
      result = "YOU LOSE"
    if computer == "SHOTGUN":
      result ="SHOTGUN!! I WIN! YOU LOSE. HA HA!"
  else:
    print("That's not a valid play. Check your spelling!")
    continue

  print("you chose: ",user)
  print("the computer chose: ",computer)
  print(result)

  retry=input("\nHave another go Y/N: ")
  retry=retry.lower()

  if retry == "y":
    continue
  else:
    break
print("\nAll done\nThank you for playing")
