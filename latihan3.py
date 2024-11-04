saldo = 1000000

while saldo > 0:
    print(f"Saldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = int(input("Pilih menu (1/2): "))

    if pilihan == 1:
        jumlah_penarikan = int(input("Masukkan jumlah penarikan: "))
        if jumlah_penarikan > saldo:
            print("Saldo tidak mencukupi!")
        else:
            saldo -= jumlah_penarikan
            print("Penarikan berhasil!")
    elif pilihan == 2:
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid!")