import time
import os 
 

thislist = ["Auto", "Trein", "Bus", "Fiets", "Benenwagen"]
print(thislist)
time.sleep(4)
thislist.reverse()
print(thislist)

time.sleep(4)
thatlist = ["Kaas", "Vis", "Komkommer", "Worst", "Brood"]
print(thatlist)
time.sleep(4)
thatlist.append("Sinasappel")
print(thatlist)

time.sleep(4)
dolist = ["Telefoon", "Tablet", "Ov-Kaart", "Laptop", "Computer"]
print(dolist)
time.sleep(4)
dolist.clear()
time.sleep(4)
os.system("cls")