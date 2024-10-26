from tabulate import tabulate

class Order:
    def __init__(self, ID=0, name="", details=""):
        self._ID = ID
        self.name = name
        self.details = details

class Delivery:
    def __init__(self, id=0, name="", information="", date="", address=""):
        self._id = id
        self.name = name
        self.information = information
        self.date = date
        self.address = address

orders = []
deliveries = []

while True:
    print("\n=== Menu Aplikasi ===")
    print("1. Tambah Order")
    print("2. Tambah Delivery")
    print("3. Lihat Semua Order")
    print("4. Lihat Semua Delivery")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        jumlah_order = int(input("Masukkan jumlah order yang ingin ditambahkan: "))
        
        for i in range(jumlah_order):
            print(f"\n--- Input Order {i+1} ---")
            ID = int(input("Masukkan Order ID: "))
            name = input("Masukkan Nama Order: ")
            details = input("Masukkan Detail Order: ")
            order = Order(ID, name, details)
            orders.append(order)
            print("Order berhasil ditambahkan!")
    
    elif pilihan == "2":
        id = int(input("Masukkan Delivery ID: "))
        name = input("Masukkan Nama Penerima: ")
        information = input("Masukkan Informasi Pengiriman: ")
        date = input("Masukkan Tanggal Pengiriman: ")
        address = input("Masukkan Alamat Pengiriman: ")
        delivery = Delivery(id, name, information, date, address)
        deliveries.append(delivery)
        print("Delivery berhasil ditambahkan!")
    
    elif pilihan == "3":
        if not orders:
            print("Belum ada order yang ditambahkan.")
        else:
            order_data = [[order._ID, order.name, order.details] for order in orders]
            headers = ["Order ID", "Nama", "Detail"]
            print("\n=== Daftar Semua Order ===")
            print(tabulate(order_data, headers, tablefmt="grid"))
    
    elif pilihan == "4":
        if not deliveries:
            print("Belum ada delivery yang ditambahkan.")
        else:
            delivery_data = [[delivery._id, delivery.name, delivery.information, delivery.date, delivery.address] for delivery in deliveries]
            headers = ["Delivery ID", "Nama Penerima", "Informasi", "Tanggal", "Alamat"]
            print("\n=== Daftar Semua Delivery ===")
            print(tabulate(delivery_data, headers, tablefmt="grid"))
    
    elif pilihan == "5":
        print("Keluar dari aplikasi. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
