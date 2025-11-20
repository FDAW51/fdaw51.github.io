#!/bin/bash

# 进入脚本所在的目录 (项目根目录)
cd "$(dirname "$0")"

echo "正在启动 Eugene 网站管理后台..."
echo "地址: http://127.0.0.1:5000"

# 自动在默认浏览器打开网页
# sleep 1 确保服务器有时间启动 (虽然 Flask 启动很快，但这是个好习惯)
(sleep 1 && open "http://127.0.0.1:5000") &

# 启动 Flask 应用
./admin/.venv/bin/python admin/app.py
