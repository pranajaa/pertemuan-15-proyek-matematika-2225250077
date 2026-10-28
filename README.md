# Program Rekap dan Analisis Nilai Matematika Kelas

Nama: Hitana Rifa Pranaja

NIM: 2225250077

Kelas: 3A

Kontribusi: mengembangkan program, melakukan pengujian, memperbaiki kesalahan, dan menyusun dokumentasi proyek.

## 1. Deskripsi

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program Python sederhana yang digunakan untuk membantu menghitung dan menganalisis nilai matematika siswa. Pengguna memasukkan jumlah siswa dan nilai masing-masing siswa. Program kemudian menampilkan jumlah siswa, rata-rata nilai, nilai minimum, nilai maksimum, jumlah siswa yang lulus, dan jumlah siswa yang tidak lulus.

## 2. Fitur

- Memasukkan jumlah siswa.
- Memasukkan nilai setiap siswa.
- Menghitung rata-rata nilai siswa.
- Menentukan nilai minimum dan maksimum.
- Menghitung jumlah siswa yang lulus dan tidak lulus.
- Memvalidasi input agar nilai berupa angka dari 0 sampai 100.
- Menangani input yang tidak valid.
- Menangani data kosong pada fungsi analisis.

## 3. Persyaratan

- Python 3.
- Visual Studio Code.
- Terminal untuk menjalankan program.

## 4. Cara Menjalankan

1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder proyek.
3. Jalankan perintah berikut:

   `python main.py`

4. Masukkan jumlah siswa sesuai petunjuk.
5. Masukkan nilai setiap siswa.
6. Periksa hasil analisis yang ditampilkan pada terminal.

Untuk menjalankan pengujian otomatis, gunakan perintah:

`python -m unittest discover -s tests -v`

## 5. Struktur Folder

- `main.py`: menjalankan program dan menerima input dari pengguna.
- `proses.py`: berisi fungsi validasi dan analisis nilai.
- `tests/test_proses.py`: berisi pengujian otomatis fungsi program.
- `tests/test_case.md`: berisi tabel pengujian dan hasil yang dicatat.
- `docs/bug_log.md`: berisi catatan bug, penyebab, perbaikan, dan status.
- `.gitignore`: mengatur file yang tidak perlu dimasukkan ke repositori Git.

## 6. Aturan Kelulusan

Siswa dinyatakan lulus jika memperoleh nilai lebih besar dari atau sama dengan 60. Siswa dengan nilai di bawah 60 dinyatakan tidak lulus. Nilai yang diterima program berada pada rentang 0 sampai 100.

## 7. Test Case

Pengujian mencakup perhitungan rata-rata, penentuan kelulusan, input berupa huruf, nilai di luar rentang, nilai minimum dan maksimum, serta kondisi data kosong.

Rincian input, hasil yang diharapkan, hasil aktual, dan status pengujian dicatat dalam file `tests/test_case.md`. Pengujian otomatis tersedia pada file `tests/test_proses.py`.

## 8. Known Issues

Program saat ini menampilkan hasil analisis melalui terminal dan belum memiliki fitur untuk menyimpan hasil ke file. Fitur penyimpanan tidak termasuk dalam versi program saat ini.

## 9. Referensi dan Bantuan

- Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi Proyek Python di VS Code, Git, dan GitHub.
- Dokumentasi Python: https://docs.python.org/3/
- Bantuan AI digunakan untuk membantu memahami dan menyusun program serta dokumentasinya.
