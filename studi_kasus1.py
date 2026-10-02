inventori = {
    "Laptop": {"harga": 7000000, "stok": 5},
    "Mouse": {"harga": 150000, "stok": 10},
    "Keyboard": {"harga": 250000, "stok": 7}
}

print("=== DAFTAR BARANG ===")
for barang, detail in inventori.items():
    print(f"{barang} - Harga: Rp{detail['harga']} | Stok: {detail['stok']}")

nama_beli = input("\nMasukkan nama barang yang dibeli: ")
jumlah_beli = int(input("Masukkan jumlah yang dibeli: "))

if nama_beli in inventori:
    if jumlah_beli <= inventori[nama_beli]["stok"]:
        total_harga = inventori[nama_beli]["harga"] * jumlah_beli
        diskon = 0
        if total_harga > 5000000:
            diskon = 0.10 * total_harga

        total_bayar = total_harga - diskon
        inventori[nama_beli]["stok"] -= jumlah_beli

        print("\n=== NOTA PEMBELIAN ===")
        print(f"Barang      : {nama_beli}")
        print(f"Jumlah      : {jumlah_beli}")
        print(f"Total Harga : Rp{int(total_harga)}")
        print(f"Diskon      : Rp{int(diskon)}")
        print(f"Total Bayar : Rp{int(total_bayar)}")
        print(f"Sisa Stok   : {inventori[nama_beli]['stok']}")
    else:
        print("Stok barang tidak mencukupi.")
else:
    print("Barang tidak ditemukan dalam inventori.")