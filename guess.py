class Guess: # model 이 관리

    def __init__(self, word):
        self.secretWord = word # 여기다 시크릿단어 저장할래
        self.guessedChars = [] #pdf 가 시켯서
        self.numTries = 0 # pdf 가 시켯서
        self.currentStatus = '' # pdf가 시켯서
        self.currentStatus = '_' * len(self.secretWord)

    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)

    def guess(self, character):
        #self.currentStatus = '_'*len(self.secretWord) # word 길이 만큼 일단 전부 '_' 하기
        self.guessedChar = character # 사용자가 입력한 추측한 단어
        #self.guessedChars.append[self.guessedChar] # 입력 단어를 저 위에 리스트에 추가
        for i in range(len(self.secretWord)):
            if self.secretWord[i] in self.guessedChar:# 입력한 단어가 시크릿단어에 있으면
                self.currentStatus = self.currentStatus[:i] + self.secretWord[i] + self.currentStatus[i+1:]
                if self.currentStatus == self.secretWord: # 현재상태랑 시크릿단어랑 똑같을 경우
                    return True
                else:
                    return False
        else: # 실패시
            self.numTries += 1
