---
language:
- vi
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

# MoziAI-35B-V3.8 — Mô hình AI đa phương thức nhỏ gọn nhưng mạnh mẽ, triển khai cục bộ miễn phí

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | Tiếng Việt | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Türkçe](README.tr.md) | [Polski](README.pl.md)

**Ngày phát hành: 2026-09-01** · **Phiên bản: V3.8**

---

## 📑 Mục lục

- [1. Tổng quan mô hình](#1-tổng-quan-mô-hình)
- [2. Tính năng chính](#2-tính-năng-chính) — Tư duy bảy chiều động / LOOP / MoziSmartBit / Trọng tâm tài chính
- [3. Ghi chú nâng cấp phiên bản](#3-ghi-chú-nâng-cấp-phiên-bản)
- [4. Năng lực cốt lõi](#4-năng-lực-cốt-lõi-lĩnh-vực-tài-chính)
- [5. Thông số kỹ thuật](#5-thông-số-kỹ-thuật)
- [6. Bắt đầu nhanh](#6-bắt-đầu-nhanh-3-tệp-100-kích-hoạt-năng-lực-suy-luận-tốt-nhất) — **tải 3 tệp**
- [7. Tải mô hình](#7-tải-mô-hình)
- [8. Lệnh khởi chạy](#8-lệnh-khởi-chạy)
- [9. Tham số suy luận được khuyến nghị](#9-tham-số-suy-luận-được-khuyến-nghị)
- [10. So sánh định dạng lượng tử hóa](#10-so-sánh-định-dạng-lượng-tử-hóa)
- [11. Tăng tốc giải mã suy đoán](#11-tăng-tốc-giải-mã-suy-đoán-tính-năng-quan-trọng)
- [12. Khuyến nghị cấu hình VRAM](#12-khuyến-nghị-cấu-hình-vram)
- [13. Phương pháp triển khai](#13-phương-pháp-triển-khai)
- [14. Điểm chuẩn](#14-điểm-chuẩn)
- [15. Tối ưu Uncensored](#15-tối-ưu-uncensored)
- [16. Giấy phép](#16-giấy-phép)
- [17. Liên hệ](#17-liên-hệ)

---

## 1. Tổng quan mô hình

MoziAI-35B-V3.8 là mô hình AI đa phương thức mã nguồn mở có thể triển khai cục bộ, được phát triển bởi đội ngũ của Chen Yumo, nhà ảnh hưởng tài chính hàng đầu Trung Quốc. Được xây dựng trên nền tảng mã nguồn mở **Ornith-1.5-35B-A3B** (kiến trúc Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, MoE 35B, giấy phép MIT), kết hợp dữ liệu tài chính tự phát triển + năng lực lĩnh vực tài chính + khung tư duy bảy chiều động + cơ chế lặp phản ánh LOOP của agent + tính năng Uncensored + thuật toán lượng tử hóa lai MoziSmartBit.

**💡 Ưu điểm kích thước: chỉ 15,9 GB** — mô hình MoE 35 tỷ tham số được nén xuống chỉ còn **15,9 GB** nhờ lượng tử hóa thông minh MoziSmartBit tự phát triển (nhỏ hơn khoảng 30% so với Q4_K_M tiêu chuẩn ~22GB). Vừa trong một gói cài đặt, chạy trên GPU tiêu dùng thông thường (20GB VRAM+), giảm chi phí token đám mây về **0**, mang lại tự do token 7×24 giờ và đảm bảo quyền riêng tư cùng bảo mật dữ liệu cục bộ. Được cấp phép sử dụng thương mại **miễn phí** — không rào cản cho cá nhân và doanh nghiệp.

---

## 2. Tính năng chính

### 🧠 Khung tư duy bảy chiều động

Khung suy luận cốt lõi do MoziAI tự phát triển. Với bất kỳ nhiệm vụ nào, mô hình trước tiên xuất ra dấu hiệu **moziAI-Think**, sau đó mở rộng tư duy có cấu trúc một cách động theo độ phức tạp của nhiệm vụ:

| Cấp độ | Tình huống | Nhiệm vụ điển hình | Chiều mở rộng |
| --- | --- | --- | --- |
| **Cấp 0** | Hỏi đáp đơn giản | Giải thích thuật ngữ, tra cứu sự kiện, dịch thuật, tóm tắt | ①Hiểu nhiệm vụ ⑤Nhu cầu tài nguyên (trả lời nhanh 2 chiều) |
| **Cấp 1** | Phân tích & chẩn đoán | Nghiên cứu thị trường, viết nội dung, phân tích dữ liệu, đọc báo cáo, đánh giá chiến lược | ①②③⑤⑥ Đánh giá năm chiều |
| **Cấp 2** | Phát triển/chiến lược phức tạp | Phát triển mã, thiết kế kiến trúc, phát triển chiến lược định lượng, quy trình nhiều bước, thiết kế hệ thống | ①②③④⑤⑥⑦ Suy luận sâu đầy đủ bảy chiều |

> Bảy chiều: ①Hiểu nhiệm vụ ②Đánh giá độ phức tạp ③Mối quan hệ phụ thuộc ④Đánh giá rủi ro ⑤Nhu cầu tài nguyên ⑥Tiêu chí nghiệm thu ⑦Chiến lược thực thi

### 🔄 Cơ chế lặp LOOP của Agent

Nhiệm vụ phức tạp tự động vào chế độ lặp **moziAI-Loop**: **Vòng 1 thực thi + đánh giá → Vòng 2 điều chỉnh + xác minh**, đảm bảo đầu ra trải qua tự kiểm chứng trước khi đưa ra câu trả lời cuối cùng. Mô hình hoạt động như kỹ sư cao cấp: «phân rã vấn đề → đánh giá giải pháp → thực thi → phản ánh → tối ưu hóa», nâng cao đáng kể độ chính xác và khả năng thực thi của nhiệm vụ phức tạp. Hỏi đáp và nhiệm vụ đơn giản tự động tắt Loop.

### 📦 Lượng tử hóa thông minh MoziSmartBit

Lượng tử hóa thông minh phân lớp tự phát triển: mô hình MoE 35 tỷ tham số được nén xuống khoảng **15,9 GB**, nhỏ hơn khoảng 6,5 GB (~30%) so với Q4_K_M tiêu chuẩn (~22 GB), duy trì độ chính xác **~99%** FP16. Lượng tử hóa truyền thống áp dụng độ chính xác đồng nhất cho tất cả các lớp; MoziSmartBit sử dụng chiến lược khác biệt thông minh phù hợp với cấu trúc MoE, có độ chính xác tốt hơn Q4_K_M. Tỷ lệ nén đạt **4,5x**.

### 💰 Trọng tâm lĩnh vực tài chính dọc

Tối ưu sâu cho hỏi đáp tài chính, lập trình định lượng và gọi công cụ. Lĩnh vực tài chính có khả năng chịu đựng rất thấp với ảo giác của mô hình, và MoziAI thể hiện hiệu suất vượt trội so với các mô hình tổng quát cùng kích thước trong lĩnh vực này.

### 🛡️ Tính năng Uncensored

Không giới hạn kiểm duyệt nội dung, đầu ra tự do, thông tin đầy đủ, riêng tư cục bộ. Phù hợp cho nghiên cứu học thuật, phân tích sâu, thảo luận tự do... (xem [Mục 15](#15-tối-ưu-uncensored)).

### 🌐 Tính năng khác

- **Hỗ trợ đa ngôn ngữ**: 201 ngôn ngữ và phương ngữ, tiếng Trung được tối ưu đặc biệt
- **Lập trình tổng quát**: phát triển full-stack, gỡ lỗi mã, thiết kế kiến trúc, bao phủ Python/JS/TS/Go/Rust
- **Viết bài**: viết chất lượng cao đa thể loại như báo cáo nghiên cứu, bài phân tích, tài liệu kỹ thuật, nội dung sáng tạo
- **Hiểu thị giác**: thị giác đa phương thức, hỗ trợ hiểu nội dung ảnh qua ảnh chụp màn hình cục bộ
- **Hỗ trợ đa khung**: llama.cpp / Ollama / LM Studio / Jan
- **Hỗ trợ đa Agent**: OpenClaw / Hermes / Cursor / Claude Code / Codex..., gọi công cụ gốc và điều phối nhiệm vụ nhiều vòng

---

## 3. Ghi chú nâng cấp phiên bản

Phiên bản V3.8 được huấn luyện lại bằng hệ thống tập dữ liệu huấn luyện tự phát triển cùng thế hệ với 27B-V3.8 (nhận dạng / tư duy bảy chiều động / lặp LOOP / lĩnh vực tài chính dọc), tập trung củng cố chế độ suy luận «tư duy bảy chiều động + lặp LOOP» do moziAI tự phát triển, giúp nhận diện độ phức tạp nhiệm vụ thông minh hơn, tỷ lệ hoàn thành nhiệm vụ phức tạp cao hơn, nâng cao khả năng «suy nghĩ trước, hành động sau»; đồng thời tiếp tục tính năng Uncensored và tối ưu sâu lĩnh vực tài chính dọc.

moziAI duy trì tần suất nâng cấp phiên bản tích cực, đảm bảo theo kịp sự phát triển AI tương lai, và không ngừng thông qua công nghệ tự phát triển làm cho mô hình AI cục bộ triển khai nhẹ nhàng hơn, năng lực ngày càng mạnh.

---

## 4. Năng lực cốt lõi lĩnh vực tài chính

| Lĩnh vực năng lực | Mô tả |
| --- | --- |
| Phân tích thị trường | Giải thích kinh tế vĩ mô/vi mô, phân tích thị trường A/HK/US/hàng hóa/tiền mã hóa và logic |
| Tài chính & báo cáo | Giải thích chỉ số chính báo cáo tài chính, trích xuất tóm tắt báo cáo nghiên cứu, hỗ trợ định giá & dự báo lợi nhuận |
| Rủi ro & tuân thủ | Đánh giá rủi ro sản phẩm, nhắc tuân thủ lời khuyên đầu tư, giải thích chính sách quản lý tài chính |
| Định lượng & chiến lược | Thiết kế ý tưởng chiến lược định lượng, lượng tử hóa Pyramid (PEL), logic backtest, xây dựng yếu tố & gọi công cụ |
| Gọi công cụ | Kết nối nguồn dữ liệu thị trường thời gian thực, cơ sở dữ liệu, tìm kiếm báo cáo tài chính |

---

## 5. Thông số kỹ thuật

| Mục | Thông số |
| --- | --- |
| Mô hình nền tảng | Ornith-1.5-35B-A3B (kiến trúc Qwen3.5-35B-A3B / Qwen3.6-35B-A3B, giấy phép MIT) |
| Quy mô tham số | 35 tỷ (35B) kiến trúc MoE, 256 chuyên gia định tuyến + 1 chuyên gia dùng chung, 8 chuyên gia kích hoạt mỗi token |
| Phương thức lượng tử hóa | Lượng tử hóa thông minh MoziSmartBit + định dạng chuẩn GGUF |
| Độ dài ngữ cảnh | 256K (262.144 token) |
| Kích thước mô hình | ~15,9 GB |
| VRAM tối thiểu | **20GB+** triển khai được (offload CPU); **24GB+** ngữ cảnh dài mượt mà; **32GB+** 256K đầy đủ + thị giác |
| Khung suy luận | llama.cpp / Ollama / LM Studio / Jan |
| Tốc độ suy luận | Với giải mã suy đoán: GPU AMD R9700 đạt **140+ token/giây** / AMD MAX+395 CPU iGPU đạt **70+ token/giây** |
| Đội phát triển | Đội ngũ Chen Yumo |

---

## 6. Bắt đầu nhanh 3 tệp 100 kích hoạt năng lực suy luận tốt nhất

> ⚠️ **Lưu ý cốt lõi**: Năng lực suy luận tốt nhất của MoziAI yêu cầu **tải đồng thời 3 tệp** — mô hình chính, máy chiếu thị giác, mẫu trò chuyện. Thiếu bất kỳ tệp nào sẽ mất năng lực tương ứng.

### 6.1 Tải tệp mô hình

Tải **3 tệp này** từ HuggingFace / ModelScope vào cùng thư mục cục bộ (mô hình chính ở **thư mục gốc kho lưu trữ**, máy chiếu thị giác ở `mmproj/35B/`, mẫu trò chuyện ở `V3.8/`):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Mô hình chính (bắt buộc, 15,9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Máy chiếu thị giác (bắt buộc, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Mẫu trò chuyện (bắt buộc, chứa hướng dẫn tư duy+Loop)
```

| Tệp | Kích thước | Tính cần thiết | Chức năng |
| --- | --- | --- | --- |
| Mô hình chính `.gguf` | ~15,9 GB | **Bắt buộc** | Trọng số mô hình, năng lực suy luận cốt lõi |
| Máy chiếu thị giác `mmproj` | ~1 GB | **Bắt buộc** | Hiểu thị giác đa phương thức, không tải sẽ mất khả năng hình ảnh |
| Mẫu trò chuyện `.jinja` | Rất nhỏ | **Bắt buộc** | Tiêm nhận dạng MoziAI + hướng dẫn tư duy bảy chiều + cơ chế LOOP |

### 6.2 Khởi chạy và sử dụng

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Mở `http://localhost:8080` trong trình duyệt để bắt đầu trò chuyện. Tham số đầy đủ khuyến nghị ở Mục 9.

---

## 7. Tải mô hình

| Nền tảng | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **Người dùng LM Studio**: tìm `moziAI` trong [LM Studio](https://lmstudio.ai) để tải một chạm, không cần tải tệp thủ công.

> 💡 **Mẹo tải**: nhấp liên kết trên để vào kho HuggingFace, mở tab **"Files and versions"**, tải mô hình chính từ **thư mục gốc kho lưu trữ**, sau đó tải máy chiếu thị giác từ `mmproj/35B/` và mẫu trò chuyện từ `V3.8/`, đảm bảo ba tệp nằm trong cùng thư mục.

---

## 8. Lệnh khởi chạy

### Khởi chạy tối giản (với 3 tệp)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Khởi chạy đầy đủ khuyến nghị

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

> 💡 Nếu VRAM hạn chế: giảm `-c` (ví dụ 131072) hoặc thêm `--fit on` để llama.cpp tự động điều chỉnh VRAM.

---

## 9. Tham số suy luận được khuyến nghị

Được tối ưu từ thử nghiệm cục bộ (AMD Radeon AI PRO R9700 32GB):

| Tham số | Tác vụ hàng ngày / Viết lách | Tác vụ phức tạp / Lập trình nâng cao | Ghi chú |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Ổn định hàng ngày; khám phá vừa phải cho lập trình phức tạp |
| top\_p | 0,95 | 0,95 | Ngưỡng lấy mẫu hạt nhân |
| top\_k | 20 | 20 | Lấy mẫu cắt ngắn |
| min\_p | 0,024 | 0,024 | Bộ lọc xác suất tối thiểu |
| repeat\_penalty | 1,05 | 1,05 | Phạt lặp lại |
| presence\_penalty | 0 | 0 | Không phạt hiện diện |
| context\_length | 131072 | 262144 | Hằng ngày 128K / Phức tạp 256K (mặc định llama.cpp 128K) |
| reasoning | on | on | Bật chuỗi suy luận (CoT) |
| reasoning\_budget | 400 | 1000 | Ngân sách token suy luận (cao hơn cho tác vụ phức tạp) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Xuất suy luận sang trường riêng |
| **spec-type** | **default** | **default** | **Tăng tốc giải mã suy đoán (ngram, tối ưu MoE, xem Mục 11)** |
| Bộ nhớ đệm KV | q4\_0 | q4\_0 | Bộ nhớ đệm KV lượng tử hóa (kv-unified) |

> 💡 **Chế độ suy nghĩ**: bật qua `--reasoning on` — mô hình suy luận nội bộ trước khi trả lời. `reasoning_budget` giới hạn số token suy nghĩ tối đa.

---

## 10. So sánh định dạng lượng tử hóa

| Định dạng | Kích thước | Độ chính xác | Ghi chú |
| --- | --- | --- | --- |
| FP16 gốc | ~70 GB | 100% | Không mất mát, cần GPU chuyên nghiệp |
| **MoziSmartBit (mô hình này)** | **~15,9 GB** | **~99%** | **Lượng tử hóa thông minh tự phát triển, độ chính xác tốt nhất trên mỗi kích thước** |
| Q4_K_M | ~22 GB | ~98% | GGUF chuẩn 4-bit |
| Q5_K_M | ~24,7 GB | ~99% | Độ chính xác cao hơn |
| Q6_K | ~28,5 GB | ~99,5% | Gần như không mất mát |
| Q8_0 | ~36,9 GB | ~100% | Không mất mát |

> MoziSmartBit giữ ~99% độ chính xác trong khi nén mô hình MoE 35B xuống 15,9 GB (tỷ lệ nén 4,5x), nhỏ hơn ~30% so với Q4_K_M — lý tưởng cho GPU tiêu dùng.

---

## 11. Tăng tốc giải mã suy đoán Tính năng quan trọng

Mô hình này tăng đáng kể tốc độ suy luận nhờ **Giải mã suy đoán (Speculative Decoding)** — đo cục bộ **nhanh hơn ~1,5-2 lần** so với khi tắt.

- **Cấu hình tối ưu MoE**: llama.cpp khuyến nghị **giải mã suy đoán ngram** (`--spec-default`) cho kiến trúc MoE — nhanh nhất và ổn định nhất trong thử nghiệm cục bộ
- **Về \"MTP\" trong tên**: \"MTP\" đề cập đến trọng số Multi-Token Prediction của mô hình nền tảng (được giữ nguyên); hỗ trợ draft MTP của llama.cpp cho MoE còn hạn chế, vì vậy MoziAI dùng sơ đồ ngram để đạt tốc độ đo tốt nhất

### Tham số kích hoạt

```bash
--spec-default
```

### Gợi ý điều chỉnh

| Cấu hình | Tình huống |
| --- | --- |
| --spec-default (mặc định) | Khuyến nghị: cân bằng tốc độ & VRAM |
| Tắt (xóa tham số) | Tình huống VRAM thấp; chậm hơn một chút |

---

## 12. Khuyến nghị cấu hình VRAM

Được đo trên bản dựng MoziSmartBit (mô hình + thị giác tổng ~16,4 GB):

| VRAM | Cấu hình khuyến nghị | Ghi chú |
| --- | --- | --- |
| 20 GB | Ngữ cảnh 150K, bộ nhớ đệm KV q4\_0, hỗ trợ thị giác | Mô hình+thị giác ~16,4 GB, 256K+thị giác chỉ ~19,5 GB VRAM |
| **24 GB** | **256K đầy đủ, bộ nhớ đệm KV q4\_0, hỗ trợ thị giác hoàn hảo** | **Cấu hình khuyến nghị**: thị giác+ngữ cảnh dài 256K ~20,4 GB, dư ~3,6 GB |
| 32 GB+ | 256K đầy đủ, dư VRAM đủ | Như R9700 32GB: thị giác+ngữ cảnh dài 256K, dư ~10 GB, cấu hình mạnh nhất |

> 💡 Ngữ cảnh càng dài, VRAM càng nhiều. Khi OOM giảm `-c` dần. Dùng `--fit on` để llama.cpp tự điều chỉnh số lớp. Hỗ trợ mọi card NVIDIA / AMD.

---

## 13. Phương pháp triển khai

### Triển khai Ollama

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

Tìm `moziAI` trong LM Studio / Jan, chọn phiên bản lượng tử hóa Q4\_K\_M để tải (LM Studio mặc định đọc mô hình từ thư mục gốc kho; với phiên bản lịch sử dùng \"thêm từ URL\" để nhập tệp từ thư mục phiên bản tương ứng, ví dụ `V3.7/`).

> 💡 Hỗ trợ của Ollama cho mmproj và chat\_template còn hạn chế, khuyến nghị ưu tiên llama.cpp để có đầy đủ chức năng.

---

## 14. Điểm chuẩn

MoziAI-35B-V3.8 dựa trên tinh chỉnh, chưng cất và phát triển thứ cấp từ nền tảng deepreinforce-ai/Ornith-1.5-35B-A3B, với lĩnh vực tài chính dọc là hướng tối ưu cốt lõi. Dưới đây là so sánh đa mô hình (năng lực tổng quát của MoziAI giống nền tảng Ornith-1.5-35B-A3B; dữ liệu dùng phép đo phiên bản V3.7, V3.8 và V3.7 cùng nền tảng cùng hệ huấn luyện):

| Điểm chuẩn | moziAI-35B-V3.8<br>(mô hình này) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Kiểm tra lập trình** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Kiểm tra suy luận** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Kiểm tra agent** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> Lĩnh vực tài chính dọc của MoziAI-35B là hướng tối ưu cốt lõi của MoziAI, thể hiện hiệu suất vượt trội so với mô hình tổng quát trong giải thích báo cáo tài chính, chiến lược định lượng, tuân thủ quản lý rủi ro và gọi công cụ agent. Dữ liệu Gemma-4 / Qwen3.6 là kết quả đánh giá chính thức công bố.

---

## 15. Tối ưu Uncensored

Mô hình này kế thừa tính năng Uncensored từ nền tảng Ornith-1.5-35B-A3B, có các ưu điểm sau:

| Ưu điểm | Mô tả |
| --- | --- |
| Không giới hạn kiểm duyệt | Không từ chối bất kỳ chủ đề nào, bao gồm nội dung nhạy cảm, gây tranh cãi |
| Đầu ra tự do | Không bị ràng buộc bởi chính sách an toàn, có thể tạo mọi loại phản hồi |
| Thông tin đầy đủ | Cung cấp thông tin đầy đủ không lọc, phù hợp nghiên cứu và phân tích |
| Riêng tư cục bộ | Triển khai cục bộ nghĩa là dữ liệu hoàn toàn riêng tư, không kiểm duyệt đám mây |

**Tình huống sử dụng**: nghiên cứu học thuật, phân tích sâu, thảo luận tự do, hội thoại AI không giới hạn.

**Lưu ý**: Đây là mô hình triển khai cục bộ — đầu ra hoàn toàn do người dùng kiểm soát; mô hình không chịu trách nhiệm kiểm duyệt nội dung.

---

## 16. Giấy phép

Mô hình này sử dụng **giấy phép hạn chế tùy chỉnh**:

- ✅ **Được phép** — sử dụng thương mại miễn phí, sao chép và phân phối
- ❌ **Bị cấm** — phát triển thêm, bán lại, cấp phép phụ
- 📋 **Yêu cầu** — giữ thông báo bản quyền gốc, ghi nguồn: moziAI-35B

Mô hình được cung cấp \"nguyên trạng\" không kèm bất kỳ bảo hành nào. Đầu ra mô hình chỉ để tham khảo và không cấu thành lời khuyên đầu tư. Người dùng tự chịu mọi rủi ro.

Xem tệp [LICENSE](LICENSE) để biết điều khoản đầy đủ.

---

## 17. Liên hệ

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-mail**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
