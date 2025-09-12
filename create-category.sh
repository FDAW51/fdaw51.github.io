#!/usr/bin/env bash
set -euo pipefail

echo "【创建类别】"
read -r -p "请输入类别名: " category
if [ -z "$category" ]; then
  echo "❌ 类别名不能为空"
  exit 1
fi

# 颜色池：可以自行扩展
colors=(
  "#FF5733" "#33C1FF" "#33FF57" "#FF33A8" "#FFD733"
  "#8E44AD" "#1ABC9C" "#2a9d8f" "#264653" "#e76f51"
  "#f4a261" "#e9c46a" "#06d6a0" "#118ab2" "#073b4c"
)

# 用于记录已使用过的颜色
used_file=".used_colors"
touch "$used_file"

# 从颜色池中筛掉已使用的颜色
available=()
for c in "${colors[@]}"; do
  if ! grep -Fxq "$c" "$used_file"; then
    available+=("$c")
  fi
done

# 如果颜色用完，就重置
if [ ${#available[@]} -eq 0 ]; then
  echo "🎨 颜色池已用完，重置..."
  > "$used_file"
  available=("${colors[@]}")
fi

# 随机选取背景色
bg=${available[$RANDOM % ${#available[@]}]}
echo "$bg" >> "$used_file"

# 根据亮度决定前景色（黑/白）
hex=${bg#\#}
R=$((16#${hex:0:2}))
G=$((16#${hex:2:2}))
B=$((16#${hex:4:2}))
lum=$(( (R*299 + G*587 + B*114) / 1000 ))
if [ "$lum" -gt 128 ]; then
  text="#000000"
else
  text="#FFFFFF"
fi

# 生成文件
file_path="content/categories/${category}/_index.md"
mkdir -p "$(dirname "$file_path")"

cat > "$file_path" <<EOF
---
title: ${category}
slug: ${category}
description: 
image: 
style:
    background: "${bg}"
    color: "${text}"
---
EOF

echo "✅ 已创建 ${file_path}"
echo "🎨 background: ${bg}"
echo "🔤 color: ${text}"
