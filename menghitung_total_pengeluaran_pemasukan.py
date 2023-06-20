# -*- coding: utf-8 -*-
"""
    Disini kita akan berandai-andai untuk menghitung total pengeluaran dan pemasukan
    yang ada pada list_cast_flow, dimana nilai (+) adalah pemasukan dan nilai (-)
    adalah pengeluaran. Kita akan menggunakan fungsi if-else guna menghitung
    total pengeluaran dan pemasukan.

    Sedikit penjelasan jika bingung dalam nilai (-1) untuk apa, maka dapat aku jawab:
    "Angka (-1) digunakan untuk mengubah nilai total_pengeluaran menjadi positif 
    setelah perhitungan." Lebih jelasnya seperti  ini:

    Pada awalnya, nilai total_pengeluaran diinisialisasi dengan angka 0 dan 
    diperbarui dengan jumlah dana negatif (pengeluaran) dari setiap elemen 
    dalam list_cash_flow menggunakan loop for. 
    
    Namun, nilai total_pengeluaran tersebut masih berupa nilai negatif 
    karena pengeluaran diwakili dengan angka negatif dalam list_cash_flow.
    
    Untuk mendapatkan nilai total_pengeluaran yang positif, kita bisa mengalikannya dengan (-1). 
    Dalam program dibawah ini, operasi (total_pengeluaran *= -1) digunakan untuk mengalikan 
    total_pengeluaran dengan (-1) dan mengubahnya menjadi nilai positif.
    
    Dengan demikian, pada baris (total_pengeluaran *= -1), nilai total_pengeluaran 
    diubah dari negatif menjadi positif sehingga dapat dicetak 
    dengan nilai pengeluaran yang sebenarnya.
"""

list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran)
print(total_pemasukan)
