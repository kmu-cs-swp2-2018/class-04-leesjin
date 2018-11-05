from hangman import Hangman
from guess import Guess
from word import Word

def gameMain():
    word = Word('words.txt')
    guess = Guess(word.randFromDB())

    finished = False
    hangman = Hangman()
    maxTries = hangman.getLife()

    while guess.numTries < maxTries:

        display = hangman.get(maxTries - guess.numTries)
        print(display)
        guess.display()

        guessedChar = input('Select a letter: ')
        if len(guessedChar) != 1: #2개단어 입력햇을경우
            print('One character at a time!')
            continue
        if guessedChar in guess.guessedChars: # 중복 입력했을 경우
            print('You already guessed \"' + guessedChar + '\"')
            continue

        if guessedChar == '0': # 0을 입력한 경우
            print(guess.secretWord)  # 시크릿 단어출력

        finished = guess.guess(guessedChar)
        if finished == True: #맞췄을 경우
            break

    if finished == True:
        print('Success')
    else:
        print(hangman.get(0))
        print('word [' + guess.secretWord + ']')
        print('guess [' + guess.currentStatus + ']')
        print('Fail')

if __name__ == '__main__':
    gameMain()
