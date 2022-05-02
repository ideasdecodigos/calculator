# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'properties.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Properties(object):
    def setupUi(self, Properties):
        if not Properties.objectName():
            Properties.setObjectName(u"Properties")
        Properties.resize(309, 249)
        self.centralwidget = QWidget(Properties)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:#ddd")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinBoxDecimal = QSpinBox(self.frame)
        self.spinBoxDecimal.setObjectName(u"spinBoxDecimal")
        self.spinBoxDecimal.setMaximum(20)
        self.spinBoxDecimal.setValue(4)

        self.gridLayout.addWidget(self.spinBoxDecimal, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBoxBgColor = QComboBox(self.frame)
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.setObjectName(u"comboBoxBgColor")

        self.gridLayout.addWidget(self.comboBoxBgColor, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBoxFtColor = QComboBox(self.frame)
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.setObjectName(u"comboBoxFtColor")

        self.gridLayout.addWidget(self.comboBoxFtColor, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)

        self.pushButtonReset = QPushButton(self.centralwidget)
        self.pushButtonReset.setObjectName(u"pushButtonReset")

        self.gridLayout_2.addWidget(self.pushButtonReset, 1, 0, 1, 1)

        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.gridLayout_2.addWidget(self.pushButtonSave, 1, 1, 1, 1)

        Properties.setCentralWidget(self.centralwidget)

        self.retranslateUi(Properties)

        self.comboBoxBgColor.setCurrentIndex(0)
        self.comboBoxFtColor.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Properties)
    # setupUi

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QCoreApplication.translate("Properties", u"Properties", None))
        self.label.setText(QCoreApplication.translate("Properties", u"Decimal Length:", None))
        self.label_2.setText(QCoreApplication.translate("Properties", u"Background-color:", None))
        self.comboBoxBgColor.setItemText(0, QCoreApplication.translate("Properties", u"none", None))
        self.comboBoxBgColor.setItemText(1, QCoreApplication.translate("Properties", u"white", None))
        self.comboBoxBgColor.setItemText(2, QCoreApplication.translate("Properties", u"gray", None))
        self.comboBoxBgColor.setItemText(3, QCoreApplication.translate("Properties", u"black", None))
        self.comboBoxBgColor.setItemText(4, QCoreApplication.translate("Properties", u"pink", None))
        self.comboBoxBgColor.setItemText(5, QCoreApplication.translate("Properties", u"red", None))
        self.comboBoxBgColor.setItemText(6, QCoreApplication.translate("Properties", u"darkred", None))
        self.comboBoxBgColor.setItemText(7, QCoreApplication.translate("Properties", u"dodgerblue", None))
        self.comboBoxBgColor.setItemText(8, QCoreApplication.translate("Properties", u"lightblue", None))
        self.comboBoxBgColor.setItemText(9, QCoreApplication.translate("Properties", u"blue", None))
        self.comboBoxBgColor.setItemText(10, QCoreApplication.translate("Properties", u"darkblue", None))
        self.comboBoxBgColor.setItemText(11, QCoreApplication.translate("Properties", u"green", None))
        self.comboBoxBgColor.setItemText(12, QCoreApplication.translate("Properties", u"darkgreen", None))
        self.comboBoxBgColor.setItemText(13, QCoreApplication.translate("Properties", u"lime", None))
        self.comboBoxBgColor.setItemText(14, QCoreApplication.translate("Properties", u"limegreen", None))
        self.comboBoxBgColor.setItemText(15, QCoreApplication.translate("Properties", u"yellow", None))
        self.comboBoxBgColor.setItemText(16, QCoreApplication.translate("Properties", u"orange", None))
        self.comboBoxBgColor.setItemText(17, QCoreApplication.translate("Properties", u"purple", None))
        self.comboBoxBgColor.setItemText(18, QCoreApplication.translate("Properties", u"violet", None))
        self.comboBoxBgColor.setItemText(19, QCoreApplication.translate("Properties", u"yellowgreen", None))
        self.comboBoxBgColor.setItemText(20, QCoreApplication.translate("Properties", u"fuchsia", None))
        self.comboBoxBgColor.setItemText(21, QCoreApplication.translate("Properties", u"maroon", None))
        self.comboBoxBgColor.setItemText(22, QCoreApplication.translate("Properties", u"alive", None))
        self.comboBoxBgColor.setItemText(23, QCoreApplication.translate("Properties", u"silver", None))
        self.comboBoxBgColor.setItemText(24, QCoreApplication.translate("Properties", u"navy", None))
        self.comboBoxBgColor.setItemText(25, QCoreApplication.translate("Properties", u"teal", None))
        self.comboBoxBgColor.setItemText(26, QCoreApplication.translate("Properties", u"aqua", None))
        self.comboBoxBgColor.setItemText(27, QCoreApplication.translate("Properties", u"beige", None))
        self.comboBoxBgColor.setItemText(28, QCoreApplication.translate("Properties", u"blueviolet", None))
        self.comboBoxBgColor.setItemText(29, QCoreApplication.translate("Properties", u"azure", None))
        self.comboBoxBgColor.setItemText(30, QCoreApplication.translate("Properties", u"coral", None))
        self.comboBoxBgColor.setItemText(31, QCoreApplication.translate("Properties", u"gold", None))

        self.label_3.setText(QCoreApplication.translate("Properties", u"Font-color:", None))
        self.comboBoxFtColor.setItemText(0, QCoreApplication.translate("Properties", u"red", None))
        self.comboBoxFtColor.setItemText(1, QCoreApplication.translate("Properties", u"white", None))
        self.comboBoxFtColor.setItemText(2, QCoreApplication.translate("Properties", u"black", None))
        self.comboBoxFtColor.setItemText(3, QCoreApplication.translate("Properties", u"blue", None))
        self.comboBoxFtColor.setItemText(4, QCoreApplication.translate("Properties", u"green", None))
        self.comboBoxFtColor.setItemText(5, QCoreApplication.translate("Properties", u"yellow", None))
        self.comboBoxFtColor.setItemText(6, QCoreApplication.translate("Properties", u"orange", None))
        self.comboBoxFtColor.setItemText(7, QCoreApplication.translate("Properties", u"gray", None))
        self.comboBoxFtColor.setItemText(8, QCoreApplication.translate("Properties", u"pink", None))
        self.comboBoxFtColor.setItemText(9, QCoreApplication.translate("Properties", u"purple", None))
        self.comboBoxFtColor.setItemText(10, QCoreApplication.translate("Properties", u"lime", None))
        self.comboBoxFtColor.setItemText(11, QCoreApplication.translate("Properties", u"dodgerblue", None))
        self.comboBoxFtColor.setItemText(12, QCoreApplication.translate("Properties", u"limegreen", None))
        self.comboBoxFtColor.setItemText(13, QCoreApplication.translate("Properties", u"darkred", None))

        self.pushButtonReset.setText(QCoreApplication.translate("Properties", u"Reset", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Properties", u"Save", None))
    # retranslateUi

