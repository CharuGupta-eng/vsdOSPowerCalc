print("convert your netlist file to .txt format from .cir file and remove analysis and .control, run, end, endc statemant\n")
s= (input("enter file name with .txt"))
C = 10
R = 100
T = float(input("Enter the time period in seconds of clock in synchronous circuit or in asynchronous circuit take time period of input having minimum time period"))
J = T*5
if R*C< T:
    print("MULTIPLICATION OF RESISTOR AND CAPACITOR of my power measure circuit is smaller THAN YOUR ENTERED TIME PERIOD")
    print("Now you have to choose value of capacitor and resistor acccordingly that product of r and c must be greater than your time perid")
    C = float(input("enter value of capacitor in nF"))
    R = float(input("enter value of resistor in Kohm"))
VDD = float(input("enter value of Supply Voltage in V"))
BETA = (VDD*C)/(T*(10**9))
Vtstp = (input("enter name of voltage source having 0V that you placed between Supply Voltage and pmos\n\n\n\n\n"))
shakes = open(s, "a")
shakes.write ("\nfp 0 POWR {} {}\n" .format(Vtstp, BETA))
shakes.write("C1 POWR 0 {}n\n".format(C))
shakes.write ("R1 POWR 0 {}K\n".format(R))
shakes.write(".tran 1e-0 {} UIC\n.control\nrun\nPLOT V(POWR)\nPRINT V(POWR)\n.endc\n.end".format(J))
print("I made required changes in your file save it again as .cir file and run in ngsice\n\n\n")

print("You got power curve and values, to find one value run avg.py")