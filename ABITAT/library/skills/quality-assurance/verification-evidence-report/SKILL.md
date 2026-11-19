---
skill_id: AION-VERIFY-001
name: "Verification & Evidence Report"
version: "1.0.0"
description: "Memverifikasi deliverable terhadap acceptance criteria dan menyusun laporan berbasis bukti, bukan asumsi."
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
  - verification\n  - qa\n  - evidence\n  - acceptance\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Verification & Evidence Report

## Purpose
Menentukan apakah hasil kerja benar-benar memenuhi kriteria penerimaan dan melaporkan gap secara transparan.

## When to Use
Gunakan pada akhir tugas, setelah perubahan penting, sebelum rilis, atau ketika CEO membutuhkan status yang dapat dipercaya.

## When Not to Use
Jangan gunakan untuk menggantikan review keamanan mendalam, mengubah hasil tes, atau menyetujui pekerjaan hanya berdasarkan klaim agent pembuat.

## Inputs
Task plan; acceptance criteria; deliverable; diff; test output; log; lingkungan dan versi yang diuji.

## Expected Outputs
Matriks kriteria vs bukti; status PASS/FAIL/BLOCKED/NOT TESTED; defect; risiko tersisa; rekomendasi keputusan.

## Procedure
1. Ambil acceptance criteria yang telah disetujui; jangan membuat kriteria baru secara diam-diam.
2. Identifikasi artefak dan versi tepat yang akan diperiksa.
3. Rancang pemeriksaan langsung untuk setiap kriteria, termasuk skenario negatif dan batas jika relevan.
4. Jalankan atau amati tes melalui tool yang diizinkan; catat perintah, waktu, lingkungan, dan exit code.
5. Periksa artefak aktual, bukan hanya ringkasan atau klaim pembuat.
6. Petakan setiap kriteria ke bukti yang spesifik dan dapat ditelusuri.
7. Catat defect dengan tingkat dampak, langkah reproduksi, dan bukti.
8. Pisahkan PASS, FAIL, BLOCKED, dan NOT TESTED; jangan mengubah yang tidak diuji menjadi PASS.
9. Periksa apakah ada perubahan di luar scope, regresi, atau risiko yang belum ditangani.
10. Kirim laporan ke CEO; rekomendasikan menerima, memperbaiki, atau menahan rilis.

## Tool Requirements
Test Runner, File/Artifact Gateway, CI output, Audit Log, observability yang diizinkan.

## Permissions & Safety
Jangan mengakses data produksi atau menjalankan tes destruktif tanpa izin. Bukti dapat memuat data sensitif; redaksi secret dan data pribadi sebelum laporan dibagikan.

## Failure Handling
Jika bukti tidak tersedia atau lingkungan tidak dapat direproduksi, tandai BLOCKED/NOT TESTED. Jelaskan batas verifikasi dan jangan memberi persetujuan final.

## Verification
Setiap PASS harus memiliki bukti. Pastikan versi artefak yang diuji sama dengan versi yang diserahkan. Hasil parsial harus diberi label parsial.

## Examples
Kriteria: endpoint mengembalikan 401 untuk token invalid. Bukti: request pengujian, response status 401, log test runner, commit/version yang diuji.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
