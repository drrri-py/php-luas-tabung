import tkinter as tk
from math import pi

def hitung_bola():
    try:
        jari_jari = float(jari_jari_entry.get())
        luas_permukaan = round(4 * pi * jari_jari**2, 2)
        volume = round((4/3) * pi * jari_jari**3, 2)
        luas_permukaan_label.config(text=f'Luas Permukaan Bola: {luas_permukaan}')
        volume_label.config(text=f'Volume Bola: {volume}')
    except ValueError:
        luas_permukaan_label.config(text='Masukkan angka valid')
        volume_label.config(text='')

root = tk.Tk()
root.title("Kalkulator Bola")

# Membuat label dan entry untuk input jari-jari bola
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

jari_jari_label = tk.Label(input_frame, text="Jari-Jari Bola:")
jari_jari_label.pack(side='left', padx=5)
jari_jari_entry = tk.Entry(input_frame)
jari_jari_entry.pack(side='left', padx=5)

# Membuat tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_bola)
hitung_button.pack(pady=5)

# Membuat label untuk menampilkan hasil perhitungan
hasil_frame = tk.Frame(root)
hasil_frame.pack(pady=10)

luas_permukaan_label = tk.Label(hasil_frame, text="Luas Permukaan Bola:")
luas_permukaan_label.pack(side='left', padx=5)
volume_label = tk.Label(hasil_frame, text="Volume Bola:")
volume_label.pack(side='left', padx=5)

# Memulai loop Tkinter
root.mainloop()
