# 开发者: 五行缺雨

# 时间: 2020/12/20 22:13
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    # 初始化
    def __init__(self, parent=None):
        # 调用父类构造函数，传入parent参数
        super(FirstMainWin, self).__init__(parent)
        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口尺寸
        self.resize(400, 300)
        # 状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置图标
    app.setWindowIcon(QIcon('./images/dragon.png'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())
