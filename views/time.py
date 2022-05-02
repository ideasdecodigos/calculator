# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Time(object):
    def setupUi(self, Time):
        if not Time.objectName():
            Time.setObjectName(u"Time")
        Time.resize(284, 396)
        Time.setContextMenuPolicy(Qt.CustomContextMenu)
        icon = QIcon()
        icon.addFile(u"../src/imgs/standar.png", QSize(), QIcon.Normal, QIcon.Off)
        Time.setWindowIcon(icon)
        Time.setStyleSheet(u"")
        self.actionStandard = QAction(Time)
        self.actionStandard.setObjectName(u"actionStandard")
        self.actionTemperature = QAction(Time)
        self.actionTemperature.setObjectName(u"actionTemperature")
        self.actionLenght = QAction(Time)
        self.actionLenght.setObjectName(u"actionLenght")
        self.actionExit = QAction(Time)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(Time)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionFQAs = QAction(Time)
        self.actionFQAs.setObjectName(u"actionFQAs")
        self.actionProperties = QAction(Time)
        self.actionProperties.setObjectName(u"actionProperties")
        self.actionTime = QAction(Time)
        self.actionTime.setObjectName(u"actionTime")
        self.centralwidget = QWidget(Time)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(266, 600))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	background:transparent;}\n"
