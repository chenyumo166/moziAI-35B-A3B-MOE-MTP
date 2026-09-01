---
language:
- id
license: other
tags:
- gguf
- MoE
- financial-llm
- MoziSmartBit
- qwen3.5
- qwen3.6
- ornith
- MoziAI
- tool-calling
- uncensored
- vision
- MTP
library_name: llama-cpp
pipeline_tag: text-generation
---

# MoziAI-35B-V3.8 — Model AI Multimodal Kecil tapi Hebat, Bisa Dijalankan Lokal Secara Gratis

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | Bahasa Indonesia | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**Tanggal Rilis: 2026-09-01** · **Versi: V3.8**

---

## 📑 Daftar Isi

- [1. Ikhtisar Model](#1-ikhtisar-model)
- [2. Fitur Utama](#2-fitur-utama) — Pemikiran Tujuh Dimensi Dinamis / LOOP / MoziSmartBit / Fokus Finansial
- [3. Catatan Upgrade Versi](#3-catatan-upgrade-versi)
- [4. Kemampuan Inti](#4-kemampuan-inti-domain-finansial)
- [5. Spesifikasi Teknis](#5-spesifikasi-teknis)
- [6. Mulai Cepat](#6-mulai-cepat-3-file-100-aktivasi-kemampuan-inferensi-terbaik) — **unduh 3 file**
- [7. Unduh Model](#7-unduh-model)
- [8. Perintah Menjalankan](#8-perintah-menjalankan)
- [9. Parameter Inferensi yang Direkomendasikan](#9-parameter-inferensi-yang-direkomendasikan)
- [10. Perbandingan Format Kuantisasi](#10-perbandingan-format-kuantisasi)
- [11. Akselerasi Decoding Spekulatif](#11-akselerasi-decoding-spekulatif-fitur-penting)
- [12. Rekomendasi Konfigurasi VRAM](#12-rekomendasi-konfigurasi-vram)
- [13. Metode Deployment](#13-metode-deployment)
- [14. Benchmark](#14-benchmark)
- [15. Optimasi Uncensored](#15-optimasi-uncensored)
- [16. Lisensi](#16-lisensi)
- [17. Kontak](#17-kontak)

---

## 1. Ikhtisar Model

MoziAI-35B-V3.8 adalah model AI multimodal open-source yang dapat di-deploy secara lokal, dikembangkan oleh tim Chen Yumo, tokoh influencer keuangan ternama China. Dibangun di atas basis open-source **Ornith-1.5-35B-A3B** (arsitektur Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, lisensi MIT), menggabungkan data finansial yang dikembangkan sendiri + kemampuan domain finansial + kerangka pemikiran tujuh dimensi dinamis + mekanisme iterasi refleksi LOOP agen + karakteristik Uncensored + algoritma kuantisasi hibrida MoziSmartBit.

**💡 Keunggulan Ukuran: hanya 15,9 GB** — model MoE 35 miliar parameter dikompresi menjadi hanya **15,9 GB** melalui kuantisasi cerdas MoziSmartBit yang dikembangkan sendiri (sekitar 30% lebih kecil dari Q4_K_M standar ~22GB). Muat dalam satu paket instalasi, berjalan di GPU konsumen biasa (20GB VRAM+), mengurangi biaya token cloud menjadi **nol**, mewujudkan kebebasan token 7×24 jam dan memastikan privasi serta keamanan data lokal. Dilisensikan untuk penggunaan komersial **gratis** — tanpa hambatan bagi individu dan perusahaan.

---

## 2. Fitur Utama

### 🧠 Kerangka Pemikiran Tujuh Dimensi Dinamis

Kerangka penalaran inti yang dikembangkan sendiri oleh MoziAI. Untuk tugas apa pun, model pertama-tama mengeluarkan penanda **moziAI-Think**, kemudian mengembangkan pemikiran terstruktur secara dinamis berdasarkan kompleksitas tugas:

| Level | Skenario | Tugas Khas | Dimensi yang Dibuka |
| --- | --- | --- | --- |
| **Level 0** | Tanya jawab sederhana | Penjelasan istilah, pencarian fakta, terjemahan, ringkasan | ①Memahami tugas ⑤Kebutuhan sumber daya (jawaban cepat 2 dimensi) |
| **Level 1** | Analisis & diagnosis | Riset pasar, penulisan konten, analisis data, membaca laporan, evaluasi strategi | ①②③⑤⑥ Evaluasi lima dimensi |
| **Level 2** | Pengembangan/strategi kompleks | Pengembangan kode, desain arsitektur, pengembangan strategi kuant, alur kerja multi-langkah, desain sistem | ①②③④⑤⑥⑦ Penalaran mendalam penuh tujuh dimensi |

> Tujuh dimensi: ①Memahami tugas ②Menilai kompleksitas ③Hubungan ketergantungan ④Menilai risiko ⑤Kebutuhan sumber daya ⑥Kriteria penerimaan ⑦Strategi eksekusi

### 🔄 Mekanisme Iterasi LOOP Agen

Tugas kompleks otomatis masuk ke mode iterasi **moziAI-Loop**: **Putaran 1 eksekusi + evaluasi → Putaran 2 penyesuaian + verifikasi**, memastikan output melewati validasi mandiri sebelum memberikan jawaban akhir. Model bekerja seperti insinyur senior: «memecah masalah → mengevaluasi solusi → mengeksekusi → merefleksi → mengoptimalkan», meningkatkan akurasi dan keterlaksanaan tugas kompleks secara signifikan. Tanya jawab dan tugas sederhana otomatis menonaktifkan Loop.

### 📦 Kuantisasi Cerdas MoziSmartBit

Kuantisasi berlapis cerdas yang dikembangkan sendiri: model MoE 35 miliar parameter dikompresi menjadi sekitar **15,9 GB**, sekitar 6,5 GB (~30%) lebih kecil dari Q4_K_M standar (~22 GB), dengan mempertahankan akurasi **~99%** FP16. Kuantisasi tradisional menerapkan presisi seragam ke semua lapisan; MoziSmartBit menggunakan strategi diferensiasi cerdas yang disesuaikan dengan struktur MoE, dengan akurasi lebih baik dari Q4_K_M. Rasio kompresi mencapai **4,5x**.

### 💰 Fokus Domain Finansial Vertikal

Optimasi mendalam untuk tanya jawab finansial, pemrograman kuantitatif, dan pemanggilan alat. Domain finansial memiliki toleransi sangat rendah terhadap halusinasi model, dan MoziAI menunjukkan kinerja jauh lebih baik daripada model umum berukuran sama di domain ini.

### 🛡️ Karakteristik Uncensored

Tanpa batasan penyaringan konten, output bebas, informasi lengkap, privasi lokal. Cocok untuk riset akademis, analisis mendalam, diskusi bebas, dll. (Lihat [Bagian 15](#15-optimasi-uncensored)).

### 🌐 Fitur Lainnya

- **Dukungan multibahasa**: 201 bahasa dan dialek, dengan optimasi khusus untuk bahasa Mandarin
- **Pemrograman umum**: pengembangan full-stack, debugging kode, desain arsitektur, mencakup Python/JS/TS/Go/Rust
- **Penulisan artikel**: penulisan berkualitas tinggi multi-genre seperti laporan riset, artikel analisis, dokumen teknis, konten kreatif
- **Pemahaman visual**: visi multimodal, mendukung pemahaman konten gambar dari screenshot lokal
- **Dukungan multi-framework**: llama.cpp / Ollama / LM Studio / Jan
- **Dukungan multi-Agent**: OpenClaw / Hermes / Cursor / Claude Code / Codex, dengan pemanggilan alat native dan orkestrasi tugas multi-putaran

---

## 3. Catatan Upgrade Versi

Versi V3.8 dilatih ulang menggunakan sistem dataset pelatihan yang dikembangkan sendiri dari generasi yang sama dengan 27B-V3.8 (identitas / pemikiran tujuh dimensi dinamis / iterasi LOOP / domain finansial vertikal), dengan fokus memperkuat mode penalaran «pemikiran tujuh dimensi dinamis + iterasi LOOP» yang dikembangkan sendiri oleh moziAI, membuatnya lebih cerdas mengenali kompleksitas tugas, tingkat penyelesaian tugas kompleks lebih tinggi, meningkatkan kemampuan «berpikir dulu, baru bertindak»; sekaligus melanjutkan karakteristik Uncensored dan optimasi mendalam domain finansial vertikal.

moziAI akan menjaga frekuensi pembaruan versi yang aktif, memastikan mengikuti perkembangan AI masa depan, dan terus melalui teknologi sendiri membuat model AI lokal lebih ringan untuk di-deploy dan semakin mampu.

---

## 4. Kemampuan Inti Domain Finansial

| Bidang Kemampuan | Deskripsi |
| --- | --- |
| Analisis Pasar | Interpretasi ekonomi makro/mikro, analisis pasar A/HK/US/komoditas/kripto dan logikanya |
| Keuangan & Laporan | Interpretasi indikator kunci laporan keuangan, ekstraksi ringkasan riset, bantuan valuasi & proyeksi laba |
| Risiko & Kepatuhan | Penilaian risiko produk, pengingat kepatuhan saran investasi, interpretasi kebijakan regulasi finansial |
| Kuant & Strategi | Desain ide strategi kuantitatif, kuantisasi Pyramid (PEL), logika backtest, konstruksi faktor & pemanggilan alat |
| Pemanggilan Alat | Terhubung ke sumber data pasar real-time, database, pencarian riset finansial |

---

## 5. Spesifikasi Teknis

| Item | Spesifikasi |
| --- | --- |
| Model Dasar | Ornith-1.5-35B-A3B (arsitektur Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, lisensi MIT) |
| Ukuran Parameter | 35 miliar (35B) arsitektur MoE, 256 expert routing + 1 expert bersama, 8 expert aktif per token |
| Metode Kuantisasi | Kuantisasi cerdas MoziSmartBit + format standar GGUF |
| Panjang Konteks | 256K (262.144 token) |
| Ukuran Model | ~15,9 GB |
| VRAM Minimum | **20GB+** dapat di-deploy (offload CPU); **24GB+** konteks panjang lancar; **32GB+** 256K penuh + visi |
| Framework Inferensi | llama.cpp / Ollama / LM Studio / Jan |
| Kecepatan Inferensi | Dengan decoding spekulatif: GPU AMD R9700 hingga **140+ token/s** / AMD MAX+395 CPU iGPU hingga **70+ token/s** |
| Tim Pengembang | Tim Chen Yumo |

---

## 6. Mulai Cepat 3 File 100 Aktivasi Kemampuan Inferensi Terbaik

> ⚠️ **Poin Penting**: Kemampuan inferensi terbaik MoziAI memerlukan **unduh 3 file sekaligus** — model utama, proyektor visi, template chat. Kehilangan salah satu akan mengurangi kemampuan terkait.

### 6.1 Unduh File Model

Unduh **3 file ini** dari HuggingFace / ModelScope ke direktori lokal yang sama (model utama di **root repositori**, proyektor visi di `mmproj/35B/`, template chat di `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Model utama (wajib, 15,9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Proyektor visi (wajib, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Template chat (wajib, berisi instruksi pemikiran + Loop)
```

| File | Ukuran | Kebutuhan | Fungsi |
| --- | --- | --- | --- |
| Model utama `.gguf` | ~15,9 GB | **Wajib** | Bobot model, kemampuan inferensi inti |
| Proyektor visi `mmproj` | ~1 GB | **Wajib** | Pemahaman visual multimodal, tanpa ini kehilangan kemampuan gambar |
| Template chat `.jinja` | Sangat kecil | **Wajib** | Menyuntikkan identitas MoziAI + instruksi pemikiran tujuh dimensi + mekanisme LOOP |

### 6.2 Menjalankan dan Menggunakan

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Buka `http://localhost:8080` di browser untuk memulai percakapan. Parameter lengkap yang direkomendasikan ada di Bagian 9.

---

## 7. Unduh Model

| Platform | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Pengguna LM Studio**: cari `moziAI` di [LM Studio](https://lmstudio.ai) untuk unduh sekali klik, tanpa perlu mengunduh file manual.

> 💡 **Tips unduh**: klik tautan di atas untuk masuk ke repositori HuggingFace, buka tab **"Files and versions"**, unduh model utama dari **root repositori**, lalu unduh proyektor visi dari `mmproj/35B/` dan template chat dari `V3.8/`, pastikan ketiga file berada di direktori yang sama.

---

## 8. Perintah Menjalankan

### Menjalankan Paling Sederhana (dengan 3 file)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Menjalankan Penuh yang Direkomendasikan

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 262144 -ngl 99 -t 28 \
  --batch-size 2048 --ubatch-size 512 \
  --flash-attn auto \
  --cache-type-k q4_0 --cache-type-v q4_0 --kv-unified \
  --poll 0 \
  --reasoning on --reasoning-format deepseek-legacy \
  --spec-default \
  --host 0.0.0.0 --port 8080 \
  --temp 0.6 --top-p 0.95 --top-k 20 --min-p 0.024 \
  --repeat-penalty 1.05 --presence-penalty 0
```

> 💡 Jika VRAM terbatas: turunkan `-c` (misal 131072), atau tambahkan `--fit on` agar llama.cpp menyesuaikan VRAM secara otomatis.

---

## 9. Parameter Inferensi yang Direkomendasikan

Dioptimalkan dari pengujian lokal (AMD Radeon AI PRO R9700 32GB):

| Parameter | Tugas Harian / Menulis | Tugas Kompleks / Coding Lanjutan | Keterangan |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Stabilitas harian; eksplorasi moderat untuk coding kompleks |
| top\_p | 0,95 | 0,95 | Ambang sampling nukleus |
| top\_k | 20 | 20 | Sampling terpotong |
| min\_p | 0,024 | 0,024 | Filter probabilitas minimum |
| repeat\_penalty | 1,05 | 1,05 | Penalti pengulangan |
| presence\_penalty | 0 | 0 | Tanpa penalti kehadiran |
| context\_length | 131072 | 262144 | Harian 128K / Kompleks 256K (default llama.cpp 128K) |
| reasoning | on | on | Aktifkan rantai penalaran (CoT) |
| reasoning\_budget | 400 | 1000 | Anggaran token penalaran (lebih tinggi untuk tugas kompleks) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Output penalaran ke field terpisah |
| **spec-type** | **default** | **default** | **Akselerasi decoding spekulatif (ngram, optimal MoE, lihat Bagian 11)** |
| Cache KV | q4\_0 | q4\_0 | Cache KV terkuantisasi (kv-unified) |

> 💡 **Mode berpikir**: diaktifkan via `--reasoning on` — model menalar secara internal sebelum menjawab. `reasoning_budget` membatasi token berpikir maksimum.

---

## 10. Perbandingan Format Kuantisasi

| Format | Ukuran | Akurasi | Keterangan |
| --- | --- | --- | --- |
| FP16 asli | ~70 GB | 100% | Tanpa loss, butuh GPU profesional |
| **MoziSmartBit (model ini)** | **~15,9 GB** | **~99%** | **Kuantisasi cerdas buatan sendiri, akurasi terbaik per ukuran** |
| Q4_K_M | ~22 GB | ~98% | GGUF standar 4-bit |
| Q5_K_M | ~24,7 GB | ~99% | Akurasi lebih tinggi |
| Q6_K | ~28,5 GB | ~99,5% | Hampir tanpa loss |
| Q8_0 | ~36,9 GB | ~100% | Tanpa loss |

> MoziSmartBit mempertahankan akurasi ~99% sambil mengompresi model MoE 35B menjadi 15,9 GB (rasio kompresi 4,5x), ~30% lebih kecil dari Q4_K_M — ideal untuk deployment lokal di GPU konsumen.

---

## 11. Akselerasi Decoding Spekulatif Fitur Penting

Model ini meningkatkan kecepatan inferensi secara signifikan melalui **Decoding Spekulatif (Speculative Decoding)** — diukur lokal **~1,5-2x lebih cepat** daripada saat dinonaktifkan.

- **Konfigurasi optimal MoE**: llama.cpp merekomendasikan **decoding spekulatif ngram** (`--spec-default`) untuk arsitektur MoE — tercepat dan paling stabil dalam pengujian lokal
- **Tentang \"MTP\" di nama**: \"MTP\" merujuk pada bobot Multi-Token Prediction bawaan model dasar (dipertahankan penuh); dukungan draft MTP llama.cpp untuk MoE terbatas, jadi MoziAI menggunakan skema ngram untuk kecepatan terbaik yang terukur

### Parameter Aktivasi

```bash
--spec-default
```

### Saran Penyesuaian

| Konfigurasi | Skenario |
| --- | --- |
| --spec-default (default) | Direkomendasikan: keseimbangan kecepatan & VRAM |
| Nonaktifkan (hapus parameter) | Skenario VRAM rendah; sedikit lebih lambat |

---

## 12. Rekomendasi Konfigurasi VRAM

Diukur pada build MoziSmartBit (model + visi total ~16,4 GB):

| VRAM | Konfigurasi yang Direkomendasikan | Keterangan |
| --- | --- | --- |
| 20 GB | Konteks 150K, cache KV q4\_0, dukung visi | Model+visi ~16,4 GB, 256K+visi hanya ~19,5 GB VRAM |
| **24 GB** | **256K penuh, cache KV q4\_0, dukungan visi sempurna** | **Konfigurasi yang direkomendasikan**: visi+konteks panjang 256K ~20,4 GB, sisa ~3,6 GB |
| 32 GB+ | 256K penuh, sisa VRAM cukup | Seperti R9700 32GB: visi+konteks panjang 256K, sisa ~10 GB, konfigurasi terkuat |

> 💡 Semakin panjang konteks, semakin banyak VRAM yang digunakan. Saat OOM turunkan `-c` bertahap. Gunakan `--fit on` agar llama.cpp menyesuaikan jumlah lapisan otomatis. Mendukung semua kartu NVIDIA / AMD.

---

## 13. Metode Deployment

### Deployment Ollama

```bash
cat > Modelfile << 'EOF'
FROM ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf
PARAMETER temperature 0.6
PARAMETER top_p 0.95
PARAMETER top_k 20
PARAMETER num_ctx 131072
PARAMETER num_gpu 99
EOF

ollama create moziAI-35B -f Modelfile
ollama run moziAI-35B
```

### LM Studio / Jan

Cari `moziAI` di LM Studio / Jan, pilih versi kuantisasi Q4\_K\_M untuk diunduh (LM Studio default membaca model dari root repositori; untuk versi historis gunakan "tambah dari URL" untuk mengimpor file dari folder versi yang sesuai, misal `V3.7/`).

> 💡 Dukungan Ollama untuk mmproj dan chat\_template terbatas, disarankan menggunakan llama.cpp terlebih dahulu untuk fungsionalitas lengkap.

---

## 14. Benchmark

MoziAI-35B-V3.8 didasarkan pada fine-tuning, distilasi, dan pengembangan sekunder dari base deepreinforce-ai/Ornith-1.5-35B-A3B, dengan domain finansial vertikal sebagai arah optimasi inti. Berikut perbandingan multi-model (kemampuan umum MoziAI sama dengan base Ornith-1.5-35B-A3B; data menggunakan pengukuran versi V3.7, V3.8 dan V3.7 memiliki base dan sistem pelatihan yang sama):

| Benchmark | moziAI-35B-V3.8<br>(model ini) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Tes pemrograman** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Tes penalaran** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Tes agen** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> Domain finansial vertikal MoziAI-35B adalah arah optimasi inti MoziAI, dengan kinerja jauh lebih baik daripada model umum dalam interpretasi laporan keuangan, strategi kuant, kepatuhan manajemen risiko, dan pemanggilan alat agen. Data Gemma-4 / Qwen3.6 adalah hasil evaluasi resmi yang dipublikasikan.

---

## 15. Optimasi Uncensored

Model ini mewarisi karakteristik Uncensored (tanpa sensor) dari base Ornith-1.5-35B-A3B, dengan keunggulan berikut:

| Keunggulan | Deskripsi |
| --- | --- |
| Tanpa batasan penyaringan | Tidak menolak topik apa pun, termasuk konten sensitif dan kontroversial |
| Output bebas | Tidak dibatasi kebijakan keamanan, dapat menghasilkan jenis respons apa pun |
| Informasi lengkap | Menyediakan informasi lengkap tanpa filter, cocok untuk riset dan analisis |
| Privasi lokal | Deployment lokal berarti data sepenuhnya privat, tanpa penyaringan cloud |

**Skenario penggunaan**: riset akademis, analisis mendalam, diskusi bebas, percakapan AI tanpa batas.

**Catatan**: Ini adalah model deployment lokal — output sepenuhnya dikendalikan pengguna; model tidak memikul tanggung jawab moderasi konten.

---

## 16. Lisensi

Model ini menggunakan **lisensi restriktif kustom**:

- ✅ **Diizinkan** — penggunaan komersial gratis, menyalin dan mendistribusikan
- ❌ **Dilarang** — pengembangan lanjutan, penjualan ulang, sub-lisensi
- 📋 **Diwajibkan** — mempertahankan pemberitahuan hak cipta asli, mencantumkan sumber: moziAI-35B

Model disediakan "sebagaimana adanya" tanpa jaminan apa pun. Output model hanya untuk referensi dan tidak merupakan saran investasi. Pengguna menanggung semua risiko.

Lihat file [LICENSE](LICENSE) untuk ketentuan lengkap.

---

## 17. Kontak

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
