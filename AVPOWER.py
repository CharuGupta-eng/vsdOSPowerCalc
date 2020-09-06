import os
import re
import math
import pandas as pd
import getopt
import sys

argv = sys.argv[1:]


opts, args = getopt.getopt(argv, "i:t:v:", ["inputfile=", "timeperiod=", "supplyvoltage"])
print(opts, args)
for opt, arg in opts:
    if opt == '-i' or opt == '--inputfile':
                s = arg
    elif opt == '-t' or opt == '--timeperiod':
                T = float(arg)
    elif opt == '-v' or opt == '--supplyvoltage':
                vs = arg


#s= input("Please enter file name with .cir or .txt (e.g. DFF_TG.cir): ")
C = 10
R = 100
#T = float(input("Enter the time period in seconds of clock in synchronous circuit or in asynchronous circuit take time period of input having minimum time period (e.g. 0.000004): "))
J = T*5
if R*C< T:
    print("MULTIPLICATION OF RESISTOR AND CAPACITOR of my power measure circuit is smaller THAN YOUR ENTERED TIME PERIOD")
    print("Now you have to choose value of capacitor and resistor acccordingly that product of r and c must be greater than your time perid")
    C = float(input("enter value of capacitor in nF:" ))
    R = float(input("enter value of resistor in Kohm: "))
#V_value = float(input("enter value of Supply Voltage in V (e.g. 1.8): "))
#vd = (input("Enter name of node of supply voltage source which you have given and used in place of all supply voltages (e.g. VDD): "))
#vs = (input("Enter the name of the voltage supply (e.g. V_V20): "))

#Vsup = (input("enter name of supply voltage source\n\n"))

myinp=open(s,"r")
shakes = open("poweranalysis.cir", "w")
done=False
firstv=True

for line in myinp.readlines():
    if re.match(r'^\.tran',line):
        line=line.rstrip()+" UIC\n"
    if re.match(r'\.control',line):
        done=True
    if firstv and re.match(r'^'+vs+'\s',line):
        if re.match(r'^'+vs+'\s+\w+\s+\d\s+\d\.?\d\w+$',line):
              vdD= re.search(r'^'+vs+'\s+(\w+)\s+\d\s+\d\.?\d\w+$',line).group(1)
              V_valueD= re.search(r'^'+vs+'\s+\w+\s+\d\s+(\d\.?\d)\w+$',line).group(1)
        elif re.match(r'^'+vs+'\s+\w+\s+\w+\s+\d\.?\d$',line):
             vdD= re.search(r'^'+vs+'\s+(\w+)\s+\w+\s+\d\.?\d$',line).group(1)
             V_valueD= re.search(r'^'+vs+'\s+\w+\s+\w+\s+(\d\.?\d)$',line).group(1)
        elif re.match(r'^'+vs+'\s+\w+\s+\w+\s+\w+\s+\d\.?\d$', line):
            vdD = re.search(r'^'+vs+'\s+(\w+)\s+\w+\s+\w+\s+\d\.?\d$', line).group(1)
            V_valueD = re.search(r'^'+vs+'\s+\w+\s+\w+\s+\w+\s+(\d\.?\d)$', line).group(1)
        elif re.match(r'^'+vs+'\s+\w+\s+\d\s+\d\w+$',line):
              vdD= re.search(r'^'+vs+'\s+(\w+)\s+\d\s+\d\w+$',line).group(1)
              V_valueD= re.search(r'^'+vs+'\s+\w+\s+\d\s+(\d)\w+$',line).group(1)
        elif re.match(r'^'+vs+'\s+\w+\s+\w+\s+\d$',line):
            vdD= re.search(r'^'+vs+'\s+(\w+)\s+\w+\s+\d$',line).group(1)
            V_valueD= re.search(r'^'+vs+'\s+\w+\s+\w+\s+(\d)$',line).group(1)
        elif re.match(r'^'+vs+'\s+\w+\s+\w+\s+\w+\s+\d$', line):
            vdD = re.search(r'^'+vs+'\s+(\w+)\s+\w+\s+\w+\s+\d$', line).group(1)
            V_valueD = re.search(r'^'+vs+'\s+\w+\s+\w+\s+\w+\s+(\d)$', line).group(1)
        vd= vdD
        V_value = float(V_valueD)
       # print(vd)
       # print(V_value)

        #if re.match(r'(\d+\.?\d*)V?d?s?\s*$',line):
           #V_value=re.match(r'(\d+\.?\d*)V?d?s?\s*$').group(1)
          # print(V_value)
        line=''
        firstv=False
    if not done and not re.match(r'^((.endc )| (.end  ))',line) :
        shakes.write(line)

myinp.close()
BETA = (V_value*C)/(T*(10**9))
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
#print(file)
FILE1 = file[file["TIME"]<=T ]
#print(FILE1)
FILE2 = file[file["TIME"]==0]
m = FILE1["POWER"].max()
n = FILE2["POWER"].max()
if math.isnan(n):
       n=0
avg = m-n
AV = avg*1000000
#print("m: {} n: {}".format(m,n))
print("AVERAGE POWER IS {} W   OR   {}uW".format(avg,AV))
