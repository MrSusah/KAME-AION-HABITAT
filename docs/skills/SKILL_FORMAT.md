# KAME AION HABITAT
## SKILL_FORMAT.md

**Document ID:** SKILL-003  
**Version:** 1.0  
**Status:** Draft

## 1. Tujuan
Menetapkan format standar skill yang dapat dibaca manusia dan divalidasi sistem, lintas model/provider.

## 2. Struktur
```text
library/skills/category/skill-name/
  SKILL.md
  references/
  scripts/
  assets/
  tests/
  CHANGELOG.md
  LICENSE
```
`SKILL.md` wajib; direktori lainnya opsional sesuai kebutuhan. Skrip eksternal harus diaudit sebelum dapat dijalankan.

## 3. Metadata YAML
Contoh:
```yaml
---
skill_id: AION-VERIFY-001
name: Verification & Evidence Report
version: 1.0.0
description: Verify work using technical checks and inspectable evidence.
category: quality-assurance
status: draft
author:
  type: aion
  id: aion-quality-team
source:
  type: internal
  repository: null
  original_skill: null
  license: internal
compatibility:
  runtime_min: "0.1.0"
  providers: [any]
  agents: [qa, software-engineer]
permissions:
  required: [workspace.read]
  optional: [terminal.execute]
  approval_required: [workspace.write, external.publish]
dependencies: []
execution:
  context_budget: medium
  timeout_seconds: 1800
  retry_policy: controlled
evaluation:
  required: true
  test_suite: verification-basic
tags: [testing, verification, quality]
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
---
```
Tanggal di atas adalah placeholder. Runtime tetap memvalidasi permission aktual; metadata tidak memberikan hak akses.

## 4. Status
`draft`, `testing`, `approved`, `deprecated`, `disabled`, `rejected`.

## 5. Struktur isi SKILL.md
```markdown
# Nama Skill
## Purpose
## When to Use
## When Not to Use
## Inputs
## Expected Outputs
## Procedure
## Tool Requirements
## Permissions & Safety
## Failure Handling
## Verification
## Examples
## References
```

## 6. Versioning
Gunakan Semantic Versioning `MAJOR.MINOR.PATCH`: MAJOR untuk perubahan tidak kompatibel, MINOR untuk kemampuan baru kompatibel, PATCH untuk perbaikan. Task history harus mencatat versi skill yang dipakai.

## 7. Validasi
Periksa YAML, metadata wajib, ID unik, versi, status, permission yang dikenali, dependensi, file referensi, path traversal, secret tertanam, sumber/lisensi, dan struktur konten.

## 8. Context Management
Instruksi utama ringkas; referensi panjang berada di `references/`; skrip tidak dimuat ke prompt kecuali diperlukan; Loader hanya memuat bagian relevan.

## 9. Acceptance Criteria
- [ ] Metadata valid dan identitas/versi unik.
- [ ] Permission dan dependensi dapat diperiksa.
- [ ] Sumber dapat dilacak.
- [ ] Struktur isi konsisten.
- [ ] Skill dapat dimuat lintas provider sesuai deklarasi.
- [ ] Versi tercatat dalam task history.

**Status:** Standar format; validator belum diimplementasikan.
