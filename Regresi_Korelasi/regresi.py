# import lib yg dibutuhkan
import pandas as pd
import csv
from matplotlib import pyplot as plt


print("Annisa Olga Zerlinda - 152018084")
print("================PREDIKSI HARGA LISTRIK BERDASARKAN LUAS TANAH==================")
# buat datasetnya
with open ('listrik.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["tanah","harga"])
    jumlahdata = int(input("Masukan jumlah data yang akan dimasukan ke dataset : "))
    for i in range(jumlahdata):
        tanah = input("Data ke " + str(i + 1) + " -> Masukan Luas Tanah : ")
        harga = input("Data ke " + str(i + 1) + " -> Masukan Biaya Listrik : ")
        myFile.writerow([tanah, harga])

# baca dataset yang udab dibuat
df = pd.read_csv('listrik.csv')

print("===============================================================================")
print("PERHITUNGAN")

# hitung meannya variabel independent
mean_x = sum(df['tanah']) / float(len(df['tanah']))
mean_tanah = str(mean_x)
print("Rata-rata Luas Tanah : " + mean_tanah)


# hitung meannya variabel dependant
mean_y = sum(df['harga']) / float(len(df['harga']))
mean_harga = str(mean_y)
print("Rata-rata Biaya Listrik : " + mean_harga)

# hitung variance semua data yg ada
def variance(values, mean):
    return sum([(val-mean)**2 for val in values])


# cari covariance dari 2 data kolom
def covariance(x, mean_x, salary , mean_y):
    covariance = 0.0
    for r in range(len(x)):
        covariance = covariance + (x[r] - mean_x) * (salary[r] - mean_y)
    return covariance

# hitung variance buat kolom 1 sama 2 secara terpisah yg diambil dari fungsi variance yg diatas
variance_x, variance_y = variance(df['tanah'], mean_x), variance(df['harga'], mean_y)
variance_tanah = str(variance_x)
print("Variance Luas Tanah : " + variance_tanah)
variance_harga = str(variance_y)
print("Variance Harga Listrik : " + variance_tanah)

# hitung covariance untuk 2 kolong bersamaan yg diambil dari fungsi covariance diatas
covariance_x_y = covariance(df['tanah'], mean_x, df['harga'], mean_y)
covariance_harga_tanah = str(covariance_x_y)
print("Covariance Harga Listrik dan Luas Tanah : " + covariance_harga_tanah)

# hitung values dari parameter a dan b nya, diambil perhitungannya dari covariance dan variance yg udah dibuat diatas
koef = covariance_x_y / variance_x
konst = mean_y - koef * mean_x
a = str(konst)
b = str(koef)
print("Konstanta (a) : " + a)
print("Koefisien (b) : " + b)
print("Persamaan Y = (" + a + ") + (" + b + ") X")
print("===============================================================================")
print("HASIL")
# prediksi menggunakan model
n = int(input("Masukan Luas Tanah (X) yang akan di proses menggunakan Regresi Linier : "))
n_hitung = str(n)
Persamaan = koef * n + konst
# xsebelum =
y = str(Persamaan)
print("Prediksi Y/Harga Listrik jika X["+ n_hitung +"] : " + y)

df.columns = ['x', 'y']
plt.scatter(df['x'],df['y'], color='g', s=100)
plt.xticks(rotation=25)
plt.xlabel('Luas Tanah (m2)')
plt.ylabel('Biaya Listrik (Rp.)')
plt.title('Harga Listrik', fontsize=20)
plt.show()