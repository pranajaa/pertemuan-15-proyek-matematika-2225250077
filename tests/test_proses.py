import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from proses import hitung_rata_rata, analisis_nilai, validasi_nilai

class TestProses(unittest.TestCase):

    def test_rata_rata(self):
        self.assertEqual(hitung_rata_rata([70, 80, 90]), 80)

    def test_data_kosong(self):
        self.assertEqual(hitung_rata_rata([]), 0)

    def test_nilai_lulus(self):
        hasil = analisis_nilai([60])
        self.assertEqual(hasil["lulus"], 1)

    def test_nilai_minimum_maksimum(self):
        hasil = analisis_nilai([50, 90])
        self.assertEqual(hasil["minimum"], 50)
        self.assertEqual(hasil["maksimum"], 90)

    def test_input_huruf(self):
        self.assertIsNone(validasi_nilai("abc"))

    def test_nilai_di_luar_rentang(self):
        self.assertIsNone(validasi_nilai("110"))


if __name__ == "__main__":
    unittest.main()