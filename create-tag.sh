#!/bin/bash

echo "【创建标签】"
read -p "请输入标签名: " tag

# 去除前后空格
tag=$(echo "$tag" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

# 创建标签文件
hugo new tags/"$tag"/_index.md

