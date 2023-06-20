# -*- coding: utf-8 -*-
"""
    Bisa kita asumsikan untuk setiap item akan kita beli 1 semua dengan potongan harga adalah 10%
    jika potongan harga 10% tersebut kita ubah menjadi nilai desimal maka akan di dapat 0.1.
    Sedangkan nilai dari 1.1 digunakan untuk mengalikan jumlah harga yang sudah dihitung sebelumnya
    (setelah diskon) dengan faktor penambahan 10% (1 + 10% = 1.1).
"""

sepatu = { "nama" : "Sepatu Niko", "harga": 150000, "diskon": 30000 }
baju = { "nama" : "Baju Unikloh", "harga": 80000, "diskon": 8000 }
celana = { "nama" : "Celana Lepis", "harga": 200000, "diskon": 60000 }
harga_sepatu = sepatu["harga"] - sepatu["diskon"]
harga_baju = baju["harga"] - baju["diskon"]
harga_celana = celana["harga"] - celana["diskon"]
total_harga = (harga_sepatu + harga_baju + harga_celana) * 1.1
print(total_harga)
