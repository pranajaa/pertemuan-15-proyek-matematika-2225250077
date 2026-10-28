# Test Case Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat menghitung rata-rata nilai, menentukan kelulusan siswa, mencari nilai minimum dan maksimum, serta menangani input yang tidak valid.

## 2. Tabel Pengujian

| ID | Fitur yang Diuji | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Menghitung rata-rata | 70, 80, 90 | Rata-rata 80.00 | Rata-rata 80.00 | PASS |
| TC02 | Batas kelulusan | 60 | Lulus | Lulus | PASS |
| TC03 | Input berupa huruf | abc | Input ditolak dan diminta ulang | Input ditolak dan diminta ulang | PASS |
| TC04 | Nilai melebihi batas | 110 | Input ditolak dan diminta ulang | Input ditolak dan diminta ulang | PASS |
| TC05 | Nilai minimum dan maksimum | 50, 90 | Minimum 50 dan maksimum 90 | Minimum 50 dan maksimum 90 | PASS |
| TC06 | Data kosong pada fungsi analisis | List kosong | Rata-rata 0 dan jumlah siswa 0 | Rata-rata 0 dan jumlah siswa 0 | PASS |
| TC07 | Nilai minimum yang diperbolehkan | 0 | Nilai diterima, tidak lulus | Nilai diterima, tidak lulus | PASS |
| TC08 | Jumlah siswa tidak valid | 0 | Program menampilkan pesan jumlah harus lebih dari 0 | Program menampilkan pesan jumlah harus lebih dari 0 | PASS |

## 3. Kesimpulan

Pengujian dilakukan terhadap perhitungan rata-rata, batas kelulusan, nilai minimum dan maksimum, validasi input, serta kondisi data kosong. Pengujian juga mencakup nilai minimum yang diperbolehkan dan jumlah siswa yang tidak valid.

Hasil pengujian dicatat berdasarkan hasil aktual saat program dijalankan.