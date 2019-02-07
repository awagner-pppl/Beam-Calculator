def callCalcSection(self):

    #Determines what calculation to perform based on radio button

    self.errorField.hide()

    if self.rectangleButton.isChecked():

        if (self.rectangleOutHeight.value() <= 0 or
            self.rectangleOutWidth.value() <= 0 or
            self.rectangleInHeight.value() <= 0 or
            self.rectangleInWidth.value() <= 0):

            errorType = 1

            self.callError(errorType)
            
        else:

            calcSectionArea = (self.rectangleOutHeight.value()*
                               self.rectangleOutWidth.value() -
                               self.rectangleInHeight.value()*
                               self.rectangleInWidth.value())
                     
            self.sectionArea.setValue(calcSectionArea)
            
            calcMoment = ((self.rectangleOutHeight.value()*
                           self.rectangleOutWidth.value()**3 -
                           self.rectangleInHeight.value()*
                           self.rectangleInWidth.value()**3)/12)

            self.sectionMoment.setValue(calcMoment)
                
    if self.iBeamButton.isChecked():

        if (iBeamHeight <= 0 or iBeamWidth <= 0 or
            iBeamFlange <= 0 or iBeamWeb <= 0):

                errorType = 1

                self.errorField()

    if self.uChannelButton.isChecked():
        
        errorType = 1

        self.errorField()

    if self.roundButton.isChecked():
        
        errorType = 1

        self.errorField()

    if self.hexButton.isChecked():
        
        errorType = 1

        self.errorField()

    if self.tBeamButton.isChecked():
        
        errorType = 1

        self.errorField()

    if self.angleButton.isChecked():
        
        errorType = 1

        self.errorField()

def callError(self, errorType):

    self.errorField.show()
    
    if errorType == 1:

        self.errorField.setText('Error: no input values')

def hideRadio(self):

    #Hides geometry inputs based on radio button choice

    self.stackedWidget.show()

    if self.rectangleButton.isChecked():
        self.stackedWidget.setCurrentIndex(2)
        sectionType = 1

    if self.iBeamButton.isChecked():
        self.stackedWidget.setCurrentIndex(3)
        sectionType = 3

    if self.uChannelButton.isChecked():
        self.stackedWidget.setCurrentIndex(1)
        sectionType = 2

    if self.roundButton.isChecked():
        self.stackedWidget.setCurrentIndex(4)
        sectionType = 4

    if self.hexButton.isChecked():
        self.stackedWidget.setCurrentIndex(0)
        sectionType = 0

    if self.tBeamButton.isChecked():
        self.stackedWidget.hide()

    if self.angleButton.isChecked():
        self.stackedWidget.hide() 
