from math import *
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QMessageBox
from views.standard import Ui_Standard
from model import temperature, time, length, properties


class Standard(QMainWindow):    
    def __init__(self):
        super(Standard,self).__init__()
        self.ui = Ui_Standard()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/imgs/standard.png"))
        self.ui.btn_del_historial.setIcon(QIcon("src/imgs/trash.png"))
        self.ui.btn_show.setIcon(QIcon("src/imgs/history.png"))
        self.ui.btn_del_one.setIcon(QIcon("src/imgs/delete.png"))
        # self.ui.label_mr.wordWrap= True
        # self.ui.label_result.wordWrap= True
        # self.ui.label_result.setMaximumWidth(400)
        
        
        
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
        self.ui.btn_e.clicked.connect(self.setE)
        self.ui.btn_rightp.clicked.connect(self.setRightParenthesis)
        self.ui.btn_plus.clicked.connect(lambda:self.getBtnText(self.ui.btn_plus))
        self.ui.btn_minus.clicked.connect(lambda:self.getBtnText(self.ui.btn_minus))
        self.ui.btn_mult.clicked.connect(lambda:self.getBtnText(self.ui.btn_mult))
        self.ui.btn_divide.clicked.connect(lambda:self.getBtnText(self.ui.btn_divide))
        self.ui.btn_percent.clicked.connect(self.setPercent)
        self.ui.btn_dot.clicked.connect(self.setDot)
        self.ui.btn_del_one.clicked.connect(self.delOne)
        self.ui.btn_equal.clicked.connect(self.equals)
        self.ui.btn_clear.clicked.connect(self.clearC)
        self.ui.btn_inverse.clicked.connect(self.inverseInput)
        self.ui.actionExit.triggered.connect(self.close)
        #General Butons
        self.ui.actionProperties.triggered.connect(self.open_properties)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionLenght.triggered.connect(self.open_length)
        self.ui.actionTime.triggered.connect(self.open_time)
        self.ui.actionTemperature.triggered.connect(self.open_temperature)
        self.ui.btn_show.clicked.connect(self.showHideHistorial)
        self.ui.btn_del_historial.clicked.connect(self.ui.list_memory.clear)
        self.ui.btn_sqrt.clicked.connect(self.setSqrt)
        
        #Globals variables
        self.input= ''
        self.operatorsList= ['+','-','*','/']
        self.expressionsList = {'sqrt':sqrt, 'pow':pow, 'sin':sin, 'cos':cos, 'tan':tan, 'e':e, 'percent': 100}
        self.restrinctionsList = [')','(','+','-','*','/','%','^']
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
        
    def open_length(self):
        if self.length is None:
            self.length = length.Length()
            self.length.show()
            self.close()
        else:
            self.length.close()
        
    def about(self):
        QMessageBox.information(self,'Info','This is a collaction of calculators v1.0.0\nDeveloped by IDCSchools \n \napr 01, 2022')

    

    #Control functions    
        
    def getBtnText(self, btn):
        """
        Get the buttons input and display it in the self.ui.label_mr
        
        """
        if btn.text() in self.operatorsList:
            self.input = ''
                
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.clear()
            
        if self.ui.label_mr.text() == '' and self.ui.label_result.text() != '' and btn.text() in self.operatorsList:  
            self.ui.label_mr.setText(self.ui.label_result.text())
            
        self.ui.label_mr.setText(self.ui.label_mr.text() + btn.text())
        
        if self.ui.label_mr.text() in self.operatorsList:
            self.ui.label_mr.setText('0')
        if btn.text() not in self.operatorsList:
            self.input += btn.text()
        self.getResult(btn.text())
        
    def equals(self):   
        """
        Show and save in historial the input result, and reset the values
        
        this function works along to eval and cleanInput functions
        
        """
        txt = self.cleanInput()     
        #show up the result
        if txt != '' and (txt[-1:] not in self.operatorsList) and (txt != self.input) and (txt.count('(') == txt.count(')')):
            try:
                result = eval(txt,self.expressionsList)
                if result % 2 == 0:
                    result = int(result)
                
                self.ui.label_result.setText(str(result))
                self.ui.list_memory.addItem(txt +  ' = ' + str(result))
                self.input = ''
                self.ui.label_mr.setText('')
            except:
                self.ui.label_mr.setStyleSheet('color:red')
        elif txt.isdigit():
            self.ui.label_result.setText(txt)
            self.input = ''
            self.ui.label_mr.setText('')
            
    def getResult(self, symbl):
        """
        Show the input result every time a button like +, -, * or / is pressed
        
        """
        txt = self.ui.label_mr.text()
        self.ui.label_mr.setStyleSheet('color:black;')
        try:
            if (symbl in txt) and (txt[-1:] not in self.operatorsList) and (txt != self.input) and (txt.count('(') == txt.count(')') and ('%' not in txt)):            
                
                result = eval(txt,self.expressionsList)
                if result % 2 == 0:
                    result = int(result)
                
                self.ui.label_result.setText(str(result))
                # self.ui.list_memory.addItem(txt +  ' = ' + str(result))
            else:
                self.ui.label_result.clear() 
        except:
            self.ui.label_mr.setStyleSheet('color:red;')   
            
    def inverseInput(self): 
        """
        Change the input to negative if it is positive and vice versa
        examples:
        1- if label = '25+30' then label = '25+(-30)' and vice versa
        2- if label = '' then label = (- and vice versa
        2- if label = '4893' then label = '(-4893' and vice versa        
        2- if label = '4893/234*422-423' then label = '4893/234*422-(-423' and vice versa        
        
        """       
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.clear()
        txt =  self.ui.label_mr.text() 
        cutlen = txt.rfind(self.input)
        firstPart = txt[:cutlen]
        secondPart = txt[cutlen:]
        newTxt = firstPart + '(-' + secondPart
        subSecondPart = '(-' + secondPart
        
        if txt == '(-':
            self.ui.label_mr.setText('0')  
        elif txt == '' and self.input == '':
            self.ui.label_mr.setText(txt + '(-')
        elif txt[-1:] not in self.operatorsList and self.input != '' and txt[cutlen-2:] != subSecondPart:
            self.ui.label_mr.setText(newTxt)
        elif txt[cutlen-2:] == subSecondPart:
            self.ui.label_mr.setText(firstPart[:-2] + secondPart)
    
    def setSqrt(self):
        """
        Add '√(' to the label to get the sqrl of the input
        examples:
        1- if the label = '' then add '√(' and vice versa
        1- if the label = '3483984' then add '3483984*√(' and vice versa
        
        """
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.clear()
        txt = self.ui.label_mr.text()
            
        if  txt[-2:] == '√(':
            pass
        elif txt[-1:] in self.operatorsList or txt == '':
            self.ui.label_mr.setText(txt + '√(')
        elif  txt[-2:] != '*√(':
            self.ui.label_mr.setText(txt + '*√(')
    
    def setE(self):
        """
        Represent the const e in the equation
        Example:
        if input = '5*e' in the eval function this it will be equal to: 5*2.718281828459045 = 13.591409142295226176801437356763
        
        """
        txt = self.ui.label_mr.text()
        if txt == '0':
            self.ui.label_mr.clear()
            
        if txt[-1:] in self.operatorsList or txt() == '':
            self.ui.label_mr.setText(txt + 'e')
        else:
            self.ui.label_mr.setText(txt + '*(e')
            
    def setPercent(self):     
        """
        Represent the percent in the equation
        Exmaple:
        if input = '80%10' in the eval fuction this it will be equal to: 80/100*10 = 0.8
        
        """
        txt = self.ui.label_mr.text()      
            
        if txt[-1:] not in self.restrinctionsList and '%' not in txt and txt != '0' and self.input != '':
            self.ui.label_mr.setText(self.ui.label_mr.text() + '%')
            
    def setLeftParenthesis(self):
        """
        Open a parethesis
        1-Example:
        if input = '' then input it will be equal to: '('
        
        2-Example:
        if input = '5453' then input it will be equal to: '5453*('
        
        3-Example:
        if input = '5453+' then input it will be equal to: '5453+('        
        
        """
        txt = self.ui.label_mr.text()         
        if txt == '0':
            self.ui.label_mr.setText('(')
        elif txt[-1:] not in self.operatorsList and txt[-1:] != '(':
            self.ui.label_mr.setText(txt + '*(')
        else:
            self.ui.label_mr.setText(txt +'(')
    
    def setRightParenthesis(self):
        """
        Open and close parenthesis
        this function works along with the setLeftParenthesis() function
        and it will close as much parenthesis as be necesary
        
        1-Example:
        if input = '' then input it will be equal to: '('
        
        2-Example:
        if input = '5453' then input it will be equal to: '5453*('
        
        3-Example:
        if input = '5453+' then input it will be equal to: '5453+('        
        
        """
        txt= self.ui.label_mr.text()
        if txt[-1:] =='(':
            self.ui.label_mr.setText(txt +'(')
        elif txt[-1:] not in self.operatorsList and txt.count('(') > txt.count(')'):
            self.ui.label_mr.setText(txt +')')
        else:
            self.setLeftParenthesis()
        
    def cleanInput(self): 
        """
        It format the input to avoit error in eval function
        
        it skip +, -, *, /, (, and ) at the beginning and at the end of the input
        
        return a correct formatted string to the eval function
        
        """        
        self.ui.label_mr.setStyleSheet('color:black;')       
        txt = self.ui.label_mr.text()
        
        #remove symbols at the end
        while txt[-1:] in self.operatorsList:
            txt = txt[:-1]
            self.ui.label_mr.setText(txt)
                
        #remove symbols at the beginning
        while txt[:1] in self.operatorsList and txt[:1] != '+' and txt[:1] != '-':
            txt = txt[1:]
            self.ui.label_mr.setText(txt)
        
        #add parethesis at the end if it need it
        while txt.count('(') > txt.count(')'):
            txt += ')'            
            self.ui.label_mr.setText(txt)
            
        txt = txt.replace('%', '/percent*')
        txt = txt.replace('√', 'sqrt')            
            
        return txt
        
    def clearC(self):
        """
        Reset all as defualt
        
        """
        self.ui.label_result.clear()
        self.ui.label_mr.setText('0')        
        self.input = ''

    def showHideHistorial(self):
        """
        Switch between contorls and historial display
        
        """
        if self.ui.stackedWidget.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
    
    def delOne(self):  
        """
        Remove the last character on the input string
        
        """
        if self.ui.label_mr.text() != '':      
            strln2 = len(self.ui.label_mr.text()) - 1            
            self.ui.label_mr.setText(self.ui.label_mr.text()[:strln2])
        if self.ui.label_mr.text() == '':
            self.ui.label_mr.setText('0')
        self.ui.label_result.clear()
            
    def setDot(self):
        """
        Add a dot in the current input only if the input is a integer, else, then skip it
        
        """
        if self.input != '' and '.' not in self.input:
            self.input += '.'
            self.ui.label_mr.setText(self.ui.label_mr.text() + '.')
    
