import sys,os
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QGridLayout,QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
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
        self.setStyleSheet(
      "QWidget"
        "{"
            
            "background-color:rgb(231, 187, 225)"
        "}"
        )
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\Anshu\\Desktop\\log.png"))
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
            "width:40px;"
            "height:40px;"            
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
        self.check1.stateChanged.connect(self.onchecking)

        mainLayout.addWidget(self.check1,350,0)
      
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
    def onchecking(self,checked):
            if Qt.Checked==checked:
                self.check_o.setChecked(False)
        
            else:
                self.check_o.setChecked(True)           

app=QApplication(sys.argv)
demo=AppDemo()
demo.show()
sys.exit(app.exec_())


