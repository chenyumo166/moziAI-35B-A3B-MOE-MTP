"""V3.6 → V3.7 批量替换脚本（dist/moziAI-35B/V3.7/ 全部文档）"""
import os, re

V37_DIR = 'F:/fin_moe/dist/moziAI-35B/V3.7'

replacements = [
    # 版本号
    ('V3.6', 'V3.7'),
    # 底座版本
    ('Ornith-1.0-35B', 'Ornith-1.5-35B-A3B'),
    ('Ornith-1.0', 'Ornith-1.5'),
    # 底座描述
    ('基于 Ornith-1.5-35B-A3B（**Qwen3.5-35B-A3B / Qwen3.6-35B-A3B** 架构）', '基于 Ornith-1.5-35B-A3B（**Qwen3.6-35B-A3B** 架构）'),
    ('继承底座 Ornith-1.5-35B-A3B 的 Uncensored', '继承底座 Ornith-1.5-35B-A3B 的 Uncensored'),
    # 量化方式（V3.6 Q4Q3 Hybrid → V3.7 Q4_K_M + MoziSmartBit）
    ('自研 Q4Q3 Hybrid 混合量化', 'MoziSmartBit 智能量化（Q4_K_M）'),
    ('Q4Q3 混合量化算法', 'MoziSmartBit 智能量化算法（Q4_K_M）'),
    ('专家层 Q3_K + 共享层 Q4_K + Norm F32', '专家层 Q4_K_M 均匀量化 + MoziSmartBit 智能比特分配'),
    # 模型体积
    ('~14.5 GB', '~15.5 GB'),
    ('约 **15.5 GB**', '约 **15.5 GB**'),
    # GGUF 文件名（V3.6 格式 → V3.7 格式）
    ('moziAI-V3.6-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf',
     'moziAI-V3.7-Qwen3.6-35B-A3B-Ornith-MoziSmartBit-Q4_K_M-Uncensored.gguf'),
    ('moziAI-V3.6-35B', 'moziAI-V3.7-35B'),
    # chat template 文件名
    ('moziAI-V3.6-35B-chat-template.jinja', 'moziAI-V3.7-35B-chat-template.jinja'),
    # 日期
    ('2026-08-20', '2026-08-21'),
]

changed = []
for root, dirs, files in os.walk(V37_DIR):
    for fname in files:
        if not fname.endswith('.md') and not fname.endswith('.jinja'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        orig = content
        for old, new in replacements:
            content = content.replace(old, new)
        if content != orig:
            with open(fpath, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            changed.append(fname)

print(f'✅ 已更新 {len(changed)} 个文件:')
for f in changed:
    print(f'  {f}')