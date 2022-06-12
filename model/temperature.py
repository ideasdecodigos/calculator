
from http.client import SEE_OTHER
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.temperature import Ui_Temperature
from model import time, length,  properties, standard

class Temperature(QMainWindow):    
    def __init__(self):
        super(Temperature,self).__init__()
        self.ui = Ui_Temperature()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/temp.png"))
        self.ui.btn_del_one.setIcon(QIcon("src/imgs/delete.png"))
        
        properties.Properties.newProperties(self) 
        
        #*******BUTTON'S ACTIONS        
        self.ui.btn1.clicked.connect(lambda:self.getBtnText(self.ui.btn1))
        self.ui.btn2.clicked.connect(lambda:self.getBtnText(self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda:self.getBtnText(self.ui.btn3))
        self.ui.btn4.clicked.connect(lambda:self.getBtnText(self.ui.btn4))
        self.ui.btn5.clicked.connect(lambda:self.getBtnText(self.ui.btn5))
        self.ui.btn6.clicked.connect(lambda:self.getBtnText(self.ui.btn6))
        self.ui.btn7.clicked.connect(lambda:self.getBtnText(self.ui.btn7))
        self.ui.btn8.clicked.connect(lambda:self.getBtnText(self.ui.btn8))
        self.ui.btn9.clicked.connect(lambda:self.getBtnText(self.ui.btn9))
        self.ui.btn0.clicked.connect(lambda:self.getBtnText(self.ui.btn0))
        self.ui.btn_dot.clicked.connect(lambda:self.setDot(self.ui.label_text))
        self.ui.btn_del_one.clicked.connect(self.deleteOne)
        self.ui.btn_clear.clicked.connect(self.deleteAll)
        self.ui.comboBox1.currentIndexChanged.connect(self.calculate)
        self.ui.comboBox2.currentIndexChanged.connect(self.calculate)
        self.ui.btn_inverse.clicked.connect(self.inverseText)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionLenght.triggered.connect(self.open_length)
        self.ui.actionTime.triggered.connect(self.open_time)
        self.ui.actionProperties.triggered.connect(self.open_properties)
        self.ui.actionStandard.triggered.connect(self.open_standard)
        self.calculate()
        #Sindows Objects 
        self.temperature = None
        self.time = None
        self.length = None
        self.properties = properties.Properties()
        
    #****Open window functions
    def open_properties(self):
        if self.properties.isVisible():           
            self.properties.setHidden(True)
        else:
            self.properties.setVisible(True)
            
    def open_standard(self):
        if self.temperature is None:
            self.temperature = standard.Standard()
            self.temperature.show()
            self.close()
        else:
            self.temperature.close()
        
    def open_time(self):
        if self.time is None:
            self.time = time.Time()
            self.time.show()
            self.close()
        else:
            self.time.close()
        
    def open_length(self):
        if self.length is None:
            self.length = length.Length()
            self.length.show()
            self.close()
        else:
            self.length.close()      
            
    def about(self):
        QMessageBox.information(self,'Info','This is a collaction of calculators v1.0.0\nDeveloped by IDCSchools \n \napr 01, 2022')

    #****FUNCTIONS CREATION    
    def getBtnText(self, btn):
        """
        get the buttons text and set it to labelOne
        
        """
        txt = ''        
        if self.ui.label_text.text() != '0':
            txt = self.ui.label_text.text()
        if len(txt) <= 16:
            txt += btn.text()
            self.ui.label_text.setText(txt)            
        self.calculate() 
        
   
    def inverseText(self):
        txt = float(self.ui.label_text.text())
        txt *= -1
        txt = str(txt)
        if txt.endswith('.0'):
            lessOne = len(txt)
            lessOne -= 2
            txt = txt[:lessOne]
        self.ui.label_text.setText(txt)
        self.calculate()
        
    def deleteOne(self):
        txt = str(self.ui.label_text.text())
        lessOne = len(txt)
        lessOne -= 1
        txt = txt[:lessOne]        
        self.ui.label_text.setText(txt)
        if len(txt) == 0 or txt == '-':
            self.ui.label_text.setText('0')
        self.calculate()
        
    def deleteAll(self):
        self.ui.label_text.setText('0')
        self.calculate()

    def calculate(self):
        val = float(self.ui.label_text.text())
        firstTemp = self.ui.comboBox1.currentText()
        secondTemp = self.ui.comboBox2.currentText()    
        
        if firstTemp == secondTemp:
            self.ui.label_result.setText(str(val))
            
            #°F = 1.8 °C + 32°
        elif ((firstTemp == 'Celsius') and (secondTemp == 'Fahrenheit')):
            
            temp = 1.8 * val + 32
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))
            
            #K = °C + 273°
        elif ((firstTemp == 'Celsius') and (secondTemp == 'Kelvin')):
            temp = val + 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))
            
            #K = 5/9 (ºF – 32) + 273.15
        elif ((firstTemp == 'Fahrenheit') and (secondTemp == 'Kelvin')):
            temp = 5/9 * (val - 32) + 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))
            
            #°C =5/9(°F-32°)
        elif ((firstTemp == 'Fahrenheit') and (secondTemp == 'Celsius')):
            temp = 5/9 * (val - 32)
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))         
            
            #°C = K - 273°
        elif ((firstTemp == 'Kelvin') and (secondTemp == 'Celsius')):
            temp = val - 273.15
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))
            
            #ºF = 1.8(K – 273.15) + 32.
        elif ((firstTemp == 'Kelvin') and (secondTemp == 'Fahrenheit')):
            temp = 1.8 * (val - 273.15) + 32
            temp = round(temp, 4)
            self.ui.label_result.setText(self.delDecimal(temp))
            
            
    def delDecimal(self, numFloat):
        """
        Delete Decimals equal to '.0' and return an integer number
        for example:
        >>> delDecimal(489.000)
        489
        
        If module is mayor than '.00' or '.0' then it will return a float number
        >>> delDecimal(590.902)
        590.902
        
        """
        txt = str(numFloat)
        if txt.endswith('.0'):
            lessOne = len(txt)
            lessOne -= 2
            txt = txt[:lessOne] 
        return txt
