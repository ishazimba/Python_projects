import random
import os
clear =lambda :os.system(('cls'))
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card


# Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []
def calculate_score(cards):
  if 11 in cards and 10 in cards and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    print("Draw 😬😇")
  elif computer_score == 0:
    print("Your opponent has the Blackjack. You lose ☹️")
  elif user_score > 21:
    print("You went over. You lose")
  elif computer_score > 21:
    print("Opponent went over. You win")
  elif user_score > computer_score:
    print("You win 😇")
  else:
    print("You lose ☹️")


def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your cards are {user_cards}, and your score is  {user_score}")
    print(f"computer's first card is {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      continue_with_another_card = input("Do you want to draw another card? Type 'y' for Yes and 'n' for No.")
      if continue_with_another_card == "y":
        user_cards.append(deal_card())
      if continue_with_another_card == "n":
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand is {user_cards}, and your final score is {user_score}")
  print(f"Computer's final hand is {computer_cards}, and computer's final score is {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play Blackjack game? ") == "y":
  clear()
  play_game()
