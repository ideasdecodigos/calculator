from PySide6.QtWidgets import  QMainWindow, QMessageBox
from views.properties import Ui_Properties
from configparser import ConfigParser
from pathlib import Path

class Properties(QMainWindow):    
    def __init__(self):
        super(Properties,self).__init__()
        self.ui=Ui_Properties()
        self.ui.setupUi(self)
        #config file path
        self.configFilePath ='src/files/db.ini'
        
        
        self.ui.pushButtonReset.clicked.connect(self.resetProperties)
        self.ui.pushButtonSave.clicked.connect(self.changeProperties)     
        self.iniPropertiesInputs()
        
    def createProperties(self):
        self.config = ConfigParser()
        self.config['properties'] = {
            'bgColor':'none',
            'ftColor':'Black',
            'decimalsLen':'4'
        }
        with open(self.configFilePath, 'w') as conf:
            self.config.write(conf)
            QMessageBox.information(self,'Info', 'Config file created successfully!', QMessageBox.Ok)
    
    def createSession(self):
        self.config.add_section('properties')
        self.config.set('properties', 'bgColor', 'none')
        self.config.set('properties', 'ftColor', 'Black')
        self.config.set('properties', 'decimalsLen', '4')
        QMessageBox.warning(self,'Warning', 'The session was not created, please try again!', QMessageBox.Ok)
            
    def resetProperties(self):
        self.config = ConfigParser()
        
        if Path(self.configFilePath).exists():
            self.config.read(self.configFilePath)
            if self.config.has_section('properties'):
                try:
                    self.config['properties']['bgColor'] = 'none'
                    self.config['properties']['ftColor'] = 'black'
                    self.config['properties']['decimalsLen'] = '4'
                    with open(self.configFilePath, 'w') as conf:
                        self.config.write(conf)
                        QMessageBox.information(self,'Info', 'Reseted successfully', QMessageBox.Ok)                  
                except:
                    QMessageBox.warning(self,'Warning', 'An error occurred!', QMessageBox.Ok) 
            else:
                QMessageBox.warning(self,'Warning', 'Section not found!', QMessageBox.Ok)             
        else:
            QMessageBox.warning(self,'Warning', 'File not found', QMessageBox.Ok) 
        
    def changeProperties(self):
        self.config = ConfigParser()
        
        if Path(self.configFilePath).exists():
            self.config.read(self.configFilePath)
            if self.config.has_section('properties'):
                try:
                    self.config['properties']['bgColor'] = self.ui.comboBoxBgColor.currentText()
                    self.config['properties']['ftColor'] = self.ui.comboBoxFtColor.currentText()
                    self.config['properties']['decimalsLen'] =str(self.ui.spinBoxDecimal.value()) 
                    with open(self.configFilePath, 'w') as conf:
                        self.config.write(conf)
                        QMessageBox.information(self,'Info', 'Restart the app to see the changes!', QMessageBox.Ok)                  
                except:
                    QMessageBox.warning(self,'Warning', 'An error occurred!', QMessageBox.Ok) 
            else:
                self.createSession()             
        else:
            self.createProperties()

    def newProperties(self):
        self.config = ConfigParser()     
        
        if Path('src/files/db.ini').exists():
            self.config.read('src/files/db.ini')
            if self.config.has_section('properties'):
                try:                    
                    bgColor =  self.config['properties']['bgColor'] 
                    ftColor = self.config['properties']['ftColor'] 
                    dcLen = self.config['properties']['decimalsLen']
                    style = "background:{0};color:{1};"
                    style = style.format(bgColor, ftColor)
                    self.setStyleSheet("QWidget{"+ style +"}")
                except:                    
                    QMessageBox.warning(self,'Warning', 'The styles were not applied, please try again!', QMessageBox.Ok)
            else:
                self.createSession()
        else:
            self.createProperties()

    def iniPropertiesInputs(self):
        self.config = ConfigParser()     
        
        if Path('src/files/db.ini').exists():
            self.config.read('src/files/db.ini')
            if self.config.has_section('properties'):
                try:                    
                    self.ui.comboBoxBgColor.setCurrentText(self.config['properties']['bgColor'])
                    self.ui.comboBoxFtColor.setCurrentText(self.config['properties']['ftColor'])
                    self.ui.spinBoxDecimal.setValue(self.config['properties']['decimalsLen'])
                except:                    
                    pass

