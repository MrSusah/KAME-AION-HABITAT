# KAME AION HABITAT

## Product Requirements Baseline



**Product:** AION Habitat  

**Interface:** AION Office  

**Slogan:** The Living AI Office  

**Document ID:** KAH-PRD-001  

**Version:** 0.1.0  

**Status:** DRAFT  

**Stage:** 12.1 - Product Requirements Baseline



---



## 1. Product Vision



KAME AION HABITAT adalah platform AI Agent Office yang memungkinkan pengguna mengelola, mengawasi, dan mengarahkan banyak AI agent spesialis melalui satu lingkungan kerja terpadu.



AION Office menjadi antarmuka utama untuk mengelola agent, proyek, task, tools, skills, model AI, memori, aktivitas, dan hasil pekerjaan.



Platform menggunakan prinsip supervised autonomy: agent dapat bekerja secara mandiri dalam batas kewenangan yang diberikan, tetapi tindakan berisiko dan tindakan konsekuensial tetap membutuhkan otorisasi yang sesuai.



## 2. Product Objectives



1. Menyediakan pusat kendali untuk banyak AI agent spesialis.

2. Mengatur pekerjaan melalui task planning, execution, verification, dan recovery.

3. Mengintegrasikan model AI lokal dan penyedia API eksternal.

4. Mengelola tools dan skills melalui sistem terkontrol.

5. Menyediakan dashboard dan virtual office 2D.

6. Menyimpan project state, task history, dan audit events secara persisten.

7. Mendukung akses LAN dan akses jarak jauh melalui internet.

8. Memastikan tindakan agent dapat diawasi, dibatasi, dihentikan, dan diperiksa.



## 3. User Access and Network Requirements



### 3.1 Local Network



AION Office harus dapat diakses dari perangkat yang terhubung ke jaringan lokal yang sama.



Target perangkat:

- Komputer utama.

- Laptop.

- Tablet.

- Smartphone.



### 3.2 Remote Internet Access



AION Office harus dapat diakses dari luar jaringan lokal melalui koneksi internet.



Persyaratan:

- Seluruh akses jarak jauh harus menggunakan koneksi terenkripsi.

- Autentikasi tetap berlaku untuk akses lokal maupun remote.

- Hak akses tidak boleh meningkat hanya karena pengguna berada di LAN.

- Session management dan revocation harus tersedia.

- Akses administratif harus memiliki perlindungan tambahan.

- Akses jaringan tidak boleh memberikan akses langsung ke database.

- Backend internal dan tool execution tidak boleh diekspos langsung ke internet.



### 3.3 Network Security



Desain harus mempertimbangkan:

- TLS untuk koneksi jaringan.

- Authentication dan authorization.

- Session expiration dan revocation.

- Rate limiting.

- Network access policy.

- Secure secret management.

- Audit logging.

- Proteksi terhadap unauthorized access.



**Proposed design direction:** gunakan private network/VPN atau secure tunnel sebagai jalur akses jarak jauh. Reverse proxy dapat menjadi gateway HTTPS. Pemilihan teknologi final menunggu evaluasi arsitektur dan risiko.



## 4. Core Product Modules



### 4.1 AION Office Dashboard

- Ringkasan aktivitas seluruh agent.

- Status sistem dan provider.

- Task yang sedang berjalan.

- Notifikasi dan approval queue.

- Ringkasan penggunaan resource.



### 4.2 Agent Management

- Daftar dan profil agent.

- Role dan spesialisasi.

- Status online, idle, busy, blocked, dan error.

- Konfigurasi model.

- Batas kewenangan.

- Aktivitas dan riwayat pekerjaan.



### 4.3 Task and Project Management

- Project workspace.

- Task planning dan decomposition.

- Task assignment.

- Dependencies.

- Execution monitoring.

- Progress tracking.

- Recovery dan cancellation.

- Task history.



### 4.4 AI Gateway

- Integrasi berbagai penyedia model.

- Dukungan API eksternal.

- Dukungan model lokal.

- Provider selection.

- Model capability registry.

- Timeout dan retry policy.

- Usage tracking.

- Provider failure handling.



### 4.5 Tool Gateway

- Tool registry.

- Tool permission policy.

- Parameter validation.

- Approval checks.

- Execution boundary.

- Tool result recording.



### 4.6 Skill System

- Skill registry.

- Skill loader.

- Skill versioning.

- Skill validation.

- Skill routing.

- Skill evaluation.

- Permission integration.



### 4.7 Memory and Knowledge

- Agent memory.

- Project knowledge.

- Search and retrieval.

- Memory access policy.

- Data provenance.

- Retention policy.



### 4.8 Virtual Office

- Lingkungan kantor 2D.

- Representasi visual agent.

- Ruang kerja dan departemen.

- Status aktivitas agent.

- Visualisasi interaksi dan task.

