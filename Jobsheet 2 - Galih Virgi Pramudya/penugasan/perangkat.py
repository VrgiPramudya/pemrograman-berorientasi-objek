class Handphone:
    def __init__(self, merk, model, harga, stok):
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"{self.merk} {self.model} | Harga : Rp {self.harga:,.0f} | Stok : {self.stok}")

    def beli(self, jumlah):
        print(f"\n--- Transaksi: Membeli {jumlah} unit {self.model} ---")
        if self.stok >= jumlah:
            total = self.harga * jumlah
            self.stok -= jumlah
            print(f"Berhasil! Total pembayaran: Rp {total:,.0f}")
            print(f"Sisa stok {self.model} sekarang: {self.stok}")
        else:
            print(f"Gagal! Stok tidak mencukupi")