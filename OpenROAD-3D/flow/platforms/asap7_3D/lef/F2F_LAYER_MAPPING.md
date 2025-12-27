# ASAP7 F2F 3DIC Tech LEF 层映射文档

## 📋 概述

本文档描述从 2D Tech LEF (`asap7_tech_1x_201209.lef`) 到 F2F 3DIC Tech LEF (`asap7_tech_f2f_3d.lef`) 的层映射关系。

**生成工具**: `mirror_tech_lef_v2_fixed.py`  
**生成日期**: 2025-10-27  
**架构类型**: Face-to-Face (F2F) 3D Integrated Circuit

---

## 🏗️ 整体架构

```
┌────────────────────────────────────────────────┐
│  顶部芯片 (Top Die) - 倒置放置                 │
│  M14 ← V13 ← M13 ← V12 ← M12 ← V11 ← M11       │
│      ← V10 ← M10 ← V9 ← M9 ← V8 ← M8           │
└─────────────────────┬──────────────────────────┘
                      │ V7_M8_BOND (Hybrid Bond)
┌─────────────────────┴──────────────────────────┐
│  底部芯片 (Bottom Die)                         │
│  M1 → V1 → M2 → V2 → M3 → V3 → M4              │
│      → V4 → M5 → V5 → M6 → V6 → M7             │
└────────────────────────────────────────────────┘
```

---

## 🔷 底部芯片层 (Bottom Die)

### 金属层 (ROUTING)

| 层名 | 类型 | 方向 | PITCH (µm) | WIDTH (µm) | 用途 |
|------|------|------|-----------|-----------|------|
| M1 | ROUTING | VERTICAL | 0.036 | 0.018 | 局部互连 |
| M2 | ROUTING | HORIZONTAL | 0.045×0.036 | 0.018 | 电源轨 |
| M3 | ROUTING | VERTICAL | 0.036 | 0.018 | 信号布线 |
| M4 | ROUTING | HORIZONTAL | 0.048 | 0.024 | 信号布线 |
| M5 | ROUTING | VERTICAL | 0.048 | 0.024 | 全局布线 |
| M6 | ROUTING | HORIZONTAL | 0.064 | 0.032 | 电源/时钟 |
| M7 | ROUTING | VERTICAL | 0.064 | 0.032 | 接合层 |

### 通孔层 (CUT)

| 层名 | WIDTH (µm) | SPACING (µm) | 特性 |
|------|-----------|-------------|------|
| V0 | 0.018 | 0.018 | 接触孔 |
| V1 | 0.018 | 0.018 | - |
| V2 | 0.018 | 0.018 | - |
| V3 | 多类别 | 0.034 | CUTCLASS (3种) |
| V4 | 多类别 | 0.034 | CUTCLASS (5种) |
| V5 | 多类别 | 0.034 | CUTCLASS (5种) |
| V6 | 多类别 | 0.034 | CUTCLASS (5种) |

---

## 🔶 顶部芯片层 (Top Die - 镜像)

### 层映射关系

| 新层名 | 镜像自 | 类型 | 方向 | PITCH (µm) | WIDTH (µm) |
|--------|--------|------|------|-----------|-----------|
| M14 | M1 | ROUTING | VERTICAL | 0.036 | 0.018 |
| M13 | M2 | ROUTING | HORIZONTAL | 0.045×0.036 | 0.018 |
| M12 | M3 | ROUTING | VERTICAL | 0.036 | 0.018 |
| M11 | M4 | ROUTING | HORIZONTAL | 0.048 | 0.024 |
| M10 | M5 | ROUTING | VERTICAL | 0.048 | 0.024 |
| M9 | M6 | ROUTING | HORIZONTAL | 0.064 | 0.032 |
| M8 | M7 | ROUTING | VERTICAL | 0.064 | 0.032 |

### 通孔映射

| 新层名 | 镜像自 | WIDTH (µm) |
|--------|--------|-----------|
| V14 | V0 | 0.018 |
| V13 | V1 | 0.018 |
| V12 | V2 | 0.018 |
| V11 | V3 | 多类别 |
| V10 | V4 | 多类别 |
| V9 | V5 | 多类别 |
| V8 | V6 | 多类别 |

---

## 🔗 3D 互连层

### V7_M8_BOND (Hybrid Bonding)

```
层名:        V7_M8_BOND
类型:        CUT (TYPE CUT)
连接:        M7 (底部) ↔ M8 (顶部)
WIDTH:       0.064 µm
SPACING:     0.1 µm
技术:        3D Hybrid Bond
属性:        LEF58_TYPE "TYPE 3D_HYBRID_BOND"
```

**用途**: 提供底部芯片顶层 (M7) 与顶部芯片顶层 (M8) 之间的直接金属键合连接。

---

## 🔌 VIA 定义

### 底部芯片 VIA

