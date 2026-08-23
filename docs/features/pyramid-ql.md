# 金字塔量化编程指南

MoziAI-35B 深度优化了金字塔（Pyramid）量化交易策略的编写能力，支持 PEL 语言。

---

## 快速开始

### 直接让模型写策略

示例提示词：

```
帮我写一个 MACD 金叉死叉的金字塔交易策略
```

### 获取帮助

```
金字塔的 BUY 函数怎么用？
```

---

## 模型内置的金字塔函数速查

以下是模型内置支持的核心金字塔函数：

### 开平仓函数

| 函数 | 说明 |
|------|------|
| `BUY(COND, V, Type, [P])` | 开多 |
| `SELL(COND, V, Type, [P])` | 平多 |
| `BUYSHORT(COND, V, Type, [P])` | 开空 |
| `SELLSHORT(COND, V, Type, [P])` | 平空 |

### 后台交易函数

| 函数 | 说明 |
|------|------|
| `TBUY(COND, V, [Type,P1,P2,AC,STOCK])` | 后台开多 |
| `TSELL(COND, V, [Type,P1,P2,AC,STOCK])` | 后台平多 |
| `TBUYSHORT(COND, V, [Type,P1,P2,AC,STOCK])` | 后台开空 |
| `TSELLSHORT(COND, V, [Type,P1,P2,AC,STOCK])` | 后台平空 |

### 报单类型 Type

| 类型 | 说明 |
|------|------|
| `MARKETR` | 本周期市价 |
| `LIMITR` | 本周期限价 |
| `THISCLOSE` | 收盘价 |
| `MARKET` | 次周期市价 |
| `LIMIT` | 次周期限价 |
| `STOPR` | 停损（本周期） |
| `STOP` | 停损（次周期） |
| `LMT` | 限价（后台） |
| `MKT` | 市价（后台） |

### 持仓函数

| 函数 | 说明 |
|------|------|
| `HOLDING` | 当前持仓量（正多负空） |
| `THOLDING` | 后台持仓 |
| `ENTERPRICE` | 开仓价 |
| `AVGENTERPRICE` | 均价 |
| `OPENPROFIT` | 浮动盈亏 |

---

## 示例策略

### MACD 金叉死叉策略

*可直接让模型生成，此处仅为示例说明*

```
// MACD金叉死叉策略示例
DIF:=EMA(CLOSE,12)-EMA(CLOSE,26);
DEA:=EMA(DIF,9);
MACD:=2*(DIF-DEA);

// 金叉开多
BUY(CROSS(DIF,DEA), 1, MARKETR);

// 死叉平多
SELL(CROSS(DEA,DIF), HOLDING, MARKETR);
```

---

## 注意事项

> ⚠️ **重要提示**
>
> 1. 模型生成的策略代码**仅供参考学习**，使用前务必在模拟环境中充分测试
> 2. 实盘交易风险自负，模型不对策略盈亏承担任何责任
> 3. 策略逻辑可能存在 bug，请仔细审查
