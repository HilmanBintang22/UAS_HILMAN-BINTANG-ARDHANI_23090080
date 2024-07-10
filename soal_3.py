class AntrianRestoran:
    def __init__(self):
        self.antrian = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        if not self.antrian:
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
            return None
        pesanan = self.antrian.pop(0)
        print(f"Pesanan '{pesanan}' telah dihapus dari antrian.")
        return pesanan

    def tampilkan_antrian(self):
        if not self.antrian:
            print("Antrian kosong.")
        else:
            print("Antrian saat ini:")
            for idx, pesanan in enumerate(self.antrian, start=1):
                print(f"{idx}. {pesanan}")