| VIA 名称 | 连接层 | 备注 |
|----------|--------|------|
| VIA12 | M1 ↔ M2 | - |
| VIA23 | M2 ↔ M3 | - |
| VIA34 | M3 ↔ M4 | - |
| VIA45 | M4 ↔ M5 | - |
| VIA56 | M5 ↔ M6 | - |
| VIA67 | M6 ↔ M7 | - |

### 顶部芯片 VIA

| VIA 名称 | 连接层 | 镜像自 |
|----------|--------|--------|
| VIA_M13_M14 | M13 ↔ M14 | VIA12 |
| VIA_M12_M13 | M12 ↔ M13 | VIA23 |
| VIA_M11_M12 | M11 ↔ M12 | VIA34 |
| VIA_M10_M11 | M10 ↔ M11 | VIA45 |
| VIA_M9_M10 | M9 ↔ M10 | VIA56 |
| VIA_M8_M9 | M8 ↔ M9 | VIA67 |

### 3D 键合 VIA

| VIA 名称 | 连接层 | 尺寸 | 用途 |
|----------|--------|------|------|
| VIA_M7_M8_BOND | M7 ↔ V7_M8_BOND ↔ M8 | 64nm × 64nm | 芯片间互连 |

---

## ⚙️ VIARULE 定义

### 底部芯片 VIARULE

| VIARULE 名称 | 连接层 | 类型 |
|--------------|--------|------|
| M2_M1 | M1 ↔ M2 | 标准 |
| M3_M2widePWR0p936 | M2 ↔ M3 | 电源宽通孔 |
| M4_M3widePWR0p864 | M3 ↔ M4 | 电源宽通孔 |
| M5_M4widePWR0p864 | M4 ↔ M5 | 电源宽通孔 |
| M6_M5 | M5 ↔ M6 | 标准 |
| M6_M5widePWR1p152 | M5 ↔ M6 | 电源宽通孔 |
| M7_M6 | M6 ↔ M7 | 标准 |
| M7_M6widePWR1p152 | M6 ↔ M7 | 电源宽通孔 |

### 顶部芯片 VIARULE

| VIARULE 名称 | 连接层 | 镜像自 |
|--------------|--------|--------|
| M13_M14 | M13 ↔ M14 | M2_M1 |
| M12_M13widePWR0p936 | M12 ↔ M13 | M3_M2widePWR0p936 |
| M11_M12widePWR0p864 | M11 ↔ M12 | M4_M3widePWR0p864 |
| M10_M11widePWR0p864 | M10 ↔ M11 | M5_M4widePWR0p864 |
| M9_M10 | M9 ↔ M10 | M6_M5 |
| M9_M10widePWR1p152 | M9 ↔ M10 | M6_M5widePWR1p152 |
| M8_M9 | M8 ↔ M9 | M7_M6 |
| M8_M9widePWR1p152 | M8 ↔ M9 | M7_M6widePWR1p152 |

### 3D 键合 VIARULE

| VIARULE 名称 | 连接层 | SPACING | ENCLOSURE |
|--------------|--------|---------|-----------|
| M7_M8_BOND | M7 ↔ M8 | 0.2 × 0.2 µm | 0.011 µm |

---

## 📊 统计信息

| 项目 | 原 2D LEF | F2F 3D LEF | 增加 |
|------|-----------|------------|------|
| **文件行数** | 836 | 1288 | +452 |
| **ROUTING 层** | 10 | 14 | +4 |
| **CUT 层** | 10 | 15 | +5 |
| **VIA 定义** | 9 | 13 | +4 |
| **VIARULE** | 12 | 17 | +5 |
| **芯片数** | 1 | 2 | +1 |

---

## 🎯 使用场景

### 适用于

- ✅ 7nm ASAP7 工艺的 F2F 3D 设计
- ✅ 高性能计算 (HPC) 芯片
- ✅ AI/ML 加速器
- ✅ 内存-逻辑混合集成

### 设计考虑

1. **底部芯片 (M1-M7)**: 通常放置逻辑电路
2. **顶部芯片 (M8-M14)**: 可放置内存、模拟电路或额外逻辑
3. **M7 ↔ M8 键合**: 提供低延迟、高带宽的芯片间互连
4. **电源规划**: 两个芯片可共享电源域或独立供电

---

## 🛠️ 生成命令

```bash
cd /home/Open3DBench/OpenROAD-3D/flow/platforms/asap7_H3D/lef
python3 mirror_tech_lef_v2_fixed.py
```

**输出文件**: `asap7_tech_f2f_3d.lef`

---

## 📝 版本历史

| 版本 | 日期 | 说明 |
|------|------|------|
| v1.0 | 2025-10-27 | 初始版本，底层 M1-M7，顶层 M8-M14 |
| v1.1 | 2025-10-27 | 修复 VIA 名称冲突，删除冗余层 |

---

**文档生成**: 自动化脚本  
**最后更新**: 2025-10-27

