#!/bin/bash

echo "【创建文章】"
read -p "请输入 slug: " input

# 获取当前日期：年份和月日
year=$(date "+%Y")
monthday=$(date "+%m%d")

# 创建文章
hugo new post/"$year"/"$input"/index.md
