# KAH-ADR-005: Primary Database

- **Status:** OWNER-CONFIRMED
- **Decision date:** 2026-11-19
- **Decision owner:** Project Owner
- **Scope:** Primary relational database technology
- **Related document:** [System Architecture](../architecture/SYSTEM-ARCHITECTURE.md)

## 1. Context

KAME AION HABITAT membutuhkan penyimpanan persisten untuk data terstruktur yang digunakan oleh aplikasi, backend, agent runtime, dan modul internal.

Data tersebut mencakup users, roles, agent profiles, projects, tasks, execution records, skills, tool registry, approvals, audit events, provider metadata, system settings, serta memory metadata dan references.

Data dan operasi tertentu memerlukan integritas relasi, transaksi yang konsisten, serta kontrol akses melalui backend.

Arsitektur menetapkan prinsip Modular Monolith dan Local-First. Database tidak boleh diekspos langsung ke jaringan publik atau diakses langsung oleh browser, agent, maupun integrasi eksternal.

## 2. Decision

Owner menyetujui **PostgreSQL sebagai primary database KAME AION HABITAT** pada 19 November 2026.

Ketentuan arsitektural:

- PostgreSQL menjadi database relasional utama untuk data terstruktur.
- Database digunakan oleh backend Modular Monolith.
- Akses database dilakukan melalui modul atau repository backend yang berwenang.
- Backend bertanggung jawab menerapkan autentikasi, otorisasi, permission, dan pembatasan scope.
- Transaksi dan integritas relasi harus dijaga pada operasi yang memerlukan konsistensi.
- Database tidak boleh diekspos langsung ke internet atau jaringan publik.
- Credential database hanya tersedia bagi komponen backend yang memang memerlukannya.
- Agent, browser client, dan integrasi eksternal tidak memperoleh akses langsung ke database.

## 3. Rationale

PostgreSQL dipilih karena:

- Mendukung data relasional dan integritas referensial.
- Mendukung transaksi untuk operasi yang memerlukan konsistensi.
- Cocok untuk data user, agent, project, task, permission, approval, dan audit.
- Mendukung constraint dan mekanisme query yang diperlukan untuk data terstruktur.
- Sesuai dengan arah teknologi yang telah tercantum dalam AGENTS.md dan System Architecture.
- Dapat digunakan sebagai satu database utama tanpa memerlukan microservices.
- Memungkinkan pengembangan bertahap dengan tetap mempertahankan batas modul backend.

## 4. Consequences

### Positive

- Teknologi database utama memiliki keputusan yang jelas.
- Relasi antarentitas dapat dijaga melalui constraint dan transaksi.
- Penyimpanan data terstruktur memiliki satu sumber utama.
- Backend dapat menerapkan akses data secara konsisten melalui repository atau modul yang berwenang.
- Strategi backup dan restore dapat dirancang berdasarkan satu database relasional utama.

### Trade-offs

- Database memerlukan konfigurasi, pemeliharaan, dan backup yang benar.
- Schema dan migration harus dikelola secara terkontrol.
- Connection pooling dan batas concurrency perlu disesuaikan dengan kapasitas perangkat.
- Backup saja tidak membuktikan bahwa restore berhasil.
- Penggunaan database harus diuji pada perangkat target dengan resource terbatas.

## 5. Constraints and Review

ADR ini menetapkan PostgreSQL sebagai teknologi database utama. ADR ini belum menetapkan:

- Versi PostgreSQL.
- Native installation, WSL deployment, atau metode deployment lainnya.
- ORM atau data access library.
- Database driver.
- Migration framework dan migration policy.
- Schema final dan seluruh relasi tabel.
- Connection pooling configuration.
- Database user, role, dan credential policy secara rinci.
- Backup schedule, retention, dan backup destination.
- Recovery Point Objective (RPO) dan Recovery Time Objective (RTO).
- Production hosting dan remote database topology.
- Monitoring, maintenance, dan upgrade policy.

Pemilihan detail tersebut harus mempertimbangkan keamanan, kompatibilitas, kebutuhan produk, kemudahan pemeliharaan, dan batas CPU/RAM perangkat.

Database hanya boleh diakses melalui backend yang berwenang. Secret tidak boleh dikirim ke browser, respons API, log biasa, atau konteks agent.

Implementasi wajib menguji integritas data, transaksi, backup, dan restore sesuai tahap pengembangan.

Perubahan teknologi database utama memerlukan analisis dampak, review, persetujuan Owner, dan ADR perubahan.

## 6. Confirmation Record

- **Confirmation:** Owner-confirmed.
- **Date:** 19 November 2026.
- **Decision:** PostgreSQL sebagai primary database KAME AION HABITAT.
- **Evidence:** Persetujuan eksplisit Owner dalam percakapan proyek setelah pemeriksaan System Architecture, AGENTS.md, dan Product Requirements Baseline.

## 7. Related Decisions

- KAH-ADR-001 — Initial Architecture Style.
- KAH-ADR-002 — Local-First Architecture Principle.
- KAH-ADR-003 — Frontend Technology.
- KAH-ADR-004 — Backend Technology.
- KAH-ADR-006 — Module Interfaces and Dependency Rules (OPEN).
- KAH-ADR-010 — Authentication and MFA (OPEN).
- KAH-ADR-013 — Audit Event Storage and Protection (OPEN).
- KAH-ADR-014 — Backup, Restore, and Disaster Recovery (OPEN).

## 8. References

- [Product Requirements Baseline](../specifications/PRODUCT-REQUIREMENTS-BASELINE.md)
- [System Architecture — Section 3](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 8](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 9](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 14](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 15](../architecture/SYSTEM-ARCHITECTURE.md)
- [AGENTS.md](../../AGENTS.md)