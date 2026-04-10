import  perangkat

def main():
    hp1 = perangkat.Handphone("Samsung", "Galaxy S25 Ultra", 18000000, 10)
    hp2 = perangkat.Handphone("iPhone", "17 Pro Max", 25000000, 3)

    #Menampilkan katalog produk
    print("\nKatalog Produk Saat Ini:")
    hp1.tampilkan_info()
    hp2.tampilkan_info()

    #Simulasi transaksi
    hp1.beli(2)
    hp2.beli(5)

    #Menampilkan Stok Akhir
    print("\n" + "====================================")
    print("Update stok akhir:")
    hp1.tampilkan_info()
    hp2.tampilkan_info()

if __name__ == "__main__":
    main()