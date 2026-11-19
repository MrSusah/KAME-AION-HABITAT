# KAH-ADR-003: Frontend Technology

- **Status:** OWNER-CONFIRMED
- **Decision date:** 2026-11-19
- **Decision owner:** Project Owner
- **Scope:** Initial web frontend technology
- **Related document:** [System Architecture](../architecture/SYSTEM-ARCHITECTURE.md)

## 1. Context

KAME AION HABITAT membutuhkan antarmuka web untuk AION Office.
Frontend harus mendukung dashboard interaktif, pengelolaan banyak
agent, project dan task workspace, approval queue, administration,
serta representasi Virtual Office 2D.

Product Requirements Baseline juga menetapkan kebutuhan akses dari
komputer, laptop, tablet, dan smartphone.

Repository menyediakan direktori `apps/web` dan `packages/ui`,
tetapi pemeriksaan pada 19 November 2026 belum menemukan implementasi
frontend maupun konfigurasi build di direktori tersebut.

`AGENTS.md` menetapkan React dan TypeScript sebagai arah teknologi
frontend awal.

## 2. Decision

Owner menyetujui **React + TypeScript + Vite** sebagai teknologi
frontend awal KAME AION HABITAT pada 19 November 2026.

Pembagian tanggung jawab:

- React digunakan untuk membangun antarmuka berbasis komponen.
- TypeScript digunakan sebagai bahasa pengembangan frontend.
- Vite digunakan sebagai development server dan build tool.
- `apps/web` menjadi lokasi aplikasi web.
- `packages/ui` menjadi lokasi komponen antarmuka bersama yang
  digunakan lintas bagian aplikasi bila diperlukan.

Frontend berkomunikasi dengan backend melalui antarmuka API yang
ditentukan.

Frontend tidak menjadi batas otorisasi. Semua permission,
approval, dan keputusan keamanan tetap harus diperiksa backend.

Antarmuka harus dirancang responsif untuk target perangkat yang
ditentukan dalam Product Requirements Baseline.

## 3. Rationale

Pilihan ini ditetapkan karena:

- Konsisten dengan arahan teknologi dalam `AGENTS.md`.
- Mendukung kebutuhan antarmuka modular dan interaktif.
- Ekosistem React dan TypeScript menyediakan pilihan library serta
  integrasi yang luas.
- Vite menyediakan workflow development dan build untuk aplikasi web
  tanpa mengharuskan penambahan server-rendering framework sejak awal.
- Sesuai untuk memulai implementasi web-first dengan pemisahan
  komponen aplikasi dan komponen UI bersama.

## 4. Consequences

### Positive

- Teknologi frontend memiliki baseline yang jelas.
- Komponen UI dapat dikembangkan dan digunakan kembali.
- TypeScript mendukung pemeriksaan tipe pada waktu pengembangan.
- Build dan development workflow dapat dikelola melalui Vite.
- Frontend tetap terpisah dari implementasi backend melalui kontrak API.

### Trade-offs

- Struktur komponen dan batas tanggung jawab harus dijaga.
- Pemilihan library tambahan memerlukan evaluasi kebutuhan dan
  kompatibilitas.
- Kualitas rendering dan penggunaan resource tetap harus diuji
  pada perangkat target.
- Integrasi Virtual Office 2D memerlukan evaluasi teknis tersendiri.

## 5. Constraints and Review

ADR ini menetapkan framework, bahasa, dan build tool awal.
ADR ini belum menetapkan:

- Routing library.
- State management library.
- CSS framework atau component library.
- Charting dan data visualization library.
- Virtual Office 2D rendering engine.
- Testing framework dan browser automation tooling.
- Detail API transport, caching, dan realtime update strategy.
- Server-side rendering atau static site generation.

Pemilihan dependensi tambahan harus didasarkan pada kebutuhan
implementasi, kompatibilitas, keamanan, pemeliharaan, dan penggunaan
resource.

Perubahan framework atau build tool utama memerlukan alasan,
analisis dampak, review, persetujuan Owner, dan ADR perubahan.

## 6. Confirmation Record

- **Confirmation:** Owner-confirmed.
- **Date:** 19 November 2026.
- **Evidence:** Persetujuan Owner dalam percakapan proyek setelah
  evaluasi kebutuhan produk dan pemeriksaan struktur frontend
  repository.

## 7. Related Decisions

- KAH-ADR-001 — Initial Architecture Style.
- KAH-ADR-002 — Local-First Architecture Principle.
- KAH-ADR-004 — Backend Technology (PROPOSED).
- KAH-ADR-006 — Module Interfaces and Dependency Rules (OPEN).

## 8. References

- [Product Requirements Baseline](../specifications/PRODUCT-REQUIREMENTS-BASELINE.md)
- [System Architecture — Section 3](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 9](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 14](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 15](../architecture/SYSTEM-ARCHITECTURE.md)
- [AGENTS.md](../../AGENTS.md)