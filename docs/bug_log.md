# Bug Log

**Nama Proyek:** Program Rekap dan Analisis Nilai Matematika Kelas

| ID Bug | Gejala | Penyebab | Perbaikan | Status |
|---|---|---|---|---|
| BUG-01 | Program error ketika input berupa huruf | Input belum divalidasi | Menambahkan fungsi `validasi_nilai()` dengan penanganan `ValueError` | Closed setelah diuji |
| BUG-02 | Program gagal menghitung rata-rata jika data kosong | Pembagian dengan jumlah data nol | Menambahkan pemeriksaan list kosong pada fungsi `hitung_rata_rata()` | Closed setelah diuji |
| BUG-03 | Nilai di luar rentang diterima | Belum ada pemeriksaan rentang nilai | Membatasi nilai pada rentang 0 sampai 100 | Closed setelah diuji |

## Kesimpulan

Bug ditangani dengan menambahkan validasi input, pemeriksaan data kosong, dan batas nilai. Setelah perbaikan, program diuji kembali untuk memastikan fitur berjalan sesuai kebutuhan.