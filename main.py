import random

class Hangman:
    def __init__(self):
        self.catagories = {
            "animal": ["lion", "tiger", "monkey", "elephant"],
            "fruit": ["apple", "banana", "kiwi", "watermelon"]
        }
        self.guesses = set()
        self.guesses_count = 0
        self.new_word = ""
    
    def print_dashes(self, word):
        for i in word:
            print("_", end=' ')
        
    def letter_guess(self, letter, word):
        for i in range(len(word)):
            if(word[i] == letter):
                self.guesses.add(i)
                # print(self.guesses)
                # print(word[i], end=' ')
        self.print_letter(word)

    def print_letter(self, word):
        self.new_word = ""
        for i in range(len(word)):
            if(i in self.guesses):
                self.new_word += word[i]
                print(word[i], end=' ')
            else:
                self.new_word += "_"
                print("_", end=' ')
        


def main():

    done = False
    while not done:
        hangman = Hangman()
        print("Categories:", end=' ')
        for key in hangman.catagories:
            print(f"{key}", end=' ')
        user_choice = input("\nSelect a categoty from the list above: ").lower()
        # check if valid user's choice 
        if user_choice in hangman.catagories:
            # get a random word from that category
            random_word = random.choice(hangman.catagories[user_choice])
            hangman.print_dashes(random_word)
            finished = False
            while not finished:
                user_guess = input("What letter would you like  to guess? ").lower()
                if user_guess in random_word:
                    hangman.letter_guess(user_guess, random_word)
                    if "_" not in hangman.new_word:
                        print("Congrats!! You got it!")
                        break
                else:
                    hangman.guesses_count += 1
                    print(f"Guesses: {hangman.guesses_count}")
                if hangman.guesses_count == 7:
                    print(f"You Lost!!, The word was {random_word}")
                    finished = True
        else:
            print("Invalid Category!!")

        confirm = input("Do you want to continue?(Y/N) ").lower()
        if confirm == 'y':
            continue
        else:
            done = True
    
    print("Thank you for playing!!")

main()
