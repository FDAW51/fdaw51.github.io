#!/usr/bin/env python3
r"""
简易 Markdown 数学语法检查脚本。

当前规则：
1. 检测 KaTeX 不支持的经典 LaTeX 命令（如 \bold、\rm、\bf 等）。
2. 检测 $$...$$ / \[...\] 这类块级公式里直接使用 \\ 换行但未包裹 aligned / array 环境的情况。
后续若有更多常见问题，可在 INVALID_COMMANDS 或 BLOCK_NEWLINE_SAFE 里继续扩展。
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
from dataclasses import dataclass
from typing import Iterable, List, Tuple

INVALID_COMMANDS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"\\bold\s*(?={|\()", re.IGNORECASE), "使用了 KaTeX 不支持的 \\bold，建议改为 \\mathbf 或 \\boldsymbol"),
    (re.compile(r"\\bf\s", re.IGNORECASE), "使用了 \\bf，建议改为 \\mathbf"),
    (re.compile(r"\\it\s", re.IGNORECASE), "使用了 \\it，建议改为 \\mathit"),
    (re.compile(r"\\rm\s", re.IGNORECASE), "使用了 \\rm，建议改为 \\mathrm"),
    (re.compile(r"\\sum_\s*<[^>]+>", re.IGNORECASE), "请将 \\sum_{<i,j>} 的尖括号改写为 \\langle i,j \\rangle"),
]

BLOCK_NEWLINE_SAFE = {"aligned", "alignedat", "cases", "array", "matrix", "pmatrix", "bmatrix"}

BLOCK_PATTERNS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"\$\$(.+?)\$\$", re.DOTALL), "$$"),
    (re.compile(r"\\\[(.+?)\\\]", re.DOTALL), "\\[\\]"),
]

INLINE_PATTERNS: List[Tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL), "$"),
    (re.compile(r"\\\((.+?)\\\)"), "\\(\\)"),
]


@dataclass
class MatchInfo:
    expr: str
    start: int
    end: int
    kind: str  # block or inline description


def iter_math_segments(text: str) -> Iterable[MatchInfo]:
    for pattern, label in BLOCK_PATTERNS:
        for m in pattern.finditer(text):
            yield MatchInfo(m.group(1), m.start(), m.end(), f"block {label}")
    for pattern, label in INLINE_PATTERNS:
        for m in pattern.finditer(text):
            yield MatchInfo(m.group(1), m.start(), m.end(), f"inline {label}")


def offset_to_line(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def check_invalid_commands(expr: str) -> Iterable[str]:
    for pattern, message in INVALID_COMMANDS:
        if pattern.search(expr):
            yield message


def check_block_newlines(expr: str) -> Iterable[str]:
    if "\\\\" not in expr:
        return
    if any(name in expr for name in BLOCK_NEWLINE_SAFE):
        return
    yield "块级公式中直接使用 \\\\，请使用 aligned/array/cases 等环境再换行"


def inspect_file(path: pathlib.Path) -> List[str]:
    text = path.read_text(encoding="utf-8")
    issues: List[str] = []
    for seg in iter_math_segments(text):
        line = offset_to_line(text, seg.start)
        for problem in check_invalid_commands(seg.expr):
            issues.append(f"{path}:{line}: {problem}")
        if seg.kind.startswith("block"):
            for problem in check_block_newlines(seg.expr):
                issues.append(f"{path}:{line}: {problem}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="检查 Markdown 文件中的常见 KaTeX 兼容性问题")
    parser.add_argument("paths", nargs="*", default=["content"], help="要扫描的目录或文件（默认 content）")
    args = parser.parse_args()

    targets: List[pathlib.Path] = []
    for raw in args.paths:
        path = pathlib.Path(raw).expanduser().resolve()
        if not path.exists():
            print(f"[WARN] 跳过不存在的路径：{path}", file=sys.stderr)
            continue
        if path.is_file():
            targets.append(path)
        else:
            targets.extend(path.glob("**/*.md"))

    all_issues: List[str] = []
    for md_file in sorted({p for p in targets if p.suffix.lower() == ".md"}):
        all_issues.extend(inspect_file(md_file))

    if not all_issues:
        print("✅ 未发现已知的 KaTeX 兼容性问题")
        return 0

    print("⚠️ 发现以下可能的数学格式问题：")
    for issue in all_issues:
        print(" -", issue)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

