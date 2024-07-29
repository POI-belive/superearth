import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Script.tts import AudioStreamer
from main_window import Ui_MainWindow
from Script.CustomMessageBox import CustomMessageBox
from PyQt5.QtCore import QThread, pyqtSignal


class AudioStreamThread(QThread):
    def __init__(self, character, text):
        super().__init__()
        self.character = character
        self.text = text

    def run(self):
        audio_streamer = AudioStreamer(self.character, self.text)
        audio_streamer.play_audio()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        self.ui.PushButton.clicked.connect(self.showDialog)
        self.ui.PushButton_2.clicked.connect(self.showDialog)

        self.starAudio()



        # 使用线程播放音频
    def starAudio(self):
        # 文本接口和切换音色接口
        character = '胡桃'
        text = '狂气的蛋幕遗产：东方绀珠传～ 疯狂王国的遗产，是由上海爱丽丝幻乐团所制作的纵向卷轴蛋幕射击游戏，东方Project系列的第十五作'

        #character=
        #text=
        self.audio_thread = AudioStreamThread(character, text)
        self.audio_thread.start()

    # 调用文件输入窗口
    def showDialog(self):
        w = CustomMessageBox(self)
        if w.show():
            print(w.urlLineEdit.text())


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mainw = MainWindow()
        mainw.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f"程序异常: {e}")
