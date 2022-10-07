import sys
from PyQt5.QtWidgets import *

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.edit1 = QLabel('안녕하세요')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()
    sys.exit(app.exec_())