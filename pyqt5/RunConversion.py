import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import pyqt5.designer.conversion
from functools import partial


def convert(ui):
    # 获取左侧输入框的内容
    left_input = ui.lineEdit.text()
    # 汇率转换
    result = float(left_input) * 6.7
    # 结果赋值到右侧输入框
    ui.lineEdit_2.setText(str(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = pyqt5.designer.conversion.Ui_mainWindow()
    ui.setupUi(window)
    window.show()
    ui.pushButton.clicked.connect(partial(convert, ui))
    sys.exit(app.exec_())
