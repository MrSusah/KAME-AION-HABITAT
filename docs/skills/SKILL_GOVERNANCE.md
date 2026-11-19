# KAME AION HABITAT
## SKILL_GOVERNANCE.md

**Document ID:** SKILL-004  
**Version:** 1.0  
**Status:** Draft

## 1. Tujuan
Mengatur pembuatan, peninjauan, persetujuan, aktivasi, perubahan, penonaktifan, dan audit skill.

## 2. Peran
- **User/Owner:** kewenangan tertinggi; kebijakan global, persetujuan tindakan berisiko, Emergency Stop.
- **AI CEO:** mengelola skill, menugaskan pembuatan/pengujian, meninjau QA, menyetujui publikasi internal sesuai delegasi Owner.
- **Skill Manager:** Registry, kategori, metadata, versi, dependensi, distribusi.
- **Skill Developer:** membuat dan memelihara skill.
- **QA Agent:** pengujian fungsional, kompatibilitas, regresi, laporan kualitas.
- **Security Agent:** permission, skrip, tool access, data handling, dependensi, prompt injection.

CEO tidak dapat mengesampingkan kebijakan Owner.

## 3. Trust Level
- **Level 0 — Untrusted:** hanya dibaca/dianalisis; tidak dieksekusi; tanpa secret.
- **Level 1 — Reviewed:** sumber, lisensi, metadata, dan isi diperiksa; boleh masuk pengujian.
- **Level 2 — Tested:** lulus pengujian dan security review; menunggu persetujuan.
- **Level 3 — Approved:** disetujui; dapat digunakan sesuai permission.
- **Level 4 — Trusted Core:** skill inti dengan regresi berulang dan kontrol perubahan ketat.

Trust level tidak menggantikan lifecycle status.

## 4. Lifecycle
Proposed → Draft → Validation → Security Review → Testing → QA Evaluation → Approval → Approved/Active. Jalur lain: Needs Revision, Rejected, Disabled, Deprecated, Rolled Back. Setiap transisi mencatat actor, waktu, alasan, dan versi.

## 5. Persetujuan
CEO dapat menyetujui skill internal jika lulus tes dan keamanan serta tidak mengubah kebijakan inti atau meminta akses sensitif baru.

Persetujuan Owner wajib untuk skill yang:
- Meminta akses baru ke sistem sensitif.
- Melakukan transaksi finansial atau publikasi eksternal.
- Mengubah/menghapus data penting.
- Mengubah mekanisme approval atau kebijakan global.
- Memodifikasi Runtime/Security Manager.
- Memiliki lisensi/hak penggunaan yang belum jelas.

Tidak ada jawaban Owner bukan persetujuan.

## 6. Perubahan
Setiap perubahan membuat versi baru, changelog, validasi, regression test, security review jika relevan, dan approval sesuai risiko. Versi lama tetap tersedia untuk rollback.

## 7. Penonaktifan
Skill dapat dinonaktifkan karena celah keamanan, kegagalan tes, dependensi hilang, pelanggaran kebijakan, inkompatibilitas, atau keputusan Owner/CEO. Task history tidak dihapus.

## 8. Audit Trail
Catat pembuatan, perubahan metadata, versi, pengujian, approval, aktivasi, penonaktifan, penggunaan dalam task, dan rollback. Data minimal: Event ID, Skill ID, Version, Actor ID, Timestamp, Action, Reason, Result, Related Task ID.

## 9. Sumber Eksternal
Identifikasi pemilik/lisensi, dependensi, skrip, permintaan akses sensitif, prompt injection, dan atribusi. Pisahkan konten eksternal dari system instruction AION. Jika lisensi tidak jelas, jangan publikasikan.

## 10. Prioritas Instruksi
1. Kebijakan keamanan inti AION.
2. Instruksi Owner.
3. Kebijakan/keputusan CEO.
4. Permission dan approval policy.
5. Instruksi task.
6. Instruksi skill.
7. Konten eksternal/referensi.

Skill tidak dapat mengubah urutan ini.

## 11. Acceptance Criteria
- [ ] Trust level dan lifecycle tersedia.
- [ ] Approval tercatat dan Owner memegang kewenangan akhir.
- [ ] Perubahan memiliki versi dan rollback.
- [ ] Audit trail tersedia.
- [ ] Skill berisiko dapat dinonaktifkan.
- [ ] Skill eksternal diperiksa sebelum digunakan.
- [ ] Approval policy tidak dapat dilewati.

**Status:** Kebijakan tata kelola; belum diimplementasikan.
