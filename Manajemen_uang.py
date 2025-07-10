import csv
import os

# Nama file CSV
nama_file = "keuangan.csv"

# Inisialisasi file jika belum ada
if not os.path.exists(nama_file):
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Jenis", "Kategori", "Jumlah"])  # Header

def tambah_transaksi():
    jenis = input("Jenis (pemasukan/pengeluaran): ").lower()
    kategori = input("Kategori: ")
    jumlah = float(input("Jumlah: Rp "))

    # Simpan ke file CSV
    with open(nama_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([jenis, kategori, jumlah])
    
    print("✅ Transaksi berhasil ditambahkan dan disimpan ke file.\n")

def lihat_saldo():
    pemasukan = 0
    pengeluaran = 0

    # Baca data dari file CSV
    with open(nama_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jumlah = float(row["Jumlah"])
            if row["Jenis"] == "pemasukan":
                pemasukan += jumlah
            elif row["Jenis"] == "pengeluaran":
                pengeluaran += jumlah

    saldo = pemasukan - pengeluaran

    print("\n=== Ringkasan Keuangan ===")
    print(f"Total Pemasukan  : Rp {pemasukan:.2f}")
    print(f"Total Pengeluaran: Rp {pengeluaran:.2f}")
    print(f"Saldo Saat Ini   : Rp {saldo:.2f}\n")

def menu():
    while True:
        print("=== MENU MANAJEMEN KEUANGAN ===")
        print("1. Tambah Transaksi")
        print("2. Lihat Saldo")
        print("3. Keluar")
        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            lihat_saldo()
        elif pilihan == "3":
            print("👋 Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("❗ Pilihan tidak valid. Coba lagi.\n")

# Jalankan program
menu()
