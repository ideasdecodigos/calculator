
from PySide6.QtWidgets import QMessageBox,QMainWindow
from model import time, temperature, length , standard
# import model 
from model.temperature import Temperature

class Modules(QMainWindow):
    def __init__(self):
        super().__init__(self)
        
        # self.time = None
        # self.length = None
        #Sindows Objects 
        self.temperature = None
        
    def open_temperature(self):
        if self.temperature is None:
            self.temperature =Temperature()
            self.temperature.show()
        else:
            self.temperature.hide()
    
    def openTimeCalculator(self):
        # if self.time is None:
        self.time =time.Time(self)
        self.time.show()
            
    def openLengthCalculator(self):
            self.length=length.Length(self)
            self.length.show()
            
    def openTemperatureCalculator(self):
        self.temp =temperature.Temperature()
        self.temp.show()
        self.close()
        
    def openStandardCalculator(self):
        self.standard =standard.Standard(self)
        self.standard.show()
        self.close()
                
    def about(self):
        QMessageBox.information(self,'Info','This is a collaction of calculators v1.0.0\nDeveloped by IDCSchools \n \napr 01, 2022')
        
    def setDot(display):
        txt = str(display.text())
        if '.' not in txt:
                display.setText(txt + '.')
            
    def delDecimal(numFloat):
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
    

        