
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.length import Ui_Length
from PySide6.QtGui import QIcon
from model import temperature, standard, time, properties

class Length(QMainWindow):    
    def __init__(self):
        super(Length,self).__init__()
        self.ui = Ui_Length()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/standard.png"))
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
        self.ui.btn_dot.clicked.connect(self.setDot)
        self.ui.btn_del_one.clicked.connect(self.deleteOne)
        self.ui.btn_clear.clicked.connect(self.deleteAll)
        self.ui.comboBox1.currentIndexChanged.connect(self.calculate)
        self.ui.comboBox2.currentIndexChanged.connect(self.calculate)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionStandard.triggered.connect(self.open_standard)
        self.ui.actionTemperature.triggered.connect(self.open_temperature)
        self.ui.actionProperties.triggered.connect(self.open_properties)
        self.ui.actionLenght.triggered.connect(self.open_time)
        self.ui.actionExit.triggered.connect(self.close)
        self.calculate()
        
        #create values list
        self.nanometers = {
            'Nanometers': 1,
            'Microns': 0.001,
            'Millimeters': 0.000001,
            'Centimeters': 0.0000001,
            'Meters': 0.000000001,
            'Kilometers': 0.000000000001,
            'Inches': 0.000000039370079,
            'Feet': 0.00000000328084,
            'Yards': 0.000000001093613,
            'Miles': 0.000000000000621,
            'Nautical Miles': 0.00000000000054,
        }
        
        self.microns = {
            'Nanometers': 1000,
            'Microns': 1,
            'Millimeters': 0.001,
            'Centimeters': 0.0001,
            'Meters': 0.000001,
            'Kilometers': 0.000000001,
            'Inches': 0.000039,
            'Feet': 0.000003,
            'Yards': 0.000001,
            'Miles': 0.000000000621371,
            'Nautical Miles': 0.000000000539957,
        }
        
        self.millimeters = {
            'Nanometers': 1000000,
            'Microns': 1000,
            'Millimeters': 1,
            'Centimeters': 0.1,
            'Meters': 0.001,
            'Kilometers': 0.000001,
            'Inches': 0.03937,
            'Feet': 0.003281,
            'Yards': 0.001094,
            'Miles': 0.000000621371192,
            'Nautical Miles': 0.000000539956803,
        }
        
        self.centimeters = {
            'Nanometers': 10000000,
            'Microns': 10000,
            'Millimeters': 10,
            'Centimeters': 1,
            'Meters': 0.01,
            'Kilometers': 0.00001,
            'Inches': 0.393701,
            'Feet': 0.032808,
            'Yards': 0.010936,
            'Miles': 0.000006,
            'Nautical Miles': 0.000005,
        }
        
        self.meters = {
            'Nanometers': 1000000000,
            'Microns': 1000000,
            'Millimeters': 1000,
            'Centimeters': 100,
            'Meters': 1,
            'Kilometers': 0.001,
            'Inches': 39.37008,
            'Feet': 3.28084,
            'Yards': 1.093613,
            'Miles': 0.000621,
            'Nautical Miles': 0.00054,
        }
        
        self.kilomenters = {
            'Nanometers': 1000000000000,
            'Microns': 1000000000,
            'Millimeters': 1000000,
            'Centimeters': 100000,
            'Meters': 1000,
            'Kilometers': 1,
            'Inches': 39370.08,
            'Feet': 3280.84,
            'Yards': 1093.613,
            'Miles': 0.621371,
            'Nautical Miles': 0.539957,
        }
        
        self.inches = {
            'Nanometers': 25400000,
            'Microns': 25400,
            'Millimeters': 25.4,
            'Centimeters': 2.54,
            'Meters': 0.0254,
            'Kilometers': 0.000025,
            'Inches': 1,
            'Feet': 0.083333,
            'Yards': 0.027778,
            'Miles': 0.000016,
            'Nautical Miles': 0.000014,
        }
        
        self.feet = {
            'Nanometers': 304800000,
            'Microns': 304800,
            'Millimeters': 304.8,
            'Centimeters': 30.48,
            'Meters': 0.3048,
            'Kilometers': 0.000305,
            'Inches': 12,
            'Feet': 1,
            'Yards': 0.333333,
            'Miles': 0.000189,
            'Nautical Miles': 0.000165,
        }
        
        self.yards = {
            'Nanometers': 914400000,
            'Microns': 9144000,
            'Millimeters': 914.4,
            'Centimeters': 91.44,
            'Meters': 0.9144,
            'Kilometers': 0.000914,
            'Inches': 36,
            'Feet': 3,
            'Yards': 1,
            'Miles': 0.000568,
            'Nautical Miles': 0.000494,
        }
        
        self.miles = {
            'Nanometers': 1609344000000,
            'Microns': 1609344000,
            'Millimeters': 1609344,
            'Centimeters': 160934.4,
            'Meters': 1609.344,
            'Kilometers': 1.609344,
            'Inches': 63360,
            'Feet': 5280,
            'Yards': 1760,
            'Miles': 1,
            'Nautical Miles': 0.868976,
        }
        
        self.nauticalMiles = {
            'Nanometers': 1852000000000,
            'Microns': 1852000000,
            'Millimeters': 1852000,
            'Centimeters': 185200,
            'Meters': 1852,
            'Kilometers': 1.852,
            'Inches': 72913.39,
            'Feet': 6076.115,
            'Yards': 2025.372,
            'Miles': 1.150779,
            'Nautical Miles': 1,
        }
        
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
        
    def open_time(self):
        if self.time is None:
            self.time = time.Time()
            self.time.show()
            self.close()
        else:
            self.time.close()
        
    def open_standard(self):
        if self.standard is None:
            self.standard = standard.Standard()
            self.standard.show()
            self.close()
        else:
            self.standard.close()
        
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
        input = float(self.ui.label_text.text())
        cbox2 = self.ui.comboBox2.currentText()
        cbox1 = self.ui.comboBox1.currentText()
        if cbox1 == cbox2:
            self.val = input
        elif cbox1 == 'Nanometers':
            self.val = input * self.nanometers[cbox2]
        elif cbox1 == 'Microns':
            self.val = input * self.microns[cbox2]
        elif cbox1 == 'Millimeters':
            self.val = input * self.millimeters[cbox2]
        elif cbox1 == 'Centimeters':
            self.val = input * self.centimeters[cbox2]
        elif cbox1 == 'Meters':
            self.val = input * self.meters[cbox2]
        elif cbox1 == 'Kilometers':
            self.val = input * self.kilomenters[cbox2]
        elif cbox1 == 'Inches':
            self.val = input * self.inches[cbox2]
        elif cbox1 == 'Feet':
            self.val = input * self.feet[cbox2]
        elif cbox1 == 'Yards':
            self.val = input * self.yards[cbox2]
        elif cbox1 == 'Miles':
            self.val = input * self.miles[cbox2]        
        elif cbox1 == 'Nautical Miles':
            self.val = input * self.nauticalMiles[cbox2]
            
        if self.val % 2 == 0: 
            self.val = int(self.val)
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
