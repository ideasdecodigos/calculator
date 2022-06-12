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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Properties(object):
    def setupUi(self, Properties):
        if not Properties.objectName():
            Properties.setObjectName(u"Properties")
        Properties.resize(426, 425)
        self.centralwidget = QWidget(Properties)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setItalic(True)
        self.centralwidget.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_8 = QWidget(self.groupBox)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_3 = QVBoxLayout(self.widget_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_8)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label.setPalette(palette)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.widget_8)
        self.label_2.setObjectName(u"label_2")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_2.setPalette(palette1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_3.setPalette(palette2)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_5.setPalette(palette3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_5)


        self.horizontalLayout_7.addWidget(self.widget_8)

        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout = QVBoxLayout(self.widget_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spinBoxDecimal = QSpinBox(self.widget_7)
        self.spinBoxDecimal.setObjectName(u"spinBoxDecimal")
        self.spinBoxDecimal.setMaximum(20)
        self.spinBoxDecimal.setValue(4)

        self.horizontalLayout_8.addWidget(self.spinBoxDecimal)

        self.line = QFrame(self.widget_7)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)


        self.verticalLayout.addWidget(self.widget_7)

        self.widget = QWidget(self.widget_6)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnBgColor = QToolButton(self.widget)
        self.btnBgColor.setObjectName(u"btnBgColor")
        self.btnBgColor.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btnBgColor)

        self.txtBgColor = QLineEdit(self.widget)
        self.txtBgColor.setObjectName(u"txtBgColor")
        self.txtBgColor.setEchoMode(QLineEdit.Normal)
        self.txtBgColor.setReadOnly(True)

        self.horizontalLayout.addWidget(self.txtBgColor)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_6)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnFrColor = QToolButton(self.widget_2)
        self.btnFrColor.setObjectName(u"btnFrColor")
        self.btnFrColor.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.btnFrColor)

        self.txtFrColor = QLineEdit(self.widget_2)
        self.txtFrColor.setObjectName(u"txtFrColor")
        self.txtFrColor.setEchoMode(QLineEdit.Normal)
        self.txtFrColor.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.txtFrColor)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnFont = QToolButton(self.widget_5)
        self.btnFont.setObjectName(u"btnFont")
        self.btnFont.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.btnFont)

        self.lblFont = QLabel(self.widget_5)
        self.lblFont.setObjectName(u"lblFont")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.lblFont.setPalette(palette4)

        self.horizontalLayout_6.addWidget(self.lblFont)


        self.verticalLayout.addWidget(self.widget_5)


        self.horizontalLayout_7.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.TextAloud = QGroupBox(self.centralwidget)
        self.TextAloud.setObjectName(u"TextAloud")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(True)
        self.TextAloud.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.TextAloud)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnEnWoman = QRadioButton(self.TextAloud)
        self.btnEnWoman.setObjectName(u"btnEnWoman")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.btnEnWoman.setPalette(palette5)
        self.btnEnWoman.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btnEnWoman)

        self.btnEnMan = QRadioButton(self.TextAloud)
        self.btnEnMan.setObjectName(u"btnEnMan")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.btnEnMan.setPalette(palette6)

        self.horizontalLayout_3.addWidget(self.btnEnMan)

        self.btnEs = QRadioButton(self.TextAloud)
        self.btnEs.setObjectName(u"btnEs")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.btnEs.setPalette(palette7)

        self.horizontalLayout_3.addWidget(self.btnEs)


        self.verticalLayout_4.addWidget(self.TextAloud)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sliderRate = QSlider(self.widget_4)
        self.sliderRate.setObjectName(u"sliderRate")
        self.sliderRate.setToolTipDuration(3)
        self.sliderRate.setMinimum(100)
        self.sliderRate.setMaximum(200)
        self.sliderRate.setSingleStep(5)
        self.sliderRate.setValue(150)
        self.sliderRate.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.sliderRate)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_4.setPalette(palette8)
        self.label_4.setToolTipDuration(-2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonReset = QPushButton(self.widget_3)
        self.pushButtonReset.setObjectName(u"pushButtonReset")

        self.horizontalLayout_4.addWidget(self.pushButtonReset)

        self.pushButtonSave = QPushButton(self.widget_3)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_4.addWidget(self.pushButtonSave)


        self.verticalLayout_4.addWidget(self.widget_3)

        Properties.setCentralWidget(self.centralwidget)

        self.retranslateUi(Properties)

        QMetaObject.connectSlotsByName(Properties)
    # setupUi

    def retranslateUi(self, Properties):
        Properties.setWindowTitle(QCoreApplication.translate("Properties", u"Properties", None))
        self.groupBox.setTitle(QCoreApplication.translate("Properties", u"Appearance", None))
        self.label.setText(QCoreApplication.translate("Properties", u"Decimal Length:", None))
        self.label_2.setText(QCoreApplication.translate("Properties", u"Background-color:", None))
        self.label_3.setText(QCoreApplication.translate("Properties", u"Font-color:", None))
        self.label_5.setText(QCoreApplication.translate("Properties", u"Font-Family:", None))
        self.btnBgColor.setText(QCoreApplication.translate("Properties", u"...", None))
        self.btnFrColor.setText(QCoreApplication.translate("Properties", u"...", None))
        self.btnFont.setText(QCoreApplication.translate("Properties", u"...", None))
        self.lblFont.setText(QCoreApplication.translate("Properties", u"Fonts Example", None))
        self.TextAloud.setTitle(QCoreApplication.translate("Properties", u"Text Aloud Language", None))
        self.btnEnWoman.setText(QCoreApplication.translate("Properties", u"English Female", None))
        self.btnEnMan.setText(QCoreApplication.translate("Properties", u"English Male", None))
        self.btnEs.setText(QCoreApplication.translate("Properties", u"Spanish", None))
#if QT_CONFIG(tooltip)
        self.sliderRate.setToolTip(QCoreApplication.translate("Properties", u"Rate", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Properties", u"Rate:", None))
        self.pushButtonReset.setText(QCoreApplication.translate("Properties", u"Reset", None))
        self.pushButtonSave.setText(QCoreApplication.translate("Properties", u"Save", None))
    # retranslateUi

