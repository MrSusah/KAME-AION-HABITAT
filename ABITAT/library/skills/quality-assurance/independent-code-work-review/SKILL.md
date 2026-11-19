---
skill_id: AION-REVIEW-001
name: "Independent Code & Work Review"
version: "1.0.0"
description: "Melakukan review independen terhadap hasil kerja untuk menemukan cacat logika, ketidaksesuaian requirement, regresi, dan masalah maintainability."
category: quality-assurance
status: draft
author:
  type: internal
  id: kame-aion-habitat
source:
  type: internal
  repository: KAME-AION-HABITAT
  original_skill: null
  license: Proprietary
compatibility:
  runtime_min: "0.1.0"
  providers:
    - any
  agents:
    - all
permissions:
  required: []
  optional: []
  approval_required: []
dependencies: []
execution:
  context_budget: 6000
  timeout_seconds: 900
  retry_policy: "No automatic retry for non-idempotent actions; retry only when safe and policy permits."
evaluation:
  required: true
  test_suite: "Manual acceptance checks defined in the Verification section."
tags:
  - review\n  - code-review\n  - quality\n  - independence\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Independent Code & Work Review

## Purpose
Memberi penilaian independen atas deliverable sebelum diterima CEO, dengan fokus pada correctness, scope, maintainability, dan risiko.

## When to Use
Gunakan untuk perubahan kode, dokumen penting, konfigurasi, desain teknis, dan deliverable lintas-agent.

## When Not to Use
Jangan gunakan sebagai pengganti pengujian runtime, audit keamanan khusus, atau persetujuan pengguna untuk tindakan berdampak eksternal.

## Inputs
Requirement; acceptance criteria; artefak/diff; keputusan arsitektur; hasil tes; konteks perubahan.

## Expected Outputs
Review findings terurut berdasarkan severity; lokasi; alasan; saran perbaikan; keputusan review; pertanyaan terbuka.

## Procedure
1. Baca requirement dan acceptance criteria terlebih dahulu, bukan hanya penjelasan pembuat.
2. Periksa diff/artefak secara menyeluruh dan pahami konteks pemanggil serta dependensinya.
3. Telusuri jalur sukses, jalur error, input batas, concurrency, state, dan kompatibilitas.
4. Periksa konsistensi desain, naming, struktur, dokumentasi, observability, dan maintainability.
5. Periksa regresi potensial dan perubahan yang tidak terkait scope.
6. Bandingkan klaim pembuat dengan bukti tes dan implementasi aktual.
7. Catat setiap temuan dengan severity, lokasi spesifik, skenario dampak, dan rekomendasi.
8. Pisahkan blocker, major, minor, dan nit; jangan memenuhi laporan dengan preferensi gaya yang tidak berdampak.
9. Jika tidak ada temuan, nyatakan cakupan review dan batas pemeriksaan; jangan menyatakan bebas bug secara absolut.
10. Serahkan keputusan rekomendasi kepada CEO; pembuat perubahan tidak boleh menyetujui review atas pekerjaannya sendiri.

## Tool Requirements
Repository/File Gateway, diff viewer, test output, architecture docs, issue/task tracker.

## Permissions & Safety
Review hanya artefak yang diizinkan. Jangan mengubah file saat review kecuali ditugaskan terpisah. Redaksi secret dan data sensitif dari laporan.

## Failure Handling
Jika konteks atau diff tidak tersedia, tandai review BLOCKED. Jika perubahan terlalu luas, minta pemecahan menjadi unit yang dapat ditinjau.

## Verification
Pastikan semua temuan memiliki lokasi dan alasan yang jelas. Pastikan reviewer independen dari agent pembuat untuk perubahan penting. Catat batas cakupan.

## Examples
Reviewer menemukan fungsi mengembalikan sukses sebelum transaksi database commit. Laporan menyebut lokasi, skenario race/failure, dan rekomendasi menunggu commit.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
