import tkinter as tk
from os.path import basename, splitext
import os
from tkinter import ANCHOR, Frame, Listbox, END, Radiobutton
from turtle import color

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárnička"
    
    def __init__(self):
        self.load_smenovnik()
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        #radiobutton,ukazovat kurz  
        self.varEntry = tk.IntVar()
        self.var_vysledek = tk.Variable()
        self.var_nakup = tk.Variable()
        self.var_prodej = tk.Variable()
        self.var_nasobnost = tk.Variable()
        self.var_akce = tk.StringVar()
        self.var_akce.set("prodej")


        vcmd = (self.register(self.callback))
        self.entry = tk.Entry(self, validate="all", validatecommand=(vcmd, '%P'), width = 3, textvariable = self.varEntry)
        self.entry.grid(row = 1, column = 1)

        self.btn_preved = tk.Button(self, text = "Akce", command = self.preved, width = 10, border = 3, background = "#75d060")
        self.btn_preved.grid(row = 2, column = 1)
        
        self.lbl_vys = tk.Label(self, text = "Výsledek: ")
        self.lbl_vys.grid(row = 8, column = 1, sticky = "w")
        self.lbl_vysledek = tk.Label(self, textvariable = self.var_vysledek)
        self.lbl_vysledek.grid(row = 8, column = 2)

        self.lbl_na = tk.Label(self, text = "Nákupní cena: ")
        self.lbl_na.grid(row = 5, column = 1, sticky = "w")
        self.lbl_nakup = tk.Label(self, textvariable = self.var_nakup)
        self.lbl_nakup.grid(row = 5, column = 2)

        self.lbl_pro = tk.Label(self, text = "Prodejní cena: ")
        self.lbl_pro.grid(row = 6, column = 1, sticky = "w") 
        self.lbl_prodej = tk.Label(self, textvariable = self.var_prodej)
        self.lbl_prodej.grid(row = 6, column = 2)

        self.lbl_nas = tk.Label(self, text = "Násobnost: ")
        self.lbl_nas.grid(row = 7, column = 1, sticky = "w")
        self.lbl_nasobnost = tk.Label(self, textvariable = self.var_nasobnost)
        self.lbl_nasobnost.grid(row = 7, column = 2)

        self.btn_quit = tk.Button(self, text = "Quit", command = self.quit)
        self.btn_quit.grid(row = 3, column = 1)

        self.listbox = Listbox(self, width = 50, height= 30)
        self.listbox.grid(row = 4, column = 1, pady = 10)
        self.listbox.bind("<ButtonRelease-1>", self.klik)
        
        akce = [("Prodej", "prodej"), ("Nákup", "nakup")] 
        self.frame = Frame(self)
        self.frame.grid(row = 1, column = 2)
        for text, akce in akce: 
            b = Radiobutton(self.frame, text = text, variable = self.var_akce, value = akce)
            b.pack()

        for i in range(0, len(self.listek)):
            self.listbox.insert(END, self.listek[i][0])

    def klik(self, event):
        index = self.listbox.curselection()[0]
        self.var_nakup.set(self.listek[index][3])
        self.var_prodej.set(self.listek[index][2])
        self.var_nasobnost.set(self.listek[index][1])


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False
    

    def preved(self):
        for i in range(0, len(self.listek)):
            if self.listek[i][0] == self.listbox.get(ANCHOR):
                pozice = i
        self.nasobky = self.listek[pozice][1]
        self.mnozstvi = self.varEntry.get()
        akce = self.var_akce.get()
        if akce == "prodej":#prodej
            self.hodnota = self.listek[pozice][2]
        else:#nakup
            self.hodnota = self.listek[pozice][3]
        self.vysledek = self.mnozstvi // float(self.nasobky) * float(self.hodnota)
        self.var_vysledek.set(self.vysledek)


    def load_smenovnik(self):
        if os.path.exists(f"listek.txt"):
            with open(f"listek.txt", "r") as file:
                listek_raw = file.readlines()
                self.listek = []
                for i in range(0, len(listek_raw)):
                    self.listek.append(listek_raw[i].split())
  

    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()