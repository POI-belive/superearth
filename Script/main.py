from PyQt5.QtWidgets import QApplication,QMainWindow
from main_window import Ui_MainWindow
from Script.CustomMessageBox import CustomMessageBox

# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        self.ui.PushButton.clicked.connect(self.showDialog)
        self.ui.PushButton_2.clicked.connect(self.showDialog)


    def showDialog(self):
        w = CustomMessageBox(self)
        if w.show():
            print(w.urlLineEdit.text())

        
        # 使用界面定义的控件，也是从ui里面访问
        #self.ui.webview.load('http://www.baidu.com')

try:
    app = QApplication([])
    mainw = MainWindow()
    mainw.show()
    app.exec()
except Exception as e:
    print(f"程序异常: {e}")