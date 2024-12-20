def hitung_gaji():
    jam_kerja = int(input("Masukkan jumlah jam kerja: "))
    tarif_per_jam = int(input("Masukkan tarif per jam: "))

    jam_normal = 40
    gaji_lembur = 0

    if jam_kerja <= jam_normal:
        gaji = jam_kerja * tarif_per_jam
    else:
        jam_lembur = jam_kerja - jam_normal
        gaji_lembur = int(jam_lembur * tarif_per_jam * 1.5)
        gaji = (jam_normal * tarif_per_jam) + gaji_lembur

    print("Gaji total: Rp", f"{gaji:,.0f}".replace(",", "."))
    print("Gaji lembur: Rp", f"{gaji_lembur:,.0f}".replace(",", "."))

hitung_gaji()


