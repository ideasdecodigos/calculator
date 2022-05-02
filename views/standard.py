# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'standard.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Standard(object):
    def setupUi(self, Standard):
        if not Standard.objectName():
            Standard.setObjectName(u"Standard")
        Standard.resize(471, 404)
        Standard.setMaximumSize(QSize(471, 404))
        Standard.setContextMenuPolicy(Qt.CustomContextMenu)
        Standard.setStyleSheet(u"")
        self.actionTime = QAction(Standard)
        self.actionTime.setObjectName(u"actionTime")
        self.actionScientific = QAction(Standard)
        self.actionScientific.setObjectName(u"actionScientific")
        self.actionLenght = QAction(Standard)
        self.actionLenght.setObjectName(u"actionLenght")
        self.actionExit = QAction(Standard)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(Standard)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionFQAs = QAction(Standard)
        self.actionFQAs.setObjectName(u"actionFQAs")
        self.actionTemperature = QAction(Standard)
        self.actionTemperature.setObjectName(u"actionTemperature")
        self.actionProperties = QAction(Standard)
        self.actionProperties.setObjectName(u"actionProperties")
        self.centralwidget = QWidget(Standard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(255, 247, 248);")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_result = QLabel(self.widget_2)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold Condensed"])
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        self.label_result.setFont(font)
        self.label_result.setTextFormat(Qt.RichText)
        self.label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_result)

        self.label_mr = QLabel(self.widget_2)
        self.label_mr.setObjectName(u"label_mr")
        self.label_mr.setEnabled(True)
        self.label_mr.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_mr.setFont(font1)
        self.label_mr.setTextFormat(Qt.RichText)
        self.label_mr.setScaledContents(False)
        self.label_mr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_mr.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_mr)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_show = QPushButton(self.widget_3)
        self.btn_show.setObjectName(u"btn_show")
        icon = QIcon()
        icon.addFile(u"../src/imgs/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_show.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btn_show)

        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(80, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_e = QPushButton(self.widget_5)
        self.btn_e.setObjectName(u"btn_e")

        self.horizontalLayout_3.addWidget(self.btn_e)

        self.btn_clear = QPushButton(self.widget_5)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setAutoDefault(False)
        self.btn_clear.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_clear)

        self.btn_del_one = QPushButton(self.widget_5)
        self.btn_del_one.setObjectName(u"btn_del_one")
        self.btn_del_one.setBaseSize(QSize(0, 0))
        self.btn_del_one.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"../src/imgs/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del_one.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_del_one)

        self.btn_clear.raise_()
        self.btn_del_one.raise_()
        self.btn_e.raise_()

        self.verticalLayout.addWidget(self.widget_5)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn4 = QPushButton(self.widget)
        self.btn4.setObjectName(u"btn4")

        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)

        self.btn0 = QPushButton(self.widget)
        self.btn0.setObjectName(u"btn0")

        self.gridLayout.addWidget(self.btn0, 3, 1, 1, 1)

        self.btn_plus = QPushButton(self.widget)
        self.btn_plus.setObjectName(u"btn_plus")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.btn_plus.setFont(font2)
        self.btn_plus.setAutoDefault(False)
        self.btn_plus.setFlat(False)

        self.gridLayout.addWidget(self.btn_plus, 3, 3, 1, 1)

        self.btn_equal = QPushButton(self.widget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setBaseSize(QSize(0, 100))

        self.gridLayout.addWidget(self.btn_equal, 3, 4, 1, 1)

        self.btn3 = QPushButton(self.widget)
        self.btn3.setObjectName(u"btn3")

        self.gridLayout.addWidget(self.btn3, 2, 2, 1, 1)

        self.btn6 = QPushButton(self.widget)
        self.btn6.setObjectName(u"btn6")

        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)

        self.btn_mult = QPushButton(self.widget)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setFont(font2)
        self.btn_mult.setAutoDefault(False)
        self.btn_mult.setFlat(False)

        self.gridLayout.addWidget(self.btn_mult, 1, 3, 1, 1)

        self.btn_inverse = QPushButton(self.widget)
        self.btn_inverse.setObjectName(u"btn_inverse")

        self.gridLayout.addWidget(self.btn_inverse, 3, 0, 1, 1)

        self.btn2 = QPushButton(self.widget)
        self.btn2.setObjectName(u"btn2")

        self.gridLayout.addWidget(self.btn2, 2, 1, 1, 1)

        self.btn_dot = QPushButton(self.widget)
        self.btn_dot.setObjectName(u"btn_dot")

        self.gridLayout.addWidget(self.btn_dot, 3, 2, 1, 1)

        self.btn1 = QPushButton(self.widget)
        self.btn1.setObjectName(u"btn1")

        self.gridLayout.addWidget(self.btn1, 2, 0, 1, 1)

        self.btn7 = QPushButton(self.widget)
        self.btn7.setObjectName(u"btn7")

        self.gridLayout.addWidget(self.btn7, 0, 0, 1, 1)

        self.btn8 = QPushButton(self.widget)
        self.btn8.setObjectName(u"btn8")

        self.gridLayout.addWidget(self.btn8, 0, 1, 1, 1)

        self.btn_minus = QPushButton(self.widget)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setFont(font2)
        self.btn_minus.setAutoDefault(False)
        self.btn_minus.setFlat(False)

        self.gridLayout.addWidget(self.btn_minus, 2, 3, 1, 1)

        self.btn_percent = QPushButton(self.widget)
        self.btn_percent.setObjectName(u"btn_percent")

        self.gridLayout.addWidget(self.btn_percent, 2, 4, 1, 1)

        self.btn_rightp = QPushButton(self.widget)
        self.btn_rightp.setObjectName(u"btn_rightp")

        self.gridLayout.addWidget(self.btn_rightp, 0, 4, 1, 1)

        self.btn9 = QPushButton(self.widget)
        self.btn9.setObjectName(u"btn9")

        self.gridLayout.addWidget(self.btn9, 0, 2, 1, 1)

        self.btn_divide = QPushButton(self.widget)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setFont(font2)
        self.btn_divide.setAutoDefault(False)
        self.btn_divide.setFlat(False)

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn5 = QPushButton(self.widget)
        self.btn5.setObjectName(u"btn5")

        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)

        self.btn_sqrt = QPushButton(self.widget)
        self.btn_sqrt.setObjectName(u"btn_sqrt")

        self.gridLayout.addWidget(self.btn_sqrt, 1, 4, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_del_historial = QPushButton(self.page_2)
        self.btn_del_historial.setObjectName(u"btn_del_historial")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del_historial.sizePolicy().hasHeightForWidth())
        self.btn_del_historial.setSizePolicy(sizePolicy)
        self.btn_del_historial.setMaximumSize(QSize(28, 24))
        self.btn_del_historial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_del_historial.setStyleSheet(u"background:transparent;\n"
"color:red;")
        icon2 = QIcon()
        icon2.addFile(u"../src/imgs/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del_historial.setIcon(icon2)
        self.btn_del_historial.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_del_historial, 0, Qt.AlignTop)

        self.list_memory = QListWidget(self.page_2)
        self.list_memory.setObjectName(u"list_memory")
        self.list_memory.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.list_memory.setAlternatingRowColors(True)
        self.list_memory.setSpacing(3)
        self.list_memory.setWordWrap(True)

        self.horizontalLayout.addWidget(self.list_memory)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 1)

        Standard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Standard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 471, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Standard.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionScientific)
        self.menuFile.addAction(self.actionTime)
        self.menuFile.addAction(self.actionLenght)
        self.menuFile.addAction(self.actionTemperature)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProperties)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFQAs)

        self.retranslateUi(Standard)

        self.btn_clear.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)
        self.btn_plus.setDefault(False)
        self.btn_mult.setDefault(False)
        self.btn_minus.setDefault(False)
        self.btn_divide.setDefault(False)


        QMetaObject.connectSlotsByName(Standard)
    # setupUi

    def retranslateUi(self, Standard):
        Standard.setWindowTitle(QCoreApplication.translate("Standard", u"Standard", None))
        self.actionTime.setText(QCoreApplication.translate("Standard", u"Time", None))
        self.actionScientific.setText(QCoreApplication.translate("Standard", u"Scientific", None))
        self.actionLenght.setText(QCoreApplication.translate("Standard", u"Lenght", None))
        self.actionExit.setText(QCoreApplication.translate("Standard", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("Standard", u"About", None))
        self.actionFQAs.setText(QCoreApplication.translate("Standard", u"FQAs", None))
        self.actionTemperature.setText(QCoreApplication.translate("Standard", u"Temperature", None))
        self.actionProperties.setText(QCoreApplication.translate("Standard", u"Properties", None))
        self.label_result.setText("")
        self.label_mr.setText(QCoreApplication.translate("Standard", u"0", None))
        self.btn_show.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Standard", u"MC", None))
        self.pushButton.setText(QCoreApplication.translate("Standard", u"MR", None))
        self.btn_e.setText(QCoreApplication.translate("Standard", u"e", None))
        self.btn_clear.setText(QCoreApplication.translate("Standard", u"C", None))
#if QT_CONFIG(tooltip)
        self.btn_del_one.setToolTip(QCoreApplication.translate("Standard", u"Back", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_one.setText("")
        self.btn4.setText(QCoreApplication.translate("Standard", u"4", None))
        self.btn0.setText(QCoreApplication.translate("Standard", u"0", None))
        self.btn_plus.setText(QCoreApplication.translate("Standard", u"+", None))
        self.btn_equal.setText(QCoreApplication.translate("Standard", u"=", None))
        self.btn3.setText(QCoreApplication.translate("Standard", u"3", None))
        self.btn6.setText(QCoreApplication.translate("Standard", u"6", None))
        self.btn_mult.setText(QCoreApplication.translate("Standard", u"*", None))
        self.btn_inverse.setText(QCoreApplication.translate("Standard", u"\u00b1", None))
        self.btn2.setText(QCoreApplication.translate("Standard", u"2", None))
        self.btn_dot.setText(QCoreApplication.translate("Standard", u".", None))
        self.btn1.setText(QCoreApplication.translate("Standard", u"1", None))
        self.btn7.setText(QCoreApplication.translate("Standard", u"7", None))
        self.btn8.setText(QCoreApplication.translate("Standard", u"8", None))
        self.btn_minus.setText(QCoreApplication.translate("Standard", u"-", None))
        self.btn_percent.setText(QCoreApplication.translate("Standard", u"%", None))
        self.btn_rightp.setText(QCoreApplication.translate("Standard", u"( )", None))
        self.btn9.setText(QCoreApplication.translate("Standard", u"9", None))
        self.btn_divide.setText(QCoreApplication.translate("Standard", u"/", None))
        self.btn5.setText(QCoreApplication.translate("Standard", u"5", None))
        self.btn_sqrt.setText(QCoreApplication.translate("Standard", u"\u221a", None))
        self.btn_del_historial.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("Standard", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Standard", u"Help", None))
    # retranslateUi

