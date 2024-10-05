import math

# 1. Balok
def balok(p, l, t):
    volume = p * l * t
    luas_permukaan = 2 * (p * l + p * t + l * t)
    return volume, luas_permukaan

# 2. Tabung
def tabung(r, t):
    volume = math.pi * (r ** 2) * t
    luas_permukaan = 2 * math.pi * r * (r + t)
    return volume, luas_permukaan

# 3. Kerucut
def kerucut(r, t):
    volume = (1/3) * math.pi * (r ** 2) * t
    luas_permukaan = math.pi * r * (r + math.sqrt(t ** 2 + r ** 2))
    return volume, luas_permukaan

def main():
    while True:
        print("\nPilih bangun ruang yang ingin dihitung:")
        print("1. Balok")
        print("2. Tabung")
        print("3. Kerucut")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == '1':
            panjang = float(input("Masukkan panjang balok: "))
            lebar = float(input("Masukkan lebar balok: "))
            tinggi = float(input("Masukkan tinggi balok: "))
            vol_balok, luas_balok = balok(panjang, lebar, tinggi)
            print(f"Volume Balok: {vol_balok}")
            print(f"Luas Permukaan Balok: {luas_balok}")

        elif pilihan == '2':
            jari_jari = float(input("Masukkan jari-jari alas tabung: "))
            tinggi = float(input("Masukkan tinggi tabung: "))
            vol_tabung, luas_tabung = tabung(jari_jari, tinggi)
            print(f"Volume Tabung: {vol_tabung}")
            print(f"Luas Permukaan Tabung: {luas_tabung}")

        elif pilihan == '3':
            jari_jari = float(input("Masukkan jari-jari alas kerucut: "))
            tinggi = float(input("Masukkan tinggi kerucut: "))
            vol_kerucut, luas_kerucut = kerucut(jari_jari, tinggi)
            print(f"Volume Kerucut: {vol_kerucut}")
            print(f"Luas Permukaan Kerucut: {luas_kerucut}")

        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
