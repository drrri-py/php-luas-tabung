import math
import os
"""
Nama    : Fidriyani
Nim     : 220511064
"""
def hitung_kubus():
    print("Menghitung kubus!")
    sisi = float(input("Masukkan sisi: "))
    luas = 6 * sisi * sisi
    volume = sisi ** 3
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_balok():
    print("Menghitung balok!")
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    tinggi = float(input("Masukkan tinggi: "))
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    volume = panjang * lebar * tinggi
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_limas_segiempat():
    print("Menghitung limas segiempat!")
    sisi_alas = float(input("Masukkan panjang sisi alas: "))
    tinggi = float(input("Masukkan tinggi limas: "))
    luas = (sisi_alas ** 2) + 4 * ((sisi_alas * tinggi) / 2)
    volume = (sisi_alas ** 2 * tinggi) / 3
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_prisma_segitiga():
    print("Menghitung prisma segitiga!")
    alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    tinggi_prisma = float(input("Masukkan tinggi prisma: "))
    luas = 2 * (0.5 * alas_segitiga * tinggi_segitiga) + 2 * (alas_segitiga * tinggi_prisma)
    volume = (0.5 * alas_segitiga * tinggi_segitiga) * tinggi_prisma
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_limas_segitiga():
    print("Menghitung limas segitiga!")
    alas_segitiga = float(input("Masukkan panjang alas segitiga: "))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    luas = (alas_segitiga * tinggi_segitiga) / 2
    tinggi_limas = float(input("Masukkan tinggi limas: "))
    volume = (alas_segitiga * tinggi_segitiga * tinggi_limas) / 6
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_tabung():
    print("Menghitung tabung!")
    jari_jari = float(input("Masukkan jari-jari tabung: "))
    tinggi = float(input("Masukkan tinggi tabung: "))
    luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    volume = math.pi * jari_jari ** 2 * tinggi
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_kerucut():
    print("Menghitung kerucut!")
    jari_jari = float(input("Masukkan jari-jari kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))
    s = math.sqrt(jari_jari ** 2 + tinggi ** 2)
    luas = math.pi * jari_jari * (jari_jari + s)
    volume = (1/3) * math.pi * jari_jari ** 2 * tinggi
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

def hitung_bola():
    print("Menghitung bola!")
    jari_jari = float(input("Masukkan jari-jari bola: "))
    luas = 4 * math.pi * jari_jari ** 2
    volume = (4/3) * math.pi * jari_jari ** 3
    print("Volume: ", volume)
    print("Luas: ", luas, "\n")

while True:
    userInput = int(input(
        "Pilih rumus yang akan digunakan:\n"
        "1. Kubus\n"
        "2. Balok\n"
        "3. Limas segiempat\n"
        "4. Prisma segitiga\n"
        "5. Limas segitiga\n"
        "6. Tabung\n"
        "7. Kerucut\n"
        "8. Bola\n"
        "9. Keluar\n\n"
        "Silakan pilih nomor berapa: "
    ))
    os.system('clear')
    if userInput == 1:
        hitung_kubus()
    elif userInput == 2:
        hitung_balok()
    elif userInput == 3:
        hitung_limas_segiempat()
    elif userInput == 4:
        hitung_prisma_segitiga()
    elif userInput == 5:
        hitung_limas_segitiga()
    elif userInput == 6:
        hitung_tabung()
    elif userInput == 7:
        hitung_kerucut()
    elif userInput == 8:
        hitung_bola()
    elif userInput == 9:
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang valid.")
