
BATAS_LULUS = 60


def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)


def analisis_nilai(nilai):
    if len(nilai) == 0:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0,
            "tidak_lulus": 0
        }

    return {
        "jumlah": len(nilai),
        "rata_rata": hitung_rata_rata(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "lulus": sum(1 for x in nilai if x >= BATAS_LULUS),
        "tidak_lulus": sum(1 for x in nilai if x < BATAS_LULUS)
    }


def validasi_nilai(data):
    try:
        nilai = float(data)
        if 0 <= nilai <= 100:
            return nilai
        return None
    except ValueError:
        return None