- Navigasi ke detail agent dan project.



Virtual office adalah representasi antarmuka. Status visual harus berasal dari status Runtime yang sebenarnya dan tidak boleh menjadi sumber kebenaran status sistem.



### 4.9 Administration and Security

- User management.

- Role-based access control.

- Permission management.

- Approval management.

- Emergency Stop.

- Audit event viewer.

- System configuration.

- Security monitoring.



## 5. Supervised Autonomy Requirements



1. Agent hanya boleh menjalankan tindakan dalam batas permission yang diberikan.

2. Skill tidak dapat memberikan permission dengan sendirinya.

3. Tool execution harus melewati pemeriksaan otorisasi Runtime.

4. Tindakan konsekuensial harus memiliki approval yang valid.

5. Tidak adanya respons Owner tidak boleh dianggap sebagai persetujuan.

6. Approval harus terikat pada tindakan, target, scope, dan masa berlaku.

7. Perubahan scope dapat membatalkan approval sebelumnya.

8. Emergency Stop harus dapat menghentikan atau memblokir eksekusi sesuai kemampuan Runtime.

9. Semua tindakan penting harus menghasilkan audit event.

10. Sistem harus mendukung cancellation dan recovery tanpa mengarang status keberhasilan.



## 6. Data and Persistence Requirements



Platform harus memiliki penyimpanan persisten untuk:

- User dan access roles.

- Agent profiles.

- Projects.

- Tasks dan task state.

- Execution records.

- Skills dan versions.

- Tool registry.

- Approval records.

- Audit events.

- Provider configuration.

- Memory dan knowledge references.

- System settings.



Database tidak boleh diakses langsung oleh agent tanpa jalur dan permission yang ditentukan.



## 7. Reliability Requirements



- Task state harus dapat dipulihkan setelah proses terhenti.

- Duplicate external side effects harus ditangani secara aman.

- Kegagalan provider tidak boleh otomatis dianggap sebagai keberhasilan task.

- Partial completion harus direkam secara eksplisit.

- Backup dan restore harus dirancang.

- Log dan audit evidence harus memiliki kebijakan retensi.

- Sistem harus membedakan status task, status QA, dan status approval.



## 8. Resource Requirements



Target deployment awal adalah komputer Windows dengan sumber daya terbatas.



Arsitektur harus:

- Mengutamakan layanan ringan.

- Menghindari container yang tidak diperlukan.

- Mendukung model lokal kecil bila sesuai kapasitas perangkat.

- Memungkinkan penggunaan API eksternal.

- Memiliki batas penggunaan CPU, RAM, dan concurrency.

- Memungkinkan komponen berat dipindahkan ke mesin lain di masa mendatang.



## 9. Initial Architecture Direction



Arah awal yang akan dievaluasi:



- Frontend: React + TypeScript.

- Backend: Python + FastAPI.

- Primary database: PostgreSQL.

- AI integration: Provider-independent AI Gateway.

- Tool execution: Permission-controlled Tool Gateway.

- Initial deployment: Local-first.

- Desktop application: Optional, setelah Web MVP tervalidasi.



Pilihan tersebut merupakan arah awal dari `AGENTS.md`, bukan keputusan implementasi final.



## 10. Acceptance Criteria



Product requirements baseline dapat diajukan untuk persetujuan apabila:



- \[ ] Visi dan tujuan produk jelas.

- \[ ] Cakupan akses LAN dan remote tercakup.

- \[ ] Modul utama teridentifikasi.

- \[ ] Batas supervised autonomy tercatat.

- \[ ] Kebutuhan keamanan jaringan tercatat.

- \[ ] Kebutuhan persistence tercatat.

- \[ ] Kebutuhan recovery dan audit tercatat.

- \[ ] Batasan resource perangkat diperhitungkan.

- \[ ] Persyaratan yang belum diputuskan tercatat secara eksplisit.

- \[ ] Tidak ada klaim bahwa fitur yang belum dibuat sudah berfungsi.



## 11. Open Decisions



Keputusan berikut masih memerlukan desain dan persetujuan:



1. Metode remote access final: VPN, private overlay, secure tunnel, atau kombinasi.

2. Model autentikasi dan MFA.

3. User roles dan delegation model.

4. Database schema dan migration strategy.

5. Agent Runtime lifecycle.

6. Task execution architecture.

7. Memory isolation dan retention.

8. Model provider selection dan fallback.

9. Emergency Stop semantics.

10. Backup, restore, dan disaster recovery.



## 12. Document Governance



Dokumen ini merupakan baseline kebutuhan produk tahap awal.



Status `DRAFT` berarti isinya belum menjadi otorisasi implementasi atau perubahan kebijakan. Setiap keputusan arsitektur penting harus ditinjau, dicatat, dan disetujui sesuai governance KAME AION HABITAT.
