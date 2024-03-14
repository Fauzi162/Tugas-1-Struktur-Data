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
