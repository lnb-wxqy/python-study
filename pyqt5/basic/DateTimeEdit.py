'''
输入各种风格的日期和时间

知识点：QDateTimeEdit类、QVBoxLayout(垂直布局)

每种信号触发条件：
dateChanged(QDate) 当日期改变时发出信号，并传递出日期
dateTimeChanged(QDateTime)当日期时间改变时发出信号，并传递出日期时间
editingFinished() 结束编辑时发出的信号(回车，Tab，鼠标都可触发)，不传递数据
timeChanged(QTime)当时间改变时发出信号，并传递出时间
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        # 垂直布局 按照从上到下的顺序添加按钮部件
        vlayout = QVBoxLayout()
        dt1 = QDateTimeEdit()
        dt2 = QDateTimeEdit(QDateTime.currentDateTime())
        dt1.setMinimumDate(QDate.currentDate().addDays(-365))  # 可选的最小日期
        dt1.setMaximumDate(QDate.currentDate().addDays(365))  # 可选的最大日期
        self.dt = dt1
        # 可弹出日历进行选择
        dt2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dt1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dt2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')

        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        dt1.dateChanged.connect(self.onDateChanged)
        dt1.dateTimeChanged.connect(self.onDateTimeChanged)
        dt1.timeChanged.connect(self.onTimeChanged)

        # 给Vlayout添加按钮部件
        vlayout.addWidget(dt1)
        vlayout.addWidget(dt2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        # 添加点击按钮
        self.btn = QPushButton('获取当前日期和时间')
        self.btn.clicked.connect(self.onButtonClicked)
        vlayout.addWidget(self.btn)

        self.setLayout(vlayout)

        # 设置窗口大小和标题
        self.resize(400, 200)
        self.setWindowTitle('使用垂直布局-设置不同风格的日期和时间')

    # 日期变化
    def onDateChanged(self, date):
        print(date)

    # 时间变化
    def onTimeChanged(self, time):
        print(time)

    # 日期和时间变化
    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    # 获取当前时间按钮
    def onButtonClicked(self):
        datetime = self.dt.dateTime()
        print(datetime)

        # 最大日期
        print(self.dt.maximumDate())

        # 最大日期和时间
        print(self.dt.maximumDateTime())

        # 最小日期和时间
        print(self.dt.minimumDateTime())


if __name__ == '__main__':
    # 创建QApplication
    app = QApplication(sys.argv)
    w = DateTimeEdit()
    w.show()
    sys.exit(app.exec_())
