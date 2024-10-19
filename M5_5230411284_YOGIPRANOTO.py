# Class Music untuk mendefinisikan atribut musik
class Music:
    def __init__(self, judul, penyanyi, genre):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

    def __str__(self):
        return f"Judul: {self.judul}, Penyanyi: {self.penyanyi}, Genre: {self.genre}"

class MusicLibrary:
    def __init__(self):
        self.library = {
            "Heavy Metal": [
                Music("Tears Don't Fall", "Bullet for My Valentine", "Heavy Metal"),
                Music("Alone", "Bullet for My Valentine", "Heavy Metal"),
                Music("Waking the Demon", "Bullet for My Valentine", "Heavy Metal"),
                Music("Your Betrayal", "Bullet for My Valentine", "Heavy Metal"),
                Music("Scream, Aim, Fire", "Bullet for My Valentine", "Heavy Metal"),
            ],
            "R&B": [
                Music("End of the Road", "Boyz II Men", "R&B"),
                Music("I'll Make Love to You", "Boyz II Men", "R&B"),
                Music("On Bended Knee", "Boyz II Men", "R&B"),
                Music("A Song for Mama", "Boyz II Men", "R&B"),

            ],
            "Alternatif": [
                Music("Misery Business", "Paramore", "Alternatif"),
                Music("Still Into You", "Paramore", "Alternatif"),
                Music("Ain't It Fun", "Paramore", "Alternatif"),
                Music("The Only Exception", "Paramore", "Alternatif"),
                Music("Hard Times", "Paramore", "Alternatif"),
            ]
        }

    def display_all(self):
        print("\n=== Semua Lagu ===")
        total_lagu = sum(len(self.library[genre]) for genre in self.library)
        print(f"Total jumlah lagu: {total_lagu}")
        print(f"{'-'*60}")
        print(f"| {'Judul':<30} | {'Penyanyi':<30} | {'Genre':<15} |")
        print(f"{'-'*60}")
        for genre in self.library:
            for music in self.library[genre]:
                print(f"| {music.judul:<30} | {music.penyanyi:<30} | {music.genre:<15} |")
        print(f"{'-'*60}")

    def add_music(self, genre, music):
        self.library[genre].append(music)
        print(f"{music.judul} telah ditambahkan ke genre {genre}.")

    def delete_music(self, genre, judul):
        for music in self.library[genre]:
            if music.judul == judul:
                self.library[genre].remove(music)
                print(f"{music.judul} telah dihapus dari genre {genre}.")
                return
        print(f"Musik dengan judul {judul} tidak ditemukan di genre {genre}.")

def menu_genre(perpustakaan_musik, genre):
    while True:
        print(f"\n=== Menu Genre: {genre} ===")
        print("1. Tampilkan Lagu")
        print("2. Tambah Lagu")
        print("3. Hapus Lagu")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == "1":
            perpustakaan_musik.display_all() 

        elif pilihan == "2":
            judul = input("Masukkan judul musik: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            perpustakaan_musik.add_music(genre, Music(judul, penyanyi, genre))

        elif pilihan == "3":
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            perpustakaan_musik.delete_music(genre, judul)

        elif pilihan == "4":
            break  
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_utama():
    perpustakaan_musik = MusicLibrary()

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Musik")
        print("2. Hapus Musik")
        print("3. Tampilkan Berdasarkan Penyanyi")
        print("4. Tampilkan Semua Musik")
        print("5. Keluar")

        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == "1":
            print("Pilih genre:")
            print("1. Heavy Metal")
            print("2. R&B")
            print("3. Alternatif")
            genre_choice = input("Masukkan pilihan genre (1-3): ")

            if genre_choice == "1":
                genre = "Heavy Metal"
            elif genre_choice == "2":
                genre = "R&B"
            elif genre_choice == "3":
                genre = "Alternatif"
            else:
                print("Pilihan genre tidak valid.")
                continue
            
            judul = input("Masukkan judul musik: ")
            penyanyi = input("Masukkan nama penyanyi: ")
            perpustakaan_musik.add_music(genre, Music(judul, penyanyi, genre))

        elif pilihan == "2":
            print("Pilih genre untuk menghapus musik:")
            print("1. Heavy Metal")
            print("2. R&B")
            print("3. Alternatif")
            genre_choice = input("Masukkan pilihan genre (1-3): ")

            if genre_choice == "1":
                genre = "Heavy Metal"
            elif genre_choice == "2":
                genre = "R&B"
            elif genre_choice == "3":
                genre = "Alternatif"
            else:
                print("Pilihan genre tidak valid.")
                continue
            
            judul = input("Masukkan judul musik yang ingin dihapus: ")
            perpustakaan_musik.delete_music(genre, judul)

        elif pilihan == "3":
            print("\n=== Tampilkan Berdasarkan Penyanyi ===")
            penyanyi = input("Masukkan nama penyanyi: ")
            print(f"{'-'*60}")
            print(f"| {'Judul':<30} | {'Penyanyi':<30} | {'Genre':<15} |")
            print(f"{'-'*60}")
            for genre in perpustakaan_musik.library:
                for music in perpustakaan_musik.library[genre]:
                    if music.penyanyi.lower() == penyanyi.lower():
                        print(f"| {music.judul:<30} | {music.penyanyi:<30} | {music.genre:<15} |")
            print(f"{'-'*60}")

        elif pilihan == "4":
            perpustakaan_musik.display_all()

        elif pilihan == "5":
            print("Terima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()
