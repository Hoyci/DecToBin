import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QSizePolicy


class BinToDec(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()
        self.botoes()

    def initUI(self):
        self.setWindowTitle('BinToDec')
        self.setFixedSize(500, 100)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        

        self.display1 = QLineEdit()
        self.display1.setPlaceholderText('Insira um número decimal')
        self.display1.setMaximumHeight(30)
        self.display1.setStyleSheet('background-color: #E8E8EC; border-radius: 5px; color: black')

        self.display2 = QLineEdit()
        self.display2.setPlaceholderText('Insira um número binário')
        self.display2.setMaximumHeight(30)
        self.display2.setStyleSheet('background-color: #E8E8EC; border-radius: 5px; color: black')

        self.grid.addWidget(self.display1, 0, 0)
        self.grid.addWidget(self.display2, 0, 1)

        self.display1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.display2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.setCentralWidget(self.cw)

    def botoes(self):
        self.btn1 = QPushButton('DecToBin', self)
        self.btn1.setStyleSheet('border: 2px solid rgb(37, 39, 48); background-color: #FCA969')
        self.btn1.clicked.connect(self.BinToDec)
        self.grid.addWidget(self.btn1, 1, 0)

        self.btn2 = QPushButton('BinToDec', self)
        self.btn2.setStyleSheet('border: 2px solid rgb(37, 39, 48); background-color: #FCA969; ')
        self.btn2.clicked.connect(self.DecToBin)
        self.grid.addWidget(self.btn2, 1, 1)

    def BinToDec(self):
        try:
            self.display2.setText(
                str(bin((int(self.display1.text()))))
            )
        except Exception as e:
            self.display1.setText('Você digitou um valor inválido')

    def DecToBin(self):
        try:
            self.display1.setText(
                str(int(self.display2.text(), 2))
            )
        except Exception as e:
            self.display2.setText('Você digitou um valor inválido')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    binToDec = BinToDec()
    binToDec.show()
    qt.exec_()
