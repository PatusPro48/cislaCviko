import tkinter as tk

cisla = []

okno = tk.Tk()
okno.title("CvičeníGUI čísla")
okno.geometry("400x300")

nadpis = tk.Label(okno, text="cvičení Čísla")
nadpis.pack()

vstup = tk.Entry(okno)
vstup.delete(0, tk.END)
vstup.pack()

def pridat():
    try:
        cislo = int(vstup.get())

    except ValueError:
        print("Nezadal jsi číslo!")
    else:
        cisla.append(cislo)
        text = ", ".join(map(str, cisla))
        pole.config(state="normal")
        pole.delete(0, tk.END)
        pole.insert(0, text)
        pole.config(state="readonly")
        soucet.config(text="Součet čísel: " + str(sum(map(int, cisla))))

tlacitko = tk.Button(okno, text="přidat číslo", command=pridat)
tlacitko.pack()

def reset():
    cisla.clear()
    soucet.config(text="Součet čísel: 0")
    pole.config(state="normal")
    pole.delete(0, tk.END)
    pole.config(state="readonly")

tlacitko_reset = tk.Button(okno, text="reset", command=reset)
tlacitko_reset.pack()

soucet = tk.Label(okno, text="Součet čísel: 0")
soucet.pack()

text = ", ".join(map(str, cisla))

pole = tk.Entry(okno, state="readonly")
pole.pack()

okno.mainloop()