import random

title = "wordie!"  # title

word_bank = []  # empty list to store words

f = open("words.txt", "r")
for word in f:
    word_bank.append(word.rstrip())  # removes whitespace from words

# print(word_bank)

your_word = random.choice(word_bank).lower()  # chooses random words

list(your_word)  # converts word user is trying to guess into list

guess_count = 0



# check guess for letters and their position
'''
goal: check users guess for letters and their position
1. convert user's guess to list

2. if letter is correct and in correct postion, leave it

3. if letter is correct and in incorrect position, add to list of misplaced letters 
and add underline at its correct postion in the word

4. if letter not in word, print in correct message

5. always update guess count after every input
'''

print(f"You have 6 guesses max! Good luck.")

while guess_count < 6:
    print(f"Guess {guess_count + 1} of 6")

    correct = []
    misplaced_letters = []

    answer = str(input("Enter a 5 letter word. What's your guess?: ")).lower()   # gets input guess from user
    # convert their guess to a list
    list(answer)

    
    if len(answer) != len(your_word):
        print("Not the right word length! Try another word.")
        quit()

    if answer == your_word:
        print("You got it!")
        quit()

    for i, letter in enumerate(answer):
       #right letter, right postion
        if letter == your_word[i]:
            correct.append(letter)

        #correct letter, wrong position
        elif letter in your_word:
            misplaced_letters.append(letter)
            correct.append("_")
            print(f"{letter} is in the word but in the wrong spot!")

        #letter is not in word
        else:
            correct.append("_")
            print(f"{letter} is not in word!")

    guess_count += 1

    #show progress
    print("Result: " + " ".join(correct))
    if misplaced_letters:
        print(f"Misplaced: {', '.join(set(misplaced_letters))}")

    if guess_count == 6 and answer != your_word:
        print(f"The word was {str(your_word)}")
        quit()



