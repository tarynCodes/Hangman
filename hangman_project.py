# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in chosen_word:
    display += "_"
print(display)

# TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word
# and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
         display[position] = letter

    print(display)

print("You've won!")
