# 8.Rock-Paper-Scissors game (two players):
# o	Take input from both players
# o	Compare:
# 	Rock beats Scissors
# 	Scissors beats Paper
# 	Paper beats Rock
# 	Same → Tie
# Ask both players for their choice
player1 = input("Player 1, enter Rock, Paper, or Scissors: ").strip().lower()
player2 = input("Player 2, enter Rock, Paper, or Scissors: ").strip().lower()

# Define winning conditions
winning_combinations = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Determine the winner
if player1 == player2:
    print("It's a Tie!")
elif winning_combinations.get(player1) == player2:
    print("Player 1 wins!")
elif winning_combinations.get(player2) == player1:
    print("Player 2 wins!")
else:
    print("Invalid input! Please enter Rock, Paper, or Scissors.")
