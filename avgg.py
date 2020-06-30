
print("NOTE: NO NODE HAS NAME AS POWR IN YOUR NETLIST")
C = 10
R = 100
T = float(input("Enter the time period in seconds of clock in synchronous circuit or in asynchronous circuit take time period of input having maximum time period"))
if R*C< T:
    print("MULTIPLICATION OF RESISTOR AND CAPACITOR of my power measure circuit is smaller THAN YOUR ENTERED TIME PERIOD")
    print("Now you have to choose value of capacitor and resistor acccordingly that product of r and c must be greater than your time perid")
    C = float(input("enter value of capacitor in nF"))
    R = float(input("enter value of resistor in Kohm"))
VDD = float(input("enter value of Supply Voltage in V"))
BETA = (VDD*C)/(T*(10**9))
Vtstp = (input("enter name of voltage source having 0V that you placed between Supply Voltage and pmos"))
print("now you have to enter these three lines in your netlist before .control")

print ("fp 0 POWR {} {}" .format(Vtstp, BETA))
print ("C1 POWR 0 {}n ".format(C))
print ("R1 POWR 0 {}K ".format(R))
print("Now during trasition analysis add uic like .tran stating_time ending_time uic")
print("now in run section after .control and run write plot V(POWR) this gives you average power plot")
print("TO get value of average power you directy read from graph or run avg.py file")


k= (input("FOR LEAKAGE POWER PERFORM THREE SIMPLE STEPS and enter node of voltage source having 0V, that you placed between Supply Voltage and pmos, which is towards the side of supply voltage "))
print ("Remove all input and clock pulses")
print("Remove all anaysis lones and write .op before .control")
print("After run write print I({})*V({})".format(Vtstp,k))
print("Run this and YOU GET LEAKAGE Power value")






