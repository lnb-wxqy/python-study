# 开发者: 五行缺雨

# 时间: 2020/12/22 20:36

# 退出应用程序
# QHBoxLayout: 水平布局
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QPushButton, QWidget


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle('退出应用程序')

        # 添加按钮（信号事件）
        self.btn = QPushButton('点击我退出应用程序')
        # 将信号与槽关联
        self.btn.clicked.connect(self.onClickButton)

        # 创建水平布局对象
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.btn)

        # 顶层控件
        window = QWidget()
        window.setLayout(hLayout)
        self.setCentralWidget(window)

    # 按钮单击事件的方法（自定义的槽：槽相当于事件的方法）
    def onClickButton(self):
        sender = self.sender()
        print(sender.text() + ' ,按钮被按下')
        # 创建QApplication实例
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())
