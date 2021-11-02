print("programování alias diskuse na všechny témata teda kromě programování")
"""
#meine program
def pocitadlo(pismeno):
    text = input("Zadej text.: ")
    count = 0
    for i in text:
        if i == pismeno:
            count = count + 1 

    return count 



start = 1
while True:
    
    if start == 1 or input("chceš znovu? ") == "a":
        start = 0
        pismeno = input("zadej co chceš zpočítat.: ")
        print(pocitadlo(pismeno))
    else:
        break

#vestaveny count

text = input("Zadej string.: ")
pismeno = input("Co chceš spočítat?: ")
print(text.count(pismeno))
"""

soubor = input("Zadej jmeno souboru: ")
try:
    f = open(soubor, "r")
except FileNotFoundError:
    print("Tento soubor nelze otevřít!")
    exit(1)
#text = f.read()
#f.close()
#text = input("zadej text.: ")
pocet = {}

while True:
    pismeno = f.read(1).lower()
    if pismeno == "":
        break

#for pismeno in text:
    if pismeno.isalpha():
        try:
            pocet[pismeno] += 1
        except:
            pocet[pismeno] = 1

#print(pocet)

for key in sorted(pocet.keys()):
    mapovany = 50 * pocet[key] / max(pocet.values()) #maximum * tvoje hodnota co chceš namapovat / maximum co dosahl tvoje hodnoty
    bar = int(mapovany) * "#" 
    print(f"{key} -----> {pocet[key]:7} | {bar}")

f.close()
