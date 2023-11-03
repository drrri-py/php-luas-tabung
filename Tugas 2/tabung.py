import tkinter as tk
from math import pi

def hitung_tabung():
    try:
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_permukaan = round(2 * pi * jari_jari * (jari_jari + tinggi), 2)
        volume = round(pi * jari_jari**2 * tinggi, 2)
        luas_permukaan_label.config(text=f'Luas Permukaan Tabung: {luas_permukaan}')
        volume_label.config(text=f'Volume Tabung: {volume}')
    except ValueError:
        luas_permukaan_label.config(text='Masukkan angka valid')
        volume_label.config(text='')

root = tk.Tk()
root.title("Kalkulator Tabung")

# Membuat label dan entry untuk input jari-jari dan tinggi tabung
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

jari_jari_label = tk.Label(input_frame, text="Jari-Jari Tabung:")
jari_jari_label.pack(side='left', padx=5)
jari_jari_entry = tk.Entry(input_frame)
jari_jari_entry.pack(side='left', padx=5)

tinggi_label = tk.Label(input_frame, text="Tinggi Tabung:")
tinggi_label.pack(side='left', padx=5)
tinggi_entry = tk.Entry(input_frame)
tinggi_entry.pack(side='left', padx=5)

# Membuat tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_tabung)
hitung_button.pack(pady=5)

# Membuat label untuk menampilkan hasil perhitungan
hasil_frame = tk.Frame(root)
hasil_frame.pack(pady=10)

luas_permukaan_label = tk.Label(hasil_frame, text="Luas Permukaan Tabung:")
luas_permukaan_label.pack(side='left', padx=5)
volume_label = tk.Label(hasil_frame, text="Volume Tabung:")
volume_label.pack(side='left', padx=5)

# Memulai loop Tkinter
root.mainloop()
