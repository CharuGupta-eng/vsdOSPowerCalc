import os
import re
import math
import pandas as pd

s= input("Please enter file name with .cir or .txt (e.g. DFF_TG.cir): ")
C = 10
R = 100
T = float(input("Enter the time period in seconds of clock in synchronous circuit or in asynchronous circuit take time period of input having minimum time period (e.g. 0.000004): "))
J = T*5
if R*C< T:
    print("MULTIPLICATION OF RESISTOR AND CAPACITOR of my power measure circuit is smaller THAN YOUR ENTERED TIME PERIOD")
    print("Now you have to choose value of capacitor and resistor acccordingly that product of r and c must be greater than your time perid")
    C = float(input("enter value of capacitor in nF:" ))
    R = float(input("enter value of resistor in Kohm: "))
V_value = float(input("enter value of Supply Voltage in V (e.g. 1.8): "))
vd = (input("Enter name of node of supply voltage source which you have given and used in place of all supply voltages (e.g. VDD): "))
vs = (input("Enter the name of the voltage supply (e.g. V_V20): "))
BETA = (V_value*C)/(T*(10**9))
#Vsup = (input("enter name of supply voltage source\n\n"))

myinp=open(s,"r")
shakes = open("poweranalysis.cir", "w")
done=False

for line in myinp.readlines():
    if re.match(r'^\.tran',line):
        line=line.rstrip()+" UIC\n"
    if re.match(r'\.control',line):
        done=True
    if re.match(r'^'+vs,line):
        #if re.match(r'(\d+\.?\d*)V?d?s?\s*$',line):
        #    V_value=re.match(r'(\d+\.?\d*)V?d?s?\s*$').group(1)
        line=''
    if not done and not re.match(r'^(V_V\d+\s+N51925|\.endc|.end)',line) :
        shakes.write(line)

myinp.close()

shakes.write("VSUP netnet 0 DC {}\n" .format(V_value))
shakes.write("Vtstp netnet {} DC 0" .format(vd))
shakes.write("\nfp 0 POWR vtstp {}\n" .format(BETA))
shakes.write("Cp POWR 0 {}n\n".format(C))
shakes.write ("Rp POWR 0 {}K\n".format(R))
shakes.write(".control\nrun\nPLOT V(POWR)\nPRINT V(POWR)\n")
shakes.write("set filetype=ascii\nset time wr_singlescale\nset pwr wr_V(POWR)\noption numdgt=3\nwrdata AVPOWER.csv V(POWR)\n")
shakes.write("quit\n")
shakes.write("\n.endc\n.end")
shakes.close()

os.system('ngspice poweranalysis.cir')

file = pd.read_csv('AVPOWER.csv',sep=' ',header=None, names=["0","TIME","1","POWER","2"])
print(file)
FILE1 = file[file["TIME"]==T]
FILE2 = file[file["TIME"]==0]
m = FILE1["POWER"].max()
n = FILE2["POWER"].max()
if math.isnan(n):
       n=0
avg = m-n
print("m: {} n: {}".format(m,n))
print("AVERAGE POWER IS {}".format(avg))
