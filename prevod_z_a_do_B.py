try:
    f = open(input("Zadej cestu k souboru: "), "r")
except FileNotFoundError as e:
    print(f"Soubor se nepovedlo otevřít. {e.filename}")
    exit(1)
fB = open("textB.txt","a")

while True:
    pismeno = f.read(1).upper()
    if pismeno == "A":
        pismeno = "@"
    if pismeno == "":
        break
    fB.write(pismeno)
    

f.close()
fB.close()
#testa