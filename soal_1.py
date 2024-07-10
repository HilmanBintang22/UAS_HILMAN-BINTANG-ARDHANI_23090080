mahasiswa_list = []

def masukkan_data_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    mahasiswa = {"NIM": nim, "Nama": nama}
    mahasiswa_list.append(mahasiswa)

def tampilkan_data_mahasiswa():
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
    else:
        print("Data Mahasiswa:")
        for mahasiswa in mahasiswa_list:
            print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

def main():
    while True:
        print("\nMenu:")
        print("1. Masukkan Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            masukkan_data_mahasiswa()
        elif pilihan == '2':
            tampilkan_data_mahasiswa()
        elif pilihan == '3':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()