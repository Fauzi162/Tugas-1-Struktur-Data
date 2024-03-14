"""Nama Kelompok
1. FAUZA AHMAD ZAIDAN 23091397144
2. NUR FATEHAH 23091397160
3. AKHMAD FAUZI 23091397162
"""

# Tugas Struktur Data 1 - Mixue
class Pesanan:
    def _init_(self, nama_menu, harga, next=None):
        self.nama_menu = nama_menu
        self.harga = harga
        self.next = next

class DaftarPesanan:
    def _init_(self):
        
        self.head = None
    def tambahkan_pesanan(self, nama_menu, harga):
        pesanan = Pesanan(nama_menu, harga)

        if self.head is None:
            self.head = pesanan
            return

        temp = self.head
        while (temp.next):
            temp = temp.next

        temp.next = pesanan
    
    def print(self):
        if self.head is None:
            print("Daftar Pesanan masih Kosong")
            return
        
        pesanan = self.head
        while pesanan:
            print(f"{pesanan.nama_menu}: {pesanan.harga}")
            pesanan = pesanan.next
    
    def total_pesanan(self):
        total = 0
        
        pesanan = self.head
        while pesanan:
            total += pesanan.harga
            pesanan = pesanan.next
        
        print(f"Total Harga Pesanan: Rp{total}")

daftar_pesanan = DaftarPesanan()

MENU = [
    ["Mixue Ice Cream", 5_000],
    ["Bobaa Shake", 16_000],
    ["mie sundae", 14_000],
    ["mie ganas", 11_000],
    ["creamy mango boba", 22_000]
]

print(
"""
1. Mixue Ice Cream: 5000
2. Bobaa Shake: 16000
3. mie sundae : 14000
4. mie ganas : 11000
5. creamy mango boba : 22000
""")
pesanan = int(input("Silahkan memesan dari menu (input nomer): "))
daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])

while True:
    pesanan = input("Ada lagi? (jika tidak, maka ketik 'exit'): ")
    if pesanan == "exit":
        break

    pesanan = int(pesanan)
    daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])

daftar_pesanan.print()
daftar_pesanan.total_pesanan()
