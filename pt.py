from prettytable import PrettyTable


class transaksi:
    def __init__(self, nama, jenismotor, namabarang, tanggal, harga):
        self.nama = nama
        self.jenismotor = jenismotor
        self.namabarang = namabarang
        self.tanggal =  tanggal
        self.harga = harga
        self.next = None


class transaksiLinkedList:
    def __init__(self):
        self.head = None

    def tambah_transaksi(self, nama, jenismotor, namabarang, tanggal, harga):
        new_trannsakksi = transaksi(nama, jenismotor, namabarang, tanggal, harga)

        if not self.head:
            self.head = new_trannsakksi
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_trannsakksi

    def tampilkan_transaksi(self):
        if not self.head:
            print("Tidak ada transaksi yang terjadi.")
        else:
            current = self.head
            table = PrettyTable(["nama", "jenis motor", "nama barang", "tanggal", "harga"])
            while current:
                table.add_row([current.nama, current.jenismotor, current.namabarang, current.tanggal, current.harga])
                current = current.next
            print(table)


    def cari_transaksi(self, nama):
        current = self.head
        while current is not None:
            if current.nama == nama:
                return current
            current = current.next
        return None

    def update_transaksi(self, nama, jenismotor, namabarang, tanggal, harga):
        transaksi = self.cari_transaksi(nama)
        if transaksi:
            transaksi.nama = nama
            transaksi.jenismotor = jenismotor
            transaksi.namabarang = namabarang
            transaksi.tanggal = tanggal
            transaksi.harga = harga
            print("Data transaksi berhasil diupdate!")
        else:
            print("Transaksi dengan nama tersebut tidak ditemukan.")

    def hapus_transaksi(self, nama):
        current = self.head
        if current and current.nama == nama:
            self.head = current.next
            current = None
            print("Transaksi berhasil dihapus!")
            return
        prev = None
        while current and current.nama != nama:
            prev = current
            current = current.next
        if current is None:
            print("Transaksi dengan nama tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Transaksi berhasil dihapus!")

def tampilan_menu():
    print("======SELAMAT DATANG DI ONE3MOTOSHOP======\n")
    print("|========================================|")
    print("|-------RIWAYAT TRANSAKSI CUSTOMER-------|")
    print("|========================================|")
    print("|1. Menambah riwayat transaksi           |")
    print("|2. Melihat riwayat transaksi            |")
    print("|3. Cari riwayat transaksi               |")
    print("|4. Update data transaksi                |")
    print("|5. Hapus data transaksi                 |")
    print("|6. Exit                                 |")
    print("|========================================|")
    print()

tampilan_menu()
my_list = transaksiLinkedList()

while True:
    pilih = input("Masukan pilihan anda: ")

    if pilih == "1":
        nama = input("Masukan nama pembeli: ")
        jenismotor = input("Masukan jenis motor: ")
        namabarang = input("Masukan Nama barang: ")
        tanggal = input("masukan tanggal transaksi: ")
        harga = input("Masukan harga barang: ")
        my_list.tambah_transaksi(nama, jenismotor, namabarang, tanggal, harga)
        print("Data transaksi berhasil ditambahkan!")
    
    elif pilih == "2":
        my_list.tampilkan_transaksi()

    elif pilih == "3":
        nama = input("Masukan nama pembeli yang ingin dicari: ")
        transaksi = my_list.cari_transaksi(nama)
        if transaksi:
            print(f"Transaksi dengan nama {nama} ditemukan")
            print(f"Nama : {transaksi.nama}")
            print(f"jenis motor : {transaksi.jenismotor}")
            print(f"Nama barang : {transaksi.namabarang}")
            print(f"Tangggal : {transaksi.tanggal}")
            print(f"Harga : {transaksi.harga}")
        else:
            print(f"Trnsaksi dengan nama {nama} tidak ditemukan.")

    elif pilih == "4":
        my_list.tampilkan_transaksi()
        namac = input("Masukan nama pembeli yang ingin diupdate: ")
        transaksi = my_list.cari_transaksi(nama)
        if transaksi:
            nama_baru = input("Masukan nama baru: ")
            jenismotor_baru = input("Masukan jenis motor baru: ")
            namabarang_baru = input("Masukan nama barang baru: ")
            tanggal_baru = input("Masuka tanggal baru: ")
            harga_baru = input("Masukan harga baru: ")
            transaksi.nama = nama_baru
            transaksi.jenismotor = jenismotor_baru
            transaksi.namabarang = namabarang_baru
            transaksi.tanggal = tanggal_baru
            transaksi.harga = harga_baru
            my_list.update_transaksi(nama_baru, jenismotor_baru, namabarang_baru, tanggal_baru, harga_baru)
        else:
            print(f"Mahasiswa dengan NIM {namac} tidak ditemukan.")

    elif pilih == "5":
        my_list.tampilkan_transaksi()
        nama = input("Masukan nama pembeli yang ingin dihapus: ")
        transaksi = my_list.cari_transaksi(nama)
        if transaksi:
            my_list.hapus_transaksi(nama)
        else:
            print(f"Transaksi dengan nama {nama} tidak ditemukan.")

    elif pilih == "6":
        exit()