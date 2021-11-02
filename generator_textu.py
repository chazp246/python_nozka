from random import randint, choice

f = open("vety.txt","w")
samohlasky = "aeiyou"
souhlasky = "qwrtpsdfghjklzxcvbnm"

def slovo(maxchars = 7):
    slovo = ""
    for i in range(randint(1, maxchars)):
        if i % 2 == randint(0, 1):
            slovo = slovo + choice(souhlasky)
        else:    
            slovo = slovo + choice(samohlasky)
    return slovo 

def veta(minslovo = 3, maxslovo = 12):
    veta = ""
    for i in range(randint(minslovo, maxslovo)):
        veta = veta + slovo() + " "
    veta = (veta[:-1] + ".").capitalize()
    return veta

print(veta())
f.close()

#ahoj