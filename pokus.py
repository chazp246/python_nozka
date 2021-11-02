rada = 1
i = 0

list=[]

#rada = int(input("costum: "))

while i < 100:
    i = i + 1
    print(f"jsi na i = {i} a číslo je = {rada}")
    list.append(rada)
    rada = rada * 3

print(list)