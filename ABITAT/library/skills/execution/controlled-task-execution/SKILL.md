---
skill_id: AION-EXEC-001
name: "Controlled Task Execution"
version: "1.0.0"
description: "Menjalankan tugas yang telah disetujui secara bertahap dengan batas izin, pencatatan status, dan pemeriksaan hasil."
category: execution
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
  - execution\n  - orchestration\n  - permissions\n  - task-state\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Controlled Task Execution

## Purpose
Melaksanakan tugas berdasarkan rencana yang disetujui, dengan perubahan yang terkontrol, dapat diaudit, dan dapat dihentikan.

## When to Use
Gunakan setelah tugas memiliki instruksi yang cukup, scope jelas, serta persetujuan yang diperlukan sudah tercatat.

## When Not to Use
Jangan gunakan untuk melewati approval, memperluas scope diam-diam, menjalankan perintah destruktif yang tidak disetujui, atau mengklaim keberhasilan tanpa bukti.

## Inputs
Task ID; instruksi dan rencana yang disetujui; acceptance criteria; izin; batas waktu; konteks workspace; status dependensi.

## Expected Outputs
Hasil kerja atau artefak; log langkah; status tugas; daftar perubahan; bukti verifikasi; isu dan kebutuhan approval lanjutan.

## Procedure
1. Muat task, versi rencana, acceptance criteria, izin, dan status approval dari Task Store.
2. Pastikan task tidak dibatalkan, tidak kedaluwarsa, dan seluruh dependensi wajib telah selesai.
3. Periksa apakah tool dan resource yang diperlukan tersedia serta tercakup dalam izin agent.
4. Ambil hanya izin minimum yang diperlukan. Jika izin kurang, hentikan langkah terkait dan minta approval melalui Approval Manager.
5. Catat status RUNNING dan checkpoint sebelum melakukan perubahan yang berdampak.
6. Kerjakan satu unit perubahan pada satu waktu; gunakan transaksi, staging, atau salinan kerja jika tersedia.
7. Setelah setiap unit, periksa hasil langsung dan simpan checkpoint yang dapat dipulihkan.
8. Jika scope berubah, temukan konflik, atau muncul tindakan berisiko baru, hentikan bagian terdampak dan eskalasi kepada CEO.
9. Jalankan acceptance criteria dan serahkan artefak beserta bukti kepada QA/reviewer independen.
10. Ubah status menjadi DONE hanya setelah bukti memadai; jika tidak, gunakan BLOCKED atau FAILED dengan alasan yang jelas.

## Tool Requirements
Task Store, Tool Gateway, Approval Manager, Audit Log, Artifact/File Service, Event Bus.

## Permissions & Safety
Tool hanya boleh dipanggil melalui Tool Gateway. Dilarang menyimpan secret di output/log. Aksi finansial, pembelian, publikasi, penghapusan penting, dan dampak eksternal memerlukan approval eksplisit sesuai policy.

## Failure Handling
Pada timeout atau error, simpan status dan checkpoint. Retry hanya untuk operasi yang aman/idempotent dan sesuai retry policy. Jangan mengulang transaksi non-idempotent tanpa pemeriksaan hasil sebelumnya.

## Verification
Cocokkan perubahan dengan scope dan acceptance criteria; pastikan log, artefak, status, dan bukti tersedia. Status sukses dari tool saja bukan bukti bahwa tujuan tugas tercapai.

## Examples
Agent diberi tugas memperbarui dokumentasi. Agent memeriksa scope, mengubah file di branch kerja, menjalankan pemeriksaan, melampirkan diff dan hasil tes, lalu meminta QA melakukan review.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
