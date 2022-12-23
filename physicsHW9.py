import math

mu0 = 4 * math.pi *10**(-7)
c = 2.998*10**8

# def function5(f,p):
#     r = 2*f
#     print(r)
#     i = (p*f)/(p-f)
#     print(i)
#     m = (-1)*i/p
#     print(m)
# # print(function5(11,16))
# print(function5(43,32))

# def function10(p,f):
#     i = (p*f)/(p-f)
#     print(i)
#     m = (-1)*i/p
#     print(m)
# print(function10(25,5)) #for function 8
# print(function10(13,-41)) #for function 10
# print(function10(13,24)) #for function 9
# '''
# The wavelength of yellow sodium light in air is 589 nm. (a) What is its frequency? (b) What is its 
# wavelength in glass whoseindex of refraction is 1.52? (c) From the results of (a)and (b), find its 
# speed in this glass.
# '''
# def function13(lam,n):
#     f = c/(lam*(10**(-9)))
#     print("Part A ==>", f, "Hz")
#     lamn = lam/n
#     print("Part B ==>", lamn, "nm")
#     v = f*(lamn*(10**(-9)))
#     print("Part C ==>", v,"m/s")
#     pass
# print(function13(660,1.52))
# '''two light rays go through different paths by reflecting from the various flat surfaces shown. The light 
#    waves have a wavelength of 420.0 nm and are initially in phase. What are the (a) smallest and (b) second 
#    smallest value of distance L that will put the waves exactly out of phase as they emerge from the region?
#    '''
# def function14(lam):
#     L1 = lam/8
#     print(L1)
#     L2 = 3*lam/8
#     print(L2)
    
# print(function14(440))
# '''Two waves of the same frequency have amplitudes 1.00 and 2.00. They interfere at a point where their phase
#     difference is 60.0°. What is the resultant amplitude?
#     '''
# def function15(f1,f2,t1):
#     #Eh = (f1**2+f2**2-(2*f1*f2*(m.cos(180-t1)*180/m.pi)))**(1/2)
#     Eh = f1 + f2*m.cos(t1) #* 
#     # print(Eh)
#     Ev = f2*m.sin(t1)
#     # print(Ev)
#     Em = (Eh**2+Ev**2)**(1/2)
#     # print(Em)
# print(function15(0.794,2.95,54*m.pi/180))


# f = [4.000,5.000,6.00,7.00,8.00,9.00,10.00,11.00,12.00,13.00,14.00]
# f_uncertainty_ab = [0.005,0.003,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01]

# R,R_uncertainty_ab,R_uncertainty_rel = 26.4, 1.32, 0.05
# inductorU1 = [130, 104, 86, 74,66,56,50,46,42,38,34]
# inductorU1_Uncertainty_rel = [12/130,10/104,4/86,8/74,6/66,6/56,4/50,4/46,4/42,4/38,4/34] # relative uncertainty for U1
# Vl = [10.8,10.8,10.6,10.6,10.4,10.2,10.0,10.0,9.6,9.6,9.2] 
# Vl_Uncertainty_rel = [.05/10.8,.05/10.8,.05/10.6,.05/10.6,.05/10.4,.05/10.2,.05/10.0,.05/10.0,.05/9.6,.05/9.6,.05/9.2] 
# ConductorU1 = [44, 56, 60, 68, 78, 88,100,108,118,128,134] # U1 values for each frequency when using the conductor in the circuit
# ConductorU1_Uncertainty_rel = [10/44,8/56,14/60,8/68,12/78,8/88,8/100,8/108,12/118,8/128,12/134] # relative uncertainty for U1
# Vc = [10.8,10.8,10.8,10.8,10.8,10.9,10.9,10.9,10.9,10.9,10.9] 
# Vc_Uncertainty_rel = [0.05/10.8,0.05/10.8,0.05/10.8,0.05/10.8,0.05/10.8,0.1/10.9,0.1/10.9,0.1/10.9,0.1/10.9,0.1/10.9,0.1/10.9]

# for i in range(11):
#     Xl = round(Vl[i]*R/ (inductorU1[i]*0.001),3)
#     Xl_uncertainty = Vl_Uncertainty_rel[i] + R_uncertainty_rel + inductorU1_Uncertainty_rel[i] 
#     print("Xl[",i,"] = ",Xl,"+-",round(Xl_uncertainty*Xl,3),"or", round(Xl_uncertainty*100,0),"%")
#     Xc = round(Vc[i]*R/ (ConductorU1[i]*0.001),3)
#     Xc_uncertainty = Vc_Uncertainty_rel[i] + R_uncertainty_rel + ConductorU1_Uncertainty_rel[i]
#     print("Xc[",i,"] = ",Xc,"+-",round(Xc_uncertainty*Xc,3),"or", round(Xc_uncertainty*100,0),"%\n")



