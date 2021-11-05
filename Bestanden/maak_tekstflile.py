import io
import os
bestand = open("klasgenoten1.txt", "r")
regel1 = bestand.readline()
regel1 = regel1.strip()
print(regel1)

regel2 = bestand.readline()
regel2 = regel2.strip()
print(regel2)

regel3 = bestand.readline()
regel3 = regel3.strip()
print(regel3)

os.mkdir(str(regel1))
os.mkdir(str(regel2))
os.mkdir(str(regel3))

import os
bestandsnaam = "demobestand.txt"
huidige_map = os.getcwd()
volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("Dit bestand gaan we hernoemen: " + volledige_pad)




