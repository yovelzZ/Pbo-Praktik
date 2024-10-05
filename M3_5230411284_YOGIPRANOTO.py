import re

class Menu:
    def __init__(self):
        self.makanan = []
        self.minuman = []
        self.daftar_makanan = {
            "Naci Goyeng": 10000,
            "Cate Ayam": 15000,
            "Rendang": 20000,
            "Bakco": 12000,
            "Mie Ayam": 10000
        }
        self.daftar_minuman = {
            "Es Teh": 3000,
            "Es Jeyuk": 4000,
            "Jus Alpukat": 10000,
            "Soda Gembira": 8000,
            "Ail Mineyal": 5000
        }

    def tampil_makanan(self):
        print("\n--- Daftar Makanan ---")
        for makanan, harga in self.makanan:
            print(f"{makanan} -----------> Rp. {harga}")
        for makanan, harga in self.daftar_makanan.items():
            print(f"{makanan} -----------> Rp. {harga}")

    def tampil_minuman(self):
        print("\n--- Daftar Minuman ---")
        for minuman, harga in self.minuman:
            print(f"{minuman} -----------> Rp. {harga}")
        for minuman, harga in self.daftar_minuman.items():
            print(f"{minuman} -----------> Rp. {harga}")

    def tambah_makanan(self):
        for makanan, harga in self.daftar_makanan.items():
            self.makanan.append((makanan, harga))
            print(f"{makanan} -----------> Rp. {harga}")

    def tambah_minuman(self):
        for minuman, harga in self.daftar_minuman.items():
            self.minuman.append((minuman, harga))
            print(f"{minuman} -----------> Rp. {harga}")

    def tambah_menu_baru(self):
        while True:
            print("\n--- Sub-menu Tambah Menu Baru ---")
            print("1. Tambah Makanan Baru")
            print("2. Tambah Minuman Baru")
            print("3. Kembali ke menu utama")

            pilihan_sub = input("Pilih opsi (1-3): ")

            if pilihan_sub == "1":
                makanan_baru = self.input_nama_manual("masakan")
                harga_makanan = self.input_harga_manual("masakan")
                self.makanan.append((makanan_baru, harga_makanan))
                print(f"{makanan_baru} -----------> Rp. {harga_makanan}")
            elif pilihan_sub == "2":
                minuman_baru = self.input_nama_manual("minuman")
                harga_minuman = self.input_harga_manual("minuman")
                self.minuman.append((minuman_baru, harga_minuman))
                print(f"{minuman_baru} -----------> Rp. {harga_minuman}")
            elif pilihan_sub == "3":
                print("Kembali ke menu utama.")
                break
            else:
                print("Opsi tidak valid, silakan coba lagi.")

    def input_harga_manual(self, jenis):
        while True:
            try:
                harga = int(input(f"Masukkan harga {jenis} baru: "))
                return harga
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

    def input_nama_manual(self, jenis):
        while True:
            nama = input(f"Masukkan nama {jenis} baru: ")
            if re.match("^[A-Za-z\s]+$", nama):
                return nama
            else:
                print("Input tidak valid. Nama hanya boleh menggunakan huruf.")

menu = Menu()

while True:
    print("\n--- Aplikasi Menu Makanan dan Minuman ---")
    print("1. Tampil Makanan ")
    print("2. Tampil Minuman ")
    print("3. Tambah Menu Baru")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1-4): ")

    if pilihan == "1":
        menu.tampil_makanan()
    elif pilihan == "2":
        menu.tampil_minuman()
    elif pilihan == "3":
        menu.tambah_menu_baru()
    elif pilihan == "4":
        print("Keluar dari aplikasi.")
        break
    else:
        print("Opsi tidak valid, silakan coba lagi.")

