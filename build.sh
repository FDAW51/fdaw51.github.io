#!/bin/sh
# 集成数学公式检查 + Hugo 构建
set -eu

ROOT_DIR="$(cd -- "$(dirname -- "$0")" && pwd)"
CHECKER="python3 \"$ROOT_DIR/scripts/check_math.py\""

echo "==> 运行数学公式检查..."
if ! eval "$CHECKER"; then
  echo "❌ 数学格式检查失败，已终止构建。"
  exit 1
fi

echo "==> 数学检查通过，开始 Hugo 构建..."
hugo server
echo "✅ 构建完成"


