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

# Choose random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
tries = 6

print("🎮 Welcome to Hangman Game!")
print(f"💡 Hint: {hint}")

# Display blank word
display_word = ["_"] * len(word)

while tries > 0:
    print("\nWord: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"❌ Wrong guess! Attempts left: {tries}")

    # Check win
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# If lost
if "_" in display_word:
    print("\n💀 Game Over! The word was:", word)
