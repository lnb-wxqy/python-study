import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pyqt5.designer.imageConvertBase64
from functools import partial
from PyQt5.QtGui import QPixmap


def uploadImage(ui):
    fname, _ = QFileDialog.getOpenFileName(ui, '打开文件', '.', '图像文件(*.jpg *.png)')
    print(fname)
    ui.textEdit.setPixmap(QPixmap(fname))
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = pyqt5.designer.imageConvertBase64.Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    ui.pushButton.clicked.connect(partial(uploadImage, ui))
    sys.exit(app.exec_())
