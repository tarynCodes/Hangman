# Step 1
import random
import hangman_art
import hangman_words
import os

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)

lives = 6
used_letters = ""

display = []
for _ in chosen_word:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    used_letters += guess + ", "

    os.system('clear' if os.name == 'posix' else 'cls')

    if guess in display:
        print(f"You've already used the letter {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word, you lose a life :(")

        if lives == 0:
            end_of_game = True
            print("Sorry, you ran out of lives! You Lose!")
            print(f"The word was {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You've won!")

    print(hangman_art.stages[lives])
    print(f"You have used these letters:  {''.join(used_letters)}")

