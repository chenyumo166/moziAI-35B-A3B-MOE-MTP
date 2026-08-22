# 多模态视觉使用指�?

MoziAI-35B 支持多模态理解，可以分析图片内容，特别适合金融图表的识别与分析�?

---

## 前置条件

- 模型文件：`moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf`
- 视觉投影器：`moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf`
- 聊天模板：`moziAI-V3.6-35B-chat-template.jinja`
- llama.cpp / LM Studio 等支持多模态的推理工具

---

## llama.cpp 中使�?

### 单张图片问答

```bash
./main \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --image kline_chart.png \
  -p "请分析这张K线图的走�?
```

### 服务模式

```bash
./server \
  -m moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf \
  --mmproj moziAI-V3.6-35B-uncensored-heretic-mmproj-BF16.gguf \
  --chat-template moziAI-V3.6-35B-chat-template.jinja \
  --host 0.0.0.0 --port 8080 -c 262144
```

通过 API 上传图片并提问�?

---

## 适用场景

### 金融场景
| 场景 | 说明 |
|------|------|
| K线图分析 | 识别趋势、形态、支撑阻力位 |
| 财报截图解读 | 提取财务数据、分析报表结�?|
| 研报图表 | 理解研报中的数据图表 |
| 行情截图 | 描述截图中的行情信息 |

### 通用场景
- 图片内容描述
- OCR 文字提取（辅助）
- 图表数据理解

---

## 提示词建�?

### 效果好的提问方式

```
请详细描述这张K线图中的走势特征
```

```
这张财务报表中营业收入是多少？同比增长了多少�?
```

```
从这张图中能看出什么技术形态？
```

### 效果可能不好的场�?

- 提取非常精确的数值（价格、成交量等可能有误差�?
- 非常复杂的多图组�?
- 极小的文字或数据

---

## 注意事项

> ⚠️ **重要提示**
>
> 1. 视觉识别�?*辅助功能**，提取的数值可能存在误�?
> 2. **交易决策请以原始数据源为�?*，不要仅依赖图片识别结果
> 3. 图片清晰度会影响识别效果，尽量使用清晰的截图
> 4. 复杂图表建议结合工具调用从数据源获取准确数据

---

## LM Studio 中使�?

1. 确保已加载模型和 mmproj
2. 在聊天界面点�?📎 / 🖼�?按钮上传图片
3. 输入问题发送即�?
