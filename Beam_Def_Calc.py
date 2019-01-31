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

    if s1 = 's' and s2 = 'f' or s1 = 'f' and s2 = 's':

        if l = 'e' or l = 'o':

            #This should return an error

        if t = 'p':

            if l = 'c': #sfpc or fspc

                f = (7*W*l^3)/(768*E*I);

            if l = 'n': #sfpn or fspn

                #This should return an error - for now
                           
        if t = 'd': 

            if l = 'u': #sfdu or fsdu

                f = (W*l^3)/(185*E*I);

    if s1 = 'f' and s2 = 'f':

        if l = 'e' or l = 'o':

            #This should return an error

        if t = 'p':

            if l = 'c': #ffpc

                f = (W*l^3)/(192*E*I);

            if l = 'n': #ffpn

                #This should return an error
                
        if t = 'd':

            if l = 'u': #ffdu

                f = (W*l^3)/(384*E*I);

    if s1 = 's' and s2 = 's'1:

        if l = 'e':

            #This should return an error

        if t = 'p':

            if l = 'c': #sspc

                f = (W*l^3)/(48*E*I);

                x = b/2;

            if l = 'n': #sspn

                f = (W*c1)/(3*E*I*b)*(c/3*(b+c1))^(3/2);

                x = (c/3*(b-c1))^(1/2);

            if l = 'o': #sspo

                f = (W*c*l^2)/(8*E*I);

                f2 = (W*c^2)/(3*E*I)*(c+3*b/2);
                
        if t = 'd':

            if l = 'c' or l = 'o' or l ='n':

                #This should return an error

            if l = 'u': #ssdu

                f = (5*W*l^3)/(384*E*I);

    if s1 = 's' and s2 = 'e' or s1 = 'e' and s2 = 's':

        #This should return an error

    if s1 = 'f' and s2 = 'r' or s1 = 'r' and s2 = 'f':

        if t = 'p':

            if l = 'c': #frpc or rfpc

                #This should return an error - for now

            if l = 'n': #frpn or rfpn

                #This should return an error - for now

            if l = 'e': #frpe or rfpe

                f = (W*l^3)/(3*E*I);
                
        if t = 'd':

            if l = 'u': #frdu or rfdu

                f = (W*l^3)/(384*E*I);             

    return()

                
    
    
