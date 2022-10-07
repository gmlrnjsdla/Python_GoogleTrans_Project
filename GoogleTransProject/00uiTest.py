from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.statusBar().showMessage('상태바')
        self.setWindowTitle('내가 만든 프로그램')
        self.setWindowIcon(QIcon('../icons/google.png'))
        self.resize(400, 300)
        self.move(500, 500)
        btn1 = QPushButton('버튼 1번', self)
        btn1.move(20, 20)
        btn2 = QPushButton('버튼 2번', self)
        btn2.move(20, 50)
        btn1.clicked.connect(self.btn_click1)
        btn2.clicked.connect(self.btn_click2)
        self.setToolTip('버튼을 누르면 <b>출력됩니다.</b>')

        label1 = QLabel('출력될 위치', self)
        label1.move(20, 150)

        self.show()

    def btn_click1(self):    # slot
        # print('버튼 1번이 클릭되었습니다!!!.')
        self.label1.setText('버튼1이 클릭되었습니다!!!')
    def btn_click2(self):    # slot
        # print('버튼 2번이 클릭되었습니다!!!.')
        self.label1.setText('버튼2가 클릭되었습니다!!!')
app = QApplication(sys.argv)
myWin = MyWindow()
app.exec_()
