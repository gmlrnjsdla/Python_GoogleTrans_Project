import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
form_class = uic.loadUiType('ui/GoogleTransUi.ui')[0]


class TransAppWin(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('구글 한줄 번역기')
        self.setWindowIcon(QIcon('icons/google.png'))
        self.statusBar().showMessage('GoogleTransApp v 1.0')
        self.init_btn.clicked.connect(self.init_btn_click)
        self.trans_btn.clicked.connect(self.trans_btn_click)
        self.kor_input.returnPressed.connect(self.trans_btn_click)
        # 한글 입력창에서 엔터키 이벤트 발생시 trans_btn_click 함수 호출

    def trans_btn_click(self):
        kor_text = self.kor_input.text()   # 한국어 라인에디트에 입력된 문자열을 가져오기
        translator = googletrans.Translator()

        trans_result_eng = translator.translate(kor_text, dest='en')
        self.eng_output.append(trans_result_eng.text)

        trans_result_jap = translator.translate(kor_text, dest='ja')
        self.jap_output.append(trans_result_jap.text)

        trans_result_chn = translator.translate(kor_text, dest='zh-CN')
        self.chn_output.append(trans_result_chn.text)

    def init_btn_click(self):
        self.kor_input.clear()
        self.eng_output.clear()
        self.jap_output.clear()
        self.chn_output.clear()


app = QApplication(sys.argv)
transAppWin = TransAppWin()
transAppWin.show()
app.exec_()
