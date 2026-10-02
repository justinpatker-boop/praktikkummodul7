mahasiswa = {
    "Andi": {"prodi" : "PTIK" , "ipk": 3.8},
    "Siti": {"prodi" : "Informatika" , "ipk": 3.9},
    "Budi": {"prodi" : "PTIK", "ipk": 3.6},
}

print("===== DATA MAHASISWA =====")
for nama, detail in mahasiswa.items():
    print(f"Nama: {nama:<6} | Prodi: {detail['prodi']:<11} | IPK: {detail['ipk']}")

total_ipk = sum(m["ipk"] for m in mahasiswa.values())
rata_ipk = total_ipk / len(mahasiswa)

mhs_tertinggi = max(mahasiswa.items(), key=lambda x: x[1]["ipk"])
mhs_terendah = min(mahasiswa.items(), key=lambda x: x[1]["ipk"])

print(f"\nRata-rata IPK: {rata_ipk:.2f}")
print(f"IPK Tertinggi: {mhs_tertinggi} ({mhs_tertinggi[1]['ipk']})")
print(f"IPK Terendah: {mhs_terendah} ({mhs_terendah[1]['ipk']})")

kelompok_prodi = {}
for nama, detail in mahasiswa.items():
    p = detail["prodi"]
    if p not in kelompok_prodi:
        kelompok_prodi[p] = []
    kelompok_prodi[p].append(nama)

print("\nPengelompokkan Berdasarkan Prodi:")
for prodi, daftar_nama in kelompok_prodi.items():
    print(f"{prodi}: {', '.join(daftar_nama)}")