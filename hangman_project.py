# Step 1
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)

lives = 6

display = []
for _ in chosen_word:
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already used the letter {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word, you lose a life :(")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You've won!")

    print(hangman_art.stages[lives])