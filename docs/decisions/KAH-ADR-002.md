# KAH-ADR-002: Local-First Architecture Principle

- **Status:** OWNER-CONFIRMED
- **Decision date:** 2026-11-19
- **Decision owner:** Project Owner
- **Scope:** Application, data, configuration, and storage control
- **Related document:** [System Architecture](../architecture/SYSTEM-ARCHITECTURE.md)

## 1. Context

KAME AION HABITAT membutuhkan prinsip pengelolaan sistem yang
mempertahankan kendali Owner atas aplikasi, data, konfigurasi, dan
penyimpanan.

Sistem juga membutuhkan fleksibilitas untuk menggunakan layanan AI
eksternal dan mendukung akses melalui jaringan lokal maupun akses
jarak jauh yang diamankan.

Karena itu, local-first harus dibedakan dari pendekatan offline-only
atau larangan menggunakan layanan cloud.

## 2. Decision

Owner mengonfirmasi **Local-First** sebagai prinsip arsitektur awal
KAME AION HABITAT pada 19 November 2026 melalui persetujuan dalam
percakapan proyek.

Prinsip ini berarti:

- Pengembangan dan pengoperasian awal mengutamakan lingkungan lokal
  yang berada dalam kendali Owner.
- Data utama dan file proyek dikelola melalui penyimpanan yang berada
  dalam kendali sistem.
- Integrasi layanan AI eksternal dapat digunakan melalui AI Gateway
  tanpa memindahkan kendali aplikasi dan kebijakan data kepada provider.
- Akses LAN dan internet jarak jauh tetap didukung dengan autentikasi,
  otorisasi, dan perlindungan komunikasi yang sesuai.
- Local-First bukan berarti offline-only.
- Local-First tidak melarang penggunaan API eksternal atau layanan
  cloud yang disetujui.

## 3. Rationale

Prinsip ini menjaga kendali lokal atas komponen dan data penting,
sekaligus memungkinkan sistem memanfaatkan layanan eksternal ketika
diperlukan dan disetujui.

Prinsip ini juga menjadi pedoman agar integrasi eksternal tidak
mengambil alih kendali atas aplikasi maupun kebijakan data sistem.

## 4. Consequences

### Positive

- Kendali atas aplikasi, konfigurasi, dan penyimpanan utama tetap
  berada pada lingkungan yang dikelola Owner.
- Integrasi AI dapat menggunakan provider eksternal melalui batas
  integrasi yang ditentukan.
- Sistem tetap dapat mendukung akses LAN dan akses jarak jauh yang
  diamankan.
- Prinsip penyimpanan lokal dapat diterapkan tanpa mengharuskan semua
  pemrosesan berlangsung secara offline.

### Trade-offs

- Pengoperasian lokal memerlukan pengelolaan penyimpanan, backup,
  pemulihan, dan keamanan lingkungan sendiri.
- Integrasi eksternal tetap memerlukan evaluasi keamanan, autentikasi,
  otorisasi, dan kebijakan data.
- Akses jarak jauh memerlukan mekanisme perlindungan komunikasi dan
  kontrol akses yang sesuai.

## 5. Constraints and Review

ADR ini menetapkan prinsip kendali lokal, bukan keputusan final
mengenai:

- Provider AI tertentu.
- Teknologi database atau konfigurasi produksinya.
- Mekanisme remote access tertentu.
- Infrastruktur hosting produksi.
- Klasifikasi dan kebijakan retensi seluruh jenis data.

Keputusan teknis tersebut tetap mengikuti status masing-masing dalam
Architecture Decision Register dan memerlukan evaluasi serta
persetujuan yang sesuai.

Perubahan terhadap prinsip Local-First harus memiliki alasan,
analisis dampak, review, dan persetujuan Owner serta dicatat melalui
ADR.

## 6. Confirmation Record

- **Confirmation:** Owner-confirmed.
- **Date:** 19 November 2026.
- **Evidence:** Persetujuan Owner dalam percakapan proyek, sebagaimana
  dirujuk pada Section 3 dan Section 15 dokumen System Architecture.

## 7. Related Decisions

- KAH-ADR-001 — Initial Architecture Style.
- KAH-ADR-009 — Remote Access (OPEN).
- KAH-ADR-010 — Authentication and MFA (OPEN).
- KAH-ADR-014 — Backup, Restore, and Disaster Recovery (OPEN).

## 8. References

- [System Architecture — Section 3](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 8](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 15](../architecture/SYSTEM-ARCHITECTURE.md)