# for i in range(0,10):
#     print()

# def function4(N,n_m,r,i,d_dt,R):
#     volt = (-1)*mu0*(N*n_m)*(m.pi*(r**2))*(i/d_dt)
#     curr = volt/R
#     return str(curr) + " A"
# f4 = function4(99,24000,0.018,1.3,0.026, 5.8)
# print(f4,"\n\n")

# def function5(c1,c2,t):
#     comp =round(((c1*2)*t)+ c2,2)
#     return str(comp) + " mV and the EMF is to the left"
# f5 =function5(8.2,10,1.7)
# print(f5,"\n\n")

# def function6(L,dB_dt,E):
#     comp =((L**2)/2)*(dB_dt)
#     E+= comp
#     return str(E) + " V and is counterclockwise"
# f6 = function6(1.7,0.87,18)
# print(f6,"\n\n")

# def function7(a,c,t):
#     comp = (a**3)*c*t
#     return str(comp) + " V and it is clockwise "
# f7 = function7(0.023,3.4,3.1)
# print(f7,"\n\n")

# def function8(r1,r2,dB_dt):
#     if (r2 == 0):
#         comp = ((m.pi*r1**2))*dB_dt *(-1)
#     elif(r1 == 0):
#         comp = ((m.pi*r2**2))*dB_dt *(-1)
#     else:
#         comp = (m.pi*((r2**2)-(r1**2)))*dB_dt
#     comp *= 10**3
#     return str(comp)

# f8a = function8(.219,0,0.0117)
# f8b = function8(0,.311,0.0117)
# f8c = function8(.219,.311,0.0117)
# print("a) ==>{0} mV\nb) ==> {1} mV\nc) ==> {2} mV\n\n".format(f8a,f8b,f8c))

# def function9(e,di_dt):
#     comp = e/(di_dt)
#     return str(comp)
# f9 = function9(24,30000)
# # f9 = function9(17,25000)
# print("a) ==> if it wants to push current to the right then it is decreasing\nb) ==> {0} H\n\n".format(f9))

# def inductParallel(L1,L2):
#     comp = (1/L1) + (1/L2)
#     Leg = (1/comp)
#     return Leg

# def function10(L1,L2,L3,L4):
#     comp = inductParallel(L2,L3)
#     comp += L1 +L4
#     return comp
    
# f10 = function10(32.9,52.7,20.9,18.4)
# print("Leq ==> ",f10," mH\n\n")

# def function11(i0,L,E):
#     comp = (i0*L)/E
#     return comp
# f11 = function11(3.0,10.0,13.0)
# print("a) ==> t=",f11," seconds\n\n")

#i1 current through resistor downward
#i2 current through conductor downward
#junction rule: i = i1+i2
#Loop rule: i1R-L(di2_dt) = 0
#(di1_dt = -(di2_dt))

# def function12(i,t):
#     exp = (t) *(-1)
#     comp = i*(1- m.e**exp)
#     return comp
# f12 = function12(1.05,80)
# print(f12,"\n\n")

# c = 0.005 *10**-6
# prob1 =[]
# def ReactanceCapacitor(f):
#     return 1/(2*m.pi*f*c)
# for i in range(4,15):
#     prob1.append( round(ReactanceCapacitor(1000*i),3))
# L = 0.08
# prob2=[]
# def ReactanceInductor(f):
#     return 2*m.pi*f*L
# for i in range(4,15):
#     prob2.append(round(ReactanceInductor(1000*i),3))
# print(prob1)
# print(prob2)
# def ReactanceSeriesCiruit(lst1,lst2):
#     reactance = []
#     for i in range(11):
#         reactance.append(lst2[i] - lst1[i])
#     return reactance
# prob3 = ReactanceSeriesCiruit(prob1,prob2)
# for i in range(11):
#     print(round(prob3[i],3))
#     print (i)

# print(prob3)

# def VelocityCoil(v0,g,x,x0):
#     v = ((v0**2) + (2*g)*(x-x0))**(1/2)
#     return v
# # print("velocity in the coil at a height of 20 cm",round(VelocityCoil(0,9.81,5,0),2)," cm/s")
# # print("velocity in the coil at a height of 15 cm",round(VelocityCoil(0,9.81,10,0),2)," cm/s")
# # print("velocity in the coil at a height of 10 cm",round(VelocityCoil(0,9.81,15,0),2)," cm/s")
# # print("velocity in the coil at a height of 5 cm",round(VelocityCoil(0,9.81,20,0),2)," cm/s")

