def format_rupiah(nominal):
    return f"Rp.{nominal:,.2f}".replace(',', '.').replace('.', ',', 1)

class KelolaDebitur:
    def __init__(self):
        self.__data_debitur = []  # Menyimpan data debitur
        # Menambahkan 5 debitur default
        self.__data_debitur.extend([
            {'nama': 'Curry', '_KelolaDebitur__ktp': '123', '_limit_pinjaman': 5000000},
            {'nama': 'Lebron', '_KelolaDebitur__ktp': '456', '_limit_pinjaman': 7000000},
            {'nama': 'Wemby', '_KelolaDebitur__ktp': '789', '_limit_pinjaman': 10000000},
            {'nama': 'Edward', '_KelolaDebitur__ktp': '987', '_limit_pinjaman': 6000000},
            {'nama': 'Davis', '_KelolaDebitur__ktp': '654', '_limit_pinjaman': 8000000},
        ])

    def tambah_debitur(self, nama, ktp, limit_pinjaman):
        for debitur in self.__data_debitur:
            if debitur['_KelolaDebitur__ktp'] == ktp:
                print("Gagal: KTP sudah terdaftar.")
                return
        debitur_baru = {
            'nama': nama,  
            '_KelolaDebitur__ktp': ktp, 
            '_limit_pinjaman': limit_pinjaman 
        }
        self.__data_debitur.append(debitur_baru)
        print(f"Debitur '{nama}' berhasil ditambahkan.")

    def tampilkan_debitur(self):
        print("\n" + "-" * 40)
        print("            DAFTAR DEBITUR")
        print("-" * 40)
        if not self.__data_debitur:
            print("Belum ada debitur yang terdaftar.")
        else:
            print(f"{'Nama':<15} {'KTP':<20} {'Limit Pinjaman':<15}")
            print("-" * 40)
            for debitur in self.__data_debitur:
                nama = debitur['nama']
                ktp = debitur['_KelolaDebitur__ktp']
                limit_pinjaman = format_rupiah(debitur['_limit_pinjaman'])  
                print(f"{nama:<15} {ktp:<20} {limit_pinjaman:<15}")
        print("-" * 40)

    def cari_debitur(self, nama):
        for debitur in self.__data_debitur:
            if debitur['nama'].lower() == nama.lower():
                return debitur
        return None

class KelolaPinjaman:
    def __init__(self, kelola_debitur):
        self.debitur_data = kelola_debitur
        self.data_pinjaman = []

    def tambah_pinjaman(self, nama, pinjaman, bunga, bulan):
        debitur = self.debitur_data.cari_debitur(nama)
        if not debitur:
            print(f"Gagal: Nama debitur '{nama}' tidak ditemukan.")
            return

        limit = debitur['_limit_pinjaman']
        if pinjaman > limit:
            print(f"Gagal: Pinjaman melebihi limit (Rp.{format_rupiah(limit)}).")
            return

        angsuran_pokok = pinjaman * (bunga / 100)
        angsuran_bulanan = angsuran_pokok / bulan
        total_angsuran = angsuran_pokok + angsuran_bulanan

        pinjaman_baru = {
            'nama': nama,
            'pinjaman': pinjaman,
            'bunga': bunga,
            'bulan': bulan,
            'angsuran_pokok': angsuran_pokok,
            'angsuran_bulanan': angsuran_bulanan,
            'total_angsuran': total_angsuran
        }
        self.data_pinjaman.append(pinjaman_baru)
        print(f"Pinjaman untuk {nama} berhasil ditambahkan.")

    def tampilkan_pinjaman(self):
        print("\n" + "-" * 90)
        print("            DAFTAR PINJAMAN")
        print("-" * 90)
        if not self.data_pinjaman:
            print("Belum ada pinjaman yang terdaftar.")
        else:
            print(f"{'Nama':<15} {'Pinjaman':<15} {'Bunga':<10} {'Bulan':<10} {'Angsuran Bulanan':<20} {'Total Angsuran':<15}")
            print("-" * 90)
            for pinjaman in self.data_pinjaman:
                print(f"{pinjaman['nama']:<15} {format_rupiah(pinjaman['pinjaman']):<15} {pinjaman['bunga']:<10} {pinjaman['bulan']:<10} {format_rupiah(pinjaman['angsuran_bulanan']):<20} {format_rupiah(pinjaman['total_angsuran']):<15}")
        print("-" * 90)

def input_nama(prompt):
    while True:
        nama = input(prompt).strip()
        if nama.isalpha():
            return nama
        print("Input tidak valid. Silakan masukkan nama yang hanya mengandung huruf.")

def input_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka bulat.")

def main():
    kelola_debitur = KelolaDebitur()
    kelola_pinjaman = KelolaPinjaman(kelola_debitur)

    while True:
        print("\n" + "=" * 90)
        print("            MENU UTAMA")
        print("=" * 90)
        print("1. Kelola Debitur")
        print("2. Kelola Pinjaman")
        print("3. Keluar")

        pilihan = input_integer("Pilih opsi (1-3): ")

        if pilihan == 1:
            while True:
                print("\n" + "-" * 90)
                print("            KELOLA DEBITUR")
                print("-" * 90)
                print("1. Tampilkan Semua Debitur")
                print("2. Cari Debitur")
                print("3. Tambah Debitur")
                print("4. Kembali ke Menu Utama")

                sub_pilihan = input_integer("Pilih opsi (1-4): ")

                if sub_pilihan == 1:
                    kelola_debitur.tampilkan_debitur()
                elif sub_pilihan == 2:
                    nama_cari = input("Masukkan nama debitur yang dicari: ")
                    debitur = kelola_debitur.cari_debitur(nama_cari)
                    if debitur:
                        print(f"Nama: {debitur['nama']}, KTP: {debitur['_KelolaDebitur__ktp']}, Limit Pinjaman: {format_rupiah(debitur['_limit_pinjaman'])}")
                    else:
                        print("Debitur tidak ditemukan.")
                elif sub_pilihan == 3:
                    nama_debitur = input_nama("Masukkan nama debitur: ")
                    ktp_debitur = input("Masukkan KTP debitur: ")
                    limit_pinjaman = input_integer("Masukkan limit pinjaman: ")
                    kelola_debitur.tambah_debitur(nama_debitur, ktp_debitur, limit_pinjaman)
                elif sub_pilihan == 4:
                    break
                else:
                    print("Opsi tidak valid, silakan coba lagi.")

        elif pilihan == 2:
            while True:
                print("\n" + "-" * 90)
                print("            KELOLA PINJAMAN")
                print("-" * 90)
                print("1. Tambah Pinjaman")
                print("2. Tampilkan Pinjaman")
                print("3. Kembali ke Menu Utama")

                sub_pilihan = input_integer("Pilih opsi (1-3): ")

                if sub_pilihan == 1:
                    nama_debitur = input("Masukkan nama debitur: ")
                    pinjaman = input_integer("Masukkan jumlah pinjaman: ")
                    bunga = input_integer("Masukkan bunga (%): ")
                    bulan = input_integer("Masukkan lama pinjaman (dalam bulan): ")
                    kelola_pinjaman.tambah_pinjaman(nama_debitur, pinjaman, bunga, bulan)
                elif sub_pilihan == 2:
                    kelola_pinjaman.tampilkan_pinjaman()
                elif sub_pilihan == 3:
                    break
                else:
                    print("Opsi tidak valid, silakan coba lagi.")

        elif pilihan == 3:
            print("Keluar dari aplikasi.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
