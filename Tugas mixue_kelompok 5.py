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

print(
"""
1. Mixue Ice Cream: 7000
2. Mi gacoan: 10000
3. Bobaa Shake: 20000
4. mie sundae : 14000
5. mie ganas : 11000
6. creamy mango boba : 22000
""")
pesanan = int(input("Silahkan memesan dari menu (input nomer): "))
daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])

MENU = [
    ["Mixue Ice Cream", 5_000],
    ["Bobaa Shake", 20_000],
