import math

def callSectionCalc(self):

    # Determines what calculation to perform based on radio button

    conFact = unitConv(self)

    if self.rectangleButton.isChecked():

        if (self.rectangleOutHeight.value() <= 0 or
            self.rectangleOutWidth.value() <= 0):

            self.callError(1 , 1)

        if (self.rectangleOutHeight.value()
            < self.rectangleInHeight.value() or
            self.rectangleOutWidth.value()
            < self.rectangleInWidth.value()):

            self.callError(3, 1)
            
        else:

            self.sectionArea.setValue(
                (self.rectangleOutHeight.value() *
                self.rectangleOutWidth.value() -
                self.rectangleInHeight.value() *
                self.rectangleInWidth.value() )* (conFact ** 2))
            
            self.sectionMoment.setValue(
                (self.rectangleOutHeight.value() *
                 self.rectangleOutWidth.value() ** 3 -
                 self.rectangleInHeight.value() *
                 self.rectangleInWidth.value() ** 3) / 12 *
                (conFact ** 4))
            
    if self.iBeamButton.isChecked():

        if (self.iBeamHeight.value() <= 0 and
            self.iBeamWidth.value() <= 0 and
            self.iBeamFlange.value() <= 0 and
            self.iBeamWeb.value() <= 0):

            self.callError(1 , 1)

        elif (self.iBeamHeight.value() <= 0 or
            self.iBeamWidth.value() <= 0 or
            self.iBeamFlange.value() <= 0 or
            self.iBeamWeb.value() <= 0):

            self.callError(3 , 1)

        else:

            self.sectionArea.setValue((
                self.iBeamHeight.value() * self.iBeamWidth.value() ** 3
                - (self.iBeamHeight.value() - 2 *
                self.iBeamFlange.value()) * (self.iBeamWidth.value() -
                self.iBeamWeb.value()) ** 3) / 12 * (conFact ** 2) )

            self.sectionMoment.setValue(
                self.iBeamHeight.value() * self.iBeamWidth.value() -
                (self.iBeamHeight.value() - 2 * self.iBeamFlange.value()
                 ) * (self.iBeamWidth.value() - self.iBeamWeb.value()
                * (conFact ** 4)))
            
    if self.uChannelButton.isChecked():

        if (self.channelHeight.value() <= 0 and
            self.channelWidth.value() <= 0 and
            self.flangeHeight.value() <= 0 and
            self.flangeWidth.value() <= 0):

            self.callError(1 , 1)

        elif (self.flangeHeight.value() > self.channelHeight.value() or
              self.flangeWidth.value() > self.channelWidth.value()):

            self.callError(3 , 1)

        else:

            self.sectionArea.setValue(
                (self.channelHeight.value() *
                self.channelWidth.value() -
                self.flangeHeight.value() * self.flangeWidth.value())
                * (conFact ** 2))

            self.sectionMoment.setValue(
                (self.channelHeight.value() *
                self.channelWidth.value() ** 3 -
                self.flangeHeight.value() * self.flangeWidth.value()
                ** 3) / 12 * (conFact ** 4))
        
    if self.roundButton.isChecked():

        if self.roundOD.value() <= 0:

            self.callError(1 , 1)

        else:
            
            self.sectionArea.setValue(
                math.pi * ((self.roundOD.value() / 2) ** 2 -
                (self.roundID.value() / 2) ** 2)  * (conFact ** 2))

            self.sectionMoment.setValue(
                (math.pi * (self.roundOD.value() ** 4 -
                self.roundID.value() ** 4) ) / 64 * (conFact ** 4))

    if self.hexButton.isChecked():

        if self.hexLength.value() <= 0:

            self.callError(1 , 1)

        else:

            self.sectionArea.setValue(
                self.hexLength.value() ** 2 * 3 / 2 * math.sqrt(3) *
                (conFact ** 2))

            self.sectionMoment.setValue(
                5 / 16 * math.sqrt(3) * self.hexLength.value() ** 4 *
                (conFact ** 4))

    if self.tBeamButton.isChecked():

        if (self.teeHeight.value() <= 0 or self.teeFlange.value() <= 0 or
        self.teeWidth.value() <= 0 or self.teeStem.value() <= 0):

            self.callError(1 , 1)

        else:
            
            self.sectionArea.setValue(
                (self.teeHeight.value() - self.teeFlange.value()) *
                self.teeStem.value() + self.teeWidth.value() *
                self.teeFlange.value() * (conFact ** 2))

            self.sectionMoment.setValue(
                self.teeStem.value() ** 3 * (self.teeHeight.value() -
                self.teeFlange.value() ) / 12 + self.teeWidth.value() ** 3 *
                self.teeFlange.value() / 12 * (conFact ** 4))

    if self.angleButton.isChecked():

        if self.angleLength.value() <= 0 or self.angleThick.value() <= 0:

            self.callError(1 , 1)

        else:

            a = self.angleLength.value()

            t = self.angleThick.value()

            y = a - (a ** 2 + a * t - t ** 2)/( 2 * (2 * a - t))

            self.sectionArea.setValue(
                (t * y ** 3 + a * (a - y) ** 3 - (a - t)
                 * (a - y - t) ** 3) / 3 * (conFact ** 2))

            self.sectionMoment.setValue()

    elif (self.angleButton.isChecked() != True
          and self.tBeamButton.isChecked() != True
          and self.hexButton.isChecked() != True
          and self.roundButton.isChecked() != True
          and self.uChannelButton.isChecked() != True
          and self.iBeamButton.isChecked() != True
          and self.rectangleButton.isChecked() != True):

        self.callError(3 , 1)

def pickShape(self):

    # Hides geometry inputs based on radio button choice

    self.stackedWidget.show()

    if self.rectangleButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(2)

    if self.iBeamButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(3)

    if self.uChannelButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(1)

    if self.roundButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(4)

    if self.hexButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(0)

    if self.tBeamButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(5)

    if self.angleButton.isChecked():
        
        self.stackedWidget.setCurrentIndex(6)

def unitConv(self):

    unitDict = {
        'Meters': ['m', 1],
        'cm': ['cm', 0.01],
        'mm': ['mm', 0.001],
        'Inches': ['in', 0.0254],
        'Feet': ['ft', 0.3048]
        }

    dictCallOut = self.outputUnit.currentText()

    dispUnit = unitDict[dictCallOut][0]

    self.sectionArea.setSuffix(' ' + dispUnit + '^2')

    self.sectionMoment.setSuffix(' ' + dispUnit + '^4')
    
    convFact = ( unitDict[self.inputUnit.currentText()][1] /
                 unitDict[dictCallOut][1] )

    return convFact
