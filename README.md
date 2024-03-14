"""Nama kelompok
1. Fauza Ahmad Zaidan 23091397144
2. Nur Fatehah 23091397160
3. Akhmad Fauzi 23091397162
"""

daftar_pesanan = DaftarPesanan()

MENU = [
    ["Mixue Ice Cream", 5_000],
    ["Boba Shake", 16_000],
    ["Mie Sundae", 14_000],
    ["Mie Ganas", 11_000],
    ["Creamy Mango Boba", 22_000]
]

print(
"""
1. Mixue Ice Cream: 5000
2. Mi gacoan: 10000
3. Boba Shake: 16000
4. Mie Sundae : 14000
5. Mie Ganas : 11000
6. Creamy Mango Boba : 22000
""")
pesanan = int(input("Silahkan memesan dari menu (input nomer): "))
daftar_pesanan.tambahkan_pesanan(MENU[pesanan - 1][0], MENU[pesanan - 1][1])







