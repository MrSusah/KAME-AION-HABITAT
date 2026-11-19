---
skill_id: AION-RECOVERY-001
name: "Task State, Recovery & Cancellation"
version: "1.0.0"
description: "Menjaga status tugas, checkpoint, retry aman, pemulihan setelah gangguan, dan pembatalan yang konsisten."
category: recovery
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
  - recovery\n  - idempotency\n  - checkpoint\n  - cancellation\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Task State, Recovery & Cancellation

## Purpose
Mencegah pekerjaan hilang atau berjalan ganda ketika agent, proses, provider, atau koneksi mengalami gangguan.

## When to Use
Gunakan untuk tugas multi-langkah, operasi yang dapat berlangsung lama, provider failover, timeout, restart, dan permintaan pembatalan.

## When Not to Use
Jangan gunakan untuk mengulang transaksi eksternal yang hasilnya belum diketahui, menghapus jejak audit, atau mengabaikan permintaan cancel.

## Inputs
Task ID; task state; event history; checkpoint; idempotency key; retry policy; approval state; hasil operasi terakhir.

## Expected Outputs
Status tugas yang konsisten; checkpoint; keputusan retry/resume/cancel; rekonsiliasi efek samping; laporan pemulihan.

## Procedure
1. Baca state dan event log terakhir dari penyimpanan otoritatif; jangan mengandalkan memori percakapan saja.
2. Validasi task ID, versi state, lease/owner, checkpoint, dan idempotency key.
3. Jika ada permintaan cancel, tandai cancellation requested dan cegah langkah baru dimulai.
4. Biarkan operasi yang tidak dapat dihentikan mencapai titik aman; hentikan proses yang aman dihentikan sesuai policy.
5. Untuk operasi terakhir yang hasilnya tidak diketahui, lakukan rekonsiliasi melalui status provider atau sistem tujuan sebelum retry.
6. Retry hanya bila operasi idempotent atau idempotency key menjamin tidak terjadi duplikasi.
7. Resume dari checkpoint terakhir yang tervalidasi; jangan mengasumsikan langkah yang tidak tercatat sudah selesai.
8. Jika state rusak atau saling bertentangan, pindahkan ke NEEDS_REVIEW dan eskalasi kepada CEO.
9. Simpan event pemulihan, alasan keputusan, waktu, dan efek samping yang ditemukan.
10. Laporkan status akhir: RESUMED, COMPLETED, CANCELLED, FAILED, atau NEEDS_REVIEW.

## Tool Requirements
Task Store, Event Bus, Audit Log, provider status APIs melalui Tool Gateway, checkpoint/artifact storage.

## Permissions & Safety
Jangan mengulang pembayaran, pengiriman pesan publik, pembelian, penghapusan, atau operasi non-idempotent tanpa rekonsiliasi dan approval yang sesuai. Jangan menghapus state historis.

## Failure Handling
Jika rekonsiliasi tidak mungkin, jangan retry. Tandai NEEDS_REVIEW dan minta intervensi CEO/pengguna. Pertahankan bukti dan checkpoint.

## Verification
Pastikan transisi status valid, tidak ada dua worker aktif tanpa lease, cancellation dihormati, dan setiap retry memiliki alasan serta bukti idempotensi.

## Examples
Provider timeout setelah permintaan pembuatan resource. Agent memeriksa apakah resource sudah tercipta menggunakan operation ID sebelum memutuskan retry.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
