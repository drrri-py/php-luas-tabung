import tkinter as tk

def hitung_limas_segiempat():
    try:
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_alas = round(panjang * lebar, 2)
        volume = round((luas_alas * tinggi) / 3, 2)
        luas_label.config(text=f'Luas Alas: {luas_alas}')
        volume_label.config(text=f'Volume Limas: {volume}')
    except ValueError:
        luas_label.config(text='Masukkan angka valid')
        volume_label.config(text='')

root = tk.Tk()
root.title("Kalkulator Limas Segiempat")

# Membuat label dan entry untuk input panjang, lebar, dan tinggi limas segiempat
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

panjang_label = tk.Label(input_frame, text="Panjang Alas:")
panjang_label.pack(side='left', padx=5)
panjang_entry = tk.Entry(input_frame)
panjang_entry.pack(side='left', padx=5)

lebar_label = tk.Label(input_frame, text="Lebar Alas:")
lebar_label.pack(side='left', padx=5)
lebar_entry = tk.Entry(input_frame)
lebar_entry.pack(side='left', padx=5)

tinggi_label = tk.Label(input_frame, text="Tinggi Limas:")
tinggi_label.pack(side='left', padx=5)
tinggi_entry = tk.Entry(input_frame)
tinggi_entry.pack(side='left', padx=5)

# Membuat tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_limas_segiempat)
hitung_button.pack(pady=5)

# Membuat label untuk menampilkan hasil perhitungan
hasil_frame = tk.Frame(root)
hasil_frame.pack(pady=10)

luas_label = tk.Label(hasil_frame, text="Luas Alas:")
luas_label.pack(side='left', padx=5)
volume_label = tk.Label(hasil_frame, text="Volume Limas:")
volume_label.pack(side='left', padx=5)

# Memulai loop Tkinter
root.mainloop()