# height = [20,15,10,5]
# percentage = []
# for i in height:
#     comp = 0.1/i
#     percentage.append(comp)

# v = [VelocityCoil(0,9.81,5,0),VelocityCoil(0,9.81,10,0),VelocityCoil(0,9.81,15,0),VelocityCoil(0,9.81,20,0)]
# v1_uncertainty = v[0]*percentage[3]
# v2_uncertainty = v[1]*percentage[1]
# v3_uncertainty = v[2]*percentage[2]
# v4_uncertainty = v[3]*percentage[0]

# print(round(v[0],2),"+-",round(v1_uncertainty,2)," cm/s")
# print(round(v[1],2),"+-",round(v2_uncertainty,2)," cm/s")
# print(round(v[2],2),"+-",round(v3_uncertainty,2)," cm/s")
# print(round(v[3],2),"+-",round(v4_uncertainty,2)," cm/s")

# def uncertaintyADD(dv1,dv2):
#     total_uncertainty = ((dv1**2)+(dv2**2))**(1/2)
#     return total_uncertainty

# print(uncertaintyADD(0.15,0.15))

# lam = 633 *10 **-9
# history=[]
# def width_of_slit(m,l,x, string):
#     a = (m*lam*l)/(x*10**-2)
#     print(string,"of the slit is", round(a*10**3,2),"mm when x =", x, "cm")
#     history.append(a)
#     return ''
# def width_of_slit_part_3(m,l,x, string, d):
#     a = d/2+(m*lam*l)/(x*10**-2)
#     print(string,"of the slit is", round(a*10**3,5),"mm when x =", x, "cm")
#     history.append(a)
#     return ''
# # Part 1
# print("Part 1")
# print(width_of_slit(1, 0.54, 0.8,"width"),end=' ')
# print(width_of_slit(2, 0.54, 1.65,"width"),end=' ')
# print(width_of_slit(3, 0.54, 2.5,"width"),end=' ')
# print("Best value",round(((history[0]+history[1]+history[2])/3)*10**3,2))
# # Part 2
# print("Part 2")
# print(width_of_slit(1, 0.6, 0.45,"diamter"),end=' ')
# print(width_of_slit(2, 0.6, 0.85,"diamter"),end=' ')
# print(width_of_slit(3, 0.6, 1.25,"diamter"),end=' ')
# print(width_of_slit(4, 0.6, 1.65,"diamter"),end=' ')
# print("Best value",round(((history[3]+history[4]+history[5]+history[6])/4)*10**3,2))
# # Part 3 Slit spacing
# print("Part 3 Slit Spacing")
# print(width_of_slit(1, 0.68, 1.65,"Slit Spacing"),end=' ')
# print(width_of_slit(2, 0.68, 3,"Slit Spacing"),end=' ')
# print("Best value",round(((history[7]+history[8])/2)*10**3,2))
# # Part 3 diameter
# print("Part 3 Width")
# print(width_of_slit_part_3(1, 0.68, 1.65,"width", history[7]),end=' ')
# print("Best value",round(((history[9]))*10**3,2))



def function4(phase, lam,n1,n2):
    L = (phase*(lam*10**-9))/(2*math.pi*(n1-n2))
    print (L)
print(function4(5.47, 598, 1.67,1.3))

def function5(lam,bigD,litd):
    deltay = lam*bigD/litd
    print (deltay)
print(function5(687*10**-9, 4.8,1.75*10**-3))

def function6(lam,litd):
    rad = lam/litd
    print("rad =", math.asin(rad),"\tdegree", math.asin(rad)*180/math.pi)
print(function6(451*10**-9, 5.48*10**-6))

def function7(lam,N,n):
    deltay = lam*N/(2*(n-1))
    print (deltay*10**9)
print(function7(697*10**-9, 6,1.33))

# def functio11(lam,N,n):
#     deltay = lam*N/(2*(n-1))
#     print (deltay*10**9)
# print(function7())
print(function6(540*10**-9, .4*10**-3))

def function11(lam,d,D):
    thetaR = 1.22*lam/d
    print (thetaR)
    L = D/thetaR
    print(L)
print(function11(505*10**-9, 5*10**-3,1.4))

def function11(lam,d,ruling):
    d /= ruling
    d*= 10**6
    #print("d=",d)
    comp1 = 4*lam/d
    print(comp1)
    largest = math.asin(comp1)* 180/math.pi
    print("largest", largest)
    sec_largest = math.asin((3*lam)/d)* 180/math.pi
    print("second largest", sec_largest)
    third_large = math.asin((2*lam)/d)* 180/math.pi
    print("third largest", third_large)
print(function11(0.844, (29.9*10**-3), 8500))