import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        name = QLabel('Name') # QLabel 지정
        age = QLabel('Age')
        score = QLabel('Score')

        self.nameEdit = QLineEdit() # QLineEdit 지정
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        hbox1 = QHBoxLayout() # 가로 상자 레이아웃을 hbox1 지정
        hbox1.addStretch(1) # 오른쪽 정렬

        hbox1.addWidget(name) # hbox1 에 추가
        hbox1.addWidget(self.nameEdit) # hbox1 에 추가

        hbox1.addWidget(age) # hbox1 에 추가
        hbox1.addWidget(self.ageEdit) # hbox1 에 추가

        hbox1.addWidget(score) # hbox1 에 추가
        hbox1.addWidget(self.scoreEdit) # hbox1 에 추가

        amount = QLabel('Amount') # QLabel 지정
        key = QLabel('Key')

        self.amountEdit = QLineEdit() # QLineEdit 지정
        self.keyEdit = QComboBox() # QComboBox 지정
        self.keyEdit.addItem("Name") # QComboBox에 사용될 이름들 추가
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        hbox3 = QHBoxLayout() # 가로 상자 레이아웃을 hbox3라 지정
        hbox3.addStretch(1) # 오른쪽 정렬

        hbox3.addWidget(amount) # hbox3 에 추가
        hbox3.addWidget(self.amountEdit)
        hbox3.addWidget(key)
        hbox3.addWidget(self.keyEdit)


        self.addButton = QPushButton("Add") # add,del,find,inc,show들의
        self.delButton = QPushButton("Del") # 푸시버튼을 만들어준다.
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("show")

        hbox = QHBoxLayout() # 가로 상자 레이아웃을 hbox 라 지정
        hbox.addStretch(1) # 위젯 오른쪽 정렬
        hbox.addWidget(self.addButton) #hbox 에 버튼들을 넣어준다.
        hbox.addWidget(self.delButton)
        hbox.addWidget(self.findButton)
        hbox.addWidget(self.incButton)
        hbox.addWidget(self.showButton)

        result = QLabel('result') # QLabel 지정

        self.resultEdit = QTextEdit() # QTextEdit 지정

        hbox2 = QHBoxLayout() # 가로 상자 레이아웃

        hbox2.addWidget(result) # hbox2 에 추가
        hbox2.addWidget(self.resultEdit) # hbox2 에 추가

        vbox = QVBoxLayout() # 세로 상자 레이아웃을 vbox 로 지정
        vbox.addStretch(1) # 오른쪽 정렬
        vbox.addLayout(hbox1) # hbox1을 vbox에 담는다
        vbox.addLayout(hbox3) # hbox3을 vbox에 담는다
        vbox.addLayout(hbox) # hbox를 vbox에담는다
        vbox.addLayout(hbox2) # hbox2를 vbox에 담는다

        self.setLayout(vbox) # self.setLayout(vbox)를 통하여 윈도우의 메인 레이아웃 설정

        self.setGeometry(300, 300, 500, 250) # 화면 크기
        self.setWindowTitle('Assignment6') # 화면 제목
        self.show() # 보여준다

        self.addButton.clicked.connect(self.buttonClicked) # add,del,find,inc,show 버튼이
        self.delButton.clicked.connect(self.buttonClicked) # buttonClicked() 메서드에 연결
        self.findButton.clicked.connect(self.buttonClicked)
        self.incButton.clicked.connect(self.buttonClicked)
        self.showButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        b =[] # 리스트 b 를 만들어줍니다.
        sender = self.sender() # sender 메서드를 호출하여 신호 소스를 결정한다.
        if sender.text() == "Add": # Add 버튼이 눌렸을 때
            try:
                record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
                if int(self.ageEdit.text()) and int(self.scoreEdit.text()): # 나이와 점수가 정수형으로 들어왔을때
                    self.scoredb += [record] # 추가한다
                    self.showScoreDB() # 밑에 show 소환
            except ValueError: # 나이와 점수창에 문자를 입력했을 경우의 예외처리
                self.resultEdit.setPlainText("int형으로 입력해주세요")

        elif sender.text() == "Del": # Del 버튼이 눌렸을 때
            count = 0
            for p in self.scoredb[:]: #scoredb 를 p 에 담아서 반복
                if p['Name'] == self.nameEdit.text(): # p 에 입력한 name 이 있으면
                    count+=1
                    self.scoredb.remove(p) # 제거한다.
                if count == 0:
                    self.resultEdit.setText("없는 name입니다.")
                else:
                    self.showScoreDB()
            #except IndexError:
                #self.resultEdit.setPlainText("DB안에 있는 name을 써주세요")

        elif sender.text() == "Find": # Find 버튼이 눌렸을 때
            count = 0
            for p in self.scoredb: #scoredb 를 p 에 담아서 반복
                if p['Name'] == self.nameEdit.text():  #p 에 입력한 name 이 있으면
                    count += 1 # count 증가
                    b.append(p) # 위에서 만든 리스트 b에 p를 추가한다.
                if count == 0: # count 가 0 이면 
                    self.resultEdit.setText("없는 name입니다.")
                else:
                    a = self.scoredb # a에 저장
                    self.scoredb = b # scoredb에 b 를 담는다.
                    self.showScoreDB() # 보여준다
                    self.scoredb = a # scoredb에 a 를 담는다. 이렇게 안하면 b만 남아있음

        elif sender.text() == "Inc": # Inc 버튼이 눌렸을 때
            for p in self.scoredb: #scoredb 를 p 에 담아서 반복
                if p['Name'] == self.nameEdit.text(): #p 에 입력한 name 이 있으면
                    p['Score'] = str(int(p['Score']) + int(self.amountEdit.text())) # 점수랑 더한 양을 int 로 변환해서 더한 후 str로 다시변환하여 p['Score']에 저장
            self.showScoreDB() #보여준다

        elif sender.text() == "show": # show 버튼이 눌렸을 때
            self.showScoreDB() # 보여준다


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)

            for a in self.scoredb:
                a['Score'] = int(a['Score']) # int 형으로 변경
                a['Age'] = int(a['Age'])
        except:
            self.resultEdit.setText("Empty DB: " + self.dbfilename)

        else:
            self.resultEdit.setText("Open DB: "+ self.dbfilename)
        fH.close()
        return self.scoredb


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        section = '' #올때마다 초기화

        keyname = self.keyEdit.currentText() # 현재 콤보 박스에 지정된 텍스트를 그대로 가져온다. 없으면 망함니다.

        for p in sorted(self.scoredb, key=lambda person: person[keyname]): # 형식 맞추기
            for attr in sorted(p):
                section += str(attr) + "=" + str(p[attr]) + '\t'

            section += '\n'

        self.resultEdit.setPlainText(section)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
