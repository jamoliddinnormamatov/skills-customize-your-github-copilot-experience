
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Implement Hangman Game

#### Description
Create a command-line Hangman game in Python. The program should randomly choose a word, accept single-letter guesses from the player, show current progress, and track remaining attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list
- Accept single-letter guesses and update the displayed word progress (e.g., `_ a _ _ _`)
- Track and display remaining attempts and incorrect guesses
- End the game when the word is fully guessed or attempts are exhausted
- Display clear win or lose messages and reveal the correct word when the player loses
- Handle invalid input (non-letters, repeated guesses) gracefully

#### Example session (conceptual)

```
Word: _ _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _ _
Incorrect guesses left: 5
```

### 🛠️ Optional: Add Extra Features

#### Description
Enhance the basic game with additional features for extra credit or practice.

#### Requirements (optional)

- Add difficulty levels that change the number of allowed attempts
- Load words from an external file (e.g., `words.txt`)
- Show a simple ASCII-art hangman for incorrect guesses
- Add a score or replay option
