import os
import re
import pandas as pd

print("You have to replace all NON CONSTANT (PULSE) input and clock pulses with 0\n\n")
s= (input("enter file name with .cir or .txt (e.g. TT.cir):"))
V_value = float(input("enter value of Supply Voltage in V (e.g. 1.8): "))
vd = (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages)(e.g. VDD) \n"))
vs = (input("Enter the name of the voltage supply (e.g. V_V20): "))
#Vsup = (input("enter name of supply voltage source\n\n"))

myinp=open(s,"r")
shakes = open("powerLeakage.cir", "w")
done=False
firstv=True
for line in myinp.readlines():
    if re.match(r'^\.tran',line):
        #line=line.rstrip()+" UIC\n"
        line=""
    if re.match(r'\.control',line):
        done=True
    if firstv and re.match(r'^'+vs+'\s',line):
        #if re.match(r'(\d+\.?\d*)V?d?s?\s*$',line):
        #    V_value=re.match(r'(\d+\.?\d*)V?d?s?\s*$').group(1)
        line=''
        firstv=False
    if not done and not re.match(r'^((.endc )| (.end  ))', line):
        shakes.write(line)

myinp.close()

shakes.write("VSUP netnet 0 DC {}\n" .format(V_value))
shakes.write("Vtstp netnet {} DC 0" .format(vd))
#Vtstp = (input("enter name of voltage source having 0V that you placed between Supply Voltage and pmos\n\n"))
#k= (input("Enter name of node of supply voltage source (which you have given and used in place of all supply voltages)\n"))

shakes.write("\n.op\n.control\nrun\nprint I(Vtstp)*V({})\n".format(vd))
shakes.write("set filetype=ascii\nset time wr_singlescale\nset pwr wr_I(Vtstp)*V({})\noption numdgt=3\nwrdata APOWER.csv I(Vtstp)*V({})\n".format(vd,vd))
shakes.write("quit\n")
shakes.write("\n.endc\n.end")
shakes.close()
os.system('ngspice powerLeakage.cir')
file = pd.read_csv('APOWER.csv',sep=' ',header=None, names=["0","TIME","1","POWER","2"])
#print(file)

avg = file["POWER"].max()


AV = avg*1000000
#print("m: {} n: {}".format(m,n))
print("LEAKAGE POWER IS {} W   OR   {}uW".format(avg,AV))

