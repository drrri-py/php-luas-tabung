import tkinter as tk

def hitung_prisma_segitiga():
    try:
        alas = float(alas_entry.get())
        tinggi_alas = float(tinggi_alas_entry.get())
        tinggi_prisma = float(tinggi_prisma_entry.get())
        luas_alas = round(0.5 * alas * tinggi_alas, 2)
        volume = round(luas_alas * tinggi_prisma, 2)
        luas_label.config(text=f'Luas Alas: {luas_alas}')
        volume_label.config(text=f'Volume Prisma Segitiga: {volume}')
    except ValueError:
        luas_label.config(text='Masukkan angka valid')
        volume_label.config(text='')

root = tk.Tk()
root.title("Kalkulator Prisma Segitiga")

# Membuat label dan entry untuk input alas, tinggi alas, dan tinggi prisma segitiga
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

alas_label = tk.Label(input_frame, text="Alas Segitiga:")
alas_label.pack(side='left', padx=5)
alas_entry = tk.Entry(input_frame)
alas_entry.pack(side='left', padx=5)

tinggi_alas_label = tk.Label(input_frame, text="Tinggi Alas Segitiga:")
tinggi_alas_label.pack(side='left', padx=5)
tinggi_alas_entry = tk.Entry(input_frame)
tinggi_alas_entry.pack(side='left', padx=5)

tinggi_prisma_label = tk.Label(input_frame, text="Tinggi Prisma:")
tinggi_prisma_label.pack(side='left', padx=5)
tinggi_prisma_entry = tk.Entry(input_frame)
tinggi_prisma_entry.pack(side='left', padx=5)

# Membuat tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_prisma_segitiga)
hitung_button.pack(pady=5)

# Membuat label untuk menampilkan hasil perhitungan
hasil_frame = tk.Frame(root)
hasil_frame.pack(pady=10)

luas_label = tk.Label(hasil_frame, text="Luas Alas:")
luas_label.pack(side='left', padx=5)
volume_label = tk.Label(hasil_frame, text="Volume Prisma Segitiga:")
volume_label.pack(side='left', padx=5)

# Memulai loop Tkinter
root.mainloop()
