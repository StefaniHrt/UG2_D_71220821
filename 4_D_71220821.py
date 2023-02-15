print("!! Selamat datang di H+ GYM !! \n Silahkan pilih menu dibawah ini: \n 1. Menambahkan data \n 2. Menampilkan data \n 3. Keluar")
pilihan=int(input("Silahkan masukan pilihan yang anda inginkan:"))
while pilihan==1 or pilihan==2 or pilihan==3:
    if pilihan==1:
        nama=input("Masukkan nama pelanggan:").list()
        member=input("Masukkan jenis member:").list()
        print("Data sudah berhasil ditambahkan!")
        gym()
    elif pilihan==2:
        print("-------------------")
        print("pelanggan    Member:", anggota)
        gym()
    elif pilihan==3:
        print("sistem berhenti")
else:
    print("silahkan coba lagi")
    