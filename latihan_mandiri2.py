"""
Latihan 2.1 Buatlah program yang dapat menghitung berat badan yang diperlukan, jika di-
ketahui tinggi badan dan nilai Body Mass Index (BMI) yang diharapkan! Body Mass Index
dihitung dengan cara: BMI = berat
tinggi2 . Perhatikan, berat badan dalam satuan kilogram (kg) dan
tinggi badan dalam satuan meter (m).
"""
tinggi = float(input("masukkan tinggi dalam meter: ")) # input tinggi
bmi = float(input("masukkan bmi: ")) # input bmi
print(f"berat adalah: {bmi * (tinggi ** 2)} kg") # hasil berat badan yang diperlukan dalam kilogram


"""
Latihan 2.2 Buatlah program yang dapat menghitung hasil dari fungsi f (x) = 2x3 + 2x + 15
x , di mana x merupakan bilangan bulat yang dimasukkan oleh pengguna
"""
x = int(input("masukkan bilangan bulat x: ")) # input angka di variable x
print("hasil fungsi f(x):", 2 * (x ** 3) + 2 * x + 15 / x) # hasil proses fungsi


"""
Latihan 2.3 Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlang-
sung selama 5 minggu. Gaji yang diberikan adalah gaji per jam. Total pajak yang harus budi
bayarkan dari penghasilannya selama bekerja adalah 14%. Setelah membayar pajak, budi
menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan
digunakan pada semester baru, dan 1% untuk membeli alat tulis. Setelah membeli baju, ak-
sesoris dan alat tulis, Budi menggunakan 25% dari sisa uangnya untuk disedekahkan. Setiap
Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim, dan sisanya akan
diserahkan ke kaum dhuafa.

Buatlah sebuah program, dengan input:
1. Gaji per jam yang anda inginkan
2. Jumlah jam kerja yang akan dilakukan dalam 1 minggu
Output dari program adalah sebagai berikut :
1. Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak.
2. Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak.
3. Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris.
4. Jumlah uang yang akan Budi habiskan untuk membeli alat tulis.
5. Jumlah uang yang akan Budi sedekahkan.
6. Jumlah uang yang akan diterima anak yatim.
7. Jumlah uang yang akan diterima kaum dhuafa.
"""
gaji_perjam = float(input("gaji per jam budi: ")) # input gaji per jam
minggu_jam = int(input("total jam kerja 1 minggu: ")) # total jam kerja 1 minggu
#=================================================================================

total = gaji_perjam * (5 * minggu_jam) # total gaji budi
print("1:", total)

pajak = 14 / 100
total = total - total * pajak
print("2:", total) # total setelah pajak

persen_baju_aksesoris = 10 / 100
uang_baju_aksesoris = total * persen_baju_aksesoris
print("3:", uang_baju_aksesoris) # uang aksesoris

persen_alat_tulis = 1 / 100
uang_alat_tulis = total * persen_alat_tulis
print("4:", uang_alat_tulis) # uang alat tulis

total = total - uang_baju_aksesoris - uang_alat_tulis
persen_sedekah = 25 / 100
uang_sedekah = total * persen_sedekah
print("5:", uang_sedekah) # uang sedekah

every_money = 1000
persen_yatim = 30 / 100
persen_dhuafa = 1 - persen_yatim
uang_yatim = every_money * persen_yatim # uang yatim per 1000
uang_dhuafa = every_money * persen_dhuafa # uang dhuafa per 1000
print("6:", uang_sedekah / every_money * uang_yatim)
print("7:", uang_sedekah / every_money * uang_dhuafa)