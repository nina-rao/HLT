# Homework 2
# Nina Rao

import sys
import pathlib
import re
import nltk
import random
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def show_guess(g):
    for c in g:
        print(c, end=' ')


def guessing_game(words):
    score = 5
    game_over = False
    print("\nLet's play a word guessing game! Press ! to quit. Don't let your score go negative... \n")
    index = random.randint(0, 49)
    word = words[index]
    guess = ['_'] * len(word)
    letters_left = len(word)
    wrong = []

    # UNCOMMENT IF YOU WANT TO CHEAT!!!!!!!!!!
    # print(word)
    show_guess(guess)

    while not game_over:

        letter = input('Guess a letter:')

        while (len(letter) > 1):
            print('Must enter a single character')
            letter = input('Guess a letter:')

        if letter in word and letter not in guess:
            score += 1
            print("Right! Score is", score)  # last letter correct guess
            if word.count(letter) == letters_left:
                for i in range(len(word)):
                    if word[i] == letter:
                        guess[i] = letter
                        letters_left -= 1
                show_guess(guess)
                print("You solved it!")
                print("Current score:", score)
                print("Guess another word")
                index = random.randint(0, 49)
                word = words[index]
                guess = ['_'] * len(word)
                letters_left = len(word)
                wrong = []
                # UNCOMMENT IF YOU WANT TO CHEAT!!!!!!!!!!
                # print(word)
                show_guess(guess)

            else:  # correct guess
                for i in range(len(word)):
                    if word[i] == letter:
                        guess[i] = letter
                        letters_left -= 1
                show_guess(guess)
        elif letter in guess or letter in wrong:
            print("You already guessed that letter! Score is", score)
            show_guess(guess)
        else:
            if letter == '!':
                print("You quit: Game over")
                print("The word was:", word)
                print("Score:", score)
                quit()
            elif score == 0:
                print("Negative score: Game over")
                show_guess(guess)
                score -= 1
                print("Score:", score)
                quit()
            else:
                score -= 1
                wrong.append(letter)
                print("Sorry, guess again. Score is", score)
                show_guess(guess)


def process_text(text):  # takes a list of strings as argument
    # part a
    text = re.sub(r'[.?!,=:;()\-\n\d]', ' ', "".join(text).lower())
    tokens = word_tokenize(text)
    # lexical diversity before removing stopwords
    lexical_diversity = len(set(tokens)) / len(tokens)
    print("lexical diversity: %.2f" % lexical_diversity)
    stop_words = set(stopwords.words('english'))
    new_tokens = [t for t in tokens if not t in stop_words and len(t) > 5]

    # part b
    wnl = WordNetLemmatizer()
    lemmas = set(wnl.lemmatize(t) for t in new_tokens)
    list_lemmas = list(lemmas)

    # part c
    pos_tags = nltk.pos_tag(list_lemmas)
    print("first 20 lemmas w/ pos tagged:", pos_tags[:20])

    # part d
    nouns = [n for (n, p) in pos_tags if p.startswith("N")]

    # part e
    print("num tokens:", len(new_tokens))
    print("num nouns:", len(nouns))

    # part f
    return new_tokens, nouns


# main
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: please enter a filename and a relative path as a system arg')
        quit()

    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
        text_in = f.readlines()

    # call function that preprocesses raw text
    allTokens, allNouns = process_text(text_in)

    # make dictionary from nouns
    noun_dict = {allNouns[i]: allTokens.count(allNouns[i]) for i in range(len(allNouns))}

    # sort by count
    sorted_nouns = sorted(noun_dict.items(), reverse=True, key=lambda x: x[1])

    # print 50 most common words and their counts
    first_fifty = sorted_nouns[0:50]
    print("fifty most common nouns:", first_fifty)
    fifty_list = [x[0] for x in first_fifty]

    # call guessing game function
    guessing_game(fifty_list)
