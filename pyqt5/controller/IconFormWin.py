'''
窗口的setWindowICon方法用于设置窗口的图标，只在windows中可用

QApplication中的setWindowIcon方法用于设置主窗口的图标和应用程序图标，但是调用了窗口的setWindowIcon方法
QApplication中的setWindowIcon方法就只能用于设置应用程序图标了
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        # 参数说明：setGeometry(x,y，宽，高)
        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle('图片ICON')
        # 设置窗口图标
        self.setWindowIcon(QIcon('./images/Basilisk.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置窗口标题
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    iconWin = IconForm()
    iconWin.show()

    sys.exit(app.exec_())
