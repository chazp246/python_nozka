import os
import tkinter as tk
from tkinter import filedialog
from os.path import basename, splitext, getsize
import json

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "FINDER 3000"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)

        self.var_adresar = tk.StringVar()
        self.var_adresar.set(r"C:\Users\admin\OneDrive\Dokumenty\projekty\python_nozka\soutez\data")

        self.lbl_external_folder = tk.Label(self, text = "Adresář:  ")
        self.lbl_external_folder.grid(row = 1, column = 1, sticky = "w")
        self.entry_external_folder = tk.Entry(self, textvariable = self.var_adresar, width = 50)
        self.entry_external_folder.grid(row = 1, column = 2)
        self.btn_external_folder = tk.Button(self, text = "...", command = self.ask_dir)
        self.btn_external_folder.grid(row = 1, column = 3)

        self.btn_hledej = tk.Button(self, text = "Hledej", command = self.hledej, width = 10, border = 3, background = "#75d060")
        self.btn_hledej.grid(row = 1, column = 4)
            
        self.btn_quit = tk.Button(self, text = "Konec", command = self.quit)
        self.btn_quit.grid(row = 8, column = 2)

    
    def ask_dir(self):
        adress = filedialog.askdirectory()
        self.var_adresar.set(adress)


    def tree(self, fullPath = "Default"):
        if fullPath != "Default":
            adresar = fullPath
        else:
            adresar = self.var_adresar.get()
        listOfFile = os.listdir(adresar)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(adresar, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + self.tree(fullPath)
            else:
                allFiles.append(fullPath)
        return allFiles

    def hledej(self):
        all = self.tree()
        data = {}
        for item in all:
            data[item] = {"lines" : self.delka(item), 
                          "size" : self.velikost(item)}
        print(self.porovnej(data, "lines"))
        print("__________")
        print(self.porovnej(data, "size"))
        self.output(data)

    def delka(self, soubor = None):
        radky = 0
        with open(soubor, "r") as f:
            while True:
                radek = f.readline()
                radky = radky + 1
                if radek == "":
                    break
        return radky

    def velikost(self, soubor = None):
        return getsize(soubor)

    def porovnej(self, data, neco):
        help = []
        for item in data:
            help.append("---")
            help.append(item)
            for item2 in data:
                if data[item][f"{neco}"] == data[item2][f"{neco}"]:
                    if item != item2:
                        if item2 not in help:
                            help.append(item2)
        return help

        


    def output(self, data):
        os.remove(f"output.json")
        with open(f"output.json", "w") as file:
            json.dump(data, file, indent = 4)
       



    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()