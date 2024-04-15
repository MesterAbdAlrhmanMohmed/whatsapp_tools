from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import to_link, plus_message
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("whatsapp tools")
        self.الخيارات=qt.QListWidget()
        self.الخيارات.clicked.connect(self.ch)
        self.الخيارات.addItem("إنشاء رابط لرقم هاتف")
        self.الخيارات.addItem("إنشاء رابط لرقم هاتف مع رسالة")        
        self.إختيار=qt.QPushButton("إختيار")
        self.إختيار.setDefault(True)
        self.إختيار.setShortcut("return")
        self.إختيار.clicked.connect(self.ch)
        l=qt.QVBoxLayout()        
        l.addWidget(self.الخيارات)
        l.addWidget(self.إختيار)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def ch(self):
        العناصر=self.الخيارات.currentRow()
        if العناصر==0:            
            to_link.dialog(self).exec()
        if العناصر==1:
            plus_message.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()