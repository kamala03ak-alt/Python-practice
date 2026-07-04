import csv
f=open("Aemoury setting","r")
data=csv.reader(f)
f1=open("Aemoury setting1.csv","w")
w=csv.writer(f1)
w.writerows(f1)