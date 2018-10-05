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

        firstlinehbox = QHBoxLayout()
        firstlinehbox.addStretch(1)

        firstlinehbox.addWidget(name)
        firstlinehbox.addWidget(self.nameEdit)

        firstlinehbox.addWidget(age)
        firstlinehbox.addWidget(self.ageEdit)

        firstlinehbox.addWidget(score)
        firstlinehbox.addWidget(self.scoreEdit)

        amount = QLabel('Amount')
        key = QLabel('Key')

        self.amountEdit = QLineEdit()
        self.keyEdit = QComboBox()
        self.keyEdit.addItem("Name")
        self.keyEdit.addItem("Age")
        self.keyEdit.addItem("Score")

        secondlinehbox = QHBoxLayout()
        secondlinehbox.addStretch(1)

        secondlinehbox.addWidget(amount)
        secondlinehbox.addWidget(self.amountEdit)
        secondlinehbox.addWidget(key)
        secondlinehbox.addWidget(self.keyEdit)


        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Del")
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("show")

        thridlinehbox = QHBoxLayout()
        thridlinehbox.addStretch(1)
        thridlinehbox.addWidget(self.addButton)
        thridlinehbox.addWidget(self.delButton)
        thridlinehbox.addWidget(self.findButton)
        thridlinehbox.addWidget(self.incButton)
        thridlinehbox.addWidget(self.showButton)

        result = QLabel('result')

        self.resultEdit = QTextEdit()

        fourthlinebox = QHBoxLayout()

        fourthlinebox.addWidget(result)
        fourthlinebox.addWidget(self.resultEdit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(firstlinehbox)
        vbox.addLayout(secondlinehbox)
        vbox.addLayout(thridlinehbox)
        vbox.addLayout(fourthlinebox)

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
                    self.showScoreDB()
            except ValueError:
                self.resultEdit.setPlainText("int형으로 입력해주세요")

        elif sender.text() == "Del":
            count = 0
            for p in self.scoredb[:]:
                if p['Name'] == self.nameEdit.text():
                    count+=1
                    self.scoredb.remove(p)
                if count == 0:
                    self.resultEdit.setText("없는 name입니다.")
                else:
                    self.showScoreDB()

        elif sender.text() == "Find":
            count = 0
            for p in self.scoredb:
                if p['Name'] == self.nameEdit.text():
                    count += 1
                    b.append(p)
                if count == 0:
                    self.resultEdit.setText("없는 name입니다.")
                else:
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
        section = ''

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