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
        name = QLabel('Name')
        age = QLabel('Age')
        score = QLabel('Score')

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)

        hbox1.addWidget(name)
        hbox1.addWidget(self.nameEdit)

        hbox1.addWidget(age)
        hbox1.addWidget(self.ageEdit)

        hbox1.addWidget(score)
        hbox1.addWidget(self.scoreEdit)

        amount = QLabel('Amount')
        key = QLabel('Key')

        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItem("Name")
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)

        hbox3.addWidget(amount)
        hbox3.addWidget(self.amountEdit)
        hbox3.addWidget(key)
        hbox3.addWidget(self.keyEdit)


        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Del")
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("show")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.addButton)
        hbox.addWidget(self.delButton)
        hbox.addWidget(self.findButton)
        hbox.addWidget(self.incButton)
        hbox.addWidget(self.showButton)

        result = QLabel('result')

        self.resultEdit = QTextEdit()
        # self.resultEdit.setText("예진이 바보")

        hbox2 = QHBoxLayout()

        hbox2.addWidget(result)
        hbox2.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

        self.addButton.clicked.connect(self.buttonClicked)
        self.delButton.clicked.connect(self.buttonClicked)
        self.findButton.clicked.connect(self.buttonClicked)
        self.incButton.clicked.connect(self.buttonClicked)
        self.showButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        b =[]
        sender = self.sender()
        if sender.text() == "Add":
            try:
                record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
                if int(self.ageEdit.text()) and int(self.scoreEdit.text()):
                    self.scoredb += [record]
                    self.showScoreDB() # 밑에 show 소환
            except ValueError:
                self.resultEdit.setPlainText("int형으로 입력해주세요")

        elif sender.text() == "Del":
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    self.scoredb.remove(p)
            self.showScoreDB()
            #except IndexError:
                #self.resultEdit.setPlainText("DB안에 있는 name을 써주세요")

        elif sender.text() == "Find":
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    b.append(p)
            a = self.scoredb
            self.scoredb = b
            self.showScoreDB()
            self.scoredb = a

        elif sender.text() == "Inc":
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    p['Score'] = str(int(p['Score']) + int(self.amountEdit.text()))
            self.showScoreDB()

        elif sender.text() == "show":
            self.showScoreDB()


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
                a['Score'] = int(a['Score'])
                a['Age'] = int(a['Age'])
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        section = '' #올때마다 초기화

        keyname = self.keyEdit.currentText()

        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                section += str(attr) + "=" + str(p[attr]) + '\t'

            section += '\n'

        self.resultEdit.setPlainText(section)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())