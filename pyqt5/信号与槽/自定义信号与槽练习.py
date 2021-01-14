from PyQt5.QtCore import Qt, QObject, pyqtSignal


# 自定义信号类
class Mysignal(QObject):
    # 定义一个信号，object表示传递一个参数
    sendmsg = pyqtSignal(object)

    def run(self):
        self.sendmsg.emit("Hello PyQt5")  # 触发信号，并传入一个string参数


# 自定义槽
class MySlot(QObject):
    # 自定义槽函数，接收一个string参数
    def slot(self, msg):
        print("接收到的信息是：", msg)


if __name__ == '__main__':
    mySignal = Mysignal()
    myslot = MySlot()
    # 将信号与槽进行绑定
    mySignal.sendmsg.connect(myslot.slot)
    # mySignal.sendmsg.disconnect(myslot.slot) 断开连接
    mySignal.run()
