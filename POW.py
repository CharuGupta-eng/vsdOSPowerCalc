import os
print("You have to remove some lines from netlist file that lines are remove analysis (.tran or .dc), supply voltage line and .control, run, end, endc statemant\n")
s= (input("enter file name with .cir or .txt"))
C = 10
R = 100
T = float(input("Enter the time period in seconds of clock in synchronous circuit or in asynchronous circuit take time period of input having minimum time period"))
J = T*5
if R*C< T:
    print("MULTIPLcd cdICATION OF RESISTOR AND CAPACITOR of my power measure circuit is smaller THAN YOUR ENTERED TIME PERIOD")
    print("Now you have to choose value of capacitor and resistor acccordingly that product of r and c must be greater than your time perid")
    C = float(input("enter value of capacitor in nF"))
    R = float(input("enter value of resistor in Kohm"))
V_value = float(input("enter value of Supply Voltage in V"))
vd = (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages\n"))
print("You got power curve and values, COPIES ALL THE OUTPUT VALUES AND MAKE .CSV FILE TO GET ONE VALUE BY runing avg.py")
BETA = (V_value*C)/(T*(10**9))
#Vsup = (input("enter name of supply voltage source\n\n"))
shakes = open(s, "a")
shakes.write("VSUP netnet 0 DC {}\n" .format(V_value))
shakes.write("Vtstp netnet {} DC 0" .format(vd))
shakes.write("\nfp 0 POWR vtstp {}\n" .format(BETA))
shakes.write("Cp POWR 0 {}n\n".format(C))
shakes.write ("Rp POWR 0 {}K\n".format(R))
shakes.write(".tran 1e-0 {} UIC\n.control\nrun\nPLOT V(POWR)\nPRINT V(POWR)\n".format(J))
shakes.write("set filetype=ascii\nset time wr_singlescale\nset pwr wr_V(POWR)\noption numdgt=3\nwrdata AVPOWER.csv V(POWR)")
shakes.write("\n.endc\n.end")
shakes.close()

os.system('ngspice '+s)
print("I made required changes in your file now you can run in ngsice\n\n\n")



