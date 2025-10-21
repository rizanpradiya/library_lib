#Public Library
from tabulate import tabulate
#Dictionary
list_buku = [
    {
        'id': 'B01',
        'judul': 'Perahu Kertas',
        'penulis': 'Dewi Lestari',
        'kategori': 'Novel',
        'stok': 3
    },
    {
        'id': 'B02',
        'judul': 'Atomic Habits',
        'penulis': 'James Clear',
        'kategori': 'Self Help',
        'stok': 2
    },
    {
        'id': 'B03',
        'judul': 'Si Juki',
        'penulis': 'Faza Meonk',
        'kategori': 'Komik',
        'stok': 3
    }
]

list_pinjam = []

def daftar_buku():
    print('\nDaftar Buku')
    tabel = []
    for buku in list_buku:
        tabel.append([
            buku['id'],
            buku['judul'],
            buku['penulis'],
            buku['kategori'],
            buku['stok']
        ])
    
    print(tabulate(tabel, headers=['ID', 'Judul', 'Penulis', 'Kategori', 'Stok']))

#Opsi untuk lihat buku (READ)
def lihat_buku():
    while True:
        print('\nMenu Lihat Buku')
        print('1. Tampilkan Daftar Buku')
        print('2. Cari Berdasarkan Judul')
        print('3. Kembali')
        pilihan = input('Pilih menu: ')
        
        if pilihan == '1':
            daftar_buku()
        elif pilihan == '2':
            keyword = input('Masukkan kata kunci judul: ').lower()
            print('\nHasil Pencarian\n')
            tabel = []
            for buku in list_buku:
                if keyword in buku['judul'].lower():
                    tabel.append([
                        buku['id'],
                        buku['judul'],
                        buku['penulis'],
                        buku['kategori'],
                        buku['stok']
                    ])
            if tabel:
                print(tabulate(tabel, headers=['ID', 'Judul', 'Penulis', 'kategori', 'Stok']))
            else:
                print('Buku tidak ditemukan')
        elif pilihan == '3':
            break

#Opsi tambah buku (CREATE)
def tambah_buku():
    print('Tambah Buku\n')
    daftar_buku()
    
    id = input('Masukkan Book ID: ').upper()
    
    #Cek ID
    for buku in list_buku:
        if buku['id'].upper() == id:
            print('Error, ID sudah terpakai')
            return
    
    judul = input('Masukkan Judul: ')
    penulis = input('Masukkan Penulis: ')
    kategori = input('Masukkan Kategori: ')
    stok = int(input('Masukkan Stok: '))
    
    if stok < 0:
        print('Error, stok tidak bisa negatif')
        return
    
    list_buku.append({
        'id': id,
        'judul': judul,
        'penulis': penulis,
        'kategori': kategori,
        'stok': stok
    })
    
    print('Buku berhasil ditambahkan')
    daftar_buku()

#Opsi ubah buku (UPDATE)
def ubah_buku():
    print('Ubah Buku\n')
    daftar_buku()
    
    id_ubah = input('Masukkan ID buku yang ingin diubah: ').upper()
    
    # Cari buku
    index = -1
    for i in range(len(list_buku)):
        if list_buku[i]['id'].upper() == id_ubah:
            index = i
            break
    
    if index == -1:
        print('Error, ID buku tidak ada')
        return
    
    print('Kosongkan jika tidak ingin mengubah')
    judul = input('Judul baru: ')
    penulis = input('Penulis baru: ')
    kategori = input('Kategori baru: ')
    stok = input('Stok baru: ')
    
    if judul != '':
        list_buku[index]['judul'] = judul
    if penulis != '':
        list_buku[index]['penulis'] = penulis
    if kategori != '':
        list_buku[index]['kategori'] = kategori
    if stok != '':
        stok_baru = int(stok)
        if stok_baru >= 0:
            list_buku[index]['stok'] = stok_baru
        else:
            print('Stok tidak bisa negatif')
    print('Buku berhasil diubah')
    daftar_buku()

#Opsi hapus buku (DELETE)
def hapus_buku():
    print('Hapus Buku\n')
    daftar_buku()
    
    id_hapus = input('Masukkan ID buku yang ingin dihapus: ').upper()
    
    # Cari buku
    for i in range(len(list_buku)):
        if list_buku[i]['id'].upper() == id_hapus:
            konfirmasi = input('Konfirmasi penghapusan? (y/n): ')
            if konfirmasi == 'y':
                del list_buku[i]
                print('Buku berhasil dihapus')
                daftar_buku()
            return
    print('Error, ID tidak ditemukan')

#Opsi pinjam buku (Fitur 1)
def pinjam_buku():
    print('Pinjam Buku\n')
    daftar_buku()
    
    id_pinjam = input('Masukkan Book ID: ').upper()
    
    #Cari buku
    for buku in list_buku:
        if buku['id'].upper() == id_pinjam:
            if buku['stok'] > 0:
                nama = input('Masukkan nama peminjam: ')
                buku['stok'] -= 1
                
                #Database peminjaman
                list_pinjam.append({
                    'id': id_pinjam,
                    'nama': nama,
                    'judul': buku['judul']
                })
                
                print('Peminjaman berhasil!')
                print(f"Peminjam: {nama}")
                print(f"Buku: {buku['judul']}")
                print(f"Sisa stok: {buku['stok']}")
            else:
                print('Maaf, stok kosong')
            return
    
    print('Error, ID tidak ditemukan')

#Opsi balikin buku (Fitur 2)
def kembalikan_buku():
    print('\nKembalikan Buku\n')
    
    #Daftar peminjam
    if len(list_pinjam) == 0:
        print('Tidak ada buku yang sedang dipinjam')
        return
    
    print('Daftar Peminjaman Aktif:')
    tabel = []
    for i in range(len(list_pinjam)):
        pinjam = list_pinjam[i]
        tabel.append([
            i,
            pinjam['id'],
            pinjam['judul'],
            pinjam['nama']
        ])
    print(tabulate(tabel, headers=['No', 'ID', 'Judul', 'Nama']))


    print()
    index_pinjam = int(input('Masukkan nomor yang ingin dikembalikan: '))
    
    if index_pinjam < 0 or index_pinjam >= len(list_pinjam):
        print('Error, nomor tidak valid')
        return
    
    pinjam = list_pinjam[index_pinjam]
    
    #Balikin stok
    for buku in list_buku:
        if buku['id'] == pinjam['id']:
            buku['stok'] += 1
            print('Pengembalian berhasil')
            print(f"Peminjam: {pinjam['nama']}")
            print(f"Buku: {pinjam['judul']}")
            print(f"Stok sekarang: {buku['stok']}")
            break
    
    #Hapus dari database
    del list_pinjam[index_pinjam]

#Main
while True:
    print('PUBLIC LIBRARY')
    print('1. Lihat Buku')
    print('2. Tambah Buku')
    print('3. Ubah Buku')
    print('4. Hapus Buku')
    print('5. Pinjam Buku')
    print('6. Kembalikan Buku')
    print('7. Keluar')
    
    pilihan = input('Pilih menu: ')
    
    if pilihan == '1':
        lihat_buku()
    elif pilihan == '2':
        tambah_buku()
    elif pilihan == '3':
        ubah_buku()
    elif pilihan == '4':
        hapus_buku()
    elif pilihan == '5':
        pinjam_buku()
    elif pilihan == '6':
        kembalikan_buku()
    elif pilihan == '7':
        print('Terima kasih')
        break
    else:
        print('Pilihan tidak valid!')