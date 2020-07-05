import os

print("You have to remove some lines from netlist file that lines are remove analysis(.dc or .tran), supply voltage line and .control, run, end, endc statemant,and most important all input and clock pulses\n\n")
s= (input("enter file name with .cir or .txt"))
V_value = float(input("enter value of Supply Voltage in V"))
vd = (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages\n"))
#Vsup = (input("enter name of supply voltage source\n\n"))
shakes = open(s, "a")
shakes.write("VSUP netnet 0 DC {}\n" .format(V_value))
shakes.write("Vtstp netnet {} DC 0" .format(vd))
#Vtstp = (input("enter name of voltage source having 0V that you placed between Supply Voltage and pmos\n\n"))
#k= (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages)\n"))

shakes.write("\n.op\n.control\nrun\nprint I(Vtstp)*V({})\n.endc\n.end".format(vd))
shakes.close()
os.system('ngspice '+s)


