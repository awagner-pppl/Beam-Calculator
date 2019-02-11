# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beam_Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 501, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 10, 181, 101))
        self.groupBox_7.setObjectName("groupBox_7")
        self.uChannelButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.uChannelButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.uChannelButton.setObjectName("uChannelButton")
        self.rectangleButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.rectangleButton.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.rectangleButton.setObjectName("rectangleButton")
        self.iBeamButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.iBeamButton.setGeometry(QtCore.QRect(20, 60, 82, 17))
        self.iBeamButton.setObjectName("iBeamButton")
        self.roundButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.roundButton.setGeometry(QtCore.QRect(110, 20, 82, 17))
        self.roundButton.setObjectName("roundButton")
        self.hexButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.hexButton.setGeometry(QtCore.QRect(110, 40, 82, 17))
        self.hexButton.setObjectName("hexButton")
        self.tBeamButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.tBeamButton.setGeometry(QtCore.QRect(110, 60, 82, 17))
        self.tBeamButton.setObjectName("tBeamButton")
        self.angleButton = QtWidgets.QRadioButton(self.groupBox_7)
        self.angleButton.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.angleButton.setObjectName("angleButton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.tab_3)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 180, 471, 241))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.hexagonGeometryBox_12 = QtWidgets.QGroupBox(self.page)
        self.hexagonGeometryBox_12.setGeometry(QtCore.QRect(20, 10, 131, 71))
        self.hexagonGeometryBox_12.setTitle("")
        self.hexagonGeometryBox_12.setObjectName("hexagonGeometryBox_12")
        self.label_24 = QtWidgets.QLabel(self.hexagonGeometryBox_12)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_24.setObjectName("label_24")
        self.hexLength = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_12)
        self.hexLength.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.hexLength.setMaximum(999999.99)
        self.hexLength.setObjectName("hexLength")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.uChannelGeometryBox_10 = QtWidgets.QGroupBox(self.page_3)
        self.uChannelGeometryBox_10.setGeometry(QtCore.QRect(20, 10, 131, 221))
        self.uChannelGeometryBox_10.setTitle("")
        self.uChannelGeometryBox_10.setObjectName("uChannelGeometryBox_10")
        self.label_18 = QtWidgets.QLabel(self.uChannelGeometryBox_10)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.uChannelGeometryBox_10)
        self.label_19.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.uChannelGeometryBox_10)
        self.label_20.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.uChannelGeometryBox_10)
        self.label_21.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_21.setObjectName("label_21")
        self.channelHeight = QtWidgets.QDoubleSpinBox(self.uChannelGeometryBox_10)
        self.channelHeight.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.channelHeight.setMaximum(999999.99)
        self.channelHeight.setObjectName("channelHeight")
        self.flangeHeight = QtWidgets.QDoubleSpinBox(self.uChannelGeometryBox_10)
        self.flangeHeight.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.flangeHeight.setMaximum(999999.99)
        self.flangeHeight.setObjectName("flangeHeight")
        self.flangeWidth = QtWidgets.QDoubleSpinBox(self.uChannelGeometryBox_10)
        self.flangeWidth.setGeometry(QtCore.QRect(10, 180, 111, 22))
        self.flangeWidth.setMaximum(999999.99)
        self.flangeWidth.setObjectName("flangeWidth")
        self.channelWidth = QtWidgets.QDoubleSpinBox(self.uChannelGeometryBox_10)
        self.channelWidth.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.channelWidth.setMaximum(999999.99)
        self.channelWidth.setObjectName("channelWidth")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.rectangleGeometryBox_9 = QtWidgets.QGroupBox(self.page_4)
        self.rectangleGeometryBox_9.setGeometry(QtCore.QRect(20, 10, 131, 221))
        self.rectangleGeometryBox_9.setTitle("")
        self.rectangleGeometryBox_9.setObjectName("rectangleGeometryBox_9")
        self.label_14 = QtWidgets.QLabel(self.rectangleGeometryBox_9)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.rectangleGeometryBox_9)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.rectangleGeometryBox_9)
        self.label_16.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.rectangleGeometryBox_9)
        self.label_17.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_17.setObjectName("label_17")
        self.rectangleOutHeight = QtWidgets.QDoubleSpinBox(self.rectangleGeometryBox_9)
        self.rectangleOutHeight.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.rectangleOutHeight.setMaximum(999999.99)
        self.rectangleOutHeight.setObjectName("rectangleOutHeight")
        self.rectangleOutWidth = QtWidgets.QDoubleSpinBox(self.rectangleGeometryBox_9)
        self.rectangleOutWidth.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.rectangleOutWidth.setMaximum(999999.99)
        self.rectangleOutWidth.setObjectName("rectangleOutWidth")
        self.rectangleInHeight = QtWidgets.QDoubleSpinBox(self.rectangleGeometryBox_9)
        self.rectangleInHeight.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.rectangleInHeight.setMaximum(999999.99)
        self.rectangleInHeight.setObjectName("rectangleInHeight")
        self.rectangleInWidth = QtWidgets.QDoubleSpinBox(self.rectangleGeometryBox_9)
        self.rectangleInWidth.setGeometry(QtCore.QRect(10, 180, 111, 22))
        self.rectangleInWidth.setMaximum(999999.99)
        self.rectangleInWidth.setObjectName("rectangleInWidth")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.iBeamGeometryBox_8 = QtWidgets.QGroupBox(self.page_5)
        self.iBeamGeometryBox_8.setGeometry(QtCore.QRect(20, 10, 131, 221))
        self.iBeamGeometryBox_8.setTitle("")
        self.iBeamGeometryBox_8.setObjectName("iBeamGeometryBox_8")
        self.label = QtWidgets.QLabel(self.iBeamGeometryBox_8)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_10 = QtWidgets.QLabel(self.iBeamGeometryBox_8)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.iBeamGeometryBox_8)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 91, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.iBeamGeometryBox_8)
        self.label_13.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_13.setObjectName("label_13")
        self.iBeamHeight = QtWidgets.QDoubleSpinBox(self.iBeamGeometryBox_8)
        self.iBeamHeight.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.iBeamHeight.setMaximum(999999.99)
        self.iBeamHeight.setObjectName("iBeamHeight")
        self.iBeamWidth = QtWidgets.QDoubleSpinBox(self.iBeamGeometryBox_8)
        self.iBeamWidth.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.iBeamWidth.setMaximum(999999.99)
        self.iBeamWidth.setObjectName("iBeamWidth")
        self.iBeamFlange = QtWidgets.QDoubleSpinBox(self.iBeamGeometryBox_8)
        self.iBeamFlange.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.iBeamFlange.setMaximum(999999.99)
        self.iBeamFlange.setObjectName("iBeamFlange")
        self.iBeamWeb = QtWidgets.QDoubleSpinBox(self.iBeamGeometryBox_8)
        self.iBeamWeb.setGeometry(QtCore.QRect(10, 180, 111, 22))
        self.iBeamWeb.setMaximum(999999.99)
        self.iBeamWeb.setObjectName("iBeamWeb")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.roundGeometryBox_11 = QtWidgets.QGroupBox(self.page_2)
        self.roundGeometryBox_11.setGeometry(QtCore.QRect(20, 10, 131, 121))
        self.roundGeometryBox_11.setTitle("")
        self.roundGeometryBox_11.setObjectName("roundGeometryBox_11")
        self.label_22 = QtWidgets.QLabel(self.roundGeometryBox_11)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.roundGeometryBox_11)
        self.label_23.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_23.setObjectName("label_23")
        self.roundOD = QtWidgets.QDoubleSpinBox(self.roundGeometryBox_11)
        self.roundOD.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.roundOD.setMaximum(999999.99)
        self.roundOD.setObjectName("roundOD")
        self.roundID = QtWidgets.QDoubleSpinBox(self.roundGeometryBox_11)
        self.roundID.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.roundID.setMaximum(999999.99)
        self.roundID.setObjectName("roundID")
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.hexagonGeometryBox_13 = QtWidgets.QGroupBox(self.page_6)
        self.hexagonGeometryBox_13.setGeometry(QtCore.QRect(20, 10, 131, 221))
        self.hexagonGeometryBox_13.setTitle("")
        self.hexagonGeometryBox_13.setObjectName("hexagonGeometryBox_13")
        self.teeFlange = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_13)
        self.teeFlange.setGeometry(QtCore.QRect(10, 180, 111, 22))
        self.teeFlange.setMaximum(999999.99)
        self.teeFlange.setObjectName("teeFlange")
        self.teeHeight = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_13)
        self.teeHeight.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.teeHeight.setMaximum(999999.99)
        self.teeHeight.setObjectName("teeHeight")
        self.label_32 = QtWidgets.QLabel(self.hexagonGeometryBox_13)
        self.label_32.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_32.setObjectName("label_32")
        self.label_34 = QtWidgets.QLabel(self.hexagonGeometryBox_13)
        self.label_34.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_34.setObjectName("label_34")
        self.label_8 = QtWidgets.QLabel(self.hexagonGeometryBox_13)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_8.setObjectName("label_8")
        self.teeWidth = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_13)
        self.teeWidth.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.teeWidth.setMaximum(999999.99)
        self.teeWidth.setObjectName("teeWidth")
        self.teeStem = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_13)
        self.teeStem.setGeometry(QtCore.QRect(10, 130, 111, 22))
        self.teeStem.setMaximum(999999.99)
        self.teeStem.setObjectName("teeStem")
        self.label_33 = QtWidgets.QLabel(self.hexagonGeometryBox_13)
        self.label_33.setGeometry(QtCore.QRect(10, 110, 71, 16))
        self.label_33.setObjectName("label_33")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.hexagonGeometryBox_14 = QtWidgets.QGroupBox(self.page_7)
        self.hexagonGeometryBox_14.setGeometry(QtCore.QRect(20, 10, 131, 121))
        self.hexagonGeometryBox_14.setTitle("")
        self.hexagonGeometryBox_14.setObjectName("hexagonGeometryBox_14")
        self.label_37 = QtWidgets.QLabel(self.hexagonGeometryBox_14)
        self.label_37.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_37.setObjectName("label_37")
        self.label_35 = QtWidgets.QLabel(self.hexagonGeometryBox_14)
        self.label_35.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_35.setObjectName("label_35")
        self.angleLength = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_14)
        self.angleLength.setGeometry(QtCore.QRect(10, 30, 111, 22))
        self.angleLength.setMaximum(999999.99)
        self.angleLength.setObjectName("angleLength")
        self.angleThick = QtWidgets.QDoubleSpinBox(self.hexagonGeometryBox_14)
        self.angleThick.setGeometry(QtCore.QRect(10, 80, 111, 22))
        self.angleThick.setMaximum(999999.99)
        self.angleThick.setObjectName("angleThick")
        self.stackedWidget.addWidget(self.page_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(260, 10, 221, 161))
        self.groupBox_8.setObjectName("groupBox_8")
        self.sectionAreaUnit = QtWidgets.QComboBox(self.groupBox_8)
        self.sectionAreaUnit.setGeometry(QtCore.QRect(140, 70, 69, 21))
        self.sectionAreaUnit.setObjectName("sectionAreaUnit")
        self.sectionAreaUnit.addItem("")
        self.sectionAreaUnit.addItem("")
        self.sectionAreaUnit.addItem("")
        self.sectionAreaUnit.addItem("")
        self.sectionAreaUnit.addItem("")
        self.label_25 = QtWidgets.QLabel(self.groupBox_8)
        self.label_25.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_8)
        self.label_26.setGeometry(QtCore.QRect(10, 100, 121, 16))
        self.label_26.setObjectName("label_26")
        self.sectionMomentUnit = QtWidgets.QComboBox(self.groupBox_8)
        self.sectionMomentUnit.setGeometry(QtCore.QRect(140, 120, 69, 21))
        self.sectionMomentUnit.setObjectName("sectionMomentUnit")
        self.sectionMomentUnit.addItem("")
        self.sectionMomentUnit.addItem("")
        self.sectionMomentUnit.addItem("")
        self.sectionMomentUnit.addItem("")
        self.sectionMomentUnit.addItem("")
        self.sectionCalc = QtWidgets.QPushButton(self.groupBox_8)
        self.sectionCalc.setGeometry(QtCore.QRect(70, 20, 75, 23))
        self.sectionCalc.setObjectName("sectionCalc")
        self.sectionArea = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.sectionArea.setGeometry(QtCore.QRect(10, 70, 111, 22))
        self.sectionArea.setReadOnly(True)
        self.sectionArea.setMaximum(999999.99)
        self.sectionArea.setObjectName("sectionArea")
        self.sectionMoment = QtWidgets.QDoubleSpinBox(self.groupBox_8)
        self.sectionMoment.setGeometry(QtCore.QRect(10, 120, 111, 22))
        self.sectionMoment.setReadOnly(True)
        self.sectionMoment.setMaximum(999999.99)
        self.sectionMoment.setObjectName("sectionMoment")
        self.errorField = QtWidgets.QLineEdit(self.groupBox_8)
        self.errorField.setGeometry(QtCore.QRect(40, 40, 151, 20))
        self.errorField.setObjectName("errorField")
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(40, 140, 81, 16))
        self.label_29.setObjectName("label_29")
        self.InputUnit = QtWidgets.QComboBox(self.tab_3)
        self.InputUnit.setGeometry(QtCore.QRect(40, 160, 69, 22))
        self.InputUnit.setObjectName("InputUnit")
        self.InputUnit.addItem("")
        self.InputUnit.addItem("")
        self.InputUnit.addItem("")
        self.InputUnit.addItem("")
        self.InputUnit.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 471, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 101, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(250, 60, 111, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(30, 100, 191, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 71, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(170, 40, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 80, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(390, 40, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 120, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_8.setGeometry(QtCore.QRect(390, 80, 69, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 110, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.defLoad = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.defLoad.setGeometry(QtCore.QRect(30, 40, 121, 22))
        self.defLoad.setObjectName("defLoad")
        self.defLength1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.defLength1.setGeometry(QtCore.QRect(30, 80, 121, 22))
        self.defLength1.setObjectName("defLength1")
        self.defLength2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.defLength2.setGeometry(QtCore.QRect(30, 120, 121, 22))
        self.defLength2.setObjectName("defLength2")
        self.defYoungs = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.defYoungs.setGeometry(QtCore.QRect(250, 40, 121, 22))
        self.defYoungs.setObjectName("defYoungs")
        self.def2ndMom = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.def2ndMom.setGeometry(QtCore.QRect(250, 80, 121, 22))
        self.def2ndMom.setObjectName("def2ndMom")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(240, 10, 111, 81))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(120, 10, 91, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(370, 10, 111, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_10.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_11.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_12.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.radioButton_12.setObjectName("radioButton_12")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 81, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 80, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 300, 471, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(30, 20, 71, 20))
        self.label_7.setObjectName("label_7")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 40, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.stress = QtWidgets.QLabel(self.groupBox_6)
        self.stress.setGeometry(QtCore.QRect(30, 70, 71, 20))
        self.stress.setObjectName("stress")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_6.setGeometry(QtCore.QRect(170, 90, 69, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(270, 20, 71, 20))
        self.label_9.setObjectName("label_9")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_7.setGeometry(QtCore.QRect(390, 40, 69, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.deflection = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.deflection.setGeometry(QtCore.QRect(30, 40, 121, 22))
        self.deflection.setObjectName("deflection")
        self.moment = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.moment.setGeometry(QtCore.QRect(260, 40, 121, 22))
        self.moment.setObjectName("moment")
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(30, 90, 121, 22))
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(180, 430, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 564, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.stackedWidget.hide()
        self.errorField.hide()

        self.uChannelButton.clicked.connect(self.pickShape)
        self.rectangleButton.clicked.connect(self.pickShape)
        self.iBeamButton.clicked.connect(self.pickShape)
        self.roundButton.clicked.connect(self.pickShape)
        self.hexButton.clicked.connect(self.pickShape)
        self.tBeamButton.clicked.connect(self.pickShape)
        self.angleButton.clicked.connect(self.pickShape)        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.sectionCalc.clicked.connect(self.callCalcSection)

    def pickShape(self):

        print('Step 1')

        Beam_Analysis_Funcs.pickShape(self)

    def callCalcSection(self):
        
        self.errorField.hide()

        Beam_Analysis_Funcs.callCalcSection(self)

    def callError(self, errorType):

        self.errorField.show()
        
        if errorType == 1:

            self.errorField.setText('Error: no input values.')

        if errorType == 2:

            self.errorField.setText('Error: not yet defined.')

        if errorType == 3:

            self.errorField.setText('Error: invalid geometry.')
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Section Shape"))
        self.uChannelButton.setText(_translate("MainWindow", "U-Channel"))
        self.rectangleButton.setText(_translate("MainWindow", "Rectangle"))
        self.iBeamButton.setText(_translate("MainWindow", "I-Beam"))
        self.roundButton.setText(_translate("MainWindow", "Round"))
        self.hexButton.setText(_translate("MainWindow", "Hexagon"))
        self.tBeamButton.setText(_translate("MainWindow", "T-beam"))
        self.angleButton.setText(_translate("MainWindow", "Angle"))
        self.label_24.setText(_translate("MainWindow", "Side Length"))
        self.label_18.setText(_translate("MainWindow", "Height"))
        self.label_19.setText(_translate("MainWindow", "Width"))
        self.label_20.setText(_translate("MainWindow", "Flange Width"))
        self.label_21.setText(_translate("MainWindow", "Flange Height"))
        self.label_14.setText(_translate("MainWindow", "Outside Height"))
        self.label_15.setText(_translate("MainWindow", "Outside Width"))
        self.label_16.setText(_translate("MainWindow", "Inside Width"))
        self.label_17.setText(_translate("MainWindow", "Inside Height"))
        self.label.setText(_translate("MainWindow", "Height"))
        self.label_10.setText(_translate("MainWindow", "Flange Width"))
        self.label_12.setText(_translate("MainWindow", "Flange Thickness"))
        self.label_13.setText(_translate("MainWindow", "Web Width"))
        self.label_22.setText(_translate("MainWindow", "Inner Diameter"))
        self.label_23.setText(_translate("MainWindow", "Outer Diameter"))
        self.label_32.setText(_translate("MainWindow", "Flange Thickness"))
        self.label_34.setText(_translate("MainWindow", "Flange width"))
        self.label_8.setText(_translate("MainWindow", "Stem height"))
        self.label_33.setText(_translate("MainWindow", "Stem thickness"))
        self.label_37.setText(_translate("MainWindow", "Leg length"))
        self.label_35.setText(_translate("MainWindow", "Leg thickness"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Outputs"))
        self.sectionAreaUnit.setItemText(0, _translate("MainWindow", "m^2"))
        self.sectionAreaUnit.setItemText(1, _translate("MainWindow", "cm^2"))
        self.sectionAreaUnit.setItemText(2, _translate("MainWindow", "mm^2"))
        self.sectionAreaUnit.setItemText(3, _translate("MainWindow", "ft^2"))
        self.sectionAreaUnit.setItemText(4, _translate("MainWindow", "in^2"))
        self.label_25.setText(_translate("MainWindow", "Area"))
        self.label_26.setText(_translate("MainWindow", "Second Moment of Area"))
        self.sectionMomentUnit.setItemText(0, _translate("MainWindow", "m^4"))
        self.sectionMomentUnit.setItemText(1, _translate("MainWindow", "cm^4"))
        self.sectionMomentUnit.setItemText(2, _translate("MainWindow", "mm^4"))
        self.sectionMomentUnit.setItemText(3, _translate("MainWindow", "ft^4"))
        self.sectionMomentUnit.setItemText(4, _translate("MainWindow", "in^4"))
        self.sectionCalc.setText(_translate("MainWindow", "Calculate"))
        self.label_29.setText(_translate("MainWindow", "Input Units"))
        self.InputUnit.setItemText(0, _translate("MainWindow", "Meters"))
        self.InputUnit.setItemText(1, _translate("MainWindow", "cm"))
        self.InputUnit.setItemText(2, _translate("MainWindow", "mm"))
        self.InputUnit.setItemText(3, _translate("MainWindow", "Feet"))
        self.InputUnit.setItemText(4, _translate("MainWindow", "Inches"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Section Calculator"))
        self.groupBox.setTitle(_translate("MainWindow", "Manual Inputs"))
        self.label_2.setText(_translate("MainWindow", " Beam Length "))
        self.label_3.setText(_translate("MainWindow", " Young\'s Modulus"))
        self.label_4.setText(_translate("MainWindow", "2nd Moment of Area"))
        self.label_5.setText(_translate("MainWindow", "Distance from load to closest support"))
        self.label_6.setText(_translate("MainWindow", "Load"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Netwons"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Pounds"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Meters"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "cm"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "mm"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Feet"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Inches"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "GPa"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Mpsi"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Meters"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "cm"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "mm"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Feet"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "Inches"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "m^4"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "cm^4"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "mm^4"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "ft^4"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "in^4"))
        self.pushButton_2.setText(_translate("MainWindow", "Import From Section Calculator"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Load Type"))
        self.radioButton_7.setText(_translate("MainWindow", "Point"))
        self.radioButton_8.setText(_translate("MainWindow", "Distributed"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Support 2"))
        self.radioButton_4.setText(_translate("MainWindow", "Fixed"))
        self.radioButton_5.setText(_translate("MainWindow", "Simple"))
        self.radioButton_6.setText(_translate("MainWindow", "Free"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Load Location"))
        self.radioButton_10.setText(_translate("MainWindow", "Centered"))
        self.radioButton_11.setText(_translate("MainWindow", "Uncentered"))
        self.radioButton_12.setText(_translate("MainWindow", "End"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Support 1"))
        self.radioButton.setText(_translate("MainWindow", "Fixed"))
        self.radioButton_2.setText(_translate("MainWindow", "Simple"))
        self.radioButton_3.setText(_translate("MainWindow", "Free"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Analysis"))
        self.label_7.setText(_translate("MainWindow", "Deflection"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Netwons"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Pounds"))
        self.stress.setText(_translate("MainWindow", "Static stress"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Pascals"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "PSI"))
        self.label_9.setText(_translate("MainWindow", "Moment"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "N-m"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "N-cm"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "N-mm"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Ft-lb"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "in-lb"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "in-oz"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Deflection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

