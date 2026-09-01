---
language:
- tr
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

# MoziAI-35B-V3.8 — Küçük ama Güçlü, Yerel Olarak Ücretsiz Dağıtılabilen Çok Modlu AI Modeli

[English](README.en.md) | [简体中文](README.zh.md) | [繁體中文](README.zh-hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Nederlands](README.nl.md) | [Italiano](README.it.md) | [Русский](README.ru.md) | Türkçe | [Español](README.es.md) | [Português](README.pt.md) | [العربية](README.ar.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [Polski](README.pl.md)

**Yayın Tarihi: 2026-09-01** · **Sürüm: V3.8**

---

## 📑 İçindekiler

- [1. Modele Genel Bakış](#1-modele-genel-bakış)
- [2. Temel Özellikler](#2-temel-özellikler) — Dinamik Yedi Boyutlu Düşünme / LOOP / MoziSmartBit / Finans Odağı
- [3. Sürüm Yükseltme Notları](#3-sürüm-yükseltme-notları)
- [4. Temel Yetenekler](#4-finansal-alan-temel-yetenekleri)
- [5. Teknik Özellikler](#5-teknik-özellikler)
- [6. Hızlı Başlangıç](#6-hızlı-başlangıç-3-dosya-100-en-i̇yi-çıkarım-yeteneğini-etkinleştirin) — **3 dosya indirme**
- [7. Model İndirme](#7-model-i̇ndirme)
- [8. Çalıştırma Komutları](#8-çalıştırma-komutları)
- [9. Önerilen Çıkarım Parametreleri](#9-önerilen-çıkarım-parametreleri)
- [10. Kuantizasyon Formatı Karşılaştırması](#10-kuantizasyon-formatı-karşılaştırması)
- [11. Spekülatif Kod Çözme Hızlandırma](#11-spekülatif-kod-çözme-hızlandırma-önemli-özellik)
- [12. VRAM Yapılandırma Önerileri](#12-vram-yapılandırma-önerileri)
- [13. Dağıtım Yöntemleri](#13-dağıtım-yöntemleri)
- [14. Kıyaslamalar](#14-kıyaslamalar)
- [15. Uncensored Optimizasyonu](#15-uncensored-optimizasyonu)
- [16. Lisans](#16-lisans)
- [17. İletişim](#17-i̇letişim)

---

## 1. Modele Genel Bakış

MoziAI-35B-V3.8, Çin'in önde gelen finans fenomeni Chen Yumo'nun ekibi tarafından geliştirilen, yerel olarak dağıtılabilir açık kaynak çok modlu AI büyük modelidir. Açık kaynak taban **Ornith-1.5-35B-A3B** (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B mimarisi, MoE 35B, MIT lisansı) üzerine inşa edilmiş olup, ekibin kendi geliştirdiği finansal veri + finansal alan yetenekleri + dinamik yedi boyutlu düşünme çerçevesi + ajan LOOP yansıtma ve yineleme mekanizması + Uncensored özelliği + MoziSmartBit hibrit kuantizasyon algoritmasını birleştirir.

**💡 Boyut Avantajı: yalnızca 15,9 GB** — 35 milyar parametreli MoE modeli, kendi geliştirilen MoziSmartBit kuantizasyonuyla yalnızca **15,9 GB**'a sıkıştırılmıştır (standart Q4_K_M ~22GB'dan yaklaşık %30 daha küçük). Tek bir kurulum paketine sığar, sıradan tüketici GPU'larında (20GB VRAM+) çalışır, bulut token maliyetlerini **sıfıra** indirir, 7×24 saat token özgürlüğü sağlar ve yerel veri gizliliği ile güvenliğini garanti eder. **Ücretsiz ticari kullanım** için lisanslıdır — bireyler ve işletmeler için sıfır engel.

---

## 2. Temel Özellikler

### 🧠 Dinamik Yedi Boyutlu Düşünme Çerçevesi

MoziAI'nin kendi geliştirdiği temel akıl yürütme çerçevesi. Herhangi bir görevde model önce **moziAI-Think** işaretini çıkarır, ardından görev karmaşıklığına göre yapılandırılmış düşünmeyi dinamik olarak genişletir:

| Seviye | Senaryo | Tipik Görevler | Genişletilen Boyutlar |
| --- | --- | --- | --- |
| **Seviye 0** | Basit soru-cevap | Terim açıklama, bilgi arama, çeviri, özetleme | ①Görevi anlama ⑤Kaynak ihtiyaçları (iki boyutlu hızlı yanıt) |
| **Seviye 1** | Analiz ve teşhis | Pazar araştırması, metin yazarlığı, veri analizi, rapor okuma, strateji değerlendirme | ①②③⑤⑥ Beş boyutlu değerlendirme |
| **Seviye 2** | Karmaşık geliştirme/strateji | Kod geliştirme, mimari tasarım, kant strateji geliştirme, çok adımlı iş akışları, sistem tasarımı | ①②③④⑤⑥⑦ Tam yedi boyutlu derin akıl yürütme |

> Yedi boyut: ①Görevi anlama ②Karmaşıklık değerlendirmesi ③Bağımlılıklar ④Risk değerlendirmesi ⑤Kaynak ihtiyaçları ⑥Kabul kriterleri ⑦Yürütme stratejisi

### 🔄 Ajan LOOP Yineleme Mekanizması

Karmaşık görevler otomatik olarak **moziAI-Loop** yineleme moduna girer: **1. Tur yürütme + değerlendirme → 2. Tur ayarlama + doğrulama**, nihai yanıt verilmeden önce çıktının öz doğrulamadan geçmesini sağlar. Model kıdemli bir mühendis gibi çalışır: «sorunu parçala → çözümü değerlendir → yürüt → yansıt → optimize et», karmaşık görevlerin doğruluğunu ve uygulanabilirliğini önemli ölçüde artırır. Basit soru-cevap ve görevlerde Loop otomatik kapanır.

### 📦 MoziSmartBit Akıllı Kuantizasyon

Kendi geliştirilen katmanlı akıllı kuantizasyon: 35 milyar parametreli MoE modeli yaklaşık **15,9 GB**'a sıkıştırılır, standart Q4_K_M'den (~22 GB) yaklaşık 6,5 GB (~%30) daha küçüktür ve FP16 **~%99** doğruluğunu korur. Geleneksel kuantizasyon tüm katmanlara tek tip hassasiyet uygular; MoziSmartBit, MoE yapısına uygun akıllı farklılaştırma stratejisi kullanır ve Q4_K_M'den daha iyi doğruluk sağlar. Sıkıştırma oranı **4,5x**.

### 💰 Finansal Dikey Alan Odağı

Finansal soru-cevap, kantitatif programlama ve araç çağrısı için derin optimizasyon. Finans alanı model halüsinasyonlarına karşı son derece düşük toleransa sahiptir ve MoziAI bu alanda aynı boyuttaki genel modellerden belirgin şekilde daha iyi performans gösterir.

### 🛡️ Uncensored Özelliği

İçerik denetim kısıtlaması yok, serbest çıktı, eksiksiz bilgi, yerel gizlilik. Akademik araştırma, derin analiz, özgür tartışma gibi senaryolar için uygundur (bkz. [Bölüm 15](#15-uncensored-optimizasyonu)).

### 🌐 Diğer Özellikler

- **Çok dilli destek**: 201 dil ve lehçe, Çince yetenekleri özel olarak optimize edilmiş
- **Genel programlama**: full-stack geliştirme, kod hata ayıklama, mimari tasarım, Python/JS/TS/Go/Rust kapsar
- **Makale yazımı**: araştırma raporları, analiz makaleleri, teknik belgeler, yaratıcı içerik gibi çok türde yüksek kaliteli yazım
- **Görsel anlama**: çok modlu görüş, yerel ekran görüntüsü ile görüntü içeriğini anlama
- **Çoklu çerçeve desteği**: llama.cpp / Ollama / LM Studio / Jan
- **Çoklu Ajan desteği**: OpenClaw / Hermes / Cursor / Claude Code / Codex vb., yerel araç çağrısı ve çok turlu görev orkestrasyonu

---

## 3. Sürüm Yükseltme Notları

V3.8 sürümü, 27B-V3.8 ile aynı nesil kendi geliştirilen eğitim veri seti sistemiyle yeniden eğitilmiştir (kimlik / dinamik yedi boyutlu düşünme / LOOP yineleme / finansal dikey alan), moziAI'nin kendi geliştirdiği «dinamik yedi boyutlu düşünme + LOOP yineleme» akıl yürütme modunu güçlendirmeye odaklanır, görev karmaşıklığını daha akıllı tanır, karmaşık görev tamamlama oranı yükselir ve «önce düşün, sonra yap» yeteneği gelişir; ayrıca Uncensored özelliği ve finansal dikey alan derin optimizasyonu sürdürülür.

moziAI, gelecekteki yapay zeka gelişimini takip etmek için aktif sürüm yükseltme sıklığını korur ve kendi teknolojileriyle yerel AI modellerini daha hafif dağıtılabilir ve giderek daha yetenekli hale getirir.

---

## 4. Finansal Alan Temel Yetenekleri

| Yetenek Alanı | Açıklama |
| --- | --- |
| Pazar Analizi | Makro/mikro ekonomik yorum, A/HK/ABD/hisse senedi/emtia/kripto piyasa ve mantık analizi |
| Finans ve Raporlar | Finansal rapor temel göstergeleri yorumlama, araştırma raporu özet çıkarma, değerleme ve kazanç tahmini desteği |
| Risk ve Uyum | Ürün risk değerlendirmesi, yatırım tavsiyesi uyum hatırlatmaları, finansal düzenleme politikaları yorumlama |
| Kant ve Strateji | Kantitatif strateji fikir tasarımı, Pyramid (PEL) kuantizasyonu, geri test mantığı, faktör oluşturma ve araç çağrısı |
| Araç Çağrısı | Gerçek zamanlı piyasa verileri, veritabanları, araştırma raporu arama gibi finansal veri kaynaklarına bağlanma |

---

## 5. Teknik Özellikler

| Öğe | Özellik |
| --- | --- |
| Taban Model | Ornith-1.5-35B-A3B (Qwen3.5-35B-A3B / Qwen3.6-35B-A3B mimarisi, MIT lisansı) |
| Parametre Boyutu | 35 milyar (35B) MoE mimarisi, 256 yönlendirme uzmanı + 1 paylaşımlı uzman, token başına 8 uzman aktif |
| Kuantizasyon Yöntemi | Kendi geliştirilen MoziSmartBit akıllı kuantizasyon + GGUF standart formatı |
| Bağlam Uzunluğu | 256K (262.144 token) |
| Model Boyutu | ~15,9 GB |
| Minimum VRAM | **20GB+** dağıtılabilir (CPU offload); **24GB+** akıcı uzun bağlam; **32GB+** tam 256K + görüş |
| Çıkarım Çerçeveleri | llama.cpp / Ollama / LM Studio / Jan |
| Çıkarım Hızı | Spekülatif kod çözme ile: AMD R9700 GPU **140+ token/sn** / AMD MAX+395 CPU iGPU **70+ token/sn** |
| Geliştirme Ekibi | Chen Yumo Ekibi |

---

## 6. Hızlı Başlangıç 3 Dosya 100 En İyi Çıkarım Yeteneğini Etkinleştirin

> ⚠️ **Temel Not**: MoziAI'nin en iyi çıkarım yeteneği için **3 dosyayı birlikte indirmeniz** gerekir — ana model, görüş projektörü, sohbet şablonu. Herhangi birinin eksik olması ilgili yeteneği kaybettirir.

### 6.1 Model Dosyalarını İndirme

HuggingFace / ModelScope'tan **bu 3 dosyayı** aynı yerel dizine indirin (ana model **depo kökünde**, görüş projektörü `mmproj/35B/` içinde, sohbet şablonu `V3.8/` içinde):

```
moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf  ← Ana model (zorunlu, 15,9 GB)
moziAI-35B-mmproj-BF16-V1.0.gguf                        ← Görüş projektörü (zorunlu, ~1 GB)
moziAI-V3.8-35B-chat-template.jinja                                        ← Sohbet şablonu (zorunlu, düşünme+Loop talimatları içerir)
```

| Dosya | Boyut | Gereklilik | İşlev |
| --- | --- | --- | --- |
| Ana model `.gguf` | ~15,9 GB | **Zorunlu** | Model ağırlıkları, temel çıkarım yeteneği |
| Görüş projektörü `mmproj` | ~1 GB | **Zorunlu** | Çok modlu görsel anlama, yüklenmezse görüntü yeteneği kaybolur |
| Sohbet şablonu `.jinja` | Çok küçük | **Zorunlu** | MoziAI kimliği + yedi boyutlu düşünme + LOOP mekanizma talimatlarını enjekte eder |

### 6.2 Başlatma ve Kullanım

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

Tarayıcıda `http://localhost:8080` adresini açarak sohbete başlayın. Tam önerilen parametreler Bölüm 9'da.

---

## 7. Model İndirme

| Platform | URL |
| --- | --- |
| HuggingFace | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://huggingface.co/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| ModelScope | [chenyumo/moziAI-35B-A3B-MOE-MTP](https://modelscope.cn/models/chenyumo/moziAI-35B-A3B-MOE-MTP) |
| GitHub | [chenyumo166/moziAI-35B](https://github.com/chenyumo166/moziAI-35B-A3B-MOE-MTP) |
| Ollama | `ollama pull chenyumo/moziAI-35B-A3B` |

> 💡 **LM Studio kullanıcıları**: [LM Studio](https://lmstudio.ai)'da `moziAI` arayarak tek tıkla indirin, dosyaları manuel indirmenize gerek yok.

> 💡 **İndirme ipucu**: yukarıdaki bağlantıya tıklayıp HuggingFace deposuna girin, **"Files and versions"** sekmesini açın, ana modeli **depo kökünden** indirin, ardından görüş projektörünü `mmproj/35B/` ve sohbet şablonunu `V3.8/` klasöründen indirin, üç dosyanın aynı dizinde olduğundan emin olun.

---

## 8. Çalıştırma Komutları

### En Basit Başlatma (3 dosya ile)

```bash
llama-server \
  -m ./moziAI-35B-V3.8-MOE-MTP-Q4_K_M-Uncensored-Qwen3.6-35B-A3B-Ornith-1.5.gguf \
  --mmproj mmproj/35B/moziAI-35B-mmproj-BF16-V1.0.gguf \
  --chat-template-file V3.8/moziAI-V3.8-35B-chat-template.jinja \
  -c 131072 -ngl 99 \
  --host 0.0.0.0 --port 8080
```

### Tam Önerilen Başlatma

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

> 💡 VRAM sınırlıysa: `-c` düşürün (örn. 131072) veya llama.cpp'nin VRAM'i otomatik uydurması için `--fit on` ekleyin.

---

## 9. Önerilen Çıkarım Parametreleri

Yerel testlerden optimize edilmiştir (AMD Radeon AI PRO R9700 32GB):

| Parametre | Günlük Görevler / Yazım | Karmaşık Görevler / İleri Kodlama | Notlar |
| --- | --- | --- | --- |
| temperature | 0,6 | 0,8 | Günlük stabilite; karmaşık kodlama için orta düzey keşif |
| top\_p | 0,95 | 0,95 | Çekirdek örnekleme eşiği |
| top\_k | 20 | 20 | Kesilmiş örnekleme |
| min\_p | 0,024 | 0,024 | Minimum olasılık filtresi |
| repeat\_penalty | 1,05 | 1,05 | Tekrar cezası |
| presence\_penalty | 0 | 0 | Varlık cezası yok |
| context\_length | 131072 | 262144 | Günlük 128K / Karmaşık 256K (llama.cpp varsayılan 128K) |
| reasoning | on | on | Akıl yürütme zincirini etkinleştir (CoT) |
| reasoning\_budget | 400 | 1000 | Akıl yürütme bütçe tokenleri (karmaşık görevlerde daha yüksek) |
| reasoning\_format | deepseek-legacy | deepseek-legacy | Akıl yürütmeyi ayrı alanda çıkar |
| **spec-type** | **default** | **default** | **Spekülatif kod çözme (ngram, MoE-optimal, bkz. Bölüm 11)** |
| KV önbelleği | q4\_0 | q4\_0 | Kuantize KV önbelleği (kv-unified) |

> 💡 **Düşünme modu**: `--reasoning on` ile etkinleştirilir — model yanıtlamadan önce dahili olarak akıl yürütür. `reasoning_budget` maksimum düşünme tokenlerini sınırlar.

---

## 10. Kuantizasyon Formatı Karşılaştırması

| Format | Boyut | Doğruluk | Notlar |
| --- | --- | --- | --- |
| FP16 orijinal | ~70 GB | %100 | Kayıpsız, profesyonel GPU gerekir |
| **MoziSmartBit (bu model)** | **~15,9 GB** | **~%99** | **Kendi geliştirilen akıllı kuantizasyon, boyut başına en iyi doğruluk** |
| Q4_K_M | ~22 GB | ~%98 | Standart GGUF 4-bit |
| Q5_K_M | ~24,7 GB | ~%99 | Daha yüksek doğruluk |
| Q6_K | ~28,5 GB | ~%99,5 | Neredeyse kayıpsız |
| Q8_0 | ~36,9 GB | ~%100 | Kayıpsız |

> MoziSmartBit, 35B MoE modelini 15,9 GB'a sıkıştırırken ~%99 doğruluğu korur (4,5x sıkıştırma), Q4_K_M'den ~%30 daha küçük — tüketici GPU'ları için ideal.

---

## 11. Spekülatif Kod Çözme Hızlandırma Önemli Özellik

Bu model, **Spekülatif Kod Çözme (Speculative Decoding)** ile çıkarım hızını önemli ölçüde artırır — yerel ölçümde kapalı duruma göre **~1,5-2 kat daha hızlı**.

- **MoE-optimal yapılandırma**: llama.cpp, MoE mimarileri için **ngram spekülatif kod çözmeyi** (`--spec-default`) önerir — yerel testlerde en hızlı ve en stabil
- **İsimdeki \"MTP\" hakkında**: \"MTP\", taban modelin Multi-Token Prediction ağırlıklarına atıfta bulunur (tamamen korunmuştur); llama.cpp'nin MoE için MTP draft desteği sınırlıdır, bu yüzden MoziAI en iyi ölçülen hız için ngram şemasını kullanır

### Etkinleştirme Parametresi

```bash
--spec-default
```

### Ayar Önerileri

| Yapılandırma | Senaryo |
| --- | --- |
| --spec-default (varsayılan) | Önerilen: hız ve VRAM dengesi |
| Devre dışı (parametreyi kaldır) | Düşük VRAM senaryoları; biraz daha yavaş |

---

## 12. VRAM Yapılandırma Önerileri

MoziSmartBit yapısıyla ölçülmüştür (model + görüş toplam ~16,4 GB):

| VRAM | Önerilen Yapılandırma | Notlar |
| --- | --- | --- |
| 20 GB | Bağlam 150K, q4\_0 KV önbelleği, görüş destekli | Model+görüş ~16,4 GB, 256K+görüş yalnızca ~19,5 GB VRAM |
| **24 GB** | **256K tam, q4\_0 KV önbelleği, mükemmel görüş desteği** | **Önerilen yapılandırma**: görüş+256K uzun bağlam ~20,4 GB, ~3,6 GB boşluk |
| 32 GB+ | 256K tam, yeterli VRAM boşluğu | R9700 32GB gibi: görüş+256K uzun bağlam, ~10 GB boşluk, en güçlü yapılandırma |

> 💡 Bağlam ne kadar uzunsa VRAM kullanımı o kadar artar. OOM durumunda `-c`'yi kademeli düşürün. llama.cpp'nin katman sayısını otomatik ayarlaması için `--fit on` kullanın. Tüm NVIDIA / AMD kartlarını destekler.

---

## 13. Dağıtım Yöntemleri

### Ollama Dağıtımı

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

LM Studio / Jan'da `moziAI` arayın ve Q4\_K\_M kuantizasyon sürümünü seçip indirin (LM Studio varsayılan olarak depo kökündeki modeli okur; tarihsel sürümler için \"URL'den ekle\" ile ilgili sürüm klasöründeki dosyaları içe aktarın, örn. `V3.7/`).

> 💡 Ollama'nın mmproj ve chat\_template desteği sınırlıdır, tam işlevsellik için öncelikle llama.cpp kullanmanız önerilir.

---

## 14. Kıyaslamalar

MoziAI-35B-V3.8, deepreinforce-ai/Ornith-1.5-35B-A3B tabanının ince ayarı, distilasyonu ve ikincil geliştirmesine dayanır; finansal dikey alan çekirdek optimizasyon yönüdür. Aşağıda çoklu model karşılaştırması (MoziAI genel yetenekleri taban Ornith-1.5-35B-A3B ile aynıdır; veriler V3.7 sürüm ölçümlerinden alınmıştır, V3.8 ve V3.7 aynı taban ve eğitim sistemine sahiptir):

| Kıyaslama | moziAI-35B-V3.8<br>(bu model) | Ornith-1.0-35B-A3B | Qwen3.6-35B-A3B | Gemma-4-31B | Muse-Glimmer-30B | Qwen3.5-397B |
|---|---|---|---|---|---|---|
| **Programlama testleri** |  |  |  |  |  |  |
| Terminal-Bench 2.1 (Terminus-2) | 67.8 | 64.2 | 52.5 | 42.1 | 51.7 | 53.5 |
| Terminal-Bench 2.1 (Claude Code) | 68.5 | 62.8 | 49.2 | - | - | 48.6 |
| SWE-bench Verified | 79 | 75.6 | 73.4 | 52 | 76 | 76.4 |
| SWE-bench Pro | 59.6 | 50.4 | 49.5 | 35.7 | 51.2 | 51.6 |
| SWE-bench Multilingual | 71.4 | 69.3 | 67.2 | 51.7 | - | 69.3 |
| DeepSWE | 22 | 0 | 0 | - | - | 1 |
| Frontier-Bench v0.1 | 5.1 | 1.4 | 1.4 | - | - | 1.4 |
| NL2Repo | 46.2 | 34.6 | 29.4 | 15.5 | - | 36.8 |
| SWE Atlas - QnA | 39.8 | 37.1 | 15.5 | - | - | 20.4 |
| **Akıl yürütme testleri** |  |  |  |  |  |  |
| HLE (no tools) | 25.6 | 20.8 | 21.4 | 19.5 | 22 | 28.7 |
| HLE (with tools) | 33.4 | 30.1 | 28.9 | 26.5 | - | 48.3 |
| GPQA Diamond | 89.2 | 86.2 | 86 | 84.3 | 83.5 | 88.4 |
| **Ajan testleri** |  |  |  |  |  |  |
| MCP-Atlas | 70.2 | 64.4 | 62.8 | 55 | 75.5 | 72.3 |
| Toolathlon-Verified | 48.7 | 42.4 | 41.7 | 40.8 | - | 38.3 |
| WideSearch | 67.8 | 63.4 | 60.1 | 54.2 | - | 74 |
| BrowseComp | 67.6 | 63.5 | 62 | - | - | 78.6 |
| ClawEval | 72.5 | 69.8 | 68.7 | 48.5 | - | 70.7 |

> MoziAI-35B finansal dikey alanı, MoziAI'nin çekirdek optimizasyon yönüdür; finansal rapor yorumlama, kantitatif strateji, risk yönetimi uyumu ve ajan araç çağrısında genel modellerden belirgin şekilde daha iyi performans gösterir. Gemma-4 / Qwen3.6 verileri resmi yayınlanmış değerlendirme sonuçlarıdır.

---

## 15. Uncensored Optimizasyonu

Bu model, taban Ornith-1.5-35B-A3B'ün Uncensored özelliğini miras alır ve şu avantajlara sahiptir:

| Avantaj | Açıklama |
| --- | --- |
| Denetim kısıtlaması yok | Hassas ve tartışmalı içerik dahil hiçbir konuyu reddetmez |
| Serbest çıktı | Güvenlik politikalarıyla kısıtlı değildir, her tür yanıt üretebilir |
| Eksiksiz bilgi | Filtrelenmemiş eksiksiz bilgi sağlar, araştırma ve analiz için uygundur |
| Yerel gizlilik | Yerel dağıtım verilerin tamamen özel olduğu anlamına gelir, bulut denetimi yok |

**Kullanım senaryoları**: akademik araştırma, derin analiz, özgür tartışma, sınırsız AI sohbeti.

**Not**: Bu yerel dağıtılan bir modeldir — çıktı tamamen kullanıcı tarafından kontrol edilir; model içerik denetimi sorumluluğu taşımaz.

---

## 16. Lisans

Bu model **özel kısıtlayıcı lisans** kullanır:

- ✅ **İzin verilir** — ücretsiz ticari kullanım, kopyalama ve dağıtım
- ❌ **Yasaktır** — daha fazla geliştirme, yeniden satış, alt lisanslama
- 📋 **Gerekli** — orijinal telif hakkı bildirimini koruyun, kaynak belirtin: moziAI-35B

Model "olduğu gibi", herhangi bir garanti olmadan sağlanır. Model çıktısı yalnızca referans içindir ve yatırım tavsiyesi oluşturmaz. Kullanıcılar tüm riskleri üstlenir.

Tam koşullar için [LICENSE](LICENSE) dosyasına bakın.

---

## 17. İletişim

- **HuggingFace**: [@chenyumo](https://huggingface.co/chenyumo)
- **GitHub**: [@chenyumo166](https://github.com/chenyumo166)
- **Weibo**: [@rimochen](https://weibo.com/rimochen)
- **E-posta**: 263515@qq.com

Copyright (c) 2026 陈雨墨 / chenyumo166. All rights reserved.
