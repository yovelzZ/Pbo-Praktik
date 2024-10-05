


def cek_bilangan_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def tampilkan_bilangan_prima(awal, akhir):
    print(f"Bilangan Prima dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if cek_bilangan_prima(num):
            print(num, end=" ")
    print()


def tampilkan_angka_ganjil(awal, akhir):
    print(f"Angka Ganjil dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if num % 2 != 0:
            print(num, end=" ")
    print()


def tampilkan_bilangan_genap(awal, akhir):
    print(f"Bilangan Genap dari {awal} sampai {akhir}:")
    for num in range(awal, akhir + 1):
        if num % 2 == 0:
            print(num, end=" ")
    print()


def main():
    while True:
        print("\nMenu:")
        print("1. Tampilkan Bilangan Prima")
        print("2. Tampilkan Angka Ganjil")
        print("3. Tampilkan Bilangan Genap")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan in ['1', '2', '3']:
            
            awal = int(input("Masukkan bilangan awal: "))
            akhir = int(input("Masukkan bilangan akhir: "))
        
        if pilihan == '1':
            tampilkan_bilangan_prima(awal, akhir)

        elif pilihan == '2':
            tampilkan_angka_ganjil(awal, akhir)

        elif pilihan == '3':
            tampilkan_bilangan_genap(awal, akhir)

        elif pilihan == '4':
            print("Terima kasih")
            break

        else:
            print("Pilihan tidak valid, coba lagi")

if __name__ == "__main__":
    main()
