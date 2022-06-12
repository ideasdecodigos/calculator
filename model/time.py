
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.time import Ui_Time
from model import length, standard, temperature, properties
from PySide6.QtGui import QIcon

class Time(QMainWindow):    
    def __init__(self):
        super(Time,self).__init__()
        self.ui = Ui_Time()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/time.png"))
        self.ui.btn_del_one.setIcon(QIcon("src/imgs/delete.png"))
        
        properties.Properties.newProperties(self)       
    
        
        #DICTIONARIES CREATION    
        self.microseconds={
            'Microseconds':1,
            'Milliseconds':1000,
            'Seconds':0.00001,
            'Minutes':0.000000016666667,
            'Hours':0.000000000277778,
            'Days':0.000000000011574,
            'Weeks':0.000000000001653,
            'Years':0.000000000000032
        }
    
        self.milliseconds={
            'Microseconds':1000,
            'Milliseconds':1,
            'Seconds':0.001,
            'Minutes':0.000017,
            'Hours':0.000000277777778,
            'Days':0.000000011574074,
            'Weeks':0.000000001653439,
            'Years':0.0000000000031688
        }
    
        self.seconds={
            'Microseconds':1000000,
            'Milliseconds':1000,
            'Seconds':1,
            'Minutes':0.016667,
            'Hours':0.000278,
            'Days':0.000012,
            'Weeks':0.000002,
            'Years':0.000000031688088
        }
    
        self.minutes={
            'Microseconds':60000000,
            'Milliseconds':60000,
            'Seconds':60,
            'Minutes':1,
            'Hours':0.016667,
            'Days':0.000694,
            'Weeks':0.000099,
            'Years':0.000002
        }
        
        self.hours= {
            'Microseconds':3600000000,
            'Milliseconds':3600000,
            'Seconds':3600,
            'Minutes':60,
            'Hours':1,
            'Days':0.041667,
            'Weeks':0.005952,
            'Years':0.000114
        }

        self.days={
            'Microseconds':86400000000,
            'Milliseconds':86400000,
            'Seconds':86400,
            'Minutes':1440,
            'Hours':24,
            'Days':1,
            'Weeks':0.142857,
            'Years':0.002738
        }
    
        self.weeks={
            'Microseconds':604800000000,
            'Milliseconds':604800000,
            'Seconds':604800,
            'Minutes':10080,
            'Hours':168,
            'Days':7,
            'Weeks':1,
            'Years':0.019165
        }
    
        self.years={
            'Microseconds':31557600000000,
            'Milliseconds':31557600000,
            'Seconds':31557600,
            'Minutes':525960,
            'Hours':8766,
            'Days':365.25,
            'Weeks':52.17857,
            'Years':1
        }
    
        
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
        self.ui.btn_dot.clicked.connect(self.setDot)
        self.ui.btn_del_one.clicked.connect(self.deleteOne)
        self.ui.btn_clear.clicked.connect(self.deleteAll)
        self.ui.comboBox1.currentIndexChanged.connect(self.calculate)
        self.ui.comboBox2.currentIndexChanged.connect(self.calculate)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionStandard.triggered.connect(self.open_standard)
        self.ui.actionTemperature.triggered.connect(self.open_temperature)
        self.ui.actionProperties.triggered.connect(self.open_properties)
        self.ui.actionLenght.triggered.connect(self.open_length)
        self.ui.actionExit.triggered.connect(self.destroy)
        self.calculate()
        #Sindows Objects 
        self.temperature = None
        self.standard = None
        self.length = None
        self.properties = properties.Properties()
        
    #****Open window functions
    def open_properties(self):
        if self.properties.isVisible():           
            self.properties.setHidden(True)
        else:
            self.properties.setVisible(True)
            
    def open_temperature(self):
        if self.temperature is None:
            self.temperature = temperature.Temperature()
            self.temperature.show()
            self.close()
        else:
            self.temperature.close()
        
    def open_standard(self):
        if self.standard is None:
            self.standard = standard.Standard()
            self.standard.show()
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
        
    def setDot(self):
        txt = str(self.ui.label_text.text())
        if '.' not in txt:
                self.ui.label_text.setText(txt + '.')

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
        label1 = float(self.ui.label_text.text())
        cbox2 = self.ui.comboBox2.currentText()
        cbox1 = self.ui.comboBox1.currentText()
        if cbox1 == cbox2:
            self.val = label1
        elif cbox1 == 'Microseconds':
            self.val = label1 * self.microseconds[cbox2]
        elif cbox1 == 'Milliseconds':
            self.val = label1 * self.milliseconds[cbox2]
        elif cbox1 == 'Seconds':
            self.val = label1 * self.seconds[cbox2]
        elif cbox1 == 'Minutes':
            self.val = label1 * self.minutes[cbox2]
        elif cbox1 == 'Hours':
            self.val = label1 * self.hours[cbox2]
        elif cbox1 == 'Days':
            self.val = label1 * self.days[cbox2]
        elif cbox1 == 'Weeks':
            self.val = label1 * self.weeks[cbox2]
        elif cbox1 == 'Years':
            self.val = label1 * self.years[cbox2]
        
        self.ui.label_result.setText(str(self.val))
            
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

