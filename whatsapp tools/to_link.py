from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import pyperclip, webbrowser
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("إنشاء رابط لرقم هاتف")
        self.إظهار=qt.QLabel("أكتب رقم الهاتف بالإضافة الى رمز الدولة")
        self.رقم_الهاتف=qt.QLineEdit()
        self.رقم_الهاتف.setAccessibleName("أكتب رقم الهاتف بالإضافة الى رمز الدولة")
        self.إنشاء=qt.QPushButton("إنشاء الرابط")
        self.إنشاء.setDefault(True)
        self.إنشاء.clicked.connect(self.link)
        self.إظهار1=qt.QLabel("الرابط هو")
        self.الرابط=qt.QLineEdit()
        self.الرابط.setReadOnly(True)
        self.الرابط.setAccessibleName("الرابط هو")
        self.نسخ=qt.QPushButton("نسخ الرابط")
        self.نسخ.setDefault(True)
        self.نسخ.clicked.connect(self.copy)
        self.فتح=qt.QPushButton("فتح الرابط")
        self.فتح.setDefault(True)
        self.فتح.clicked.connect(self.opin)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.إظهار)
        l.addWidget(self.رقم_الهاتف)
        l.addWidget(self.إنشاء)
        l.addWidget(self.إظهار1)
        l.addWidget(self.الرابط)
        l.addWidget(self.نسخ)
        l.addWidget(self.فتح)
    def link(self):
        رقم_الهاتف=self.رقم_الهاتف.text()
        الرابط="https://wa.me/"+رقم_الهاتف
        self.الرابط.setText(الرابط)
        self.الرابط.setFocus()        
    def copy(self):
        pyperclip.copy(self.الرابط.text())
        qt.QMessageBox.information(self,"تم","تم نسخ الرابط بنجاح")
    def opin(self):
        webbrowser.open(self.الرابط.text())