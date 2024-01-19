# Step 1
import random
import hangman_art
import hangman_words

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)

lives = 6

display = []
for _ in chosen_word:
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You've won!")

    print(hangman_art.stages[lives])