""" tady to je pomocí listu
#1
print("1.uloha")
potrech = 1
i = 0
rada = []
while i < 100:
    i = i + 1
    rada.append(potrech)
    potrech = potrech + 3
rada = tuple(rada)
print(rada)
"""

#1
print("1.uloha")
potrech = 1
i = 0
rada = (potrech, )
while i < 100:
    i = i + 1
    rada = rada + (potrech, )
    potrech = potrech + 3
print(rada)



#2
print("2.uloha")
rada2 = 1
i = 0
mocniny=[] 

while i < 100:
    i = i + 1
    mocniny.append(rada2)
    rada2 = rada2 * 2
print(mocniny)

#3
print("3.uloha")
rada = list(rada) 
vysledek = []
vysledek = set(rada) & set(mocniny)
vysledek = list(vysledek)
print(vysledek)

#4
print("4.uloha")
vyseledekbez = []
vysledekbez = vysledek [1:-1]
print(vysledekbez)

#5
print("5.uloha")
notvysledek = vysledek
notvysledek.reverse()
print(notvysledek)