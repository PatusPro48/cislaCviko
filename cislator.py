import tkinter as tk

# Slovník pro uložení výsledku:
stav = {
    "seznam": [],
    "soucet": 0,
}

# Přidání čísla do seznamu - reakce na tlačítko:
def pridej_cislo():
    cislo_text = vstup.get().strip()

    # Zkontroluj, že se skutečně jedná o číslo:
    try:
        cislo = int(cislo_text)
    except ValueError:
        chyba.config(text="Zadej celé číslo")
        vstup.select_range(0, tk.END)
        vstup.focus()
        return

    # Zařaď číslo do souboru a aktualizuj součet:
    stav["seznam"].append(str(cislo))
    stav["soucet"] += cislo

    lb_vystup.config(text=str(stav["soucet"]))
    novy_vypis_seznamu = ", ".join(stav["seznam"])

    entry_seznam.config(state="normal")
    entry_seznam.delete(0, tk.END)
    entry_seznam.insert(0, novy_vypis_seznamu)
    entry_seznam.config(state="readonly")

    # Vymaž chybu:
    chyba.config(text="")

    # Aktivuj pole pro zadání nového čísla:
    vstup.select_range(0, tk.END)
    vstup.focus()

# Reakce na tlačítko "Reset"
def resetuj():
    stav["seznam"] = []
    stav["soucet"] = 0
    lb_vystup.config(text="0")
    entry_seznam.config(state="normal")
    entry_seznam.delete(0, tk.END)
    entry_seznam.config(state="readonly")
    vstup.delete(0, tk.END)
    chyba.config(text="")
    vstup.focus()

okno = tk.Tk()
okno.title("Cvičení na GUI")
okno.geometry("300x300")

lb_vstup = tk.Label(okno, text="Nové číslo:")
lb_vstup.pack()
vstup = tk.Entry(okno)
vstup.pack()
vstup.bind("<Return>", lambda event: pridej_cislo())

chyba = tk.Label(okno, text="", fg="red")
chyba.pack()

tlacitko = tk.Button(okno, text="Přidej číslo", command=pridej_cislo)
tlacitko.pack()

tlacitko_reset = tk.Button(okno, text="Reset", command=resetuj)
tlacitko_reset.pack()

lb_vystup_popis = tk.Label(okno, text="Součet čísel:")
lb_vystup_popis.pack()

lb_vystup = tk.Label(okno, text="0")
lb_vystup.pack()

lb_seznam = tk.Label(okno, text="Seznam čísel:")
lb_seznam.pack()
entry_seznam = tk.Entry(okno, state="readonly")
entry_seznam.pack()

vstup.focus()
okno.mainloop()