while True:
    print('==========MENU==========')
    print('1. tambah menu')
    print('2. lihat menu')
    print('3. exit')

    a=input('pilih nomor menu: ')
    if a=='1':
        b=input('masukkan nama menu: ')
        c=input('masukkan harga menu: ')
    elif a=='2':
        print('MENU YANG DI TAMBAH')
        print('Menu','          ',b)
        print('Harga','          ',c)
        
    elif a=='3':
        print('Berhasil Keluar')
        break
    else:
        print('Menu yang di pilih tidak tersedia mohon masukkan kembali Menu Anda')
