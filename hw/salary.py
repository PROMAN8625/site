# those extra commented numbers are to test this program

nm=input("Enter The Employee Name : ")

bs=float(input("Input The Basic Salary : "))

da=bs*20/100  #0.2

hr=bs*15/100  #0.15

pf=bs*9.20/100 #0.092

np=bs+hr  #100.15

gp=np-pf  #100.058

print("The Gross Pay Of ",nm," Is ",gp)

quit=input("\nPress Enter To Quit")
