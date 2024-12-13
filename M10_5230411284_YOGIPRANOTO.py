import sqlite3

conn = sqlite3.connect('penjualan.db')
cursor = conn.cursor()


def create_tables():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pegawai (
        NID INTEGER PRIMARY KEY,
        Nama TEXT NOT NULL,
        Alamat TEXT NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produk (
        Kode_Produk INTEGER PRIMARY KEY,
        Nama_Produk TEXT NOT NULL,
        Jenis_Produk TEXT NOT NULL,
        Harga REAL NOT NULL
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaksi (
        No_Transaksi INTEGER PRIMARY KEY,
        NID INTEGER,
        Tanggal_Transaksi DATE NOT NULL,
        Total_Harga REAL NOT NULL,
        FOREIGN KEY (NID) REFERENCES Pegawai(NID)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Makanan (
        Kode_Makanan INTEGER PRIMARY KEY,
        Nama_Makanan TEXT NOT NULL,
        FOREIGN KEY (Kode_Makanan) REFERENCES Produk(Kode_Produk)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Minuman (
        Kode_Minuman INTEGER PRIMARY KEY,
        Nama_Minuman TEXT NOT NULL,
        FOREIGN KEY (Kode_Minuman) REFERENCES Produk(Kode_Produk)
    );
    ''')

    conn.commit()

def insert_data():
    cursor.execute("INSERT INTO Pegawai (NID, Nama, Alamat) VALUES (1, 'Ali', 'Jakarta')")
    cursor.execute("INSERT INTO Pegawai (NID, Nama, Alamat) VALUES (2, 'Budi', 'Bandung')")
    
    cursor.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (101, 'Nasi Goreng', 'Makanan', 20000)")
    cursor.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (102, 'Ayam Penyet', 'Makanan', 25000)")
    cursor.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (201, 'Teh Botol', 'Minuman', 10000)")
    cursor.execute("INSERT INTO Produk (Kode_Produk, Nama_Produk, Jenis_Produk, Harga) VALUES (202, 'Kopi', 'Minuman', 15000)")

    cursor.execute("INSERT INTO Transaksi (No_Transaksi, NID, Tanggal_Transaksi, Total_Harga) VALUES (1, 1, '2023-12-01', 45000)")
    cursor.execute("INSERT INTO Transaksi (No_Transaksi, NID, Tanggal_Transaksi, Total_Harga) VALUES (2, 2, '2023-12-02', 35000)")

    cursor.execute("INSERT INTO Makanan (Kode_Makanan, Nama_Makanan) VALUES (101, 'Nasi Goreng')")
    cursor.execute("INSERT INTO Makanan (Kode_Makanan, Nama_Makanan) VALUES (102, 'Ayam Penyet')")

    cursor.execute("INSERT INTO Minuman (Kode_Minuman, Nama_Minuman) VALUES (201, 'Teh Botol')")
    cursor.execute("INSERT INTO Minuman (Kode_Minuman, Nama_Minuman) VALUES (202, 'Kopi')")

    conn.commit()

def fetch_data():
    cursor.execute("SELECT * FROM Pegawai")
    print("Pegawai:")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM Produk")
    print("\nProduk:")
    for row in cursor.fetchall():
        print(row)


def delete_data():
    cursor.execute("DELETE FROM Pegawai WHERE NID = 1")
    conn.commit()


create_tables()
insert_data()
fetch_data()
delete_data()

# Menutup koneksi
conn.close()