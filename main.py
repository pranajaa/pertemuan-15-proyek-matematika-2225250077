
from proses import analisis_nilai, validasi_nilai


def main():
    print("=" * 40)
    print("PROGRAM REKAP DAN ANALISIS NILAI")
    print("MATEMATIKA KELAS")
    print("=" * 40)

    nilai_siswa = []

    try:
        jumlah = int(input("Masukkan jumlah siswa: "))
        if jumlah <= 0:
            print("Jumlah siswa harus lebih dari 0.")
            return
    except ValueError:
        print("Jumlah siswa harus berupa bilangan bulat.")
        return

    for i in range(jumlah):
        while True:
            data = input(f"Masukkan nilai siswa ke-{i + 1}: ")
            nilai = validasi_nilai(data)

            if nilai is not None:
                nilai_siswa.append(nilai)
                break

            print("Input tidak valid. Masukkan nilai 0 sampai 100.")

    hasil = analisis_nilai(nilai_siswa)

    print("\n===== HASIL ANALISIS NILAI =====")
    print(f"Jumlah siswa : {hasil['jumlah']}")
    print(f"Rata-rata    : {hasil['rata_rata']:.2f}")
    print(f"Nilai minimum: {hasil['minimum']}")
    print(f"Nilai maksimum: {hasil['maksimum']}")
    print(f"Jumlah lulus : {hasil['lulus']}")
    print(f"Tidak lulus  : {hasil['tidak_lulus']}")


if __name__ == "__main__":
    main()