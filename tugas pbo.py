import math

# Masukkan jari-jari tabung dan tinggi tabung
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Hitung luas permukaan tabung
luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Tampilkan hasil
print(f"Luas permukaan tabung adalah: {luas_permukaan:.2f}")
