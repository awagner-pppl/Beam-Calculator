import math

def callCalcSection(self):

    # Determines what calculation to perform based on radio button

    conFact = unitConv(self)

    if self.rectangleButton.isChecked():

        if (self.rectangleOutHeight.value() <= 0 or
            self.rectangleOutWidth.value() <= 0):

            errorType = 1

            self.callError(errorType)
            
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

        if (self.iBeamHeight.value() <= 0 or
            self.iBeamWidth.value() <= 0 or
            self.iBeamFlange.value() <= 0 or
            self.iBeamWeb.value() <= 0):

            errorType = 1

            self.callError(errorType)

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

        if (self.channelHeight.value() <= 0 or
            self.channelWidth.value() <= 0 or
            self.flangeHeight.value() <= 0 or
            self.flangeWidth.value() <= 0):

            errorType = 1

            self.callError(errorType)

        elif (self.flangeHeight.value() > self.channelHeight.value() or
              self.flangeWidth.value() > self.channelWidth.value()):

            errorType = 3

            self.callError(errorType)

        else:

            self.sectionArea.setValue(
                self.channelHeight.value() *
                self.channelWidth.value() -
                self.flangeHeight.value() * self.flangeWidth.value()
                * (conFact ** 2))

            self.sectionMoment.setValue(
                (self.channelHeight.value() *
                self.channelWidth.value() ** 3 -
                self.flangeHeight.value() * self.flangeWidth.value()
                ** 3) / 12 * (conFact ** 4))
        
    if self.roundButton.isChecked():

        if self.roundOD.value() <= 0:

            errorType = 1

            self.callError(errorType)

        else:
            
            self.sectionArea.setValue(
                math.pi * ((self.roundOD.value() / 2) ** 2 -
                (self.roundID.value() / 2) ** 2)  * (conFact ** 2))

            self.sectionMoment.setValue(
                (math.pi * (self.roundOD.value() ** 4 -
                self.roundID.value() ** 4) ) / 64 * (conFact ** 4))

    if self.hexButton.isChecked():

        if self.hexLength.value() <= 0:

            errorType = 1

            self.callError(errorType)

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

            errorType = 1

            self.callError(errorType)

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

            errorType = 1

            self.callError(errorType)

        else:

            a = self.angleLength.value()

            t = self.angleThick.value()

            y = a - (a ** 2 + a * t - t ** 2)/( 2 * (2 * a - t))

            self.sectionArea.setValue(
                (t * y ** 3 + a * (a - y) ** 3 - (a - t) * (a - y - t) ** 3)
                / 3 * (conFact ** 2))

            self.sectionMoment.setValue()


def pickShape(self):
    
##    print('Step 2')

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

    outFact = outputUnitLabel(self)

    if str(self.inputUnit.currentText()) == 'Meters':

        inFact = 1

    elif str(self.inputUnit.currentText()) == 'cm':

        inFact = 0.01

    elif str(self.inputUnit.currentText()) == 'mm':

        inFact = 0.001

    elif str(self.inputUnit.currentText()) == 'Inches':

        inFact = 0.0254

    elif str(self.inputUnit.currentText()) == 'Feet':

        inFact = 0.3048

    convFact = inFact / outFact

    return convFact

def outputUnitLabel(self):
    
    if str(self.outputUnit.currentText()) == 'Meters':
        
        self.sectionArea.setSuffix(' m^2')

        self.sectionMoment.setSuffix(' m^4')

        outConvFact = 1

    elif str(self.outputUnit.currentText()) == 'cm':

        self.sectionArea.setSuffix(' cm^2')

        self.sectionMoment.setSuffix(' cm^4')

        outConvFact = 0.01

    elif str(self.outputUnit.currentText()) == 'mm':

        self.sectionArea.setSuffix(' mm^2')

        self.sectionMoment.setSuffix(' mm^4')

        outConvFact = 0.001

    elif str(self.outputUnit.currentText()) == 'Inches':

        self.sectionArea.setSuffix(' in^2')

        self.sectionMoment.setSuffix(' in^4')

        outConvFact = 0.0254

    elif str(self.outputUnit.currentText()) == 'Feet':

        self.sectionArea.setSuffix(' ft^2')

        self.sectionMoment.setSuffix(' ft^4')

        outConvFact = 0.3048

    else:

        print('Error: not yet defined.')

    return outConvFact
