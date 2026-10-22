import os 

daftartotal = []

def tampilkan_riwayat():
    if not os.path.exists("riwayat_belanja.txt"):
        print("Belum ada riwayat belanja.")
        return
    with open("riwayat_belanja.txt", "r") as f:
        print(f.read())

def validasi_input(pesan):
    while True:
        try:
            angka = int(input(pesan))
            if angka > 0:
                return angka
            print("angka harus lebih dari 0")

        except ValueError:
            print("masukkan angka bukan huruf")      

def hitungbelanja(harga, jumlahbrg):
    subtotal = harga * jumlahbrg
    diskon = subtotal * 10 // 100
    total = subtotal - diskon
    return subtotal, diskon, total

tampilkan_riwayat()

while True:
    barang = input("Nama barang (ketik selesai untuk berhenti): ")
    if barang.lower() == "selesai":
        break
    hargasatuan = validasi_input("harga satuan: ")
    jumlah = validasi_input("Jumlah barang: ")

    subtotal, diskon, total = hitungbelanja(hargasatuan, jumlah)
    daftartotal.append(total)

    print("Barang                     ", barang)
    print("Harga satuan               ", hargasatuan)
    print("jumlah                     ", jumlah)
    print("subtotal                   ", subtotal)
    print("diskon                     ", diskon)
    print("Total barang ini           ", total)
    print("-" * 40)

    with open("riwayat_belanja.txt", "a") as f:
        f.write(f"{barang} | {hargasatuan} x {jumlah} | subtotal {subtotal} | diskon {diskon} | total {total}\n")

print("Total belanja keseluruhan  ", sum(daftartotal))

with open("riwayat_belanja.txt", "a") as f:
    f.write(f"TOTAL KESELURUHAN: {sum(daftartotal)}\n{'-' * 40}\n")