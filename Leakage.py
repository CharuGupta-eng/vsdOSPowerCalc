print("You have to remove some lines from netlist file that lines are remove analysis(.dc or .tran) and .control, run, end, endc statemant,and most important all input and clock pulses\n\n")
s= (input("enter file name with .cir or .txt"))
Vtstp = (input("enter name of voltage source having 0V that you placed between Supply Voltage and pmos\n\n"))
k= (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages)\n"))
shakes = open(s, "a")

shakes.write("\n.op\n.control\nrun\nprint I({})*V({})\n.endc\n.end".format(Vtstp,k))

# exec --ngspice(s)
print("I made required changes in your file now you can run in ngsice\n\n\n")

print("You got leakage power value")

