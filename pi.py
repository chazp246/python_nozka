jmenovatel = 1
pi = 0 
znamenko = + 1

while True:
    zlomek = 1 / jmenovatel
    pi = pi + znamenko * zlomek
    if zlomek < 1e-6:
        break
    jmenovatel = jmenovatel + 2
    znamenko = znamenko * -1

pi = 4 * pi
print(pi)