import pandas as pd
print("To get value average value")
print("Write one more line print V(POWR)")
print("cpoy the output you get in table format and make .csv file in excel")
print("name each coloumn as INDEX, TIME and POWER")
s = input("Enter the file name with extension .csv")

file = pd.read_csv(s)
t = float(input("Enter the time period in seconds"))
FILE1 = file[file["TIME"]==t]
# print(FILE1)
avg = FILE1["POWER"].mean()
print("AVERAGE POWER IS {}".format(avg))