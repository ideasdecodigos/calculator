from asyncio import set_event_loop
# from asyncio.windows_events import NULL
from concurrent.futures import thread
from math import *
from statistics import *

import re, random, threading, pyttsx3, speech_recognition as sr
from PySide6.QtWidgets import QMainWindow, QMessageBox, QToolBar, QWidget, QColorDialog, QFontDialog
from views.scientific import Ui_Scientific
from model import temperature, time, length, properties, standard
from configparser import ConfigParser
from pathlib import Path
# import speech_recognition as sr
from PySide6.QtGui import QIcon

class Scientific(QMainWindow):    
    def __init__(self):
        super(Scientific,self).__init__()
        self.ui = Ui_Scientific()
        self.ui.setupUi(self)       
        properties.Properties.newProperties(self) 
        self.setGeometry(50,50,685,540)
        self.ui.st_controls.setGeometry(-10,122,0,0)
        
        
        
        #*******BUTTON'S ACTIONS        
        self.ui.btn1.clicked.connect(lambda:self.setNums(self.ui.btn1))
        self.ui.btn2.clicked.connect(lambda:self.setNums(self.ui.btn2))
        self.ui.btn3.clicked.connect(lambda:self.setNums(self.ui.btn3))
        self.ui.btn4.clicked.connect(lambda:self.setNums(self.ui.btn4))
        self.ui.btn5.clicked.connect(lambda:self.setNums(self.ui.btn5))
        self.ui.btn6.clicked.connect(lambda:self.setNums(self.ui.btn6))
        self.ui.btn7.clicked.connect(lambda:self.setNums(self.ui.btn7))
        self.ui.btn8.clicked.connect(lambda:self.setNums(self.ui.btn8))
        self.ui.btn9.clicked.connect(lambda:self.setNums(self.ui.btn9))
        self.ui.btn0.clicked.connect(lambda:self.setNums(self.ui.btn0))
        self.ui.btn00.clicked.connect(lambda:self.setNums(self.ui.btn00))
        self.ui.btn000.clicked.connect(lambda:self.setNums(self.ui.btn000))
        
        self.ui.btn_e.clicked.connect(lambda:self.setConstant('e'))
        self.ui.btn_pi.clicked.connect(lambda:self.setConstant('π'))
        self.ui.btn_tau.clicked.connect(lambda:self.setConstant('T'))
        self.ui.btn_rand.clicked.connect(lambda:self.setConstant('rnd'))
                
        self.ui.btn_parenthesis.clicked.connect(self.setRightParenthesis)
        
        self.ui.btn_plus.clicked.connect(lambda:self.setOperator(self.ui.btn_plus))
        self.ui.btn_minus.clicked.connect(lambda:self.setOperator(self.ui.btn_minus))
        self.ui.btn_mult.clicked.connect(lambda:self.setOperator(self.ui.btn_mult))
        self.ui.btn_divide.clicked.connect(lambda:self.setOperator(self.ui.btn_divide)) 
        
        self.ui.btn_sin.clicked.connect(lambda:self.setFuncton('sin('))
        self.ui.btn_cos.clicked.connect(lambda:self.setFuncton('cos('))
        self.ui.btn_tan.clicked.connect(lambda:self.setFuncton('tan('))
        self.ui.btn_atan2.clicked.connect(lambda:self.setFuncton('atan2('))
        
        self.ui.btn_sinh.clicked.connect(lambda:self.setFuncton('sinh('))
        self.ui.btn_cosh.clicked.connect(lambda:self.setFuncton('cosh('))
        self.ui.btn_tanh.clicked.connect(lambda:self.setFuncton('tanh('))
        
        self.ui.btn_asin.clicked.connect(lambda:self.setFuncton('asin('))
        self.ui.btn_acos.clicked.connect(lambda:self.setFuncton('acos('))
        self.ui.btn_atan.clicked.connect(lambda:self.setFuncton('atan('))
        
        self.ui.btn_asinh.clicked.connect(lambda:self.setFuncton('asinh('))
        self.ui.btn_acosh.clicked.connect(lambda:self.setFuncton('acosh('))
        self.ui.btn_atanh.clicked.connect(lambda:self.setFuncton('atanh('))
        
        self.ui.btn_factorial.clicked.connect(lambda:self.setFuncton('n!('))
        self.ui.btn_mod.clicked.connect(lambda:self.setPows('mod'))
        self.ui.btn_percent.clicked.connect(lambda:self.setPows('%'))
        self.ui.btn_sqrtroot.clicked.connect(lambda:self.setFuncton('²√('))
        self.ui.btn_cuberoot.clicked.connect(lambda:self.setFuncton('ᵌ√('))
        self.ui.btn_yroot.clicked.connect(lambda:self.setFuncton('ⁿ√('))
        self.ui.btn_1dividedX.clicked.connect(lambda:self.setFuncton('1/'))
        self.ui.btn_10powX.clicked.connect(lambda:self.setFuncton('10^('))
        self.ui.btn_2X.clicked.connect(lambda:self.setFuncton('2^('))
        self.ui.btn_sqrt.clicked.connect(lambda:self.setPows('^(2)'))
        self.ui.btn_sqrt3.clicked.connect(lambda:self.setPows('^(3)'))
        self.ui.btn_sqrtN.clicked.connect(lambda:self.setPows('^('))  
        
        self.ui.btn_ln.clicked.connect(lambda:self.setFuncton('ln('))
        self.ui.btn_log2.clicked.connect(lambda:self.setFuncton('log2('))
        self.ui.btn_log.clicked.connect(lambda:self.setFuncton('log('))
        self.ui.btn_gma.clicked.connect(lambda:self.setFuncton('gma('))
        self.ui.btn_lgma.clicked.connect(lambda:self.setFuncton('lgma('))
        self.ui.btn_log1p.clicked.connect(lambda:self.setFuncton('log1p('))
        self.ui.btn_exp.clicked.connect(lambda:self.setFuncton('exp('))
        self.ui.btn_expm1.clicked.connect(lambda:self.setFuncton('expm1('))
        self.ui.btn_prod.clicked.connect(lambda: self.setFuncton('prod('))        
        self.ui.btn_gcd.clicked.connect(lambda: self.setFuncton('gcd('))        
        self.ui.btn_hypot.clicked.connect(lambda: self.setFuncton('hypot('))        
        self.ui.btn_comb.clicked.connect(lambda: self.setFuncton('comb('))        
        self.ui.btn_frexp.clicked.connect(lambda: self.setFuncton('frexp('))        
        self.ui.btn_ldexp.clicked.connect(lambda: self.setFuncton('ldexp('))        
        self.ui.btn_sum.clicked.connect(lambda: self.setFuncton('sum(')) 
        self.ui.btn_perm.clicked.connect(lambda: self.setFuncton('perm(')) 
        self.ui.btn_lcm.clicked.connect(lambda: self.setFuncton('lcm(')) 
        self.ui.btn_min.clicked.connect(lambda: self.setFuncton('min(')) 
        self.ui.btn_max.clicked.connect(lambda: self.setFuncton('max(')) 
        self.ui.btn_mean.clicked.connect(lambda: self.setFuncton('mean(')) 
        self.ui.btn_medn.clicked.connect(lambda: self.setFuncton('medn(')) 
        self.ui.btn_mode.clicked.connect(lambda: self.setFuncton('mode('))
    
        self.ui.btn_trunc.clicked.connect(lambda: self.setFuncton('trunc(')) 
        self.ui.btn_abs.clicked.connect(lambda: self.setFuncton('abs(')) 
        self.ui.btn_fabs.clicked.connect(lambda: self.setFuncton('fabs(')) 
        self.ui.btn_floor.clicked.connect(lambda: self.setFuncton('floor(')) 
        self.ui.btn_ceil.clicked.connect(lambda: self.setFuncton('ceil(')) 
        self.ui.btn_round.clicked.connect(lambda: self.setFuncton('round(')) 
                
        self.ui.btn_RAD.clicked.connect(lambda:self.transResult('rad'))
        self.ui.btn_DEG.clicked.connect(lambda:self.transResult('deg'))
        
        self.ui.btn_ce.clicked.connect(self.clearCE)
        self.ui.btn_dot.clicked.connect(self.setDot)
        self.ui.btn_back.clicked.connect(self.delOne)
        self.ui.btn_equal.clicked.connect(self.equals)
        self.ui.btn_c.clicked.connect(self.clearC)
        self.ui.btn_inverse.clicked.connect(self.inverseInput)
        self.ui.actionExit.triggered.connect(self.close)
        # General Butons
        self.ui.actionProperties.triggered.connect(self.open_properties)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionLength.triggered.connect(self.open_length)
        self.ui.actionTime.triggered.connect(self.open_time)
        self.ui.actionTemperature.triggered.connect(self.open_temperature)
        self.ui.actionStandard.triggered.connect(self.open_standard)
        
        self.ui.btn_historial_show.clicked.connect(self.showHideHistory)
        self.ui.btn_m_show.clicked.connect(self.showHideMemory)
        self.ui.btn_showFun1.clicked.connect(self.showHideHistory)
        self.ui.btn_showFun2.clicked.connect(self.showHideMemory)
        
        
        self.ui.actionPlay_Result.triggered.connect(self.fromTextToVoice)
        self.ui.actionDict_input.triggered.connect(self.fromVoiceToText)
        
        self.ui.list_historial.clicked.connect(self.getHistory)
        self.ui.btn_ms.clicked.connect(self.setMS)
        self.ui.btn_m_plus.clicked.connect(self.addM)
        self.ui.btn_m_minus.clicked.connect(self.subtractM)
        self.ui.btn_mr.clicked.connect(self.getMemory)
        self.ui.btn_mr_prod.clicked.connect(self.mrProduct)        
        self.ui.btn_mr_sum.clicked.connect(self.addAction)  
            
        self.ui.btn_comma.clicked.connect(self.setComma)        
        
        self.ui.btn_or.clicked.connect(lambda: self.setlogicalOperator(' or ')) 
        self.ui.btn_and.clicked.connect(lambda: self.setlogicalOperator(' and ')) 
        self.ui.btn_greater.clicked.connect(lambda: self.setlogicalOperator('>')) 
        self.ui.btn_greater_than.clicked.connect(lambda: self.setlogicalOperator('≧')) 
        self.ui.btn_less.clicked.connect(lambda: self.setlogicalOperator('<')) 
        self.ui.btn_less_than.clicked.connect(lambda: self.setlogicalOperator('≦')) 
        self.ui.btn_not_equals.clicked.connect(lambda: self.setlogicalOperator('≠')) 
        self.ui.btn_not.clicked.connect(lambda: self.setlogicalOperator(' not ')) 
        
        self.ui.btn_rd_bin.clicked.connect(lambda:self.sys_convert('bin'))
        self.ui.btn_rd_dec.clicked.connect(lambda:self.sys_convert('dec'))
        self.ui.btn_rd_fe.clicked.connect(lambda:self.sys_convert('f-e'))
        self.ui.btn_rd_hex.clicked.connect(lambda:self.sys_convert('hex'))
        self.ui.btn_rd_oct.clicked.connect(lambda:self.sys_convert('oct'))
        
        self.ui.btn_rad_dec.clicked.connect(self.setRounded)
        self.ui.btn_rad_abs.clicked.connect(self.setRounded)
        self.ui.btn_rad_fabs.clicked.connect(self.setRounded)
        self.ui.btn_rad_floor.clicked.connect(self.setRounded)
        self.ui.btn_rad_ceil.clicked.connect(self.setRounded)
        self.ui.btn_rad_trunc.clicked.connect(self.setRounded)
        
            
        
        
        #Globals variables
        self.input= ''
        self.operatorsList= ('+','-','*','/')
        self.simpleSymobolsList= ('+','-','(')
        self.expressionsList = {
                                'sqrt':sqrt,'cuberoot':self.cubeRoot,'yroot':self.yRoot, 'e':e,'pi':pi, 'T':tau, 'percent': 100,
                                'fact':factorial,'abs':abs,'rad':radians, 'deg':degrees,'gma':gamma, 'lgma':lgamma,
                                'trunc':trunc,'ceil':ceil, 'floor':floor,'fabs':fabs, 'mode':mode,'mean':mean,'medn':median,
                                'ln':log,'log':log10, 'log2':log2,'log1p':log1p, 'exp':exp,'expm1':expm1,
                                'sin':sin, 'cos':cos, 'tan':tan, 'sinh':sinh, 'cosh':cosh, 'tanh':tanh, 'atan2':atan2,
                                'asin':asin, 'acos':acos, 'atan':atan, 'asinh':asinh, 'acosh':acosh, 'atanh':atanh,
                                'gcd':gcd, 'prod':self.fprod, 'sum':self.fsum, 'frexp':frexp,
                                'comb':comb, 'hypot':hypot, 'perm':perm, 'ldexp':ldexp, 'lcm':self.lcm, 'rnd':random.random(),
                                'min':min, 'max':max, 'mean':self.mean, 'medn':self.medn, 'mode':mode
                                }
        
        self.symbolsList = [')','(','+','-','*','/','%','mod','√','^','e','π','exp','in','n!','log','x²','χʸ']
        
        self.funcsList = (
                        'mod','rnd','pi','','²√(','ᵌ√(','ⁿ√(','^(2)','^(3)','^(','10^(','*(','n!(', ' or ',' and ',' not ','≠','==',
                        'rad(','deg(','trunc(','ceil(','floor(','abs(','fabs(','round(',
                        'lgma(','gma(','log2(','ln(','log(','log1p(', 'exp(','expm1(','frexp(','ldexp(', 'perm(','hypot(',
                        'comb(', 'min(','max(','prod(','sum(', 'lcm(','gcd(','mean(','medn(', 'mode('
                        'sin(','cos(','tan(','sinh(','cosh(','tanh(','asin(', 'acos(','atan(','asinh(', 'acosh(','atanh(','atan2('
        )
        self.input_microphone = [
            'cero','one', 'two', 'three', 'four', 'five', 'seven', 'eight', 'nine', 'ten', 'eleven', 
        ]
        #Sindows Objects 
        self.temperature = None
        self.time = None
        self.length = None
        self.standard = None
        self.base = 'dec'
        self.result = ''
        self.properties = properties.Properties()
    
    def getResultInfo(self, value):
        if isfinite(value): self.ui.statusbar.showMessage('Finite number',5000)
        
    def setlogicalOperator(self, lgop):
        txt = self.ui.label_mr.text() 
        if txt == '0':
            self.ui.statusbar.showMessage("can't compare cero", 5000)
        elif txt[-3:] == ' < ' or txt[-3:] == ' > ' or txt[-4:] == ' or ' or txt[-4:] == ' <= ' or txt[-4:] == ' >= ' or txt[-5:] == ' and ':
            self.ui.label_mr.setText(txt[:len(lgop)] + lgop)
        elif txt != '0' or txt[-1:] != ',' or txt[-1:] != '(':
            self.ui.label_mr.setText(txt + lgop) 
        
    def setRounded(self):   
        '''
        Return a rounded number only whent the result is a decimal value, whent the system be on decimal and whent don't be a tuple, a bool value
        
        '''     
        if not(self.result == '0' or self.result == '') and not(isinstance(self.result, bool) or isinstance(self.result, tuple)) and self.ui.label_result.text() != '' and self.ui.btn_rd_dec.isChecked():
            txt = ''
            if self.ui.btn_rad_abs.isChecked():
                txt=f'{abs(float(self.result))}'
            elif self.ui.btn_rad_trunc.isChecked():
                txt=f'{trunc(float(self.result))}'
            elif self.ui.btn_rad_fabs.isChecked():
                txt=f'{fabs(float(self.result))}'      
            elif self.ui.btn_rad_floor.isChecked():
                txt=f'{floor(float(self.result))}'
            elif self.ui.btn_rad_ceil.isChecked():
                txt=f'{ceil(float(self.result))}'
            else:
                txt=f'{self.result}'
            self.ui.label_result.setText(txt)
        
    
    
    # least common multiple
    def lcm(self, a, b):
        return (a * b) / gcd(a, b)   
            
    def yRoot(self, n, x):
        '''
        Return n root of x number
        >>> yRoot(81,4)
        return 1.0173
        
        '''
        nroot = x ** (1 / n)
        return nroot
    
    def cubeRoot(self, x):
        cuberoot = x ** (1 / 3)
        return cuberoot
    
    def fsum(self, *args):
        return fsum(args) # return the sum n items as float
    
    def fprod(self, *args):
        return prod(args)
    
    def mean(self, *args):
        return mean(args)
    
    def medn(self, *args):
        return median(args)    
    
    def mode(self, *args):
        return mode(args)
    
    def setFuncItems(self, func):
        self.ui.btn_comma.setEnabled(True)
        self.setFuncton(func)
    
        
    def setComma(self):
        txt = self.ui.label_mr.text()
        if txt != '0':   
            noneComma =(
                '²√(','ᵌ√(','n!(', 'expm1(','log1p(',
                'rad(','deg(','trunc(','ceil(','floor(','abs(','fabs(','lgma(','gma(','log2(','ln(','log(','log2(', 
                'exp(','expm1(','sin(','cos(','tan(','sec(', 'csc(','cot(','sinh(', 'cosh(','tanh(','sech(','csch(','coth('
                )
            listFuncs =('gcd(','comb(','hypot(','min(','max(','sum(','prod(','avg(','round(','perm(','ldexp(')
            x = txt.rfind('(')
            func = ''
            if txt[x-4:x+1] in listFuncs or txt[x-4:x+1] in noneComma:
                func = txt[x-4:x+1]
            elif txt[x-3:x+1] in listFuncs or txt[x-3:x+1] in noneComma:
                func = txt[x-3:x+1]
            elif txt[x-2:x+1] in listFuncs or txt[x-2:x+1] in noneComma:
                func = txt[x-2:x+1]
            
            #take the last func and its attrs
            brk= txt.rfind(func)
            funcAttr = txt[brk:]
            if re.match(r'^[gcd(]+[0-9]+[,]+[0-9]+$' , funcAttr): 
                self.ui.statusbar.showMessage(f'{func} recive 2 parameter only', 7000)
            elif re.match(r'^[perm(]+[0-9]+[,]+[0-9]+$' , funcAttr): 
                self.ui.statusbar.showMessage(f'{func} recive 2 parameter only', 7000)
            elif re.match(r'^[comb(]+[0-9]+[,]+[0-9]+$' , funcAttr): 
                self.ui.statusbar.showMessage(f'{func} recive 2 parameter only', 7000)
            elif re.match(r'^[round(]+[0-9]+[,]+[0-9]+$' , funcAttr): 
                self.ui.statusbar.showMessage(f'{func} recive 2 parameter only', 7000)
            elif re.match(r'^[ldexp(]+[0-9]+[,]+[0-9]+$' , funcAttr): 
                self.ui.statusbar.showMessage(f'{func} recive 2 parameter only', 7000)
            elif func in noneComma:
                self.ui.statusbar.showMessage(f'Takes only one argument ex: {func}x)', 7000)
            else:              
                if not txt.endswith(','): self.ui.label_mr.setText(txt + ',')
                    
    def fromTextToVoice(self):
        try:            
            if threading.active_count() <= 1:
                self.ui.actionDict_input.setDisabled(True)
                threading.Thread(target=self.talkAloud).start()          
        except:
            pass   
        finally:
            self.ui.actionDict_input.setEnabled(True)   
        
    def fromVoiceToText(self):
        try:            
            if threading.active_count() <= 1:
                self.ui.actionPlay_Result.setDisabled(True)
                threading.Thread(target=self.get_microphone).start()                                    
        except:
            pass   
        finally:
            self.ui.actionPlay_Result.setEnabled(True)   
            
        
    def mrProduct(self):
        '''
        List all memory values in the prod function
        
        example: prod(34, 53, 3, 98, ..., n)
        
        '''
        ms = self.ui.list_memory
        if ms.count() > 1:
            lbl_txt = 'prod('
            for i in range(ms.count()):               
                lbl_txt += ms.item(i).text() + ','
            lbl_txt = lbl_txt[:-1] + ')'
            self.setFuncton(lbl_txt)
                            
    def mrAddition(self):
        '''
        List all memory values in the sum function
        
        example: sum(34, 53, 3, 98, ..., n)
        
        '''
        ms = self.ui.list_memory
        if ms.count() > 1:
            lbl_txt = 'sum('
            for i in range(ms.count()):               
                lbl_txt += ms.item(i).text() + ','
            lbl_txt = lbl_txt[:-1] + ')'
            self.setFuncton(lbl_txt)
                        
    def addM(self):
        ms = self.ui.list_memory
        if ms.count() > 0:
            oldValue = ms.item(0).text()         
            self.ui.list_memory.removeItemWidget(ms.takeItem(0))
        
            rest = self.ui.label_result.text()
            txt = self.ui.label_mr.text()
            
            newtxt=''
            if rest != '':
                self.ui.list_memory.insertItem(0, str(eval(f'{rest} + {oldValue}')))
                self.ui.statusbar.showMessage('Added to memory',5000)
            elif re.match(r'^[0-9.]+$', txt[-1:]) and txt != '0':
                for i in reversed(txt) :
                    if re.match(r'^[0-9.]+$', i) and txt != '0':
                        newtxt += i
                    else:
                        break  
                self.ui.list_memory.insertItem(0, str(eval(f'{newtxt[::-1]} + {oldValue}')))
                self.ui.statusbar.showMessage('Added to memory',5000) 
            
        else:
            self.setMS()
                        
    def subtractM(self):
        ms = self.ui.list_memory
        if ms.count() > 0:
            oldValue = ms.item(0).text()         
            self.ui.list_memory.removeItemWidget(ms.takeItem(0))
        
            rest = self.ui.label_result.text()
            txt = self.ui.label_mr.text()
            newtxt=''
            if rest != '':
                self.ui.list_memory.insertItem(0, str(eval(f'{oldValue} - {rest}')))
                self.ui.statusbar.showMessage('Subtract memory',5000)
            elif re.match(r'^[0-9.]+$', txt[-1:]) and txt != '0':
                for i in reversed(txt) :
                    if re.match(r'^[0-9.]+$', i) and txt != '0':
                        newtxt += i
                    else:
                        break  
                self.ui.list_memory.insertItem(0, str(eval(f'{oldValue} - {newtxt[::-1]}')))
                self.ui.statusbar.showMessage('Subtract memory',5000) 
            
            # if self.ui.list_memory.item(0).text() == '0':
            #     self.ui.list_memory.removeItemWidget(ms.takeItem(0))
        else:
            self.setMS()
                        
    def setMS(self):
        pass
        # rest = self.ui.label_result.text()
        # txt = self.ui.label_mr.text()
        txt=''
        if self.ui.label_result.text() != '':
            self.ui.list_memory.insertItem(0, self.ui.label_result.text())
            self.ui.statusbar.showMessage('Saved to memory',5000)
        elif re.match(r'^[0-9.]+$', self.ui.label_mr.text()[-1:]) and self.ui.label_mr.text() != '0':
            for i in reversed(self.ui.label_mr.text()) :
                if re.match(r'^[0-9.]+$', i) and self.ui.label_mr.text() != '0':
                    txt += i
                else:
                    break  
            self.ui.list_memory.insertItem(0,txt[::-1])
            self.ui.statusbar.showMessage('Saved to memory',5000)   
        
    def getHistory(self):
        if self.ui.list_historial.count() > 0:
            txt = self.ui.list_historial.currentItem().text()
            t=[]
            if txt.startswith('= '):  
                t=txt[2:].split(' (')  
                txt=t[0]
            if self.ui.radioButton.isChecked():
                self.ui.label_mr.setText(txt)
            else:
                self.ui.label_mr.setText(self.ui.label_mr.text() + txt)
            
    def getMemory(self):
        if self.ui.list_memory.count() > 0:
            txt = self.ui.list_memory.item(0).text()
            self.ui.label_result.setText('')
            
            if re.match(r'^[0-9.]+$', self.ui.label_mr.text()[-1:]):
                self.ui.label_mr.setText(txt)
            else:
                self.ui.label_mr.setText(self.ui.label_mr.text() + txt)

    def clearCE(self):
        txt = self.ui.label_mr.text()          
        self.ui.label_result.setText('')         
        
        if txt[-5:] in self.funcsList:
            txt = txt[:-5]        
        elif txt[-4:] in self.funcsList:
            txt = txt[:-4]    
        elif txt[-3:] in self.funcsList:
            txt = txt[:-3]
        elif txt[-2:] in self.funcsList:
            txt = txt[:-2] 
        elif re.match(r'^[0-9.]+$', txt[-1:]) and txt != '0':
            for i in reversed(txt) :
                if re.match(r'^[0-9.]+$', i) and txt != '0':
                    txt= txt[:-1] 
                else:
                    break
        else:
            txt = txt[:-1]
        
        if txt == '': txt = '0'
        self.ui.statusbar.showMessage('') 
        self.ui.label_mr.setText(txt)
        self.getResult()
        
    def setPows(self, num):
        txt = self.ui.label_mr.text()    
        
        if txt =='' and self.ui.label_result.text() != '':            
            self.ui.label_mr.setText(self.ui.label_result.text() + num)
            self.ui.label_result.setText('')
        elif re.match(r'^[0-9]+$', txt[-1:]) and self.input != '':
            self.ui.label_mr.setText(txt + num)
                
    def voiceToText(self):
        pass    
        threading.Thread(target=self.get_microphone())      
                
    def formatVoiceToTextInput(self, txt):
        txt = txt.replace('cien', '100')
        txt = txt.replace('uno', '1')
        inputList = txt.split()
        
        newtxt = ''
        isnum=False
        for n in inputList:
            try:# verify if n is an int or a float number
                eval(n)
                isnum=True
            except:
                isnum=False
            # verify that the str newtxt be able to works in eval function                    
            if n in self.symbolsList or isnum:
                newtxt+=n   
        return newtxt       
                
    def transResult(self, func):
        rest = self.ui.label_result.text()
        txt = self.ui.label_mr.text()
        if rest != '':
            self.ui.label_mr.setText(f'{func}({rest})') 
            self.ui.label_result.setText('')
        elif re.match(r'^[0-9.]+$', txt[-1:]) and txt != '0':
            for i in reversed(txt) :
                if re.match(r'^[0-9.]+$', i) and txt != '0':
                    txt += i
                else:
                    break  
            self.ui.label_mr.setText(f'{func}({txt})')  
            self.ui.label_result.setText('')      
            
                
    def setNums(self, btn): 
        txt = self.ui.label_mr.text()
        if txt == '0': txt = '' 
        
        if txt.endswith(')'):            
            self.ui.label_mr.setText(txt + f'*{btn.text()}')  
        else:                 
            self.ui.label_mr.setText(txt + btn.text())
        self.input += btn.text() 
        self.getResult()
    
    def setOperator(self, btn): 
        self.input = ''          
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.setText('') 
        txt = self.ui.label_mr.text()
        
        if txt == '' and self.ui.label_result.text() != '': 
            txt = self.ui.label_result.text()  
            
            
        self.ui.label_mr.setText(self.txtFormat(txt, btn.text()))
        self.ui.statusbar.showMessage('Awaiting input...',5000) 
        
        self.ui.label_result.setText('')            
        if self.ui.label_mr.text() == '':
            self.ui.label_mr.setText('0') 
    
        
    def txtFormat(self, label, input):
        txt = label + input
                    
        txt = txt.replace('**', input)
        txt = txt.replace('(*', input)
        txt = txt.replace('(/', input)
        txt = txt.replace('(mod', input)
        txt = txt.replace('(%', input)
        txt = txt.replace('(^', input)
        txt = txt.replace('(^', input)
        txt = txt.replace('//', input)
        txt = txt.replace('/*', input)
        txt = txt.replace('*/', input)
        txt = txt.replace('^^', input)
        
        if txt in self.simpleSymobolsList: 
            txt = input
            # block any operator
        elif txt in self.symbolsList: 
            txt = ''
        
        return txt
    
    def equals(self):   
        """
        Show and save in historial the input result, and reset the values
        
        this function works along to eval and cleanInput functions
        
        """
        unformattedtxt= self.ui.label_mr.text()
        while unformattedtxt.count('(') > unformattedtxt.count(')'):
            unformattedtxt += ')' 
            
        while unformattedtxt.count('[') > unformattedtxt.count(']'):
            unformattedtxt += ']' 
            
        txt = self.cleanInput()     
        #show up the result
        if txt != '' and (txt[-1:] not in self.operatorsList) and (txt != self.input) and (txt.count('(') == txt.count(')')):
            try:
                self.result = eval(txt,self.expressionsList)                                            
                self.sys_convert(self.base)
                
                self.ui.list_historial.addItem(unformattedtxt)
                self.ui.list_historial.addItem(f"= {self.result} ({self.base}:  {self.ui.label_result.text()})")
                self.input = ''
                self.ui.label_mr.setText('')
            except Exception as ex:                
                self.ui.label_mr.setStyleSheet('color:red')
                self.ui.statusbar.showMessage(str(ex),5000)
                
        elif re.match(r'^[0-9.,]', txt):
            self.ui.label_result.setText(txt)
            self.input = ''
            self.ui.label_mr.setText('')
            self.ui.statusbar.showMessage('')
            
            
    def getResult(self):
        """
        Show the input result every time a button like +, -, * or / is pressed
        
        """
        txt = self.outputFormat()
        self.ui.label_mr.setStyleSheet('color:black;')
        try:
            if self.input != '' and txt != '0' and (txt != self.input) and (txt.count('(') == txt.count(')')):               
                self.result = eval(txt,self.expressionsList)                
                self.sys_convert(self.base)                
            else:
                self.ui.label_result.setText('')
        except Exception as ex:                
            self.ui.label_mr.setStyleSheet('color:red')
            self.ui.statusbar.showMessage(str(ex),5000)
            
            
    def outputFormat(self): 
    
        txt = self.ui.label_mr.text()
            
        txt = txt.replace('%', '/percent*')
        txt = txt.replace('²√', 'sqrt')           
        txt = txt.replace('^', '**')             
        txt = txt.replace('mod', '%')             
        txt = txt.replace('e˟', 'e_x')             
        txt = txt.replace('ᵌ√', 'cuberoot')             
        txt = txt.replace('ⁿ√', 'yroot')             
        txt = txt.replace('π', 'pi')                       
        txt = txt.replace('n!', 'fact')               
        txt = txt.replace('≦', '<=')             
        txt = txt.replace('≧', '>=')             
        txt = txt.replace('≠', '!=')             
            
        return txt
    
    def sys_convert(self, base):
        self.base = base
        if self.result != '' and isinstance(self.result, tuple):
            self.ui.label_result.setText(str(self.result))
        elif self.result != '' and isinstance(self.result, bool):
            self.ui.label_result.setText('True') if self.result == True else self.ui.label_result.setText('False')
        elif self.result != '':
            if self.base == 'f-e':
                self.ui.label_result.setText(f"{self.result:.1E}")
            elif self.base == 'hex':
                self.ui.label_result.setText(f"{round(self.result):X}")
            elif self.base == 'oct':
                self.ui.label_result.setText(f"{round(self.result):o}")
            elif self.base == 'bin':
                self.ui.label_result.setText(f"{round(self.result):b}")
            else:
                # r_arr = f'{self.result:G}'.split('.')
                # print(self.result)    
                # print(r_arr[1]) 
                
                if '.' in str(self.result):     
                    r_arr = str(self.result).split('.')
                    if int(r_arr[1]) == 0: 
                        self.ui.label_result.setText(f"{self.result :,.0F}") 
                    else:
                        txt = f"{r_arr[0]}.{r_arr[1]}"
                        self.ui.label_result.setText(txt)
                else:
                #     if int(r_arr[1]) == 0: 
                #         self.ui.label_result.setText(f"{self.result :.0F}") 
                #     else:
                    self.ui.label_result.setText(f"{self.result :,.0F}") 
                
        else:
            self.ui.statusbar.showMessage('No result to convert', 5000)
                
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
            self.ui.label_mr.setText('')
        txt =  self.ui.label_mr.text() 
        cutlen = txt.rfind(self.input)
        firstPart = txt[:cutlen]
        secondPart = txt[cutlen:]
        newTxt = f'{firstPart}(-{secondPart}'
        subSecondPart = f'(-{secondPart}'
        
        if txt == '(-' or txt == '-':
            self.ui.label_mr.setText('0')  
        elif txt[-1:] == '(' and self.input == '':
            self.ui.label_mr.setText(txt + '-')
        elif txt == '' and self.input == '':
            self.ui.label_mr.setText(txt + '-')
        elif re.match(r'^[0-9.]+$', txt[-1:]) and self.input != '' and txt[cutlen-2:] != subSecondPart:
        # elif re.match(r'^[0-9]+$', txt[-1:]) not in self.operatorsList and self.input != '' and txt[cutlen-2:] != subSecondPart:
            self.ui.label_mr.setText(newTxt)
        elif txt[cutlen-2:] == subSecondPart:
            self.ui.label_mr.setText(firstPart[:-2] + secondPart)
    
    
    def setFuncton(self, func):
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.setText('')
        txt = self.ui.label_mr.text()
        
        if txt[-1:] in self.operatorsList or txt == '' or re.match(r'^[,( ]+$', txt[-1:] ):
            self.ui.label_mr.setText(txt + func)
        elif  txt[-3:] != '*'+ func:
            self.ui.label_mr.setText(txt + '*'+ func)
        
        self.input = ''
        self.ui.statusbar.showMessage('Awaiting input...',5000) 
    
    def setConstant(self, const):
        """
        Represent the const e in the equation
        Example:
        if input = '5*e' in the eval function this it will be equal to: 5*2.718281828459045 = 13.591409142295226176801437356763
        
        """
        
        if self.ui.label_mr.text() == '0':
            self.ui.label_mr.setText('')
        txt = self.ui.label_mr.text()
            
        if re.match(r'^[0-9π]+$',txt[-1:]):
            self.ui.label_mr.setText(f'{txt}*({const}')
        else:
            self.ui.label_mr.setText(txt + const)
            
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
        elif re.match(r'^[0-9.)]+$',txt[-1:]):
        # elif txt[-1:] not in self.operatorsList and txt[-1:] != '(':
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
        if txt[-1:] ==',':
            pass
        elif txt[-1:] =='(':
            self.ui.label_mr.setText(txt +'(')
        elif txt[-1:] not in self.operatorsList and txt.count('(') > txt.count(')'):
            self.ui.label_mr.setText(txt +')')
        else:
            self.setLeftParenthesis()
        self.getResult()
        
        
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
        txt = txt.replace('²√', 'sqrt')           
        txt = txt.replace('^', '**')             
        txt = txt.replace('mod', '%')             
        txt = txt.replace('e˟', 'e_x')             
        txt = txt.replace('ᵌ√', 'cuberoot')             
        txt = txt.replace('ⁿ√', 'yroot')             
        txt = txt.replace('π', 'pi')                       
        txt = txt.replace('n!', 'fact')             
        txt = txt.replace('≦', '<=')             
        txt = txt.replace('≧', '>=')             
        txt = txt.replace('≠', '!=')               
        txt = txt.replace('⩵', '==')               
            
        return txt
        
    def clearC(self):
        """
        Reset all as defualt
        
        """
        self.ui.label_result.setText('')
        self.ui.label_mr.setText('0')        
        self.input = ''
        self.ui.statusbar.showMessage('')
        
            
    def showHideMemory(self):
        """
        Show and switch between contorls and historial display
        
        """
        if self.ui.st_controls.width() == 0 and self.ui.st_controls.currentIndex() == 1:
            self.ui.st_controls.setGeometry(-10,122,321,351)
        elif self.ui.st_controls.width() != 0 and self.ui.st_controls.currentIndex() == 0:
            self.ui.st_controls.setCurrentIndex(1)
        elif self.ui.st_controls.width() == 0 and self.ui.st_controls.currentIndex() == 0:
            self.ui.st_controls.setCurrentIndex(1)
            self.ui.st_controls.setGeometry(-10,122,321,351)
        else:
            self.ui.st_controls.setGeometry(-10,122,0,0)
            
    
    def showHideHistory(self):
        """
        Show and switch between contorls and memory display
        
        """
            
        if self.ui.st_controls.width() == 0 and self.ui.st_controls.currentIndex() == 0:
            self.ui.st_controls.setGeometry(-10,122,321,351)
        elif self.ui.st_controls.width() != 0 and self.ui.st_controls.currentIndex() == 1:
            self.ui.st_controls.setCurrentIndex(0)
        elif self.ui.st_controls.width() == 0 and self.ui.st_controls.currentIndex() == 1:
            self.ui.st_controls.setCurrentIndex(0)
            self.ui.st_controls.setGeometry(-10,122,321,351)
        else:
            self.ui.st_controls.setGeometry(-10,122,0,0)
            
            
    
    def delOne(self):  
        """
        Remove the last character on the input string
        
        """
        txt = self.ui.label_mr.text()          
        
        if txt[-5:] in self.funcsList:
            txt = txt[:-5]        
        elif txt[-4:] in self.funcsList:
            txt = txt[:-4]    
        elif txt[-3:] in self.funcsList:
            txt = txt[:-3]
        elif txt[-2:] in self.funcsList:
            txt = txt[:-2] 
        else:
            txt = txt[:-1]        
        
        # if last char in label is a number, then input var del the last char
        if re.match(r'^[0-9.]+$',txt[-1:]):
            self.input = self.input[:-1]
            
        if txt == '':
            txt = '0'
        
        self.ui.label_mr.setText(txt)   
        self.ui.label_result.setText('')
            
    def setDot(self):
        """
        Add a dot in the current input only if the input is a integer, else, then skip it
        
        """
        if self.input != '' and '.' not in self.input or self.ui.label_mr.text() == '0':
            self.input += '.'
            self.ui.label_mr.setText(self.ui.label_mr.text() + '.')
    
    

    def get_microphone(self):
        speech_engine = sr.Recognizer()
        self.ui.actionDict_input.setIcon(QIcon("src/imgs/microOn.png"))
        try:
            with sr.Microphone() as micro:
                self.ui.statusbar.showMessage("Listening...")
                speech_engine.adjust_for_ambient_noise(micro)
                audio = speech_engine.listen(micro)
                self.ui.statusbar.showMessage("Recognizing...")
                text = speech_engine.recognize_google(audio)
                # text = speech_engine.recognize_google(audio, language="es-ES")
                self.ui.label_mr.setText(text)
        except:
            self.ui.statusbar.showMessage("Couldn't hear you :(", 5000)
        finally:
            self.ui.actionDict_input.setIcon(QIcon("src/imgs/microOff.png"))
            self.ui.statusbar.showMessage("")

    #speak aloud code   
    def talkAloud(self):
        self.init_speaker()#init the voice and the rate      
        
        try:
            self.ui.actionPlay_Result.setIcon(QIcon("src/imgs/volumeOn.png"))  
            self.ui.statusbar.showMessage('Talking aloud...')     
            speaker = pyttsx3.init()  
            voces = speaker.getProperty('voices')
            speaker.setProperty('voice',voces[self.lang].id) 
            speaker.setProperty('rate',self.rate)
            if self.lang == 0 or self.lang == 1:
                speaker.say(self.play_en()) 
            elif self.lang == 2:  
                speaker.say(self.play_es()) 
            else:  
                speaker.say(self.play_en())   
            speaker.runAndWait() 
        except:
            pass
        finally:
            self.ui.actionPlay_Result.setIcon(QIcon("src/imgs/valumeOff.png"))
            self.ui.statusbar.showMessage('') 
        
    def play_en(self):
        rst = self.ui.label_result.text()
        txt = self.ui.label_mr.text()
        
        txt = txt.replace('-',' minus ')
        txt = txt.replace('+',' plus ')
        txt = txt.replace('*',' by ')
        txt = txt.replace('ᵌ√',' cube root of ')
        txt = txt.replace('²√',' square root of ')
        txt = txt.replace('%',' percent of ')
        txt = txt.replace('/',' divided by ')
        txt = txt.replace('sin',' sine of ')
        txt = txt.replace('cos',' cosine of ')
        txt = txt.replace('tan',' tangent of ')
        txt = txt.replace('sec',' secant of ')
        txt = txt.replace('csc',' cosecant of ')
        txt = txt.replace('cot',' cotangent of ')
        
        txt = txt.replace('asin',' cotangent of ')
            
        if txt == '0' and rst == '':
            txt = '0'
        elif rst != '' and txt == '':
            txt = rst            
        elif  rst != '' and txt != '0':
            txt = txt + ' = a  ' + rst
            
        return txt
    
    def play_es(self):
        rst = self.ui.label_result.text()
        txt = self.ui.label_mr.text()
        
        txt = txt.replace('-',' menos ')
        txt = txt.replace('+',' + ')
        txt = txt.replace('*',' por ')
        txt = txt.replace('√',' raíz de ')
        txt = txt.replace('%',' porciento de ')
        txt = txt.replace('/',' entre ')
            
        if txt == '0' and rst == '':
            txt = '0'
        elif rst != '' and txt == '':
            txt = rst            
        elif  rst != '' and txt != '0':
            txt = txt + ' = a  ' + rst
            
        return txt
    
    def init_speaker(self):
        config = ConfigParser()     
        
        if Path('src/files/config.ini').exists():
            config.read('src/files/config.ini')
            if config.has_section('lang_outputs'):
                try:                    
                    self.lang = int(config['lang_outputs']['lang'])
                    self.rate = int(config['lang_outputs']['rate'])
                except:                    
                    self.lang = 2
                    self.rate = 140
        else:
            self.lang = 2
            self.rate = 140

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
            self.standard.close()
        
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
        # QMessageBox.information(self,'Info','This is a collaction of calculators v1.0.0\nDeveloped by IDCSchools \n \napr 01, 2022')
        import webbrowser
        webbrowser.open("https://www.en4es.com", new=2, autoraise=True)



        