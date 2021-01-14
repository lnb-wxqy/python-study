from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class DemoWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(400, 250)
        self.btn = QPushButton("发送信号", self)
        # 发送一个client信号，绑定槽函数self.onClick()
        self.btn.clicked.connect(self.onClick)
        # 添加窗口标题
        self.setWindowTitle('SingalDemo')

    # 槽函数，接收btn的clicked信号
    def onClick(self):
        self.btn.setText('接收到信号')
        self.btn.setStyleSheet('max-width:200px;min-width:200px')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DemoWin()
    win.show()
    sys.exit(app.exec_())
