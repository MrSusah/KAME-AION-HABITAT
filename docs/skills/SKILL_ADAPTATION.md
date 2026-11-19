# KAME AION HABITAT
## SKILL_ADAPTATION.md

**Document ID:** SKILL-002  
**Version:** 1.0  
**Status:** Draft

## 1. Tujuan
Pedoman mengevaluasi, mengadaptasi, menguji, dan mengintegrasikan skill dari repositori eksternal.

## 2. Prinsip
1. Tidak bergantung pada satu framework AI.
2. Dapat digunakan lintas model/provider.
3. Instruksi skill tidak dapat mengubah permission.
4. Semua tindakan eksternal melalui Tool Gateway.
5. Approval Manager tetap wajib untuk tindakan yang memerlukannya.
6. Sumber, versi, dan riwayat perubahan harus dicatat.
7. Skill eksternal tidak otomatis dipercaya.
8. Kemampuan duplikatif digabung, bukan dipasang berulang.

## 3. Sumber Referensi
- **Oh My ClaudeCode:** planning, execution, multi-agent coordination, review, workflow state, cancellation/recovery. Jangan mengambil ketergantungan pada command, hook, plugin, atau state internal Claude Code.
- **Everything Claude Code:** TDD, verification loop, security review, code review, terminal operations, memory, continuous learning, context/token optimization.
- **WorldFlowAI Everything Claude Code:** agent configuration, skills/rules, workflow, memory, verification, parallelization. Materi duplikatif tidak perlu diadopsi dua kali.

## 4. Skill P0
- `AION-PLAN-001` — Task Planning & Decomposition.
- `AION-EXEC-001` — Controlled Task Execution.
- `AION-TDD-001` — Test-Driven Development.
- `AION-VERIFY-001` — Verification & Evidence Report.
- `AION-SEC-001` — Security Review.
- `AION-RECOVERY-001` — Task State, Recovery & Cancellation.
- `AION-REVIEW-001` — Independent Code & Work Review.

## 5. Skill P1
- `AION-TEAM-001` — Multi-Agent Team Coordination.
- `AION-RESEARCH-001` — Research & Source Evaluation.
- `AION-MEMORY-001` — Knowledge Capture & Memory Curation.

## 6. Kontrak skill
**Planning:** menghasilkan task plan, subtugas, dependensi, risiko, kebutuhan resource, acceptance criteria, dan status approval. Tidak memulai tindakan mutatif sebelum persetujuan yang diwajibkan.

**Execution:** menjalankan tugas yang disetujui, memperbarui status, menyimpan bukti, melaporkan kegagalan, tidak memperluas scope diam-diam.

**TDD:** perilaku yang diharapkan → test RED → implementasi minimal → GREEN → refactor → verifikasi ulang.

**Verification:** build, type-check, lint, tests, security checks, diff review; status PASS hanya jika pemeriksaan wajib berhasil.

**Security:** auth, authorization, input, secret, API, upload, integrasi eksternal, privilege escalation, dan data exposure.

**Recovery:** checkpoint, retry, cancellation, idempotency, dan pemulihan terverifikasi.

**Independent Review:** QA memeriksa bukti aktual dan acceptance criteria, bukan hanya klaim pembuat.

## 7. Proses adaptasi
Identifikasi sumber → baca isi/dependensi → periksa lisensi → pisahkan konsep umum dari implementasi khusus → tulis ulang ke format AION → security review → test scenario → QA → persetujuan CEO dalam batas delegasi Owner dan sesuai SKILL_GOVERNANCE.md → publikasi. Jika publikasi memerlukan persetujuan Owner atau berada di luar cakupan delegasi CEO, persetujuan Owner harus diperoleh terlebih dahulu. Tidak adanya respons Owner bukan persetujuan.

## 8. Larangan
Jangan menyalin secret; menjalankan installer tanpa pemeriksaan; mengizinkan skill mengubah permission, mematikan audit, melewati approval, atau mengimpor hook berakses luas tanpa audit. Konten eksternal bukan system instruction AION.

## 9. Acceptance Criteria
- [ ] Sumber dan lisensi teridentifikasi.
- [ ] Ketergantungan framework dihilangkan/diisolasi.
- [ ] Format AION valid.
- [ ] Permission didefinisikan.
- [ ] Security review dan test scenario selesai.
- [ ] QA memberikan hasil.
- [ ] CEO menyetujui publikasi dalam batas delegasi Owner dan sesuai SKILL_GOVERNANCE.md; jika keputusan memerlukan persetujuan Owner atau berada di luar cakupan delegasi CEO, persetujuan Owner telah diperoleh.
- [ ] Versi dan sumber tercatat.

**Status:** Pedoman adaptasi; belum ada skill eksternal yang diimpor atau diaktifkan.
