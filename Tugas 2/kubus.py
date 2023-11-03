import tkinter as tk

def hitung():
    try:
        sisi = float(sisi_entry.get())
        luas = round(sisi * sisi, 2)
        volume = round(sisi ** 3, 2)
        luas_label.config(text=f'Luas Kubus: {luas}')
        volume_label.config(text=f'Volume Kubus: {volume}')
    except ValueError:
        luas_label.config(text='Masukkan angka valid')
        volume_label.config(text='')

root = tk.Tk()
root.title("Kalkulator Kubus")

# Membuat label dan entry untuk input sisi kubus
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

sisi_label = tk.Label(input_frame, text="Panjang Sisi Kubus:")
sisi_label.pack(side='left', padx=5)
sisi_entry = tk.Entry(input_frame)
sisi_entry.pack(side='left', padx=5)

# Membuat tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.pack(pady=5)

# Membuat label untuk menampilkan hasil perhitungan
hasil_frame = tk.Frame(root)
hasil_frame.pack(pady=10)

luas_label = tk.Label(hasil_frame, text="Luas Kubus:")
luas_label.pack(side='left', padx=5)
volume_label = tk.Label(hasil_frame, text="Volume Kubus:")
volume_label.pack(side='left', padx=5)

# Memulai loop Tkinter
root.mainloop()
