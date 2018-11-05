class Guess: # model 이 관리

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = ''
        self.currentStatus = '_' * len(self.secretWord)

    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)

    def guess(self, character):
        self.guessedChar = character  # 사용자가 입력한 추측한 단어
        self.guessedChars.append(self.guessedChar) # 입력 단어를 저 위에 리스트에 추가
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == self.guessedChar:  # 입력한 단어가 시크릿단어에 있으면
                self.currentStatus = self.currentStatus[:i] + self.secretWord[i] + self.currentStatus[i + 1:]
                if self.currentStatus == self.secretWord:  # 현재상태랑 시크릿단어랑 똑같을 경우
                    return True
                else:
                    return False
        else:  # 실패시
            self.numTries += 1
