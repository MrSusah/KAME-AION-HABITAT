# KAH-ADR-001: Initial Architecture Style

- **Status:** OWNER-CONFIRMED
- **Decision date:** 2026-11-19
- **Decision owner:** Project Owner
- **Scope:** Initial system architecture
- **Related document:** [System Architecture](../architecture/SYSTEM-ARCHITECTURE.md)

## 1. Context

KAME AION HABITAT membutuhkan bentuk arsitektur awal yang dapat
dikembangkan dan dioperasikan secara bertahap, dengan batas modul
yang jelas dan overhead infrastruktur yang sesuai dengan kapasitas
lingkungan pengembangan awal.

Arsitektur perlu menjaga pemisahan tanggung jawab antarmodul tanpa
mewajibkan pemisahan deployment menjadi beberapa service sejak awal.

## 2. Decision

Owner mengonfirmasi **Modular Monolith** sebagai gaya arsitektur
awal KAME AION HABITAT pada 19 November 2026 melalui persetujuan
dalam percakapan proyek.

Implikasi baseline:

- Aplikasi utama berjalan sebagai satu deployment backend.
- Backend dibagi menjadi modul internal dengan tanggung jawab yang jelas.
- Setiap modul memiliki antarmuka dan aturan dependensi sendiri.
- Komunikasi antarmodul menggunakan interface internal yang ditentukan.
- Modul tidak boleh mengakses implementasi internal modul lain secara
  bebas.
- Microservices bukan kebutuhan awal.
- Message broker atau container orchestration tidak ditambahkan tanpa
  kebutuhan yang dapat dibuktikan.

## 3. Rationale

Arah ini dipilih sebagai baseline awal karena:

- Lebih sederhana untuk dikembangkan dan dioperasikan.
- Mengurangi overhead jaringan dan infrastruktur.
- Sesuai dengan keterbatasan sumber daya lingkungan pengembangan awal.
- Mempermudah debugging dan pengujian integrasi.
- Memungkinkan batas modul dipertahankan sebelum kebutuhan pemisahan
  deployment benar-benar muncul.

## 4. Consequences

### Positive

- Deployment awal lebih sederhana.
- Komunikasi internal tidak membutuhkan jaringan antarlayanan.
- Batas tanggung jawab modul tetap dapat ditinjau dan diuji.
- Sistem dapat berkembang tanpa langsung menanggung kompleksitas
  operasional microservices.

### Trade-offs

- Modul berjalan dalam satu deployment dan berbagi lingkungan proses.
- Scaling dan deployment independen per modul belum menjadi kemampuan
  bawaan.
- Disiplin interface dan dependency boundary harus dijaga agar
  modularitas tidak hanya menjadi pemisahan folder.

## 5. Constraints and Review

Keputusan ini menetapkan gaya arsitektur awal, bukan persetujuan
terhadap seluruh detail implementasi.

Perubahan menuju microservices, worker terpisah, atau service extraction
harus didasarkan pada kebutuhan concurrency, reliability, deployment,
atau kebutuhan lain yang terbukti.

Perubahan baseline memerlukan alasan, analisis dampak, review, dan
persetujuan Owner. Perubahan keputusan harus dicatat melalui ADR.

## 6. Confirmation Record

- **Confirmation:** Owner-confirmed.
- **Date:** 19 November 2026.
- **Evidence:** Persetujuan Owner dalam percakapan proyek, sebagaimana
  dirujuk pada Section 3 dan Section 15 dokumen System Architecture.

## 7. Related Decisions

- KAH-ADR-002 — Local-First Architecture Principle.
- KAH-ADR-006 — Module Interfaces and Dependency Rules (OPEN).
- KAH-ADR-015 — Worker or Service Extraction (DEFERRED).

## 8. References

- [System Architecture — Section 3](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 9](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 15](../architecture/SYSTEM-ARCHITECTURE.md)
