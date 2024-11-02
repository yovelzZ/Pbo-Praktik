class Pegawai:
    def __init__(self, nik, nama, alamat):
        self.nik = nik
        self.nama = nama
        self.alamat = alamat

class Transaksi:
    def __init__(self, no_transaksi, detail_transaksi):
        self.no_transaksi = no_transaksi
        self.detail_transaksi = detail_transaksi

class Produk:
    def __init__(self, kode_produk, nama_produk, harga):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.harga = harga

    def info_produk(self):
        return f"{self.kode_produk:<10} | {self.nama_produk:<20} | {self.harga:>8} IDR"

class Snack(Produk):
    def __init__(self, kode_produk, nama_snack, harga):
        super().__init__(kode_produk, nama_snack, harga)
    
    def info_produk(self):  
        return f"{self.kode_produk:<10} | Snack    | {self.nama_produk:<20} | {self.harga:>8} IDR"

class Makanan(Produk):
    def __init__(self, kode_produk, nama_makanan, harga):
        super().__init__(kode_produk, nama_makanan, harga)
    
    def info_produk(self):
        return f"{self.kode_produk:<10} | Makanan  | {self.nama_produk:<20} | {self.harga:>8} IDR"

class Minuman(Produk):
    def __init__(self, kode_produk, nama_minuman, harga):
        super().__init__(kode_produk, nama_minuman, harga)
    
    def info_produk(self):  
        return f"{self.kode_produk:<10} | Minuman  | {self.nama_produk:<20} | {self.harga:>8} IDR"

class Struk:
    def __init__(self, no_transaksi, pegawai, daftar_produk):
        self.no_transaksi = no_transaksi
        self.pegawai = pegawai

    def total_harga(self):
        total = sum(produk.harga * jumlah for produk, jumlah in self.daftar_produk)
        return total

class Struk:
    def __init__(self, no_transaksi, nama_pegawai, daftar_produk):
        self.no_transaksi = no_transaksi
        self.nama_pegawai = nama_pegawai
        self.daftar_produk = daftar_produk  

    def total_harga(self):
        total = sum(produk.harga * jumlah for produk, jumlah in self.daftar_produk)
        return total

    def cetak_struk(self):
        print("=" * 30)
        print("        STRUK TRANSAKSI       ")
        print("=" * 30)
        print(f"No Transaksi: {self.no_transaksi}")
        print(f"Pegawai: {self.nama_pegawai}")
        print("=" * 30)
        print("Daftar Produk:")
        print("Kode       | Tipe     | Nama Produk           |   Jumlah |   Subtotal")
        print("-" * 70)
        
        for produk, jumlah in self.daftar_produk:
            subtotal = produk.harga * jumlah
            print(f"{produk.kode_produk:<10} | {produk.__class__.__name__:<8} | {produk.nama_produk:<20} | {jumlah:<7} | {subtotal:>10} IDR")
        
        print("-" * 70)
        print(f"Total Harga: {self.total_harga():>50} IDR")
        print("=" * 30)




def tampilkan_menu():
    print("\n=== Warung Serba Ada ===")
    print("1. Tambah Pesanan")
    print("2. Lihat Daftar Pesanan")
    print("3. Buat Transaksi")
    print("4. Keluar")
    return input("Pilih menu (1-4): ")

def kode_berikutnya(daftar):
    if not daftar:
        return 1
    last_code = daftar[-1].kode_produk
    return int(last_code[1:]) + 1

def tambah_produk(daftar_snack, daftar_makanan, daftar_minuman):
    tipe = input("Masukkan tipe produk (S = Snack, M = Makanan, D = Minuman): ").upper()
    nama_produk = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))

    if tipe == 'S':
        kode_produk = f"S{kode_berikutnya(daftar_snack):03}"
        produk = Snack(kode_produk, nama_produk, harga)
        daftar_snack.append(produk)
    elif tipe == 'M':
        kode_produk = f"M{kode_berikutnya(daftar_makanan):03}"
        produk = Makanan(kode_produk, nama_produk, harga)
        daftar_makanan.append(produk)
    elif tipe == 'D':
        kode_produk = f"D{kode_berikutnya(daftar_minuman):03}"
        produk = Minuman(kode_produk, nama_produk, harga)
        daftar_minuman.append(produk)
    else:
        print("Tipe produk tidak valid!")
        return

    print("Produk berhasil ditambahkan!")

def lihat_daftar_produk(daftar_snack, daftar_makanan, daftar_minuman):
    print("\nDaftar Produk:")
    print("Kode       | Tipe     | Nama Produk           |   Harga")
    print("-" * 50)
    
    for produk in daftar_snack:
        print(produk.info_produk())
    
    for produk in daftar_makanan:
        print(produk.info_produk())
    
    for produk in daftar_minuman:
        print(produk.info_produk())
    
    print("-" * 50)

def buat_transaksi(pegawai, daftar_snack, daftar_makanan, daftar_minuman):
    daftar_produk = daftar_snack + daftar_makanan + daftar_minuman
    
    if not daftar_produk:
        print("Belum ada produk yang bisa dijual.")
        return

    no_transaksi = input("Masukkan nomor transaksi: ")
    transaksi = Transaksi(no_transaksi, "Pembelian Produk")
    
    print("Masukkan kode produk yang ingin dibeli (ketik 'selesai' untuk selesai):")
    produk_terbeli = []
    while True:
        kode = input("Kode Produk: ")
        if kode.lower() == 'selesai':
            break
        produk = next((p for p in daftar_produk if p.kode_produk == kode), None)
        if produk:
            jumlah = int(input(f"Masukkan jumlah untuk {produk.nama_produk}: "))
            produk_terbeli.append((produk, jumlah))
        else:
            print("Produk tidak ditemukan.")

    if produk_terbeli:
        struk = Struk(transaksi.no_transaksi, pegawai.nama, produk_terbeli)
        struk.cetak_struk()
    else:
        print("Tidak ada produk yang dipilih.")

def inisialisasi_data_produk():
    daftar_snack = [
        Snack("S001", "Keripik Kentang", 10000),
        Snack("S002", "Popcorn", 12000),
        Snack("S003", "Cokelat Batangan", 15000),
        Snack("S004", "Wafer", 8000),
        Snack("S005", "Permen Karet", 5000),
    ]
    
    daftar_makanan = [
        Makanan("M001", "Nasi Goreng", 20000),
        Makanan("M002", "Mie Goreng", 18000),
        Makanan("M003", "Sate Ayam", 25000),
        Makanan("M004", "Bakso", 15000),
        Makanan("M005", "Soto Ayam", 17000),
    ]
    
    daftar_minuman = [
        Minuman("D001", "Es Teh", 5000),
        Minuman("D002", "Kopi Hitam", 10000),
        Minuman("D003", "Jus Jeruk", 12000),
        Minuman("D004", "Es Kelapa", 15000),
        Minuman("D005", "Smoothie Berry", 20000),
    ]
    
    return daftar_snack, daftar_makanan, daftar_minuman

def main():
    pegawai1 = Pegawai("123", "Budi", "Jl. Merdeka")
    daftar_snack, daftar_makanan, daftar_minuman = inisialisasi_data_produk()  

    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            tambah_produk(daftar_snack, daftar_makanan, daftar_minuman)
        elif pilihan == '2':
            lihat_daftar_produk(daftar_snack, daftar_makanan, daftar_minuman)
        elif pilihan == '3':
            buat_transaksi(pegawai1, daftar_snack, daftar_makanan, daftar_minuman)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid!")
                  
main()
