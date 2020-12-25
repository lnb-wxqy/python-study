import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QLabel


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        self.button1 = QPushButton("上传图片")
        vlayout.addWidget(self.button1)

        self.imageLabel=QLabel()

        self.resize(400,300)
        self.setLayout(vlayout)

    def loadImage(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
