#!/usr/bin/env python


#############################################################################
##
## Copyright (C) 2013 Riverbank Computing Limited.
## Copyright (C) 2010 Nokia Corporation and/or its subsidiary(-ies).
## All rights reserved.
##
## This file is part of the examples of PyQt.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of Nokia Corporation and its Subsidiary(-ies) nor
##     the names of its contributors may be used to endorse or promote
##     products derived from this software without specific prior written
##     permission.
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
## $QT_END_LICENSE$
##
#############################################################################


from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createLeftCenterGroupBox()
        self.createRightCenterGroupBox()
        self.createinputGroupBox()
        self.createoutputGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)       
        mainLayout.addWidget(self.leftCenterGroupBox, 1, 1)
        mainLayout.addWidget(self.rightCenterGroupBox, 1, 2)
        mainLayout.addWidget(self.topRightGroupBox, 1, 3)
        mainLayout.addWidget(self.inputGroupBox, 2, 0, 1, 4)
        mainLayout.addWidget(self.outputGroupBox, 3, 0, 1, 4)
        self.setLayout(mainLayout)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        if (self.useStylePaletteCheckBox.isChecked()):
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(self.originalPalette)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Support 1")

        radioButton1 = QRadioButton("Fixed")
        radioButton2 = QRadioButton("Simple")
        radioButton3 = QRadioButton("Free")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createLeftCenterGroupBox(self):
        self.leftCenterGroupBox = QGroupBox("Support 2")

        radioButton1 = QRadioButton("Fixed")
        radioButton2 = QRadioButton("Simple")
        radioButton3 = QRadioButton("Free")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)
        self.leftCenterGroupBox.setLayout(layout)

    def createRightCenterGroupBox(self):
        self.rightCenterGroupBox = QGroupBox("Load Type")

        radioButton1 = QRadioButton("Point")
        radioButton2 = QRadioButton("Distributed")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addStretch(1)
        self.rightCenterGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Load Location")

        radioButton1 = QRadioButton("Centered")
        radioButton2 = QRadioButton("Uncentered")
        radioButton3 = QRadioButton("End")
        radioButton4 = QRadioButton("Outside")

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createinputGroupBox(self):
        self.inputGroupBox = QGroupBox("Manual Inputs")
        
        label1 = QLabel('Load')
        textField1 = QLineEdit('',self)
        dropBox1 = QComboBox()
        dropBox1.addItems(["Newtons", "Pounds"])

        label2 = QLabel('Beam Length')
        textField2 = QLineEdit('',self)
        dropBox2 = QComboBox()
        dropBox2.addItems(["Meters", "cm", "mm", "Feet", "Inches"])

        label3 = QLabel("Young's Modulus")
        textField3 = QLineEdit('',self)
        dropBox3 = QComboBox()
        dropBox3.addItems(["GPa", "Mpsi"])

        label4 = QLabel('2nd Moment of Area')
        textField4 = QLineEdit('',self)
        dropBox4 = QComboBox()
        dropBox4.addItems(["m^4", "ft^4"])

        label5 = QLabel('Distance from load to closest support')
        textField5 = QLineEdit('',self)
        dropBox5 = QComboBox()
        dropBox5.addItems(["Meters", "cm", "mm", "Feet", "Inches"])
      
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0, 1, 2)
        layout.addWidget(textField1, 1, 0, 1, 2)
        layout.addWidget(dropBox1, 1, 3, 1, 2)
        
        layout.addWidget(label2, 2, 0, 1, 2)
        layout.addWidget(textField2, 3, 0, 1, 2)
        layout.addWidget(dropBox2, 3, 3, 1, 2)

        layout.addWidget(label3, 0, 6, 1, 2)
        layout.addWidget(textField3, 1, 6, 1, 2)
        layout.addWidget(dropBox3, 1, 8, 1, 2)

        layout.addWidget(label4, 2, 6, 1, 2)
        layout.addWidget(textField4, 3, 6, 1, 2)
        layout.addWidget(dropBox4, 3, 8, 1, 2)

        layout.addWidget(label5, 0, 12, 1, 4)
        layout.addWidget(textField5, 1, 12, 1, 2)
        layout.addWidget(dropBox5, 1, 14, 1, 2)   
        
        layout.setRowStretch(5, 1)
        self.inputGroupBox.setLayout(layout)

    def createoutputGroupBox(self):
        self.outputGroupBox = QGroupBox("Outputs")

        layout = QGridLayout()
        self.outputGroupBox.setLayout(layout)
   
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 
