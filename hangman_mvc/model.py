from word import Word

class Model:

    def __init__(self, word):
        self.secretWord = word # 비밀단어
        self.guessedChars = [] # 사용한 글자를 담는 리스트
        self.numTries = 0 # 실패 횟수
        self.current= [] # 현재 상태 데이터를 담는 리스트
        self.currentStatus = ""
        for i in range(len(self.secretWord)) :
            self.current.append("_ ")

    def display(self):
        self.currentStatus = "".join(self.current)  # 현재 맞춘 글자들을 표시
        self.used = ""
        self.used += " ".join(self.guessedChars) # 현재 사용된 글자들을 표시
        print("Current: " + self.currentStatus)
        print("Tries:", self.numTries)
        print("Already Used:", self.used)

    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord :
            for i in range(len(self.secretWord)) :
                if self.secretWord[i] == character :
                    self.current[i] = character
                    if not("_ " in self.current) :
                        return True
        self.numTries += 1
        return False

    def gameMain():
        word = Word('words.txt')
        guess = Model(word.randFromDB())

        finished = False
        hangman = Hangman()
        maxTries = hangman.getLife()

        while guess.numTries < maxTries:

            display = hangman.get(maxTries - guess.numTries)
            print(display)
            guess.display()

            guessedChar = input('Select a letter: ')
            if len(guessedChar) != 1:  # 2개단어 입력햇을경우
                print('One character at a time!')
                continue
            if guessedChar in guess.guessedChars:  # 중복 입력했을 경우
                print('You already guessed \"' + guessedChar + '\"')
                continue

            if guessedChar == '0':  # 0을 입력한 경우
                print(guess.secretWord)  # 시크릿 단어출력

            finished = guess.guess(guessedChar)
            if finished == True:  # 맞췄을 경우
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