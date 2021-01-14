from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import pyqt5.designer.hello_pyqt5


# 注意：此方法需在 if __name=='__main__'之前定义
# 否则if __name=='__main__'中调用click_success报无法解析
def click_success():
    print('success')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWind = QMainWindow()
    main = pyqt5.designer.hello_pyqt5.Ui_MainWindow()
    main.setupUi(mainWind)
    mainWind.show()
    main.pushButton.clicked.connect(click_success)
    sys.exit(app.exec_())
