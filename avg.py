import pandas as pd

print("copy the output you get in table format and make .csv file in excel\n\n")
print("name each coloumn as INDEX, TIME and POWER\n\n\n\n")
s = input("Enter the file name with extension .csv...")

file = pd.read_csv(s)
#print(file)
t = float(input("\nEnter the time period in seconds..."))
FILE1 = file[file["TIME"]==t]
FILE2 = file[file["TIME"]==0]
m = FILE1["POWER"].max()
n = FILE2["POWER"].max()
avg = m-n
print("AVERAGE POWER IS {}".format(avg))