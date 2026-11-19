# KAH-ADR-004: Backend Technology

- **Status:** OWNER-CONFIRMED
- **Decision date:** 2026-11-19
- **Decision owner:** Project Owner
- **Scope:** Initial backend language and API framework
- **Related document:** [System Architecture](../architecture/SYSTEM-ARCHITECTURE.md)

## 1. Context

KAME AION HABITAT membutuhkan backend untuk menjalankan fungsi inti AION Habitat, termasuk pengelolaan user, agent, project, task, AI Gateway, Tool Gateway, permission, approval, audit, dan persistence.

Backend harus mendukung arsitektur Modular Monolith dengan batas modul internal yang jelas. Backend juga harus mendukung integrasi model AI lokal dan penyedia API eksternal melalui AI Gateway.

Product Requirements Baseline menetapkan kebutuhan keamanan, pembatasan resource, serta kemampuan pengembangan dan pemindahan komponen ke mesin lain pada masa mendatang.

Repository menyediakan direktori `apps/api`, tetapi pemeriksaan pada 19 November 2026 belum menemukan implementasi backend di direktori tersebut.

`AGENTS.md` dan System Architecture telah menetapkan Python dan FastAPI sebagai arah teknologi backend awal.

## 2. Decision

Owner menyetujui **Python + FastAPI** sebagai teknologi backend utama KAME AION HABITAT pada 19 November 2026.

Pembagian tanggung jawab:

- Python digunakan sebagai bahasa implementasi backend.
- FastAPI digunakan sebagai framework untuk membangun HTTP API.
- `apps/api` menjadi lokasi aplikasi backend.
- Backend menjadi bagian dari satu deployment Modular Monolith pada tahap awal.
- Modul internal berkomunikasi melalui interface dan dependency rules yang ditetapkan arsitektur.
- Frontend berkomunikasi dengan backend melalui API yang ditentukan.
- Integrasi model AI dilakukan melalui AI Gateway.
- Eksekusi tool dilakukan melalui Tool Gateway dengan kontrol permission dan approval yang sesuai.

Backend merupakan batas otoritatif untuk autentikasi, otorisasi, validasi permission, approval, dan penerapan kebijakan keamanan.

Framework API tidak menggantikan Permission Engine, Approval Engine, Tool Gateway, atau Audit System.

## 3. Rationale

Pilihan ini ditetapkan karena:

- Konsisten dengan arahan teknologi dalam `AGENTS.md` dan System Architecture.
- Python memiliki ekosistem yang relevan untuk integrasi AI, agent runtime, dan pemrosesan data.
- FastAPI mendukung pembangunan API dengan validasi request dan response berbasis type annotations serta Pydantic.
- Mendukung endpoint asynchronous untuk kebutuhan I/O dan integrasi provider.
- Mendukung pemisahan kontrak API dari implementasi frontend.
- Sesuai untuk memulai backend sebagai Modular Monolith tanpa mengharuskan microservices.
- Dapat dikembangkan secara bertahap dengan memperhatikan batas resource perangkat.

## 4. Consequences

### Positive

- Teknologi backend memiliki baseline yang jelas.
- Backend dapat mengelola API untuk frontend dan integrasi internal.
- Ekosistem Python mendukung kebutuhan AI Gateway dan Agent Runtime.
- Validasi data request dan response dapat diterapkan secara konsisten.
- Batas modul dan kontrak API dapat dikembangkan tanpa memisahkan deployment sejak awal.
- Implementasi dapat diuji secara modular.

### Trade-offs

- Penggunaan asynchronous code harus dirancang dan diuji dengan benar.
- Batas concurrency dan penggunaan resource perlu diterapkan.
- Dependency dan lifecycle aplikasi harus dikelola secara konsisten.
- Keamanan tidak boleh hanya bergantung pada framework atau validasi request.
- Performa dan stabilitas harus diuji pada perangkat target.

## 5. Constraints and Review

ADR ini menetapkan bahasa backend dan framework API awal.

ADR ini belum menetapkan:

- Versi Python dan kebijakan runtime environment.
- Dependency manager dan packaging strategy.
- ORM, database driver, atau migration framework.
- Authentication framework dan session strategy.
- Background worker, scheduler, atau message broker.
- Detail API versioning dan WebSocket strategy.
- Deployment server dan reverse proxy.
- Logging, metrics, tracing, dan observability implementation.
- Strategi testing dan integration testing tooling.

Pemilihan dependency tambahan harus mempertimbangkan keamanan, kompatibilitas, pemeliharaan, kebutuhan produk, dan penggunaan resource.

Implementasi harus mempertahankan Modular Monolith, least privilege, validasi input, batas concurrency, dan pemisahan tanggung jawab antarmodul.

Perubahan bahasa atau framework backend utama memerlukan alasan, analisis dampak, review, persetujuan Owner, dan ADR perubahan.

## 6. Confirmation Record

- **Confirmation:** Owner-confirmed.
- **Date:** 19 November 2026.
- **Evidence:** Persetujuan eksplisit Owner dalam percakapan proyek setelah pemeriksaan AGENTS.md, Product Requirements Baseline, System Architecture, dan struktur apps/api.

## 7. Related Decisions

- KAH-ADR-001 — Initial Architecture Style.
- KAH-ADR-002 — Local-First Architecture Principle.
- KAH-ADR-003 — Frontend Technology.
- KAH-ADR-005 — Primary Database (PROPOSED).
- KAH-ADR-006 — Module Interfaces and Dependency Rules (OPEN).
- KAH-ADR-008 — Agent Lifecycle and Concurrency (OPEN).
- KAH-ADR-011 — Permission Engine and Approval Binding (OPEN).

## 8. References

- [Product Requirements Baseline](../specifications/PRODUCT-REQUIREMENTS-BASELINE.md)
- [System Architecture — Section 3](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 9](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 14](../architecture/SYSTEM-ARCHITECTURE.md)
- [System Architecture — Section 15](../architecture/SYSTEM-ARCHITECTURE.md)
- [AGENTS.md](../../AGENTS.md)