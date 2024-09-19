import tkinter as tk
from tkinter import messagebox

def szamolj_netto():
    try:
        brutto_jovedelem = float(brutto_entry.get())
        eletkor = int(eletkor_entry.get())

        # Költségek százalékai
        nyugdij_jarulek = 0.10
        tb_jarulek = 0.07
        munkavallaloi_jarulek = 0.015
        szja = 0.15 if eletkor >= 25 else 0.0

        # Költségek számítása
        nyugdij_koltseg = brutto_jovedelem * nyugdij_jarulek
        tb_koltseg = brutto_jovedelem * tb_jarulek
        munkavallaloi_koltseg = brutto_jovedelem * munkavallaloi_jarulek
        szja_koltseg = brutto_jovedelem * szja

        # Nettó jövedelem kiszámítása
        netto_jovedelem = brutto_jovedelem - (nyugdij_koltseg + tb_koltseg + munkavallaloi_koltseg + szja_koltseg)

        # Eredmények megjelenítése
        result_label.config(text=f"Nettó jövedelem: {netto_jovedelem:.2f} Ft")
        levonasok_label.config(text=f"Levont összegek:\n"
                                    f"Nyugdíjjárulék (10%): {nyugdij_koltseg:.2f} Ft\n"
                                    f"TB járulék (7%): {tb_koltseg:.2f} Ft\n"
                                    f"Munkavállalói járulék (1.5%): {munkavallaloi_koltseg:.2f} Ft\n"
                                    f"Szja (15%): {szja_koltseg:.2f} Ft")
    except ValueError:
        messagebox.showerror("Hiba", "Kérlek, érvényes számot adj meg!")

# GUI ablak létrehozása
window = tk.Tk()
window.title("Nettó jövedelem kalkulátor")

# Bruttó jövedelem címke és beviteli mező
brutto_label = tk.Label(window, text="Bruttó jövedelem (Ft):")
brutto_label.grid(row=0, column=0, padx=10, pady=10)
brutto_entry = tk.Entry(window)
brutto_entry.grid(row=0, column=1, padx=10, pady=10)

# Életkor címke és beviteli mező
eletkor_label = tk.Label(window, text="Életkor:")
eletkor_label.grid(row=1, column=0, padx=10, pady=10)
eletkor_entry = tk.Entry(window)
eletkor_entry.grid(row=1, column=1, padx=10, pady=10)

# Számítás gomb
szamitas_button = tk.Button(window, text="Számolj", command=szamolj_netto)
szamitas_button.grid(row=2, column=0, columnspan=2, pady=10)

# Eredmény címke
result_label = tk.Label(window, text="Nettó jövedelem:")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Levonások részletezése
levonasok_label = tk.Label(window, text="Levont összegek:")
levonasok_label.grid(row=4, column=0, columnspan=2, pady=10)

# GUI ablak futtatása
window.mainloop()
