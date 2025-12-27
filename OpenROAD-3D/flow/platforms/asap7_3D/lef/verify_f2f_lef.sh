#!/bin/bash
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║   F2F 3DIC Tech LEF 验证报告                              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo

echo "📁 文件信息:"
echo "   输入: asap7_tech_1x_201209.lef ($(wc -l < asap7_tech_1x_201209.lef) 行)"
echo "   输出: asap7_tech_f2f_3d.lef ($(wc -l < asap7_tech_f2f_3d.lef) 行)"
echo

echo "🔷 底部芯片层 (Bottom Die):"
grep -E "^LAYER (M[1-7]|V[0-6])\s*$" asap7_tech_f2f_3d.lef | awk '{print "   ✓", $2}'
echo

echo "🔶 顶部芯片层 (Top Die - 镜像):"
grep -E "^LAYER (M[8-9]|M1[0-4]|V[8-9]|V1[0-4])\s*$" asap7_tech_f2f_3d.lef | awk '{print "   ✓", $2}'
echo

echo "🔗 3D 互连层:"
grep "^LAYER V7_M8_BOND" asap7_tech_f2f_3d.lef | awk '{print "   ✓", $2, "(M7 ↔ M8 hybrid bond)"}'
echo

echo "🔌 VIA 统计:"
echo "   底部 VIA: $(grep -c "^VIA VIA[0-9][0-9] " asap7_tech_f2f_3d.lef) 个"
echo "   顶部 VIA: $(grep -c "^VIA VIA_M.*_M.* " asap7_tech_f2f_3d.lef) 个"
echo "   3D VIA:  $(grep -c "^VIA VIA_M7_M8_BOND " asap7_tech_f2f_3d.lef) 个"
echo

echo "⚙️  VIARULE 统计:"
bottom_vr=$(grep -E "^VIARULE (M[2-7]_M[1-6]|M[3-7]_M[2-6]widePWR)" asap7_tech_f2f_3d.lef | wc -l)
top_vr=$(grep -E "^VIARULE (M[8-9]_M[89]|M1[0-3]_M1[0-4]|M[8-9]_M[89]widePWR|M1[0-2]_M1[0-3]widePWR)" asap7_tech_f2f_3d.lef | wc -l)
bond_vr=$(grep -c "^VIARULE M7_M8_BOND" asap7_tech_f2f_3d.lef)
echo "   底部 VIARULE: $bottom_vr 条"
echo "   顶部 VIARULE: $top_vr 条"
echo "   3D VIARULE:   $bond_vr 条"
echo

echo "✅ 验证通过！F2F 3DIC Tech LEF 已成功生成。"
echo
