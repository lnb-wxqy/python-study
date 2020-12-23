# 开发者: 五行缺雨

# 时间: 2020/12/20 22:44

# 主窗口居中
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterMainWindow(QMainWindow):
    def __init__(self):
        super(CenterMainWindow, self).__init__()

        # 设置窗口标题
        self.setWindowTitle('主窗口居中')
        # 设置窗口大小
        self.resize(400, 300)
        self.status = self.statusBar()
        self.status.showMessage('消息存在5秒', 5000)

        # 调用center方法
        self.center()

    # 设置窗口居中的方法
    def center(self):
        print('进入center方法...')
        # 获取屏幕的坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口的坐标
        curWinSize = self.geometry()
        newLeft = (screen.width() - curWinSize.width()) // 2
        newTop = (screen.height() - curWinSize.height()) // 2

        print(newLeft, newTop)
        # 移动窗口
        self.move(newLeft, newTop)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/dragon.png'))
    main = CenterMainWindow()
    # 此处需调用center方法或者在构造函数__init__中调用
    # main.center()
    main.show()
    sys.exit(app.exec_())
