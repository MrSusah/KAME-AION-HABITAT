# Pengujian Perilaku Skill AION

## 1. Tujuan

Direktori ini berisi katalog skenario untuk mempersiapkan pengujian perilaku tujuh skill inti AION.

Pengujian ini bertujuan memeriksa apakah instruksi skill menghasilkan perilaku yang sesuai dengan kontrak, batas kewenangan, dan bukti yang diharapkan.

## 2. Struktur Direktori

- `catalog/`: berisi berkas JSON skenario pengujian untuk setiap skill.
- `reports/`: tempat menyimpan laporan hasil simulasi pengujian.
- `test_catalog_integrity.py`: memeriksa kelengkapan dan konsistensi katalog.
- `README.md`: dokumentasi penggunaan pengujian perilaku.

## 3. Daftar Katalog

| Skill ID | Jumlah Kasus |
|---|---:|
| AION-PLAN-001 | 7 |
| AION-EXEC-001 | 10 |
| AION-TDD-001 | 9 |
| AION-VERIFY-001 | 8 |
| AION-SEC-001 | 10 |
| AION-REVIEW-001 | 8 |
| AION-RECOVERY-001 | 10 |
| **Total** | **62** |

## 4. Status Pengujian

Setiap kasus menggunakan salah satu status berikut:

- `NOT_TESTED`: belum diuji.
- `PASS`: pengujian dijalankan dan hasil sesuai harapan.
- `FAIL`: pengujian dijalankan tetapi hasil tidak sesuai harapan.
- `BLOCKED`: pengujian tidak dapat dilanjutkan karena hambatan.
- `SKIPPED`: sengaja tidak dijalankan dengan alasan yang dicatat.
- `FLAKY`: hasil tidak konsisten pada pengulangan.
- `INCONCLUSIVE`: bukti belum cukup untuk menentukan hasil.

Hanya status `PASS` yang dihitung sebagai keberhasilan.

## 5. Menjalankan Pemeriksaan Integritas Katalog

Jalankan perintah berikut dari direktori utama proyek:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s .\packages\skill-system\tests\behavioral -p "test_*.py" -v
```

Pemeriksaan ini memvalidasi keberadaan berkas, metadata, pemetaan skenario, struktur kasus, dan keunikan ID pengujian.

Pemeriksaan integritas katalog **bukan** simulasi perilaku agen.

## 6. Batasan Pengujian

- Seluruh kasus dimulai dengan status `NOT_TESTED`.
- Katalog hanya mendefinisikan skenario dan hasil yang diharapkan.
- Pemeriksaan otomatis saat ini hanya memvalidasi integritas katalog.
- Simulasi perilaku skill harus dilakukan secara terpisah dan hasilnya dicatat sebagai bukti.
- Pengujian ini tidak membuktikan bahwa Runtime, Tool Gateway, Approval Manager, sandbox, atau pengendalian izin telah diimplementasikan.
- Pengujian simulasi tidak boleh diklaim sebagai bukti penegakan keamanan pada runtime.

## 7. Aturan Pelaporan

Setiap simulasi harus mencatat setidaknya:

1. ID kasus pengujian dan skill yang diuji.
2. Versi skill dan tanggal pengujian.
3. Kondisi awal serta masukan pengujian.
4. Perilaku aktual yang diamati.
5. Bukti yang mendukung hasil.
6. Status, temuan, dan alasan jika pengujian tidak dapat diselesaikan.

Jangan mengubah status kasus menjadi `PASS` tanpa pengujian dan bukti yang dapat diperiksa.

## 8. Tahap Berikutnya

Setelah integritas katalog lolos pemeriksaan, tahap berikutnya adalah melakukan simulasi perilaku secara terkendali. Simulasi harus mengikuti batas kewenangan dan persetujuan yang ditetapkan dalam dokumen Governance serta dokumen pengujian.