"#label_text,#label_result{\n"
"	font: 75 20pt \"Rockwell Condensed\";\n"
"	background:none;\n"
"}#label_result{\n"
"	font: 16pt \"Rockwell Condensed\";\n"
"}#comboBox1,#comboBox2{\n"
"	border:none;\n"
"	background:none;\n"
"}\n"
"#comboBox1:checked,#comboBox2:checked{\n"
"	background:none;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_text = QLabel(self.widget_2)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setMaximumSize(QSize(248, 16777215))
        self.label_text.setTextFormat(Qt.RichText)
        self.label_text.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_text, 0, Qt.AlignRight)

        self.comboBox1 = QComboBox(self.widget_2)
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.addItem("")
        self.comboBox1.setObjectName(u"comboBox1")
        self.comboBox1.setMaximumSize(QSize(130, 40))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.comboBox1.setFont(font)
        self.comboBox1.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox1.setAutoFillBackground(False)
        self.comboBox1.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.comboBox1, 0, Qt.AlignRight)

        self.line = QFrame(self.widget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label_result = QLabel(self.widget_2)
        self.label_result.setObjectName(u"label_result")

        self.verticalLayout.addWidget(self.label_result, 0, Qt.AlignRight)

        self.comboBox2 = QComboBox(self.widget_2)
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.addItem("")
        self.comboBox2.setObjectName(u"comboBox2")
        self.comboBox2.setMaximumSize(QSize(130, 40))
        palette = QPalette()
        self.comboBox2.setPalette(palette)
        self.comboBox2.setFont(font)
        self.comboBox2.setContextMenuPolicy(Qt.NoContextMenu)
        self.comboBox2.setAutoFillBackground(False)
        self.comboBox2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.comboBox2, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{background:transparent;}\n"
"QPushButton{\n"
"	color:black;\n"
"	background:white rgba(255, 255, 255, 0.8);\n"
"	border:0;\n"
"	offline:none;\n"
"	margin:0px;\n"
"	font: 500 16pt \"Arial Black\";\n"
" 	height:50px;\n"
"}\n"
"QPushButton:hover{\n"
"	background:rgba(0, 0, 0, 0.1);\n"
"}\n"
"#btn_clear,#btn_del_one{	font: 12pt \"Arial\";padding:0px 2px;}\n"
"#btn_clear{color:red;}\n"
"#btn_del_one:hover{color:red}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self._2 = QGridLayout(self.widget)
        self._2.setSpacing(1)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self._2.setContentsMargins(1, 1, 1, 1)
        self.btn2 = QPushButton(self.widget)
        self.btn2.setObjectName(u"btn2")

        self._2.addWidget(self.btn2, 2, 1, 1, 1)

        self.btn3 = QPushButton(self.widget)
        self.btn3.setObjectName(u"btn3")

        self._2.addWidget(self.btn3, 2, 2, 1, 1)

        self.btn8 = QPushButton(self.widget)
        self.btn8.setObjectName(u"btn8")

        self._2.addWidget(self.btn8, 0, 1, 1, 1)

        self.btn5 = QPushButton(self.widget)
        self.btn5.setObjectName(u"btn5")

        self._2.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn0 = QPushButton(self.widget)
        self.btn0.setObjectName(u"btn0")

        self._2.addWidget(self.btn0, 3, 1, 1, 1)

        self.btn1 = QPushButton(self.widget)
        self.btn1.setObjectName(u"btn1")

        self._2.addWidget(self.btn1, 2, 0, 1, 1)

        self.btn7 = QPushButton(self.widget)
        self.btn7.setObjectName(u"btn7")

        self._2.addWidget(self.btn7, 0, 0, 1, 1)

        self.btn6 = QPushButton(self.widget)
        self.btn6.setObjectName(u"btn6")

        self._2.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn9 = QPushButton(self.widget)
        self.btn9.setObjectName(u"btn9")

        self._2.addWidget(self.btn9, 0, 2, 1, 1)

        self.btn4 = QPushButton(self.widget)
        self.btn4.setObjectName(u"btn4")

        self._2.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn_dot = QPushButton(self.widget)
        self.btn_dot.setObjectName(u"btn_dot")

        self._2.addWidget(self.btn_dot, 3, 0, 1, 1)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"QWidget{background:rgba(255,255,255,0.8)}\n"
"QPushButton{background:transparent}")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_del_one = QPushButton(self.widget_3)
        self.btn_del_one.setObjectName(u"btn_del_one")
        icon1 = QIcon()
        icon1.addFile(u"../src/imgs/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del_one.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_del_one)

        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color:red\n"
"")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.line_3 = QFrame(self.widget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.btn_clear = QPushButton(self.widget_3)
        self.btn_clear.setObjectName(u"btn_clear")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_clear.setFont(font1)
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_clear)


        self._2.addWidget(self.widget_3, 3, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        Time.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Time)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 284, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Time.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionLenght)
        self.menuFile.addAction(self.actionStandard)
        self.menuFile.addAction(self.actionTemperature)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProperties)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFQAs)

        self.retranslateUi(Time)

        self.comboBox1.setCurrentIndex(4)
        self.comboBox2.setCurrentIndex(3)
        self.btn_clear.setDefault(False)


        QMetaObject.connectSlotsByName(Time)
    # setupUi

    def retranslateUi(self, Time):
        Time.setWindowTitle(QCoreApplication.translate("Time", u"Time", None))
        self.actionStandard.setText(QCoreApplication.translate("Time", u"Standard", None))
        self.actionTemperature.setText(QCoreApplication.translate("Time", u"Temperature", None))
        self.actionLenght.setText(QCoreApplication.translate("Time", u"Lenght", None))
        self.actionExit.setText(QCoreApplication.translate("Time", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("Time", u"About", None))
        self.actionFQAs.setText(QCoreApplication.translate("Time", u"FQAs", None))
        self.actionProperties.setText(QCoreApplication.translate("Time", u"Properties", None))
        self.actionTime.setText(QCoreApplication.translate("Time", u"Time", None))
        self.label_text.setText(QCoreApplication.translate("Time", u"0", None))
        self.comboBox1.setItemText(0, QCoreApplication.translate("Time", u"Microseconds", None))
        self.comboBox1.setItemText(1, QCoreApplication.translate("Time", u"Milliseconds", None))
        self.comboBox1.setItemText(2, QCoreApplication.translate("Time", u"Seconds", None))
        self.comboBox1.setItemText(3, QCoreApplication.translate("Time", u"Minutes", None))
        self.comboBox1.setItemText(4, QCoreApplication.translate("Time", u"Hours", None))
        self.comboBox1.setItemText(5, QCoreApplication.translate("Time", u"Days", None))
        self.comboBox1.setItemText(6, QCoreApplication.translate("Time", u"Weeks", None))
        self.comboBox1.setItemText(7, QCoreApplication.translate("Time", u"Years", None))

        self.comboBox1.setPlaceholderText("")
        self.label_result.setText(QCoreApplication.translate("Time", u"0", None))
        self.comboBox2.setItemText(0, QCoreApplication.translate("Time", u"Microseconds", None))
        self.comboBox2.setItemText(1, QCoreApplication.translate("Time", u"Milliseconds", None))
        self.comboBox2.setItemText(2, QCoreApplication.translate("Time", u"Seconds", None))
        self.comboBox2.setItemText(3, QCoreApplication.translate("Time", u"Minutes", None))
        self.comboBox2.setItemText(4, QCoreApplication.translate("Time", u"Hours", None))
        self.comboBox2.setItemText(5, QCoreApplication.translate("Time", u"Days", None))
        self.comboBox2.setItemText(6, QCoreApplication.translate("Time", u"Weeks", None))
        self.comboBox2.setItemText(7, QCoreApplication.translate("Time", u"Years", None))

        self.comboBox2.setPlaceholderText("")
        self.btn2.setText(QCoreApplication.translate("Time", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Time", u"3", None))
        self.btn8.setText(QCoreApplication.translate("Time", u"8", None))
        self.btn5.setText(QCoreApplication.translate("Time", u"5", None))
        self.btn0.setText(QCoreApplication.translate("Time", u"0", None))
        self.btn1.setText(QCoreApplication.translate("Time", u"1", None))
        self.btn7.setText(QCoreApplication.translate("Time", u"7", None))
        self.btn6.setText(QCoreApplication.translate("Time", u"6", None))
        self.btn9.setText(QCoreApplication.translate("Time", u"9", None))
        self.btn4.setText(QCoreApplication.translate("Time", u"4", None))
        self.btn_dot.setText(QCoreApplication.translate("Time", u"\u2022", None))
        self.btn_del_one.setText("")
        self.btn_clear.setText(QCoreApplication.translate("Time", u"C", None))
        self.menuFile.setTitle(QCoreApplication.translate("Time", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Time", u"Help", None))
    # retranslateUi

