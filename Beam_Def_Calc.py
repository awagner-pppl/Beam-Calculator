'''These functions output the maximum deflection magnitude and location.

Parameters for specifying the mechanical geometry are:

s1 = support on one end:
    f = fixed
    s = simply supported
    r = free (fixed at other end only)
s2 = support on other end:
    f = fixed
    s = simply supported
    r = free (fixed at other end only)
t = type of load:
    p = point
    d = distributed    
l = location:
    point loads: c = center; n = uncentered; e = end; o = outside
    supports (simply supported only)
    distributed loads: u = uniform; 
    
Parameters
----------
s1(support 1): string
s2(support 2): string
t(load type): string
l(load location):string
W(load): integer
b(beam length): integer
E(Modulus of elasticity): integer
I(Beam 2nd moment of area): integer
c(Distance from load to furthest support): integer
c1(Distance from load to closest support): integer

Outputs are:

f = Maximum deflection
x = Location of f [max deflection]

All calculations are based on Marks' Standard Handbook for Mechanical
Engineers, 10th edition, section 5-23, table 5.2.2.

'''

#Inputs
s1 = None; #support 1
s2  = None; #support 2
t = None; #load type
l = None; #load location
W = 0; #load
b = 0; #beam length
E = 0; #Modulus of elasticity
I = 0; #Beam 2nd moment of area
c = None; #Distance from load to furthest support
c1 = None; #Distance from load to closest support

#Outputs
x = 0; #Location of f [max deflection]
f = 0; #Maximum deflection between supports
f2 = 0; #Maximum deflection outside simple supports


def bdc(s1, s2, t, l, W, b, E, I, c, c1):

    W = self.defLoad.value()

    E = self.defYoungs.value()

    I = self.def2ndMom.value()

    b = self.defLength1.value()

    L = self.defLength2.value()

    if self.sFS.isChecked():

        if self.loadP.isChecked() and self.loadC.isChecked():

            f = (7 * W * L ** 3) / (768 * E * I)
                           
        if self.loadD.isChecked() and self.loadUn.isChecked(): 

            f = (W * L ** 3) / (185 * E * I)

        else:

            self.error(1 , 2)

    if self.sFF.isChecked():

        if t = 'p':

            if l = 'c': #ffpc

                f = (W * L ** 3) / (192 * E * I)
               
        if t = 'd':

            if l = 'u': #ffdu

                f = (W * L ** 3) / (384 * E * I)

    if self.sSS.isChecked():

        if self.cLoad.isChecked():

            f = (W * L ** 3) / (48 * E * I)

            x = b / 2

        if self.uLoad.isChecked(): #sspn

            f = ((W * c1) / (3 * E * I * b) * (c / 3 * (b + c1) )
                ** (3 / 2))
                
            x = (c / 3 * (b - c1) ) ** (1 / 2)

        if self.oLoad.isChecked(): #sspo

            f = (W * c * L ** 2) / (8 * E * I);

            f2 = (W * c ** 2) / (3 * E * I) * (c + 3 * b / 2)

            x = b / 2
                
        if self.ueLoad.isChecked():

            f = (5 * W * L ** 3) / (384 * E * I)

    if self.sFR.isChecked():

        if self.eLoad.isChecked(): #frpe or rfpe

            f = (W * L ** 3) / (3 * E * I);

        if self.ueLoad.isChecked(): #frdu or rfdu

            f = (W * L ** 3) / (384 * E * I);             

    return()

def pL(self):

    
                
    
    
