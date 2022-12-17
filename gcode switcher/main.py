def menic(soubor, puvodni, novy, puvodni2, novy2):
    soubor2 = soubor.split(".")[0]
    fB = open(f"{soubor2}_meneno.ngc", "w")
    
    with open(soubor, "r") as f:
        for radek in f:
            radek = radek.strip()
            if radek == puvodni:
                radek = novy
                print(radek)
            elif radek == puvodni2:
                radek = novy2
            elif radek == "G00 X0.0000 Y0.0000":
                radek = "M3 S90\nG00 X0.0000 Y0.0000"
            elif radek == "":
                radek = ""
            fB.write(radek + "\n")
        
    fB.close()



menic("text.ngc", "G00 Z5.000000", "M3 S90", "G01 Z-1.000000 F100.0(Penetrate)", "M5")