import sys,os
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout,QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignRight)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
        QLabel{
            border: 4px dashed #aaa
        }
        ''')
    def setPixmap(self,image):
        super().setPixmap(image)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1300,1000)
        self.setWindowTitle("LOGISIM SIMULATION")
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\Anshu\\Desktop\\log.png"))
        self.setStyleSheet(
      "QWidget"
        "{"
            
            "background-color:rgb(231, 187, 225)"
        "}"
        )
        self.setAcceptDrops(True)
        mainLayout=QGridLayout()
        self.photoViewer=ImageLabel()
        mainLayout.addWidget(self.photoViewer,350,350)

        self.check1=QCheckBox("INPUT 1")
        self.check1.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:25px;"
            "height:25px;"            
        "}"
        )

        self.check2=QCheckBox("INPUT 2")
        self.check2.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:25px;"
            "height:25px;"            
        "}"
        )

        self.check3=QCheckBox("INPUT 3")
        self.check3.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:25px;"
            "height:25px;"            
        "}"
        )

        self.check_o=QCheckBox("0")
        self.check_o.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o1=QCheckBox("1")
        self.check_o1.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o2=QCheckBox("2")
        self.check_o2.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o3=QCheckBox("3")
        self.check_o3.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o4=QCheckBox("4")
        self.check_o4.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o5=QCheckBox("5")
        self.check_o5.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o6=QCheckBox("6")
        self.check_o6.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check_o7=QCheckBox("7")
        self.check_o7.setStyleSheet("QCheckBox::indicator:unchecked"
        "{"
            
            "background-color:red;"
        "}"
        "QCheckBox::indicator:checked"
        "{"
            
            "background-color:green;"
        "}"
        "QCheckBox::indicator"
        "{"
            "width:40px;"
            "height:40px;"            
        "}"
        )
        self.check1.stateChanged.connect(self.onchecking1)
        self.check2.stateChanged.connect(self.onchecking2)
        self.check3.stateChanged.connect(self.onchecking3)

        mainLayout.addWidget(self.check1,349,0)

        mainLayout.addWidget(self.check2,350,0)

        mainLayout.addWidget(self.check3,351,0)
      
        mainLayout.addWidget(self.check_o,346,700)
        mainLayout.addWidget(self.check_o1,347,700)

        mainLayout.addWidget(self.check_o2,348,700)

        mainLayout.addWidget(self.check_o3,349,700)
      
        mainLayout.addWidget(self.check_o4,350,700)
        mainLayout.addWidget(self.check_o5,351,700)

        mainLayout.addWidget(self.check_o6,352,700)

        mainLayout.addWidget(self.check_o7,353,700)
      

        self.setLayout(mainLayout)
    def dragEnterEvent(self,event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()   
    def dragMoveEvent(self,event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
    def dropEvent(self,event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path=event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()
        else:
            event.ignore()
    def set_image(self,file_path):
        self.photoViewer.setPixmap(QPixmap(file_path)) 
  
    def onchecking1(self,checked):
        if(Qt.Checked==checked and not self.check2.isChecked() and not self.check3.isChecked):
            self.check_o4.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check2.isChecked() and not self.check3.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(True)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check2.isChecked() and not self.check3.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(True)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check2.isChecked() and self.check3.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(True)
        if  Qt.Checked==checked and not self.check2.isChecked() and  self.check3.isChecked:
            self.check_o5.setChecked(True)
            
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check2.isChecked() and self.check3.isChecked:
            self.check_o3.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and not self.check2.isChecked() and self.check3.isChecked:
            self.check_o1.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)    

        if not Qt.Checked==checked and not self.check2.isChecked() and not self.check3.isChecked:
            self.check_o.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
    def onchecking2(self,checked):
        if(Qt.Checked==checked and not self.check1.isChecked() and not self.check3.isChecked):
            self.check_o2.setChecked(True)
            self.check_o4.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check1.isChecked() and not self.check3.isChecked:
            self.check_o4.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check1.isChecked() and not self.check3.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(True)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check1.isChecked() and self.check3.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(True)
        if  Qt.Checked==checked and not self.check1.isChecked() and  self.check3.isChecked:
            self.check_o3.setChecked(True)
            
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check1.isChecked() and self.check3.isChecked:
            self.check_o5.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and not self.check1.isChecked() and self.check3.isChecked:
            self.check_o1.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)    

        if not Qt.Checked==checked and not self.check1.isChecked() and not self.check3.isChecked:
            self.check_o.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
    def onchecking3(self,checked):
        if(Qt.Checked==checked and not self.check1.isChecked() and not self.check2.isChecked):
            self.check_o1.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check1.isChecked() and not self.check2.isChecked:
            self.check_o1.setChecked(False)
            self.check_o4.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check1.isChecked() and not self.check2.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o5.setChecked(True)
            self.check_o7.setChecked(False)
        if  Qt.Checked==checked and self.check1.isChecked() and self.check2.isChecked:
            self.check_o4.setChecked(False)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(True)
        if  Qt.Checked==checked and not self.check1.isChecked() and  self.check2.isChecked:
            self.check_o3.setChecked(True)
            
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and self.check1.isChecked() and self.check2.isChecked:
            self.check_o6.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o7.setChecked(False)
        if not Qt.Checked==checked and not self.check1.isChecked() and self.check2.isChecked:
            self.check_o2.setChecked(True)
            self.check_o1.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False)    

        if not Qt.Checked==checked and not self.check1.isChecked() and not self.check2.isChecked:
            self.check_o.setChecked(True)
            self.check_o2.setChecked(False)
            self.check_o1.setChecked(False)
            self.check_o4.setChecked(False)
            self.check_o3.setChecked(False)
            self.check_o5.setChecked(False)
            self.check_o6.setChecked(False)
            self.check_o7.setChecked(False) 



app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())


