import random

class FlashCard:
    def __init__(self):
        self.fruits = {"Banana": "yellow", "Strawberries": "pink", "Watermelon": "green"}
    
    def play_quiz(self):
        print("Welcome to the fruit quiz!")
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            answer = input(f"What is the color of {fruit}? ").strip().lower()
            if answer == color.lower():
                print("Correct answer!")
            else:
                print("Wrong answer!")
            play_again = input("Enter 0 if you want to play again: ").strip()
            if play_again != '0':
                break

# Usage
flashcard = FlashCard()
flashcard.play_quiz()
