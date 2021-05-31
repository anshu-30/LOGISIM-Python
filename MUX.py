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

        self.check1=QCheckBox("INPUT 0")
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

        self.check2=QCheckBox("INPUT 1")
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

        self.check3=QCheckBox("INPUT 2")
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
        self.check4=QCheckBox("INPUT 3")
        self.check4.setStyleSheet("QCheckBox::indicator:unchecked"
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
        self.select1=QCheckBox("select1")
        self.select1.setStyleSheet("QCheckBox::indicator:unchecked"
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
        self.select2=QCheckBox("select2")
        self.select2.setStyleSheet("QCheckBox::indicator:unchecked"
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

        self.check_o=QCheckBox("OUTPUT")
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
        self.select1.stateChanged.connect(self.onchecking1)
        self.select2.stateChanged.connect(self.onchecking2)
        

        mainLayout.addWidget(self.check1,348,0)

        mainLayout.addWidget(self.check2,349,0)

        mainLayout.addWidget(self.check3,350,0)
        mainLayout.addWidget(self.check4,351,0)

        mainLayout.addWidget(self.select1,700,350)

        mainLayout.addWidget(self.select2,700,351)
      
        mainLayout.addWidget(self.check_o,350,700)

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
        if not Qt.Checked==checked and not self.select2.isChecked() and self.check1.isChecked():
            
            self.check_o.setChecked(True)
        
        elif not Qt.Checked==checked and self.select2.isChecked() and self.check2.isChecked():
            
            self.check_o.setChecked(True)
           
             
        elif  Qt.Checked==checked and not self.select2.isChecked() and self.check3.isChecked():
            
            self.check_o.setChecked(True)
            
                
        elif Qt.Checked==checked and self.select2.isChecked() and self.check4.isChecked():
          
            self.check_o.setChecked(True)
        else:
            self.check_o.setChecked(False)   

           
    def onchecking2(self,checked):
        if not Qt.Checked==checked and not self.select2.isChecked() and self.check1.isChecked():
            
            self.check_o.setChecked(True)
        
        elif not Qt.Checked==checked and self.select2.isChecked() and self.check3.isChecked():
            
            self.check_o.setChecked(True)
           
             
        elif  Qt.Checked==checked and not self.select2.isChecked() and self.check2.isChecked():
            
            self.check_o.setChecked(True)
            
                
        elif Qt.Checked==checked and self.select2.isChecked() and self.check4.isChecked():
          
            self.check_o.setChecked(True)
        else:
            self.check_o.setChecked(False)
              
                

app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())


