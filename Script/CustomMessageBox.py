# coding:utf-8
import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout
from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, PushButton, setTheme, Theme

class CustomMessageBox(MessageBoxBase):
    """ Custom message box """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.titleLabel = SubtitleLabel('打开 URL', self)
        self.urlLineEdit = LineEdit(self)
        #使窗口允许拖拽输入文件
        self.setAcceptDrops(True)




        self.urlLineEdit.setPlaceholderText('输入/拖入文件、流或者播放列表的 URL')
        self.urlLineEdit.setClearButtonEnabled(True)

        # 将控件添加到布局中
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        # 按钮文本
        self.yesButton.setText('打开')
        self.cancelButton.setText('取消')

        #禁用开始按钮
        self.widget.setMinimumWidth(350)
        self.yesButton.setDisabled(True)
        # 连接 URL 输入框文本变化信号到验证函数
        self.urlLineEdit.textChanged.connect(self._validateUrl)

    def dragEnterEvent(self,event: QDragEnterEvent)-> None:
            # 判断有没有接受到内容
        if event.mimeData().hasUrls():
            # 如果接收到内容了，就把它存在事件中
            event.accept()
        else:
            # 没接收到内容就忽略
            event.ignore()

    def dropEvent(self, event: QDropEvent) -> None:
        try:
            if event:
                # 遍历所有拖拽的 URL
                for i in event.mimeData().urls():
                    print(i.path())  # 打印 URL 路径
                    file_path = i.path()[1:]  # 去掉路径前面的 '/'
                    self.urlLineEdit.setText(file_path)  # 修改：将文件路径设置到 URL 输入框
        except Exception as e:
            print(f"处理拖拽事件异常: {e}")

    def _validateUrl(self, text):
        #验证URL是否有效，启用打开按钮
        self.yesButton.setEnabled(QUrl(text).isValid())

