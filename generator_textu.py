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

def text(minvet = 3, maxvet = 10):
    text = ""
    for i in range(randint(minvet, maxvet)):
        text = text + veta()
        if randint(1, 3) == 2:
            text = text + "\n"
    return text


f.write(text(30, 100))
f.close()

