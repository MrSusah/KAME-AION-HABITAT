---
skill_id: AION-TDD-001
name: "Test-Driven Development"
version: "1.0.0"
description: "Mengembangkan atau memperbaiki kode melalui siklus red-green-refactor dengan tes yang relevan dan perubahan minimal."
category: development
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
  - development\n  - testing\n  - tdd\n  - software-quality\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Test-Driven Development

## Purpose
Mengurangi regresi dan memastikan perilaku kode ditentukan oleh tes yang dapat dijalankan.

## When to Use
Gunakan untuk fitur baru, bug fix, refactor yang mengubah perilaku, atau perubahan pada komponen inti.

## When Not to Use
Jangan gunakan untuk mengarang hasil tes, menonaktifkan tes yang gagal demi membuat pipeline hijau, atau mengubah kontrak tanpa persetujuan.

## Inputs
Issue/requirement; kode terkait; acceptance criteria; test framework; batasan kompatibilitas; lingkungan pengujian.

## Expected Outputs
Tes yang mereproduksi perilaku; implementasi minimal; hasil test/lint/type-check yang benar-benar dijalankan; ringkasan perubahan.

## Procedure
1. Pelajari requirement, arsitektur lokal, konvensi kode, dan tes yang sudah ada sebelum mengedit.
2. Identifikasi perilaku yang diharapkan dan kasus normal, batas, error, serta regresi yang relevan.
3. Tulis atau perbarui tes yang gagal pada implementasi saat ini dan pastikan kegagalannya memang menunjukkan gap yang dimaksud.
4. Jalankan tes terarah dan simpan output sebagai bukti tahap RED.
5. Buat perubahan implementasi sekecil mungkin agar tes yang ditargetkan lulus.
6. Jalankan kembali tes terarah dan simpan bukti tahap GREEN.
7. Refactor hanya jika meningkatkan kejelasan atau struktur tanpa mengubah perilaku; jalankan tes setelah refactor.
8. Jalankan suite terkait, lint, type-check, dan pemeriksaan build sesuai proyek.
9. Periksa diff untuk perubahan tak terkait, secret, dependency baru, dan risiko keamanan.
10. Serahkan perubahan kepada AION-REVIEW-001 dan AION-VERIFY-001 sebelum dinyatakan selesai.

## Tool Requirements
Repository/File Gateway, Terminal Gateway, test runner, lint/type-check/build tools yang diizinkan.

## Permissions & Safety
Jangan menjalankan script tak dikenal atau dependency install tanpa pemeriksaan. Jangan menghapus atau melemahkan tes untuk menutupi kegagalan. Jangan menyentuh secret atau data produksi.

## Failure Handling
Jika tes tidak dapat dijalankan, laporkan penyebab dan bukti. Jika tes flaky, pisahkan ketidakstabilan lingkungan dari bug dan jangan menyatakan lulus. Jika perubahan melampaui scope, hentikan dan minta arahan.

## Verification
Laporan harus menyebut perintah yang dijalankan, exit code, jumlah tes, kegagalan, serta tes yang tidak dijalankan. Jangan mengklaim RED/GREEN bila tahap itu tidak benar-benar dijalankan.

## Examples
Bug: validasi menerima path traversal. Tambahkan tes yang membuktikan input traversal ditolak, jalankan dan amati gagal, perbaiki validasi, lalu jalankan tes sampai lulus.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
