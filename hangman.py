import random

# Word list with hints
words = {
    "python": "Programming language",
    "apple": "A fruit",
    "tiger": "A wild animal",
    "india": "A country",
    "laptop": "Electronic device",
    "ocean": "Large water body",
    "doctor": "Medical professional"
}

def play_game():
    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed_letters = []
    tries = 6

    print("\nNew Game Started!")
    print(f"Hint: {hint}")

    while tries > 0:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Correct! The word was '{word}'")
            return True   # End immediately after correct guess
        else:
            tries -= 1
            print(f"Wrong guess! Attempts left: {tries}")

    print(f"\nGame Over! The word was: {word}")
    return False


# Main loop
while True:
    result = play_game()

    if result:
        choice = input("\nDo you want to play again? (yes/no): ").lower()
        if choice != "yes":
            print("Thankuu for playing!")
            break
    else:
        print("Thankuu for playing!")
        break
