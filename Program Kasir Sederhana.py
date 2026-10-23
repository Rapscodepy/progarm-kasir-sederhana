# Fungsi format rupiah
def rupiah(angka):
    return "Rp {:,}".format(angka).replace(",", ".")

grand_total = 0  # total semua belanja

while True:
    print("\n======== INPUT DATA PEMBELIAN ========")

    nama_pembeli = input("Masukkan nama pembeli  : ")
    nama_barang = input("Masukkan nama barang   : ")

    try:
        harga = int(input("Masukkan harga barang  : "))
        jumlah = int(input("Masukkan jumlah barang : "))

        # Validasi
        if harga < 0:
            print("Error: Harga tidak boleh kurang dari 0!")
            continue
        elif jumlah <= 0:
            print("Error: Jumlah tidak boleh kurang atau sama dengan 0!")
            continue

        # Perhitungan
        total = harga * jumlah

        # Diskon
        if total >= 100000:
            diskon_persen = 10
        elif total >= 50000:
            diskon_persen = 5
        else:
            diskon_persen = 0

        diskon = total * diskon_persen / 100
        total_bayar = total - diskon

        # Tambah ke total keseluruhan
        grand_total += total_bayar

        # Output struk
        print("\n========== STRUK PEMBELIAN ===========")
        print("Nama Pembeli :", nama_pembeli)
        print("Nama Barang  :", nama_barang)
        print("Harga        :", rupiah(harga))
        print("Jumlah       :", jumlah)
        print("Total        :", rupiah(total))
        print("Diskon       :", str(diskon_persen) + "%")
        print("Total Bayar  :", rupiah(int(total_bayar)))

    except ValueError:
        print("Error: Input harga dan jumlah harus angka!")
        continue

    # Tanya lanjut atau tidak
    ulang = input("\nIngin input belanjaan lagi? (y/n): ").lower()
    if ulang != 'y':
        break

# Tampilkan total semua belanja
print("\n======== TOTAL SEMUA TRANSAKSI ========")
print("Grand Total :", rupiah(int(grand_total)))
print("Terima kasih telah menggunakan program kasir!")