#!/usr/bin/env bash
set -euo pipefail

echo "【创建文章】"
read -p "请输入 slug: " slug
if [ -z "$slug" ]; then
  echo "❌ slug 不能为空"
  exit 1
fi

# 输入附加信息
read -p "请输入文章标题: " title
read -p "请输入文章描述 (description): " description
read -p "请输入封面图地址 (image URL): " image
read -p "请输入分类 (category): " category
read -p "请输入标签 (tags，用逗号分隔): " tags_input

# 获取当前日期
year=$(date "+%Y")
monthday=$(date "+%m%d")
datetime=$(date +"%Y-%m-%dT%H:%M:%S%z")

# 创建文件路径
file_path="content/post/${year}/${slug}/index.md"
mkdir -p "$(dirname "$file_path")"

# 处理 tags 为 YAML 列表
tags_array=()
IFS=',' read -ra tags_array <<< "$tags_input"
tags_yaml=""
for tag in "${tags_array[@]:-}"; do
  clean_tag=$(echo "$tag" | xargs)
  if [ -n "$clean_tag" ]; then
    tags_yaml+="  - \"$clean_tag\"\n"
  fi
done

# 写入 Front Matter
cat > "$file_path" <<EOF
---
title: "${title:-$slug}"
slug: "${slug}"
description: "${description}"
image: "${image}"
categories: ["${category}"]
tags:
${tags_yaml}date: ${datetime}
draft: true
---
EOF

echo "✅ 已创建文章：${file_path}"
