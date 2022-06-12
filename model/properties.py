from PySide6.QtWidgets import  QMainWindow, QMessageBox, QColorDialog, QFontDialog
from views.properties import Ui_Properties
from configparser import ConfigParser
from pathlib import Path

class Properties(QMainWindow):    
    def __init__(self):
        super(Properties,self).__init__()
        self.ui=Ui_Properties()
        self.ui.setupUi(self)
        #config file path
        self.configFilePath ='src/files/config.ini'        
        
        self.ui.pushButtonReset.clicked.connect(self.resetProperties)
        self.ui.pushButtonSave.clicked.connect(self.changeProperties)     
        self.ui.btnBgColor.clicked.connect(self.bgColor)     
        self.ui.btnFrColor.clicked.connect(self.frColor)     
        self.ui.btnFont.clicked.connect(self.setFont)     
        self.iniPropertiesInputs()
        self.iniLangOutputs()
        
    def createProperties(self):
        self.config = ConfigParser()
        self.config['properties'] = {
            'bgColor':'none',
            'ftColor':'Black',
            'decimalsLen':'4',
            'ftFont':'<PySide6.QtGui.QFont(Roboto Slab Light,12,-1,5,300,0,0,0,0,0,0,0,0,0,0,1,Regular) at 0x000002865309E680>'
        }
        self.config['lang_outputs'] = {
            'lang':'0',
            'rate':'150'
        }
        with open(self.configFilePath, 'w') as conf:
            self.config.write(conf)
            QMessageBox.information(self,'Info', 'Config file created successfully!', QMessageBox.Ok)
    
    def createSession(self):
        self.config.add_section('properties')
        self.config.set('properties', 'bgColor', 'none')
        self.config.set('properties', 'ftColor', 'Black')
        self.config.set('properties', 'decimalsLen', '4')
        self.config.set('properties', 'ftFont', '<PySide6.QtGui.QFont(Roboto Slab Light,12,-1,5,300,0,0,0,0,0,0,0,0,0,0,1,Regular) at 0x000002865309E680>')
        
        self.config.add_section('lang_outputs')
        self.config.set('lang_outputs', 'lang', '0')
        self.config.set('lang_outputs', 'rate', '150')
        QMessageBox.warning(self,'Warning', 'The session was not created, please try again!', QMessageBox.Ok)
            
    def resetProperties(self):
        self.config = ConfigParser()
        
        if Path(self.configFilePath).exists():
            self.config.read(self.configFilePath)
            if self.config.has_section('properties') and self.config.has_section('properties'):
                try:
                    self.config['properties']['bgColor'] = 'none'
                    self.config['properties']['ftColor'] = 'black'
                    self.config['properties']['decimalsLen'] = '4'
                    self.config['properties']['ftFont'] = '<PySide6.QtGui.QFont(Roboto Slab Light,12,-1,5,300,0,0,0,0,0,0,0,0,0,0,1,Regular) at 0x000002865309E680>'
                    
                    self.config['lang_outputs']['lang'] = '0'
                    self.config['lang_outputs']['rate'] = '150'
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
            if self.config.has_section('properties') and self.config.has_section('lang_outputs'):
                try:
                    self.config['properties']['bgColor'] = self.ui.txtBgColor.text()
                    self.config['properties']['ftColor'] = self.ui.txtFrColor.text()
                    self.config['properties']['decimalsLen'] = str(self.ui.spinBoxDecimal.value()) 
                    self.config['properties']['ftFont'] = str(self.ui.lblFont.font()) 
                    
                    if self.ui.btnEnWoman.isChecked():
                        self.config['lang_outputs']['lang'] = '0'
                    elif self.ui.btnEnMan.isChecked():
                        self.config['lang_outputs']['lang'] = '1'
                    elif self.ui.btnEs.isChecked():
                        self.config['lang_outputs']['lang'] = '2'
                    else:
                        self.config['lang_outputs']['lang'] = '0'
                        
                    self.config['lang_outputs']['rate'] = str(self.ui.sliderRate.value())
                    
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
        
        if Path('src/files/config.ini').exists():
            self.config.read('src/files/config.ini')
            if  self.config.has_section('properties'):
                try:                    
                    bgColor =  self.config['properties']['bgColor'] 
                    ftColor = self.config['properties']['ftColor'] 
                    dcLen = self.config['properties']['decimalsLen']                    
                    font = self.config['properties']['ftFont']
                    
                    style = "background:{0};color:{1};"
                    style = style.format(bgColor, ftColor)
                    self.setStyleSheet("QWidget{"+ style +"}")
                    # self.setStyleSheet("QWidget {background-color: %s; color: %s;}" % bgColor % ftColor) 
                    self.setFont(font)
                except:                    
                    QMessageBox.warning(self,'Warning', 'The styles were not applied, please try again!', QMessageBox.Ok)
            else:
                self.createSession()
                
            # if self.config.has_section('lang_outputs'):
            #     try:                    
            #         lang =  self.config['lang_outputs']['lang'] 
            #         rete = self.config['lang_outputs']['rate'] 
            #     except:                    
            #         QMessageBox.warning(self,'Warning', 'The lang output was not applied, please try again!', QMessageBox.Ok)
            # else:
            #     self.createSession()
        else:
            self.createProperties()

    def iniPropertiesInputs(self):
        self.config = ConfigParser()     
        
        if Path('src/files/config.ini').exists():
            self.config.read('src/files/config.ini')
            if self.config.has_section('properties'):
                try:                    
                    self.ui.txtBgColor.setText(self.config['properties']['bgColor'])
                    self.ui.txtFrColor.setText(self.config['properties']['ftColor'])
                    font = self.config['properties']['ftFont']
                    self.ui.lblFont.setText(font.family())
                    self.ui.spinBoxDecimal.setValue(self.config['properties']['decimalsLen'])
                except:                    
                    pass

    def iniLangOutputs(self):
        self.config = ConfigParser()     
        
        if Path('src/files/config.ini').exists():
            self.config.read('src/files/config.ini')
            if self.config.has_section('lang_outputs'):
                try:  
                    if self.config['lang_outputs']['lang'] == 0:               
                        self.ui.btnEnWoman.setChecked(True)
                    elif self.config['lang_outputs']['lang'] == 1:
                        self.ui.btnEnMan.setChecked(True)
                    else:
                        self.ui.btnEs.setChecked(True)
                    
                    self.ui.sliderRate.value(self.config['lang_outputs']['rate'])
                except:                    
                    pass

    def bgColor(self):
            color = QColorDialog.getColor()
            self.ui.txtBgColor.setText(color.name())
            self.ui.txtBgColor.setStyleSheet("QWidget { background-color: %s}" % color.name())       
    
    def frColor(self):
            color = QColorDialog.getColor()
            self.ui.txtFrColor.setText(color.name())
            self.ui.txtFrColor.setStyleSheet("QWidget {background-color:transparent; color: %s}" % color.name()) 
            
    def setFont(self):
        ok, font = QFontDialog.getFont()        
        if ok:
            self.ui.lblFont.setText(font.family())
            self.ui.lblFont.setFont(font)
        