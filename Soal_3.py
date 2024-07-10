class AntrianRestoran:
    def __init__(self):
        self.queque = []

    def enqueue(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan '{pesanan}'ditambahkan ke dalam antrian.")

    def dequeue(self):
        if self.antrian_kosong():
            print("Antrian kosong, tidak ada pesanan yang bisa dihapus.")
            return None
        pesanan_dihapus = self.queque.pop(0)
        print(f"Pesanan '{pesanan_dihapus}' telah dihapus dari antrian.")
        return pesanan_dihapus

    def antrian_kosong(self):
        return len(self.antrian) == 0

    def tampilkan_antrian(self):
        if self.antrian_kosong():
            print("Antrian saat ini kosong.")
        else:
            print("Antrian saat ini:", self.antrian)

if __name__ == "__main__":
    antrian_restoran = AntrianRestoran()
    antrian_restoran.tambah_pesanan("Pesanan 1")
    antrian_restoran.tambah_pesanan("Pesanan 2")
    antrian_restoran.tambah_pesanan("Pesanan 3")
    antrian_restoran.tampilkan_antrian()
    antrian_restoran.hapus_pesanan()
    antrian_restoran.tampilkan_antrian()
    antrian_restoran.hapus_pesanan()
    antrian_restoran.hapus_pesanan()
    antrian_restoran.hapus_pesanan()
    antrian_restoran.tampilkan_antrian()
