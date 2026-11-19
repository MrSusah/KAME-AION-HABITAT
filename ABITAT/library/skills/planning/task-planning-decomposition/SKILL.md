---
skill_id: AION-PLAN-001
name: "Task Planning & Decomposition"
version: "1.0.0"
description: "Mengubah instruksi pengguna menjadi rencana kerja terstruktur, dapat dilacak, dan memiliki kriteria penerimaan."
category: planning
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
  - planning\n  - decomposition\n  - estimation\n  - dependencies\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Task Planning & Decomposition

## Purpose
Menyusun rencana yang dapat dieksekusi dari tujuan pengguna, termasuk ruang lingkup, hasil, dependensi, risiko, urutan, dan kriteria selesai.

## When to Use
Gunakan ketika CEO menerima permintaan baru, tujuan masih luas, pekerjaan memiliki beberapa tahap, atau perlu estimasi dan pembagian tugas.

## When Not to Use
Jangan gunakan untuk mengubah keputusan pengguna, memulai tindakan berisiko tanpa persetujuan, atau mengarang fakta dan estimasi yang tidak didukung.

## Inputs
Tujuan pengguna; konteks proyek; batasan; tenggat atau prioritas jika ada; sumber daya dan kemampuan agent yang tersedia.

## Expected Outputs
Rencana dengan tujuan, ruang lingkup, asumsi, deliverables, subtugas, dependensi, penanggung jawab yang disarankan, risiko, checkpoint, serta acceptance criteria.

## Procedure
1. Ringkas tujuan pengguna dan bedakan kebutuhan wajib dari preferensi.
2. Periksa konteks proyek, keputusan terdahulu, file, dan status tugas yang relevan sebelum bertanya ulang.
3. Catat informasi yang belum diketahui. Tanyakan hanya hal yang benar-benar menghalangi rencana atau menimbulkan risiko material.
4. Tentukan ruang lingkup, hasil akhir, batasan, asumsi, dan hal yang secara eksplisit tidak termasuk.
5. Pecah pekerjaan menjadi subtugas yang cukup kecil untuk dikerjakan dan diverifikasi secara mandiri.
6. Susun dependensi dan urutan; tandai pekerjaan yang dapat berjalan paralel tanpa konflik.
7. Tetapkan owner berdasarkan kompetensi, akses, beban kerja, dan izin; jangan memberi akses yang tidak diperlukan.
8. Definisikan acceptance criteria yang dapat diamati atau diuji untuk setiap deliverable.
9. Identifikasi risiko, rencana mitigasi, checkpoint, serta kondisi eskalasi ke CEO atau pengguna.
10. Serahkan rencana untuk persetujuan bila ruang lingkup, biaya, dampak eksternal, atau tindakan berisiko memerlukan approval.

## Tool Requirements
Task Store, Project Context/Knowledge, Agent Registry, Skill Registry. Read-only retrieval diutamakan saat perencanaan.

## Permissions & Safety
Tidak boleh mengubah data atau menjalankan tool eksternal hanya karena rencana menyebutkannya. Asumsi harus diberi label. Keputusan yang mengubah ruang lingkup atau prioritas pengguna harus dieskalasikan.

## Failure Handling
Jika konteks tidak cukup, keluarkan rencana parsial dengan pertanyaan penghambat. Jika dependensi tidak tersedia, tandai blocked dan berikan alternatif. Jangan menyamarkan ketidakpastian sebagai kepastian.

## Verification
Pastikan setiap subtugas memiliki hasil, owner/role, dependensi, dan kriteria selesai. Pastikan seluruh tujuan pengguna tercakup dan tidak ada tindakan approval-required yang dianggap telah disetujui.

## Examples
Permintaan: “Bangun halaman dashboard dengan autentikasi.” Hasil: subtugas desain alur, skema pengguna, API autentikasi, UI, pengujian, review keamanan, dan acceptance criteria untuk setiap bagian.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
