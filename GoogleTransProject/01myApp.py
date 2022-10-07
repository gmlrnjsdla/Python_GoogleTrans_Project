import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType('../ui/test.ui')[0]
# qt designer로 제작한 ui 불러오기


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn1.clicked.connect(self.btn_click1)
        self.btn2.clicked.connect(self.btn_click2)

    def btn_click1(self):
        self.label1.setText('버튼1이 클릭되었습니다.')

    def btn_click2(self):
        self.label1.setText('버튼2이 클릭되었습니다.')

# 메인 윈도우를 실행시키고 그 후에 종료되지 않게 루프시키는 역할.
app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()     # 이벤트 루프 생성
