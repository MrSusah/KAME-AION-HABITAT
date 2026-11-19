---
skill_id: AION-SEC-001
name: "Security Review"
version: "1.0.0"
description: "Meninjau perubahan dan rancangan untuk menemukan risiko keamanan, penyalahgunaan izin, kebocoran data, dan kelemahan konfigurasi."
category: security
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
  - security\n  - threat-model\n  - secrets\n  - permissions\ncreated_at: "2026-11-18"
updated_at: "2026-11-18"
---

# Security Review

## Purpose
Mengidentifikasi risiko keamanan sebelum perubahan diterima atau dirilis, lalu memberi rekomendasi mitigasi yang proporsional.

## When to Use
Gunakan untuk autentikasi, otorisasi, secret, file upload, jaringan, integrasi eksternal, tool execution, perubahan dependency, dan rilis.

## When Not to Use
Jangan gunakan untuk melakukan eksploitasi terhadap sistem pihak ketiga, mengakses data tanpa izin, atau mengubah kontrol keamanan tanpa persetujuan.

## Inputs
Scope perubahan; arsitektur; diff; dependency manifest; konfigurasi contoh; permission matrix; threat model; hasil tes.

## Expected Outputs
Temuan dengan severity, bukti, dampak, kemungkinan, rekomendasi, status mitigasi, dan residual risk.

## Procedure
1. Tentukan aset, trust boundary, aktor, entry point, dan data yang diproses.
2. Periksa autentikasi, otorisasi, least privilege, session handling, dan pemisahan tenant/project.
3. Periksa validasi input, output encoding, injection, path traversal, SSRF, CSRF, dan upload handling sesuai konteks.
4. Periksa secret management, logging/redaction, enkripsi, backup, dan retensi data.
5. Periksa tool execution, command injection, sandbox boundary, approval gate, dan auditability.
6. Periksa dependency, lisensi, provenance, versi rentan, serta proses update.
7. Uji hanya pada lingkungan dan target yang diizinkan; utamakan pemeriksaan statis dan tes non-destruktif.
8. Berikan severity berdasarkan dampak dan kemudahan eksploitasi; sertakan bukti yang dapat direproduksi.
9. Rekomendasikan mitigasi, kontrol kompensasi, dan tes regresi.
10. Blokir rekomendasi rilis jika ada temuan kritis/tinggi yang belum ditangani sesuai kebijakan AION; eskalasi ke CEO.

## Tool Requirements
Repository/File Gateway, dependency scanner, static analysis, test runner, configuration inspection, Audit Log.

## Permissions & Safety
Hanya lakukan pengujian pada aset yang dimiliki atau secara eksplisit diizinkan. Jangan menampilkan secret. Jangan melakukan destructive testing atau mengirim payload ke sistem eksternal tanpa approval.

## Failure Handling
Jika bukti tidak cukup, tandai risiko sebagai belum terverifikasi. Jika ditemukan kemungkinan kebocoran aktif atau kompromi, hentikan aktivitas terkait dan eskalasi segera.

## Verification
Setiap temuan harus memiliki lokasi/bukti, dampak, severity, dan rekomendasi. Setelah perbaikan, lakukan retest pada temuan dan catat residual risk.

## Examples
Review endpoint upload: periksa ukuran file, tipe konten, nama file, penyimpanan di luar web root, otorisasi akses, malware scanning bila diperlukan, dan batas request.

## References
- `docs/skills/SKILL_SYSTEM_SPECIFICATION.md`
- `docs/skills/SKILL_FORMAT.md`
- `docs/skills/SKILL_GOVERNANCE.md`
