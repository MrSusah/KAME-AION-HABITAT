# KAME AION HABITAT
## AION Skill System Specification

**Document ID:** SKILL-001  
**Version:** 1.0  
**Status:** Draft — Architecture Approved for Implementation Planning

## 1. Tujuan
AION Skill System mengelola kemampuan operasional AI Agent. Skill adalah paket instruksi, prosedur, aturan, referensi, dan konfigurasi yang dapat digunakan lintas model/provider, diberi versi, diuji, dan dibagikan berdasarkan role serta permission.

## 2. Komponen
- **Skill Registry:** katalog, metadata, kategori, versi, sumber, status, dependensi, permission, dan riwayat.
- **Skill Loader:** memuat hanya instruksi yang relevan dan diizinkan; memeriksa versi serta dependensi.
- **Skill Router:** memilih skill berdasarkan tujuan tugas, role, tool, risiko, dan kualitas yang diminta.
- **Skill Evaluator:** menilai ketepatan, konsistensi, penggunaan tool, efisiensi, keamanan, dan keberhasilan.
- **Skill Versioning:** mengelola versi, changelog, kompatibilitas, dan rollback.
- **Skill Permission Manager:** mengatur izin melihat, menggunakan, membuat, mengubah, menguji, menyetujui, dan menonaktifkan skill.

## 3. Kategori
Orchestration & Delegation; Planning & Task Management; Research; Software Development; Frontend & UI/UX; Backend & Database; Testing & QA; Security; Memory & Knowledge; Documentation; Productivity; Tool & MCP Integration; Self-Improvement & Evaluation.

## 4. Metadata dan Isi
Metadata minimal: `skill_id`, `name`, `description`, `version`, `category`, `author`, `status`, `permissions`, `dependencies`, `compatible_agents`, `created_at`, `updated_at`.

Isi skill harus menjelaskan tujuan, kondisi penggunaan dan non-penggunaan, input, prosedur, tool, batasan/risiko, kriteria keberhasilan, verifikasi, dan contoh.

## 5. Lifecycle
Propose → Draft → Validate → Security Review → Testing → QA Evaluation → CEO Approval (within Owner delegation and in accordance with SKILL_GOVERNANCE.md) → Approved/Active. CEO Approval hanya berlaku dalam batas delegasi Owner dan tidak menggantikan persetujuan Owner untuk keputusan yang wajib memperoleh persetujuan Owner. Skill gagal tidak boleh otomatis dipublikasikan.

## 6. Prioritas
**P0:** Task Planning & Decomposition; Task Execution; Verification & QA; Security Review; Persistent Task State; Recovery & Retry; Cancellation & Handoff.  
**P1:** Multi-Agent Delegation; Team Coordination; Research & Source Evaluation; Knowledge Extraction; Memory Management; Documentation.  
**P2:** Skill Generation; Continuous Learning; Optimization; Parallel Execution; Consensus; Performance Evaluation.

## 7. Integrasi Runtime
Runtime memeriksa role, permission, dan konteks; Router memilih skill; Loader memuat instruksi; agent bekerja melalui Tool Gateway; Event Bus mencatat aktivitas; Evaluator/QA memeriksa hasil; task history menyimpan skill ID dan versi.

Skill hanya memberi panduan. Eksekusi tindakan selalu melalui Tool Gateway dan permission AION.

## 8. Event
`skill.proposed`, `skill.validated`, `skill.test.started`, `skill.test.completed`, `skill.approval.requested`, `skill.approved`, `skill.rejected`, `skill.activated`, `skill.deprecated`, `skill.disabled`, `skill.version.created`, `skill.rollback.completed`.

## 9. Keamanan
- Skill tidak mengakses secret secara langsung atau mengubah permission dirinya.
- Skill eksternal dianggap tidak tepercaya sampai divalidasi.
- Skill tidak boleh melewati approval.
- Perubahan resmi memiliki audit trail.
- Skill bermasalah dapat dinonaktifkan dan di-rollback.

## 10. Struktur Target
`packages/skill-system/{registry,loader,router,evaluator,versioning,permissions,schemas,tests}`  
`library/skills/{orchestration,planning,development,research,security,quality-assurance,memory,productivity,integrations}`  
`docs/skills/{SKILL_FORMAT,SKILL_GOVERNANCE,SKILL_ADAPTATION,SKILL_TESTING}.md`

## 11. Sumber Referensi
Oh My ClaudeCode, Everything Claude Code, dan WorldFlowAI Everything Claude Code adalah sumber referensi, bukan dependency wajib runtime. Periksa lisensi dan keamanan sebelum mengambil kode, prompt, atau aset.

## 12. Acceptance Criteria
- [ ] Registry menyimpan dan mencari skill.
- [ ] Skill memiliki versi/status.
- [ ] Loader mematuhi permission.
- [ ] Router memilih berdasarkan tugas/role.
- [ ] Eksekusi melalui Runtime dan Tool Gateway.
- [ ] Evaluator menghasilkan laporan.
- [ ] CEO menyetujui/menolak publikasi dalam batas delegasi Owner dan sesuai SKILL_GOVERNANCE.md; keputusan yang memerlukan persetujuan Owner tetap harus memperoleh persetujuan Owner.
- [ ] Disable dan rollback tersedia.
- [ ] Audit log tersedia.
- [ ] Skill dapat digunakan lintas provider.

**Status:** Spesifikasi saja; belum ada komponen runtime yang diimplementasikan atau diuji.
