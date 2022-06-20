pc=int(input("\nEnter The Pc Price In INR (enter 0 if none bought) : "))    #getting the price
lp=int(input("\nEnter The Laptop Price In INR(enter 0 if none bought) : "))

ppc=pc-(pc*5/100)#calculating pc price
print("The PC Costs ",ppc,"INR With A Discount Of 5%.")

plp=lp-(lp*10/100)#calculating lappy price
print("The Laptop Costs ",plp,"INR With A Discount Of 10%.")


quit=input("\nPress Enter To Quit")#so lappy price can be printed in cmd mode
