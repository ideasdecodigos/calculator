# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scientific.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStackedWidget, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)
from src.files import icons

class Ui_Scientific(object):
    def setupUi(self, Scientific):
        if not Scientific.objectName():
            Scientific.setObjectName(u"Scientific")
        Scientific.resize(643, 537)
        icon = QIcon()
        icon.addFile(u":/icons/scientific.png", QSize(), QIcon.Normal, QIcon.Off)
        Scientific.setWindowIcon(icon)
        Scientific.setAutoFillBackground(True)
        Scientific.setIconSize(QSize(30, 30))
        self.actionStandard = QAction(Scientific)
        self.actionStandard.setObjectName(u"actionStandard")
        icon1 = QIcon()
        icon1.addFile(u":/icons/standard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStandard.setIcon(icon1)
        self.actionLength = QAction(Scientific)
        self.actionLength.setObjectName(u"actionLength")
        icon2 = QIcon()
        icon2.addFile(u":/icons/length.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLength.setIcon(icon2)
        self.actionTime = QAction(Scientific)
        self.actionTime.setObjectName(u"actionTime")
        icon3 = QIcon()
        icon3.addFile(u":/icons/time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTime.setIcon(icon3)
        self.actionTemperature = QAction(Scientific)
        self.actionTemperature.setObjectName(u"actionTemperature")
        icon4 = QIcon()
        icon4.addFile(u":/icons/temp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTemperature.setIcon(icon4)
        self.actionProperties = QAction(Scientific)
        self.actionProperties.setObjectName(u"actionProperties")
        icon5 = QIcon()
        icon5.addFile(u":/icons/tool.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionProperties.setIcon(icon5)
        self.actionPlay_Result = QAction(Scientific)
        self.actionPlay_Result.setObjectName(u"actionPlay_Result")
        icon6 = QIcon()
        icon6.addFile(u":/icons/valumeOff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPlay_Result.setIcon(icon6)
        self.actionExit = QAction(Scientific)
        self.actionExit.setObjectName(u"actionExit")
        icon7 = QIcon()
        icon7.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionAbout = QAction(Scientific)
        self.actionAbout.setObjectName(u"actionAbout")
        icon8 = QIcon()
        icon8.addFile(u":/icons/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbout.setIcon(icon8)
        self.actionFQAs = QAction(Scientific)
        self.actionFQAs.setObjectName(u"actionFQAs")
        icon9 = QIcon()
        icon9.addFile(u":/icons/faqs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFQAs.setIcon(icon9)
        self.actionDict_input = QAction(Scientific)
        self.actionDict_input.setObjectName(u"actionDict_input")
        icon10 = QIcon()
        icon10.addFile(u":/icons/microOff.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDict_input.setIcon(icon10)
        self.widget = QWidget(Scientific)
        self.widget.setObjectName(u"widget")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, -1, 611, 491))
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.widget_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_result = QLabel(self.frame_2)
        self.label_result.setObjectName(u"label_result")
        font = QFont()
        font.setFamilies([u"Roboto Slab"])
        font.setPointSize(26)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_result.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_result)

        self.label_mr = QLabel(self.frame_2)
        self.label_mr.setObjectName(u"label_mr")
        self.label_mr.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(20)
        self.label_mr.setFont(font1)
        self.label_mr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_mr.setWordWrap(True)
        self.label_mr.setMargin(3)
        self.label_mr.setIndent(3)
        self.label_mr.setTextInteractionFlags(Qt.TextEditable)

        self.verticalLayout.addWidget(self.label_mr)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.qglayout = QGroupBox(self.widget_4)
        self.qglayout.setObjectName(u"qglayout")
        self.qglayout.setStyleSheet(u"")
        self.qglayout.setFlat(False)
        self.gridLayout_4 = QGridLayout(self.qglayout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_log1p = QPushButton(self.qglayout)
        self.btn_log1p.setObjectName(u"btn_log1p")
        self.btn_log1p.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.gridLayout_4.addWidget(self.btn_log1p, 11, 6, 1, 1)

        self.btn_ln = QPushButton(self.qglayout)
        self.btn_ln.setObjectName(u"btn_ln")
        self.btn_ln.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_ln.setAutoDefault(False)
        self.btn_ln.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_ln, 11, 3, 1, 1)

        self.btn_equal = QPushButton(self.qglayout)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.gridLayout_4.addWidget(self.btn_equal, 11, 10, 1, 2)

        self.btn_pi = QPushButton(self.qglayout)
        self.btn_pi.setObjectName(u"btn_pi")
        self.btn_pi.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.btn_pi.setAutoDefault(False)
        self.btn_pi.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_pi, 6, 6, 1, 1)

        self.btn_c = QPushButton(self.qglayout)
        self.btn_c.setObjectName(u"btn_c")
        self.btn_c.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_c.setAutoDefault(False)
        self.btn_c.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_c, 6, 9, 1, 1)

        self.btn_sqrt = QPushButton(self.qglayout)
        self.btn_sqrt.setObjectName(u"btn_sqrt")
        self.btn_sqrt.setStyleSheet(u"background:limegreen;")
        self.btn_sqrt.setAutoDefault(False)
        self.btn_sqrt.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sqrt, 6, 5, 1, 1)

        self.btn_less = QPushButton(self.qglayout)
        self.btn_less.setObjectName(u"btn_less")
        self.btn_less.setStyleSheet(u"background-color: rgb(66, 205, 255);")

        self.gridLayout_4.addWidget(self.btn_less, 8, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.qglayout)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, -1)
        self.btn_rd_bin = QRadioButton(self.groupBox_2)
        self.btn_rd_bin.setObjectName(u"btn_rd_bin")

        self.horizontalLayout_3.addWidget(self.btn_rd_bin)

        self.btn_rd_oct = QRadioButton(self.groupBox_2)
        self.btn_rd_oct.setObjectName(u"btn_rd_oct")

        self.horizontalLayout_3.addWidget(self.btn_rd_oct)

        self.btn_rd_dec = QRadioButton(self.groupBox_2)
        self.btn_rd_dec.setObjectName(u"btn_rd_dec")
        self.btn_rd_dec.setChecked(True)

        self.horizontalLayout_3.addWidget(self.btn_rd_dec)

        self.btn_rd_hex = QRadioButton(self.groupBox_2)
        self.btn_rd_hex.setObjectName(u"btn_rd_hex")

        self.horizontalLayout_3.addWidget(self.btn_rd_hex)

        self.btn_rd_fe = QRadioButton(self.groupBox_2)
        self.btn_rd_fe.setObjectName(u"btn_rd_fe")

        self.horizontalLayout_3.addWidget(self.btn_rd_fe)


        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 5)

        self.btn_sinh = QPushButton(self.qglayout)
        self.btn_sinh.setObjectName(u"btn_sinh")
        self.btn_sinh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_sinh.setAutoDefault(False)
        self.btn_sinh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sinh, 9, 3, 1, 1)

        self.btn_mean = QPushButton(self.qglayout)
        self.btn_mean.setObjectName(u"btn_mean")
        self.btn_mean.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_mean, 13, 4, 1, 1)

        self.btn00 = QPushButton(self.qglayout)
        self.btn00.setObjectName(u"btn00")
        self.btn00.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn00.setAutoDefault(False)
        self.btn00.setFlat(False)

        self.gridLayout_4.addWidget(self.btn00, 10, 9, 1, 1)

        self.btn_cos = QPushButton(self.qglayout)
        self.btn_cos.setObjectName(u"btn_cos")
        self.btn_cos.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_cos.setAutoDefault(False)
        self.btn_cos.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_cos, 9, 1, 1, 1)

        self.btn_log2 = QPushButton(self.qglayout)
        self.btn_log2.setObjectName(u"btn_log2")
        self.btn_log2.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_log2.setAutoDefault(False)
        self.btn_log2.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_log2, 11, 5, 1, 1)

        self.btn5 = QPushButton(self.qglayout)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn5.setAutoDefault(False)
        self.btn5.setFlat(False)

        self.gridLayout_4.addWidget(self.btn5, 8, 9, 1, 1)

        self.btn_m_minus = QPushButton(self.qglayout)
        self.btn_m_minus.setObjectName(u"btn_m_minus")
        self.btn_m_minus.setStyleSheet(u"background-color: rgb(255, 179, 169)")

        self.gridLayout_4.addWidget(self.btn_m_minus, 0, 8, 1, 1)

        self.btn_yroot = QPushButton(self.qglayout)
        self.btn_yroot.setObjectName(u"btn_yroot")

        self.gridLayout_4.addWidget(self.btn_yroot, 8, 4, 1, 1)

        self.btn_mode = QPushButton(self.qglayout)
        self.btn_mode.setObjectName(u"btn_mode")
        self.btn_mode.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_mode, 13, 6, 1, 1)

        self.btn_DEG = QPushButton(self.qglayout)
        self.btn_DEG.setObjectName(u"btn_DEG")
        self.btn_DEG.setToolTipDuration(3)
        self.btn_DEG.setStyleSheet(u"background-color: rgb(255, 189, 250);")
        self.btn_DEG.setAutoDefault(False)
        self.btn_DEG.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_DEG, 13, 10, 1, 1)

        self.btn1 = QPushButton(self.qglayout)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn1.setAutoDefault(False)
        self.btn1.setFlat(False)

        self.gridLayout_4.addWidget(self.btn1, 9, 8, 1, 1)

        self.btn_ceil = QPushButton(self.qglayout)
        self.btn_ceil.setObjectName(u"btn_ceil")
        self.btn_ceil.setStyleSheet(u"background-color: rgb(223, 223, 0);")
        self.btn_ceil.setAutoDefault(False)
        self.btn_ceil.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_ceil, 12, 4, 1, 1)

        self.btn_not_equals = QPushButton(self.qglayout)
        self.btn_not_equals.setObjectName(u"btn_not_equals")
        self.btn_not_equals.setStyleSheet(u"background-color: rgb(66, 205, 255);")

        self.gridLayout_4.addWidget(self.btn_not_equals, 6, 1, 1, 1)

        self.btn_ce = QPushButton(self.qglayout)
        self.btn_ce.setObjectName(u"btn_ce")
        self.btn_ce.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.btn_ce.setAutoDefault(False)
        self.btn_ce.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_ce, 6, 10, 1, 1)

        self.btn_comma = QPushButton(self.qglayout)
        self.btn_comma.setObjectName(u"btn_comma")
        self.btn_comma.setEnabled(True)
        self.btn_comma.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout_4.addWidget(self.btn_comma, 13, 8, 1, 1)

        self.btn000 = QPushButton(self.qglayout)
        self.btn000.setObjectName(u"btn000")
        self.btn000.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn000.setAutoDefault(False)
        self.btn000.setFlat(False)

        self.gridLayout_4.addWidget(self.btn000, 10, 10, 1, 1)

        self.btn_max = QPushButton(self.qglayout)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_max, 13, 1, 1, 1)

        self.btn_less_than = QPushButton(self.qglayout)
        self.btn_less_than.setObjectName(u"btn_less_than")
        self.btn_less_than.setStyleSheet(u"background-color: rgb(66, 205, 255);")

        self.gridLayout_4.addWidget(self.btn_less_than, 7, 0, 1, 1)

        self.btn_ms = QPushButton(self.qglayout)
        self.btn_ms.setObjectName(u"btn_ms")
        self.btn_ms.setStyleSheet(u"background-color: rgb(255, 179, 169)")

        self.gridLayout_4.addWidget(self.btn_ms, 0, 9, 1, 1)

        self.btn_expm1 = QPushButton(self.qglayout)
        self.btn_expm1.setObjectName(u"btn_expm1")
        self.btn_expm1.setStyleSheet(u"background:limegreen;")
        self.btn_expm1.setAutoDefault(False)
        self.btn_expm1.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_expm1, 10, 6, 1, 1)

        self.btn_parenthesis = QPushButton(self.qglayout)
        self.btn_parenthesis.setObjectName(u"btn_parenthesis")
        self.btn_parenthesis.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.btn_parenthesis.setAutoDefault(False)
        self.btn_parenthesis.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_parenthesis, 6, 8, 1, 1)

        self.btn9 = QPushButton(self.qglayout)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn9.setAutoDefault(False)
        self.btn9.setFlat(False)

        self.gridLayout_4.addWidget(self.btn9, 7, 10, 1, 1)

        self.btn_cuberoot = QPushButton(self.qglayout)
        self.btn_cuberoot.setObjectName(u"btn_cuberoot")
        self.btn_cuberoot.setStyleSheet(u"background:limegreen;")
        self.btn_cuberoot.setAutoDefault(False)
        self.btn_cuberoot.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_cuberoot, 7, 4, 1, 1)

        self.btn0 = QPushButton(self.qglayout)
        self.btn0.setObjectName(u"btn0")
        self.btn0.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn0.setAutoDefault(False)
        self.btn0.setFlat(False)

        self.gridLayout_4.addWidget(self.btn0, 10, 8, 1, 1)

        self.btn_prod = QPushButton(self.qglayout)
        self.btn_prod.setObjectName(u"btn_prod")
        self.btn_prod.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_prod, 13, 3, 1, 1)

        self.btn6 = QPushButton(self.qglayout)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn6.setAutoDefault(False)
        self.btn6.setFlat(False)

        self.gridLayout_4.addWidget(self.btn6, 8, 10, 1, 1)

        self.btn_minus = QPushButton(self.qglayout)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.btn_minus.setAutoDefault(False)
        self.btn_minus.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_minus, 9, 11, 1, 1)

        self.btn_min = QPushButton(self.qglayout)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_min, 13, 0, 1, 1)

        self.btn_back = QPushButton(self.qglayout)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        icon11 = QIcon()
        icon11.addFile(u":/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_back.setIcon(icon11)
        self.btn_back.setAutoDefault(False)
        self.btn_back.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_back, 6, 11, 1, 1)

        self.btn_m_show = QPushButton(self.qglayout)
        self.btn_m_show.setObjectName(u"btn_m_show")
        self.btn_m_show.setStyleSheet(u"background-color: rgb(255, 169, 185);")

        self.gridLayout_4.addWidget(self.btn_m_show, 0, 10, 1, 1)

        self.btn_RAD = QPushButton(self.qglayout)
        self.btn_RAD.setObjectName(u"btn_RAD")
        self.btn_RAD.setToolTipDuration(3)
        self.btn_RAD.setStyleSheet(u"background-color: rgb(255, 189, 250);")
        self.btn_RAD.setAutoDefault(False)
        self.btn_RAD.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_RAD, 13, 9, 1, 1)

        self.btn_gma = QPushButton(self.qglayout)
        self.btn_gma.setObjectName(u"btn_gma")
        self.btn_gma.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_gma.setAutoDefault(False)
        self.btn_gma.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_gma, 11, 1, 1, 1)

        self.btn_lgma = QPushButton(self.qglayout)
        self.btn_lgma.setObjectName(u"btn_lgma")
        self.btn_lgma.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_lgma.setAutoDefault(False)
        self.btn_lgma.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_lgma, 11, 2, 1, 1)

        self.btn_floor = QPushButton(self.qglayout)
        self.btn_floor.setObjectName(u"btn_floor")
        self.btn_floor.setStyleSheet(u"background-color: rgb(223, 223, 0);")
        self.btn_floor.setAutoDefault(False)
        self.btn_floor.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_floor, 12, 3, 1, 1)

        self.btn_sin = QPushButton(self.qglayout)
        self.btn_sin.setObjectName(u"btn_sin")
        self.btn_sin.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_sin.setAutoDefault(False)
        self.btn_sin.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sin, 9, 0, 1, 1)

        self.btn_exp = QPushButton(self.qglayout)
        self.btn_exp.setObjectName(u"btn_exp")
        self.btn_exp.setStyleSheet(u"background:limegreen;")
        self.btn_exp.setAutoDefault(False)
        self.btn_exp.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_exp, 9, 6, 1, 1)

        self.btn_2X = QPushButton(self.qglayout)
        self.btn_2X.setObjectName(u"btn_2X")
        self.btn_2X.setStyleSheet(u"background:limegreen;")
        self.btn_2X.setAutoDefault(False)
        self.btn_2X.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_2X, 10, 7, 1, 1)

        self.btn_gcd = QPushButton(self.qglayout)
        self.btn_gcd.setObjectName(u"btn_gcd")
        self.btn_gcd.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_gcd, 12, 7, 1, 1)

        self.btn_and = QPushButton(self.qglayout)
        self.btn_and.setObjectName(u"btn_and")
        self.btn_and.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_and, 6, 2, 1, 1)

        self.btn_frexp = QPushButton(self.qglayout)
        self.btn_frexp.setObjectName(u"btn_frexp")
        self.btn_frexp.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_frexp, 12, 9, 1, 1)

        self.btn_mult = QPushButton(self.qglayout)
        self.btn_mult.setObjectName(u"btn_mult")
        self.btn_mult.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.btn_mult.setAutoDefault(False)
        self.btn_mult.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_mult, 8, 11, 1, 1)

        self.btn_atanh = QPushButton(self.qglayout)
        self.btn_atanh.setObjectName(u"btn_atanh")
        self.btn_atanh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_atanh.setAutoDefault(False)
        self.btn_atanh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_atanh, 10, 5, 1, 1)

        self.btn_greater = QPushButton(self.qglayout)
        self.btn_greater.setObjectName(u"btn_greater")
        self.btn_greater.setStyleSheet(u"background-color: rgb(66, 205, 255);")

        self.gridLayout_4.addWidget(self.btn_greater, 8, 1, 1, 1)

        self.btn_round = QPushButton(self.qglayout)
        self.btn_round.setObjectName(u"btn_round")
        self.btn_round.setStyleSheet(u"background-color: rgb(223, 223, 0);")

        self.gridLayout_4.addWidget(self.btn_round, 12, 5, 1, 1)

        self.btn3 = QPushButton(self.qglayout)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn3.setAutoDefault(False)
        self.btn3.setFlat(False)

        self.gridLayout_4.addWidget(self.btn3, 9, 10, 1, 1)

        self.btn_asin = QPushButton(self.qglayout)
        self.btn_asin.setObjectName(u"btn_asin")
        self.btn_asin.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_asin.setAutoDefault(False)
        self.btn_asin.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_asin, 10, 0, 1, 1)

        self.btn_sqrtroot = QPushButton(self.qglayout)
        self.btn_sqrtroot.setObjectName(u"btn_sqrtroot")
        self.btn_sqrtroot.setStyleSheet(u"background:limegreen;")
        self.btn_sqrtroot.setAutoDefault(False)
        self.btn_sqrtroot.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sqrtroot, 6, 4, 1, 1)

        self.btn_mr = QPushButton(self.qglayout)
        self.btn_mr.setObjectName(u"btn_mr")
        self.btn_mr.setStyleSheet(u"background-color: rgb(255, 179, 169)")

        self.gridLayout_4.addWidget(self.btn_mr, 0, 6, 1, 1)

        self.btn_fabs = QPushButton(self.qglayout)
        self.btn_fabs.setObjectName(u"btn_fabs")
        self.btn_fabs.setStyleSheet(u"background-color: rgb(223, 223, 0);")

        self.gridLayout_4.addWidget(self.btn_fabs, 12, 2, 1, 1)

        self.btn_tan = QPushButton(self.qglayout)
        self.btn_tan.setObjectName(u"btn_tan")
        self.btn_tan.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_tan.setAutoDefault(False)
        self.btn_tan.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_tan, 9, 2, 1, 1)

        self.btn2 = QPushButton(self.qglayout)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn2.setAutoDefault(False)
        self.btn2.setFlat(False)

        self.gridLayout_4.addWidget(self.btn2, 9, 9, 1, 1)

        self.btn_atan2 = QPushButton(self.qglayout)
        self.btn_atan2.setObjectName(u"btn_atan2")

        self.gridLayout_4.addWidget(self.btn_atan2, 11, 0, 1, 1)

        self.btn_lcm = QPushButton(self.qglayout)
        self.btn_lcm.setObjectName(u"btn_lcm")
        self.btn_lcm.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_lcm, 12, 8, 1, 1)

        self.btn_asinh = QPushButton(self.qglayout)
        self.btn_asinh.setObjectName(u"btn_asinh")
        self.btn_asinh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_asinh.setAutoDefault(False)
        self.btn_asinh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_asinh, 10, 3, 1, 1)

        self.btn_acos = QPushButton(self.qglayout)
        self.btn_acos.setObjectName(u"btn_acos")
        self.btn_acos.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_acos.setAutoDefault(False)
        self.btn_acos.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_acos, 10, 1, 1, 1)

        self.btn_rand = QPushButton(self.qglayout)
        self.btn_rand.setObjectName(u"btn_rand")
        self.btn_rand.setStyleSheet(u"background-color: rgb(0, 220, 106);")

        self.gridLayout_4.addWidget(self.btn_rand, 13, 11, 1, 1)

        self.btn_1dividedX = QPushButton(self.qglayout)
        self.btn_1dividedX.setObjectName(u"btn_1dividedX")
        self.btn_1dividedX.setStyleSheet(u"background:limegreen;")
        self.btn_1dividedX.setAutoDefault(False)
        self.btn_1dividedX.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_1dividedX, 9, 7, 1, 1)

        self.btn_percent = QPushButton(self.qglayout)
        self.btn_percent.setObjectName(u"btn_percent")
        self.btn_percent.setStyleSheet(u"background:limegreen;")
        self.btn_percent.setAutoDefault(False)
        self.btn_percent.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_percent, 8, 7, 1, 1)

        self.btn_medn = QPushButton(self.qglayout)
        self.btn_medn.setObjectName(u"btn_medn")
        self.btn_medn.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_medn, 13, 5, 1, 1)

        self.btn_not = QPushButton(self.qglayout)
        self.btn_not.setObjectName(u"btn_not")
        self.btn_not.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_not, 8, 2, 1, 1)

        self.btn_e = QPushButton(self.qglayout)
        self.btn_e.setObjectName(u"btn_e")
        self.btn_e.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.btn_e.setAutoDefault(False)
        self.btn_e.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_e, 8, 6, 1, 1)

        self.btn_sqrtN = QPushButton(self.qglayout)
        self.btn_sqrtN.setObjectName(u"btn_sqrtN")
        self.btn_sqrtN.setStyleSheet(u"background:limegreen;")
        self.btn_sqrtN.setAutoDefault(False)
        self.btn_sqrtN.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sqrtN, 8, 5, 1, 1)

        self.btn_divide = QPushButton(self.qglayout)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.btn_divide.setAutoDefault(False)
        self.btn_divide.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_divide, 7, 11, 1, 1)

        self.btn_cosh = QPushButton(self.qglayout)
        self.btn_cosh.setObjectName(u"btn_cosh")
        self.btn_cosh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_cosh.setAutoDefault(False)
        self.btn_cosh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_cosh, 9, 4, 1, 1)

        self.btn_mod = QPushButton(self.qglayout)
        self.btn_mod.setObjectName(u"btn_mod")
        self.btn_mod.setStyleSheet(u"background:limegreen;")
        self.btn_mod.setAutoDefault(False)
        self.btn_mod.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_mod, 6, 7, 1, 1)

        self.btn_dot = QPushButton(self.qglayout)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.btn_dot.setAutoDefault(False)
        self.btn_dot.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_dot, 11, 9, 1, 1)

        self.btn_atan = QPushButton(self.qglayout)
        self.btn_atan.setObjectName(u"btn_atan")
        self.btn_atan.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_atan.setAutoDefault(False)
        self.btn_atan.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_atan, 10, 2, 1, 1)

        self.btn_tanh = QPushButton(self.qglayout)
        self.btn_tanh.setObjectName(u"btn_tanh")
        self.btn_tanh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_tanh.setAutoDefault(False)
        self.btn_tanh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_tanh, 9, 5, 1, 1)

        self.btn_historial_show = QPushButton(self.qglayout)
        self.btn_historial_show.setObjectName(u"btn_historial_show")
        palette = QPalette()
        brush = QBrush(QColor(255, 169, 185, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush3 = QBrush(QColor(255, 0, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush4 = QBrush(QColor(120, 120, 120, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush3)
        self.btn_historial_show.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Roboto Black"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.btn_historial_show.setFont(font2)
        self.btn_historial_show.setStyleSheet(u"background-color: rgb(255, 169, 185);")
        icon12 = QIcon()
        icon12.addFile(u":/icons/history.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_historial_show.setIcon(icon12)
        self.btn_historial_show.setAutoDefault(False)
        self.btn_historial_show.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_historial_show, 0, 11, 1, 1)

        self.btn4 = QPushButton(self.qglayout)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn4.setAutoDefault(False)
        self.btn4.setFlat(False)

        self.gridLayout_4.addWidget(self.btn4, 8, 8, 1, 1)

        self.btn_hypot = QPushButton(self.qglayout)
        self.btn_hypot.setObjectName(u"btn_hypot")
        self.btn_hypot.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_hypot, 13, 7, 1, 1)

        self.btn_comb = QPushButton(self.qglayout)
        self.btn_comb.setObjectName(u"btn_comb")
        self.btn_comb.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_comb, 12, 6, 1, 1)

        self.btn_trunc = QPushButton(self.qglayout)
        self.btn_trunc.setObjectName(u"btn_trunc")
        self.btn_trunc.setStyleSheet(u"background-color: rgb(223, 223, 0);")
        self.btn_trunc.setAutoDefault(False)
        self.btn_trunc.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_trunc, 12, 0, 1, 1)

        self.btn_10powX = QPushButton(self.qglayout)
        self.btn_10powX.setObjectName(u"btn_10powX")
        self.btn_10powX.setStyleSheet(u"background:limegreen;")
        self.btn_10powX.setAutoDefault(False)
        self.btn_10powX.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_10powX, 11, 7, 1, 1)

        self.btn_greater_than = QPushButton(self.qglayout)
        self.btn_greater_than.setObjectName(u"btn_greater_than")
        self.btn_greater_than.setStyleSheet(u"background-color: rgb(66, 205, 255);")

        self.gridLayout_4.addWidget(self.btn_greater_than, 7, 1, 1, 1)

        self.btn7 = QPushButton(self.qglayout)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn7.setAutoDefault(False)
        self.btn7.setFlat(False)

        self.gridLayout_4.addWidget(self.btn7, 7, 8, 1, 1)

        self.btn_tau = QPushButton(self.qglayout)
        self.btn_tau.setObjectName(u"btn_tau")
        self.btn_tau.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.btn_tau.setAutoDefault(False)
        self.btn_tau.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_tau, 7, 6, 1, 1)

        self.btn_equals_equals = QPushButton(self.qglayout)
        self.btn_equals_equals.setObjectName(u"btn_equals_equals")

        self.gridLayout_4.addWidget(self.btn_equals_equals, 6, 0, 1, 1)

        self.btn_sum = QPushButton(self.qglayout)
        self.btn_sum.setObjectName(u"btn_sum")
        self.btn_sum.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.btn_sum.setAutoDefault(False)
        self.btn_sum.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sum, 13, 2, 1, 1)

        self.btn_perm = QPushButton(self.qglayout)
        self.btn_perm.setObjectName(u"btn_perm")
        self.btn_perm.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_perm, 12, 11, 1, 1)

        self.btn_acosh = QPushButton(self.qglayout)
        self.btn_acosh.setObjectName(u"btn_acosh")
        self.btn_acosh.setStyleSheet(u"background-color: rgb(255, 250, 199);")
        self.btn_acosh.setAutoDefault(False)
        self.btn_acosh.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_acosh, 10, 4, 1, 1)

        self.btn_sqrt3 = QPushButton(self.qglayout)
        self.btn_sqrt3.setObjectName(u"btn_sqrt3")
        self.btn_sqrt3.setStyleSheet(u"background:limegreen;")
        self.btn_sqrt3.setAutoDefault(False)
        self.btn_sqrt3.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_sqrt3, 7, 5, 1, 1)

        self.btn_factorial = QPushButton(self.qglayout)
        self.btn_factorial.setObjectName(u"btn_factorial")
        self.btn_factorial.setStyleSheet(u"background:limegreen;")
        self.btn_factorial.setAutoDefault(False)
        self.btn_factorial.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_factorial, 7, 7, 1, 1)

        self.btn_inverse = QPushButton(self.qglayout)
        self.btn_inverse.setObjectName(u"btn_inverse")
        self.btn_inverse.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.btn_inverse.setAutoDefault(False)
        self.btn_inverse.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_inverse, 11, 8, 1, 1)

        self.btn_plus = QPushButton(self.qglayout)
        self.btn_plus.setObjectName(u"btn_plus")
        self.btn_plus.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.btn_plus.setAutoDefault(False)
        self.btn_plus.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_plus, 10, 11, 1, 1)

        self.btn_mc = QPushButton(self.qglayout)
        self.btn_mc.setObjectName(u"btn_mc")

        self.gridLayout_4.addWidget(self.btn_mc, 0, 5, 1, 1)

        self.btn_log = QPushButton(self.qglayout)
        self.btn_log.setObjectName(u"btn_log")
        self.btn_log.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.btn_log.setAutoDefault(False)
        self.btn_log.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_log, 11, 4, 1, 1)

        self.btn_abs = QPushButton(self.qglayout)
        self.btn_abs.setObjectName(u"btn_abs")
        self.btn_abs.setStyleSheet(u"background-color: rgb(223, 223, 0);")
        self.btn_abs.setAutoDefault(False)
        self.btn_abs.setFlat(False)

        self.gridLayout_4.addWidget(self.btn_abs, 12, 1, 1, 1)

        self.btn_m_plus = QPushButton(self.qglayout)
        self.btn_m_plus.setObjectName(u"btn_m_plus")
        self.btn_m_plus.setStyleSheet(u"background-color: rgb(255, 179, 169)")

        self.gridLayout_4.addWidget(self.btn_m_plus, 0, 7, 1, 1)

        self.btn8 = QPushButton(self.qglayout)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.btn8.setAutoDefault(False)
        self.btn8.setFlat(False)

        self.gridLayout_4.addWidget(self.btn8, 7, 9, 1, 1)

        self.btn_or = QPushButton(self.qglayout)
        self.btn_or.setObjectName(u"btn_or")
        self.btn_or.setStyleSheet(u"background-color: rgb(85, 170, 255);")

        self.gridLayout_4.addWidget(self.btn_or, 7, 2, 1, 1)

        self.btn_ldexp = QPushButton(self.qglayout)
        self.btn_ldexp.setObjectName(u"btn_ldexp")
        self.btn_ldexp.setStyleSheet(u"background-color: rgb(231, 201, 48)")

        self.gridLayout_4.addWidget(self.btn_ldexp, 12, 10, 1, 1)


        self.verticalLayout_2.addWidget(self.qglayout)

        self.groupBox = QGroupBox(self.widget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.btn_rad_dec = QRadioButton(self.groupBox)
        self.btn_rad_dec.setObjectName(u"btn_rad_dec")
        self.btn_rad_dec.setChecked(True)

        self.horizontalLayout_2.addWidget(self.btn_rad_dec)

        self.btn_rad_abs = QRadioButton(self.groupBox)
        self.btn_rad_abs.setObjectName(u"btn_rad_abs")

        self.horizontalLayout_2.addWidget(self.btn_rad_abs)

        self.btn_rad_fabs = QRadioButton(self.groupBox)
        self.btn_rad_fabs.setObjectName(u"btn_rad_fabs")

        self.horizontalLayout_2.addWidget(self.btn_rad_fabs)

        self.btn_rad_floor = QRadioButton(self.groupBox)
        self.btn_rad_floor.setObjectName(u"btn_rad_floor")

        self.horizontalLayout_2.addWidget(self.btn_rad_floor)

        self.btn_rad_ceil = QRadioButton(self.groupBox)
        self.btn_rad_ceil.setObjectName(u"btn_rad_ceil")

        self.horizontalLayout_2.addWidget(self.btn_rad_ceil)

        self.btn_rad_trunc = QRadioButton(self.groupBox)
        self.btn_rad_trunc.setObjectName(u"btn_rad_trunc")

        self.horizontalLayout_2.addWidget(self.btn_rad_trunc)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.st_controls = QStackedWidget(self.widget)
        self.st_controls.setObjectName(u"st_controls")
        self.st_controls.setGeometry(QRect(-10, 122, 21, 391))
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_2 = QWidget(self.page_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_showFun1 = QPushButton(self.widget_2)
        self.btn_showFun1.setObjectName(u"btn_showFun1")
        icon13 = QIcon()
        icon13.addFile(u":/icons/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_showFun1.setIcon(icon13)

        self.verticalLayout_3.addWidget(self.btn_showFun1)

        self.radioButton_2 = QRadioButton(self.widget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton = QRadioButton(self.widget_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(False)

        self.verticalLayout_3.addWidget(self.radioButton)

        self.btn_del_historial = QPushButton(self.widget_2)
        self.btn_del_historial.setObjectName(u"btn_del_historial")
        icon14 = QIcon()
        icon14.addFile(u":/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_del_historial.setIcon(icon14)

        self.verticalLayout_3.addWidget(self.btn_del_historial)


        self.horizontalLayout_5.addWidget(self.widget_2)

        self.list_historial = QListWidget(self.page_4)
        self.list_historial.setObjectName(u"list_historial")

        self.horizontalLayout_5.addWidget(self.list_historial)

        self.st_controls.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout = QHBoxLayout(self.page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_5 = QWidget(self.page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_3 = QGroupBox(self.widget_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_showFun2 = QPushButton(self.groupBox_3)
        self.btn_showFun2.setObjectName(u"btn_showFun2")
        self.btn_showFun2.setIcon(icon13)

        self.verticalLayout_4.addWidget(self.btn_showFun2)

        self.btn_mr_min = QPushButton(self.groupBox_3)
        self.btn_mr_min.setObjectName(u"btn_mr_min")

        self.verticalLayout_4.addWidget(self.btn_mr_min)

        self.btn_mr_max = QPushButton(self.groupBox_3)
        self.btn_mr_max.setObjectName(u"btn_mr_max")

        self.verticalLayout_4.addWidget(self.btn_mr_max)

        self.btn_mr_sum = QPushButton(self.groupBox_3)
        self.btn_mr_sum.setObjectName(u"btn_mr_sum")

        self.verticalLayout_4.addWidget(self.btn_mr_sum)

        self.btn_mr_prod = QPushButton(self.groupBox_3)
        self.btn_mr_prod.setObjectName(u"btn_mr_prod")

        self.verticalLayout_4.addWidget(self.btn_mr_prod)

        self.btn_mr_mean = QPushButton(self.groupBox_3)
        self.btn_mr_mean.setObjectName(u"btn_mr_mean")

        self.verticalLayout_4.addWidget(self.btn_mr_mean)

        self.btn_mr_median = QPushButton(self.groupBox_3)
        self.btn_mr_median.setObjectName(u"btn_mr_median")

        self.verticalLayout_4.addWidget(self.btn_mr_median)

        self.btn_mr_mode = QPushButton(self.groupBox_3)
        self.btn_mr_mode.setObjectName(u"btn_mr_mode")

        self.verticalLayout_4.addWidget(self.btn_mr_mode)

        self.btn_mr_clear = QPushButton(self.groupBox_3)
        self.btn_mr_clear.setObjectName(u"btn_mr_clear")

        self.verticalLayout_4.addWidget(self.btn_mr_clear)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.list_memory = QListWidget(self.widget_5)
        self.list_memory.setObjectName(u"list_memory")

        self.horizontalLayout_4.addWidget(self.list_memory)


        self.horizontalLayout.addWidget(self.widget_5)

        self.st_controls.addWidget(self.page)
        Scientific.setCentralWidget(self.widget)
        self.menubar = QMenuBar(Scientific)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 643, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Scientific.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Scientific)
        self.statusbar.setObjectName(u"statusbar")
        Scientific.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(Scientific)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(16, 16))
        Scientific.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionStandard)
        self.menuFile.addAction(self.actionLength)
        self.menuFile.addAction(self.actionTime)
        self.menuFile.addAction(self.actionTemperature)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionProperties)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPlay_Result)
        self.menuFile.addAction(self.actionDict_input)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionFQAs)
        self.toolBar.addAction(self.actionStandard)
        self.toolBar.addAction(self.actionLength)
        self.toolBar.addAction(self.actionTime)
        self.toolBar.addAction(self.actionTemperature)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDict_input)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlay_Result)

        self.retranslateUi(Scientific)
        self.btn_del_historial.clicked.connect(self.list_historial.clear)
        self.btn_mc.clicked.connect(self.list_memory.clear)

        self.btn_ln.setDefault(False)
        self.btn_pi.setDefault(False)
        self.btn_c.setDefault(False)
        self.btn_sqrt.setDefault(False)
        self.btn_sinh.setDefault(False)
        self.btn00.setDefault(False)
        self.btn_cos.setDefault(False)
        self.btn_log2.setDefault(False)
        self.btn5.setDefault(False)
        self.btn_DEG.setDefault(False)
        self.btn1.setDefault(False)
        self.btn_ceil.setDefault(False)
        self.btn_ce.setDefault(False)
        self.btn000.setDefault(False)
        self.btn_expm1.setDefault(False)
        self.btn_parenthesis.setDefault(False)
        self.btn9.setDefault(False)
        self.btn_cuberoot.setDefault(False)
        self.btn0.setDefault(False)
        self.btn6.setDefault(False)
        self.btn_minus.setDefault(False)
        self.btn_back.setDefault(False)
        self.btn_RAD.setDefault(False)
        self.btn_gma.setDefault(False)
        self.btn_lgma.setDefault(False)
        self.btn_floor.setDefault(False)
        self.btn_sin.setDefault(False)
        self.btn_exp.setDefault(False)
        self.btn_2X.setDefault(False)
        self.btn_mult.setDefault(False)
        self.btn_atanh.setDefault(False)
        self.btn3.setDefault(False)
        self.btn_asin.setDefault(False)
        self.btn_sqrtroot.setDefault(False)
        self.btn_tan.setDefault(False)
        self.btn2.setDefault(False)
        self.btn_asinh.setDefault(False)
        self.btn_acos.setDefault(False)
        self.btn_1dividedX.setDefault(False)
        self.btn_percent.setDefault(False)
        self.btn_e.setDefault(False)
        self.btn_sqrtN.setDefault(False)
        self.btn_divide.setDefault(False)
        self.btn_cosh.setDefault(False)
        self.btn_mod.setDefault(False)
        self.btn_dot.setDefault(False)
        self.btn_atan.setDefault(False)
        self.btn_tanh.setDefault(False)
        self.btn_historial_show.setDefault(False)
        self.btn4.setDefault(False)
        self.btn_trunc.setDefault(False)
        self.btn_10powX.setDefault(False)
        self.btn7.setDefault(False)
        self.btn_tau.setDefault(False)
        self.btn_sum.setDefault(False)
        self.btn_acosh.setDefault(False)
        self.btn_sqrt3.setDefault(False)
        self.btn_factorial.setDefault(False)
        self.btn_inverse.setDefault(False)
        self.btn_plus.setDefault(False)
        self.btn_log.setDefault(False)
        self.btn_abs.setDefault(False)
        self.btn8.setDefault(False)
        self.st_controls.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Scientific)
    # setupUi

    def retranslateUi(self, Scientific):
        Scientific.setWindowTitle(QCoreApplication.translate("Scientific", u"Scientific", None))
        self.actionStandard.setText(QCoreApplication.translate("Scientific", u"Standard", None))
        self.actionLength.setText(QCoreApplication.translate("Scientific", u"Length", None))
        self.actionTime.setText(QCoreApplication.translate("Scientific", u"Time", None))
        self.actionTemperature.setText(QCoreApplication.translate("Scientific", u"Temperature", None))
        self.actionProperties.setText(QCoreApplication.translate("Scientific", u"Properties", None))
        self.actionPlay_Result.setText(QCoreApplication.translate("Scientific", u"Play Result", None))
        self.actionExit.setText(QCoreApplication.translate("Scientific", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("Scientific", u"About", None))
        self.actionFQAs.setText(QCoreApplication.translate("Scientific", u"FQAs", None))
        self.actionDict_input.setText(QCoreApplication.translate("Scientific", u"Dict input", None))
        self.label_result.setText("")
        self.label_mr.setText(QCoreApplication.translate("Scientific", u"0", None))
        self.qglayout.setTitle("")
#if QT_CONFIG(tooltip)
        self.btn_log1p.setToolTip(QCoreApplication.translate("Scientific", u"Returns log(1+number), computed in a way that is accurate even when the value of number is close to zero.\n"
"\n"
"Syntax: log1p(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_log1p.setText(QCoreApplication.translate("Scientific", u"log1p", None))
#if QT_CONFIG(tooltip)
        self.btn_ln.setToolTip(QCoreApplication.translate("Scientific", u"Returns the natural logarithm of a number, or the logarithm of number to base.\n"
"\n"
"Syntax: ln(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ln.setText(QCoreApplication.translate("Scientific", u"ln", None))
        self.btn_equal.setText(QCoreApplication.translate("Scientific", u"=", None))
#if QT_CONFIG(tooltip)
        self.btn_pi.setToolTip(QCoreApplication.translate("Scientific", u"Returns the value of PI constant.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_pi.setText(QCoreApplication.translate("Scientific", u"\u03c0", None))
#if QT_CONFIG(tooltip)
        self.btn_c.setToolTip(QCoreApplication.translate("Scientific", u"Clear all", None))
#endif // QT_CONFIG(tooltip)
        self.btn_c.setText(QCoreApplication.translate("Scientific", u"C", None))
        self.btn_sqrt.setText(QCoreApplication.translate("Scientific", u"x\u00b2", None))
        self.btn_less.setText(QCoreApplication.translate("Scientific", u"<", None))
        self.groupBox_2.setTitle("")
#if QT_CONFIG(tooltip)
        self.btn_rd_bin.setToolTip(QCoreApplication.translate("Scientific", u"display results in binary", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rd_bin.setText(QCoreApplication.translate("Scientific", u"BIN", None))
#if QT_CONFIG(tooltip)
        self.btn_rd_oct.setToolTip(QCoreApplication.translate("Scientific", u"display results in octal", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rd_oct.setText(QCoreApplication.translate("Scientific", u"OCT", None))
#if QT_CONFIG(tooltip)
        self.btn_rd_dec.setToolTip(QCoreApplication.translate("Scientific", u"display results in decimal", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rd_dec.setText(QCoreApplication.translate("Scientific", u"DEC", None))
#if QT_CONFIG(tooltip)
        self.btn_rd_hex.setToolTip(QCoreApplication.translate("Scientific", u"display results in hexadecimal", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rd_hex.setText(QCoreApplication.translate("Scientific", u"HEX", None))
#if QT_CONFIG(tooltip)
        self.btn_rd_fe.setToolTip(QCoreApplication.translate("Scientific", u"display results in scientific notation", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rd_fe.setText(QCoreApplication.translate("Scientific", u"F-E", None))
#if QT_CONFIG(tooltip)
        self.btn_sinh.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the arc sine of a number</p><p><br/></p><p>Syntax: asin(x)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sinh.setText(QCoreApplication.translate("Scientific", u"sinh", None))
#if QT_CONFIG(tooltip)
        self.btn_mean.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the mean of all the values in a list.</p><p>Syntax: mean(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mean.setText(QCoreApplication.translate("Scientific", u"mean", None))
        self.btn00.setText(QCoreApplication.translate("Scientific", u"00", None))
#if QT_CONFIG(tooltip)
        self.btn_cos.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the cosine of a number.</p><p><br/></p><p>Syntax: cos(x)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cos.setText(QCoreApplication.translate("Scientific", u"cos", None))
#if QT_CONFIG(tooltip)
        self.btn_log2.setToolTip(QCoreApplication.translate("Scientific", u"Returns the base-2 logarithm of a number.\n"
"\n"
"Syntax: log2(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_log2.setText(QCoreApplication.translate("Scientific", u"log2", None))
        self.btn5.setText(QCoreApplication.translate("Scientific", u"5", None))
#if QT_CONFIG(tooltip)
        self.btn_m_minus.setToolTip(QCoreApplication.translate("Scientific", u"Memory sustract", None))
#endif // QT_CONFIG(tooltip)
        self.btn_m_minus.setText(QCoreApplication.translate("Scientific", u"M-", None))
#if QT_CONFIG(tooltip)
        self.btn_yroot.setToolTip(QCoreApplication.translate("Scientific", u"Returns n root of a number.\n"
"\n"
"Syntax:  \u207f\u221a(n, x)\n"
"\n"
"Example: \u207f\u221a(x)  -> \u207f\u221a(n,x)  ->   \u207f\u221a(2,9) = 3", None))
#endif // QT_CONFIG(tooltip)
        self.btn_yroot.setStyleSheet(QCoreApplication.translate("Scientific", u"background:limegreen;", None))
        self.btn_yroot.setText(QCoreApplication.translate("Scientific", u"\u207f\u221ax", None))
#if QT_CONFIG(tooltip)
        self.btn_mode.setToolTip(QCoreApplication.translate("Scientific", u"Returns the mode of all the values in a list.\n"
"\n"
"Syntax: mode(x1, x2, x3, ..., xn)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mode.setText(QCoreApplication.translate("Scientific", u"mode", None))
#if QT_CONFIG(tooltip)
        self.btn_DEG.setToolTip(QCoreApplication.translate("Scientific", u"Converts an angle result from radians to degrees.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_DEG.setWhatsThis(QCoreApplication.translate("Scientific", u"Converts an angle from radians to degrees", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_DEG.setText(QCoreApplication.translate("Scientific", u"DEG", None))
        self.btn1.setText(QCoreApplication.translate("Scientific", u"1", None))
#if QT_CONFIG(tooltip)
        self.btn_ceil.setToolTip(QCoreApplication.translate("Scientific", u"Rounds a number UP to the nearest integer, if necessary, and returns the result.\n"
"\n"
"Syntax: ceil(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ceil.setText(QCoreApplication.translate("Scientific", u"ceil", None))
        self.btn_not_equals.setText(QCoreApplication.translate("Scientific", u"\u2260", None))
#if QT_CONFIG(tooltip)
        self.btn_ce.setToolTip(QCoreApplication.translate("Scientific", u"Clear entry", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ce.setText(QCoreApplication.translate("Scientific", u"CE", None))
#if QT_CONFIG(tooltip)
        self.btn_comma.setToolTip(QCoreApplication.translate("Scientific", u"Separates values in a list and expressions out of a list.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_comma.setText(QCoreApplication.translate("Scientific", u",", None))
        self.btn000.setText(QCoreApplication.translate("Scientific", u"000", None))
#if QT_CONFIG(tooltip)
        self.btn_max.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the highest value in a list.</p><p><br/></p><p>Syntax: max(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_max.setText(QCoreApplication.translate("Scientific", u"max", None))
        self.btn_less_than.setText(QCoreApplication.translate("Scientific", u"\u2266", None))
#if QT_CONFIG(tooltip)
        self.btn_ms.setToolTip(QCoreApplication.translate("Scientific", u"Memory store", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ms.setText(QCoreApplication.translate("Scientific", u"MS", None))
#if QT_CONFIG(tooltip)
        self.btn_expm1.setToolTip(QCoreApplication.translate("Scientific", u"Returns Ex - 1 raised to the power of x (Ex-1).\n"
"\n"
"Syntax: expm1(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_expm1.setText(QCoreApplication.translate("Scientific", u"expm1", None))
        self.btn_parenthesis.setText(QCoreApplication.translate("Scientific", u"( )", None))
        self.btn9.setText(QCoreApplication.translate("Scientific", u"9", None))
        self.btn_cuberoot.setText(QCoreApplication.translate("Scientific", u"\u1d4c\u221ax", None))
        self.btn0.setText(QCoreApplication.translate("Scientific", u"0", None))
#if QT_CONFIG(tooltip)
        self.btn_prod.setToolTip(QCoreApplication.translate("Scientific", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Returns the product of all the values in a list.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Syntax: prod(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_prod.setText(QCoreApplication.translate("Scientific", u"prod", None))
        self.btn6.setText(QCoreApplication.translate("Scientific", u"6", None))
        self.btn_minus.setText(QCoreApplication.translate("Scientific", u"-", None))
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the lowest value in a list.</p><p><br/></p><p>Syntax: min(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText(QCoreApplication.translate("Scientific", u"min", None))
        self.btn_back.setText("")
#if QT_CONFIG(tooltip)
        self.btn_m_show.setToolTip(QCoreApplication.translate("Scientific", u"Memory history", None))
#endif // QT_CONFIG(tooltip)
        self.btn_m_show.setText(QCoreApplication.translate("Scientific", u"\u25c0 M \u25b6", None))
#if QT_CONFIG(tooltip)
        self.btn_RAD.setToolTip(QCoreApplication.translate("Scientific", u"Converts a degree value result into radians.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_RAD.setText(QCoreApplication.translate("Scientific", u"RAD", None))
#if QT_CONFIG(tooltip)
        self.btn_gma.setToolTip(QCoreApplication.translate("Scientific", u"Return the gamma function at a numbers.\n"
"\n"
"Syntax: gma(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_gma.setText(QCoreApplication.translate("Scientific", u"gma", None))
#if QT_CONFIG(tooltip)
        self.btn_lgma.setToolTip(QCoreApplication.translate("Scientific", u"Returns the natural logarithm gamma value of a number.\n"
"\n"
"Syntax: lgma(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_lgma.setText(QCoreApplication.translate("Scientific", u"lgma", None))
#if QT_CONFIG(tooltip)
        self.btn_floor.setToolTip(QCoreApplication.translate("Scientific", u"Rounds a number DOWN to the nearest integer, if necessary, and returns the result.\n"
"\n"
"Syntax: floor(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_floor.setText(QCoreApplication.translate("Scientific", u"floor", None))
#if QT_CONFIG(tooltip)
        self.btn_sin.setToolTip(QCoreApplication.translate("Scientific", u"Returns the sine of a number.\n"
"\n"
"Syntax: sin(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sin.setText(QCoreApplication.translate("Scientific", u"sin", None))
#if QT_CONFIG(tooltip)
        self.btn_exp.setToolTip(QCoreApplication.translate("Scientific", u"Returns E raised to the power of x (Ex).\n"
"\n"
"Syntax: epx(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_exp.setText(QCoreApplication.translate("Scientific", u"exp", None))
        self.btn_2X.setText(QCoreApplication.translate("Scientific", u"2\u207f", None))
#if QT_CONFIG(tooltip)
        self.btn_gcd.setToolTip(QCoreApplication.translate("Scientific", u"Returns the greatest common divisor of the two integers int1 and int2.\n"
"\n"
"GCD is the largest common divisor that divides the numbers without a remainder.\n"
"\n"
"GCD is also known as the highest common factor (HCF).\n"
"\n"
"Syntax: gcd(int1, int2)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_gcd.setText(QCoreApplication.translate("Scientific", u"gcd", None))
        self.btn_and.setText(QCoreApplication.translate("Scientific", u"and", None))
#if QT_CONFIG(tooltip)
        self.btn_frexp.setToolTip(QCoreApplication.translate("Scientific", u"Returns the mantissa and the exponent of a specified number, as a pair (m,e).\n"
"\n"
"The mathematical formula for this method is: number = m * 2**e.\n"
"\n"
"Syntax: frexp(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_frexp.setText(QCoreApplication.translate("Scientific", u"frexp", None))
        self.btn_mult.setText(QCoreApplication.translate("Scientific", u"*", None))
#if QT_CONFIG(tooltip)
        self.btn_atanh.setToolTip(QCoreApplication.translate("Scientific", u"Return the inverse hyperbolic tangent of numbers.\n"
"\n"
"Syntax: atanh(x)\n"
"\n"
"Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atanh.setText(QCoreApplication.translate("Scientific", u"tanh\u207b\u00b9", None))
        self.btn_greater.setText(QCoreApplication.translate("Scientific", u">", None))
#if QT_CONFIG(tooltip)
        self.btn_round.setToolTip(QCoreApplication.translate("Scientific", u"Rounds a number DOWN or UP to the nearest integer, if necessary, and returns the result.\n"
"\n"
"Syntax: round(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_round.setText(QCoreApplication.translate("Scientific", u"round", None))
        self.btn3.setText(QCoreApplication.translate("Scientific", u"3", None))
#if QT_CONFIG(tooltip)
        self.btn_asin.setToolTip(QCoreApplication.translate("Scientific", u"Returns the hyperbolic sine of a number.\n"
"\n"
"Syntax: sinh(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_asin.setText(QCoreApplication.translate("Scientific", u"sin\u207b\u00b9", None))
        self.btn_sqrtroot.setText(QCoreApplication.translate("Scientific", u"\u00b2\u221ax", None))
#if QT_CONFIG(tooltip)
        self.btn_mr.setToolTip(QCoreApplication.translate("Scientific", u"Memory recall", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mr.setText(QCoreApplication.translate("Scientific", u"MR", None))
#if QT_CONFIG(tooltip)
        self.btn_fabs.setToolTip(QCoreApplication.translate("Scientific", u"Returns the absolute value of a number as float.\n"
"\n"
"Syntax: fabs(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_fabs.setText(QCoreApplication.translate("Scientific", u"fabs", None))
#if QT_CONFIG(tooltip)
        self.btn_tan.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the tangent of a number.</p><p><br/></p><p>Syntax: tan(x)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tan.setText(QCoreApplication.translate("Scientific", u"tan", None))
        self.btn2.setText(QCoreApplication.translate("Scientific", u"2", None))
#if QT_CONFIG(tooltip)
        self.btn_atan2.setToolTip(QCoreApplication.translate("Scientific", u"Returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y).\n"
"\n"
"Syntax: atan2(y, x)\n"
"\n"
"The returned value is between PI and -PI.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atan2.setStyleSheet(QCoreApplication.translate("Scientific", u"background-color: rgb(255, 250, 199);", None))
        self.btn_atan2.setText(QCoreApplication.translate("Scientific", u"atan2", None))
#if QT_CONFIG(tooltip)
        self.btn_lcm.setToolTip(QCoreApplication.translate("Scientific", u"Returns the least common multiple of 2 numbers.\n"
"\n"
"Syntax: lcm(n1, n2)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_lcm.setText(QCoreApplication.translate("Scientific", u"lcm", None))
#if QT_CONFIG(tooltip)
        self.btn_asinh.setToolTip(QCoreApplication.translate("Scientific", u"Return the inverse hyperbolic sine of numbers.\n"
"\n"
"Syntax: asinh(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_asinh.setText(QCoreApplication.translate("Scientific", u"sinh\u207b\u00b9", None))
#if QT_CONFIG(tooltip)
        self.btn_acos.setToolTip(QCoreApplication.translate("Scientific", u"Returns the hyperbolic cosine of a number.\n"
"\n"
"Syntax: cosh(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_acos.setText(QCoreApplication.translate("Scientific", u"cos\u207b\u00b9", None))
#if QT_CONFIG(tooltip)
        self.btn_rand.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Return a random number between 0 and 1</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_rand.setText(QCoreApplication.translate("Scientific", u"rand", None))
        self.btn_1dividedX.setText(QCoreApplication.translate("Scientific", u"\u00b9/\u2093", None))
        self.btn_percent.setText(QCoreApplication.translate("Scientific", u"%", None))
#if QT_CONFIG(tooltip)
        self.btn_medn.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the medean of all the values in a list.</p><p>Syntax: medn(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_medn.setText(QCoreApplication.translate("Scientific", u"medn", None))
        self.btn_not.setText(QCoreApplication.translate("Scientific", u"not", None))
#if QT_CONFIG(tooltip)
        self.btn_e.setToolTip(QCoreApplication.translate("Scientific", u"Returns the value of E constant.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_e.setText(QCoreApplication.translate("Scientific", u"e", None))
        self.btn_sqrtN.setText(QCoreApplication.translate("Scientific", u"x\u207f", None))
        self.btn_divide.setText(QCoreApplication.translate("Scientific", u"/", None))
#if QT_CONFIG(tooltip)
        self.btn_cosh.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the arc cosine of a number.</p><p><br/></p><p>Syntax: acos(x)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cosh.setText(QCoreApplication.translate("Scientific", u"cosh", None))
#if QT_CONFIG(tooltip)
        self.btn_mod.setToolTip(QCoreApplication.translate("Scientific", u"Retruns the module of a number", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mod.setText(QCoreApplication.translate("Scientific", u"mod", None))
        self.btn_dot.setText(QCoreApplication.translate("Scientific", u".", None))
#if QT_CONFIG(tooltip)
        self.btn_atan.setToolTip(QCoreApplication.translate("Scientific", u"Returns the hyperbolic tangent of a number.\n"
"\n"
"Syntax: tanh(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_atan.setText(QCoreApplication.translate("Scientific", u"tan\u207b\u00b9", None))
#if QT_CONFIG(tooltip)
        self.btn_tanh.setToolTip(QCoreApplication.translate("Scientific", u"Returns  the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians.\n"
"\n"
"Syntax: atan(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tanh.setText(QCoreApplication.translate("Scientific", u"tanh", None))
#if QT_CONFIG(tooltip)
        self.btn_historial_show.setToolTip(QCoreApplication.translate("Scientific", u"Results history", None))
#endif // QT_CONFIG(tooltip)
        self.btn_historial_show.setText("")
        self.btn4.setText(QCoreApplication.translate("Scientific", u"4", None))
#if QT_CONFIG(tooltip)
        self.btn_hypot.setToolTip(QCoreApplication.translate("Scientific", u"Returns the Euclidean norm. The Euclidian norm is the distance from the origin to the coordinates given.\n"
"\n"
"Syntax: hypot(x1, x2, x3, ..., xn)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_hypot.setText(QCoreApplication.translate("Scientific", u"hypot", None))
#if QT_CONFIG(tooltip)
        self.btn_comb.setToolTip(QCoreApplication.translate("Scientific", u"Returns the number of ways picking k unordered outcomes from n possibilities, without repetition, also known as combinations.\n"
"\n"
"Syntax: comb(n, k)\n"
"\n"
"Note: The parameters passed in this method must be positive integers.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_comb.setText(QCoreApplication.translate("Scientific", u"comb", None))
#if QT_CONFIG(tooltip)
        self.btn_trunc.setToolTip(QCoreApplication.translate("Scientific", u"Returns the truncated integer part of a number.\n"
"\n"
"Syntax: trunc(x)\n"
"\n"
"Note: This function will NOT round the number up/down to the nearest integer, but simply remove the decimals.\n"
"\n"
"example: trunc(58.90) returns 58", None))
#endif // QT_CONFIG(tooltip)
        self.btn_trunc.setText(QCoreApplication.translate("Scientific", u"trunc", None))
        self.btn_10powX.setText(QCoreApplication.translate("Scientific", u"10\u207f", None))
        self.btn_greater_than.setText(QCoreApplication.translate("Scientific", u"\u2267", None))
        self.btn7.setText(QCoreApplication.translate("Scientific", u"7", None))
#if QT_CONFIG(tooltip)
        self.btn_tau.setToolTip(QCoreApplication.translate("Scientific", u"Returns the value of T constant.", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tau.setText(QCoreApplication.translate("Scientific", u"Tau", None))
        self.btn_equals_equals.setStyleSheet(QCoreApplication.translate("Scientific", u"background-color: rgb(66, 205, 255);", None))
        self.btn_equals_equals.setText(QCoreApplication.translate("Scientific", u"==", None))
#if QT_CONFIG(tooltip)
        self.btn_sum.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Returns the sum of all values in a list.</p><p><br/></p><p>Syntax: sum(x1, x2, x3, ..., xn)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sum.setText(QCoreApplication.translate("Scientific", u"sum", None))
#if QT_CONFIG(tooltip)
        self.btn_perm.setToolTip(QCoreApplication.translate("Scientific", u"Returns the number of ways to choose k items from n items with order and without repetition.\n"
"\n"
"Syntax: perm(n, k)\n"
"\n"
"Note: The k parameter is optional. If we do not provide one, this method will return n! (for example, perm(7) will return 5040).", None))
#endif // QT_CONFIG(tooltip)
        self.btn_perm.setText(QCoreApplication.translate("Scientific", u"perm", None))
#if QT_CONFIG(tooltip)
        self.btn_acosh.setToolTip(QCoreApplication.translate("Scientific", u"Return the inverse hyperbolic cosine of numbers.\n"
"\n"
"Syntax: acosh(X)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_acosh.setText(QCoreApplication.translate("Scientific", u"cosh\u207b\u00b9", None))
        self.btn_sqrt3.setText(QCoreApplication.translate("Scientific", u"x\u1d4c", None))
#if QT_CONFIG(tooltip)
        self.btn_factorial.setToolTip(QCoreApplication.translate("Scientific", u"Returns the factorial of a number", None))
#endif // QT_CONFIG(tooltip)
        self.btn_factorial.setText(QCoreApplication.translate("Scientific", u"n!", None))
        self.btn_inverse.setText(QCoreApplication.translate("Scientific", u"+/-", None))
        self.btn_plus.setText(QCoreApplication.translate("Scientific", u"+", None))
#if QT_CONFIG(tooltip)
        self.btn_mc.setToolTip(QCoreApplication.translate("Scientific", u"Memory clear", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mc.setStyleSheet(QCoreApplication.translate("Scientific", u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"", None))
        self.btn_mc.setText(QCoreApplication.translate("Scientific", u"MC", None))
#if QT_CONFIG(tooltip)
        self.btn_log.setToolTip(QCoreApplication.translate("Scientific", u"Returns the base-10 logarithm of a number.\n"
"\n"
"Syntax: log(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_log.setText(QCoreApplication.translate("Scientific", u"log", None))
#if QT_CONFIG(tooltip)
        self.btn_abs.setToolTip(QCoreApplication.translate("Scientific", u"Returns the absolute value of a number.\n"
"\n"
"Syntax: abs(x)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_abs.setText(QCoreApplication.translate("Scientific", u"abs", None))
#if QT_CONFIG(tooltip)
        self.btn_m_plus.setToolTip(QCoreApplication.translate("Scientific", u"Memory add", None))
#endif // QT_CONFIG(tooltip)
        self.btn_m_plus.setText(QCoreApplication.translate("Scientific", u"M+", None))
        self.btn8.setText(QCoreApplication.translate("Scientific", u"8", None))
        self.btn_or.setText(QCoreApplication.translate("Scientific", u"or", None))
#if QT_CONFIG(tooltip)
        self.btn_ldexp.setToolTip(QCoreApplication.translate("Scientific", u"Returns x * (2**i) of the given numbers x and i, which is the inverse of frexp().\n"
"\n"
"Syntax: ldexp(x, i)", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ldexp.setText(QCoreApplication.translate("Scientific", u"ldexp", None))
        self.groupBox.setTitle(QCoreApplication.translate("Scientific", u"Round Result", None))
        self.btn_rad_dec.setText(QCoreApplication.translate("Scientific", u"Dec", None))
        self.btn_rad_abs.setText(QCoreApplication.translate("Scientific", u"abs", None))
        self.btn_rad_fabs.setText(QCoreApplication.translate("Scientific", u"fabs", None))
        self.btn_rad_floor.setText(QCoreApplication.translate("Scientific", u"floor", None))
        self.btn_rad_ceil.setText(QCoreApplication.translate("Scientific", u"ceil", None))
        self.btn_rad_trunc.setText(QCoreApplication.translate("Scientific", u"trunc", None))
#if QT_CONFIG(tooltip)
        self.btn_showFun1.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Show controls</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_showFun1.setText("")
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Append text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("Scientific", u"Append", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Replace text</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("Scientific", u"Replace", None))
#if QT_CONFIG(tooltip)
        self.btn_del_historial.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Clear history</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_historial.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Scientific", u"GroupBox", None))
#if QT_CONFIG(tooltip)
        self.btn_showFun2.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p>Hide the memory history</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_showFun2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_mr_min.setToolTip(QCoreApplication.translate("Scientific", u"Delete from memory the selected values", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mr_min.setText(QCoreApplication.translate("Scientific", u"M-min", None))
        self.btn_mr_max.setText(QCoreApplication.translate("Scientific", u"M-max", None))
#if QT_CONFIG(tooltip)
        self.btn_mr_sum.setToolTip(QCoreApplication.translate("Scientific", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">returns the function sum with all the values in memory</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mr_sum.setText(QCoreApplication.translate("Scientific", u"M-sum", None))
#if QT_CONFIG(tooltip)
        self.btn_mr_prod.setToolTip(QCoreApplication.translate("Scientific", u"<html><head/><body><p><span style=\" font-family:'Consolas','Menlo','courier new','monospace'; font-size:8pt; color:#000000; background-color:#ffffff;\">Returns the function prod with all the values in memory</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_mr_prod.setText(QCoreApplication.translate("Scientific", u"M-prod", None))
        self.btn_mr_mean.setText(QCoreApplication.translate("Scientific", u"M-mean", None))
        self.btn_mr_median.setText(QCoreApplication.translate("Scientific", u"M-median", None))
        self.btn_mr_mode.setText(QCoreApplication.translate("Scientific", u"M-mode", None))
        self.btn_mr_clear.setText(QCoreApplication.translate("Scientific", u"M-clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("Scientific", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Scientific", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("Scientific", u"toolBar", None))
    # retranslateUi

