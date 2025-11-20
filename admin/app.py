#!/usr/bin/env python3
import os
import re
import random
import subprocess
import socket
import time
from datetime import datetime
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

BASE_DIR = Path(__file__).resolve().parent.parent  # repo root
CONTENT_DIR = BASE_DIR / "content"
POSTS_DIR = CONTENT_DIR / "post"
CATEGORIES_DIR = CONTENT_DIR / "categories"

app = Flask(__name__)
app.secret_key = "dev-secret"  # for flash messages; replace if you like

COLOR_POOL = [
    "#FF5733", "#33C1FF", "#33FF57", "#FF33A8", "#FFD733",
    "#8E44AD", "#1ABC9C", "#2a9d8f", "#264653", "#e76f51",
    "#f4a261", "#e9c46a", "#06d6a0", "#118ab2", "#073b4c",
]
USED_COLORS_FILE = BASE_DIR / ".used_colors"


def ensure_parent(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)


def slugify(text: str) -> str:
    text = text.strip()
    text = text.replace(" ", "-")
    text = re.sub(r"[^\w\-]", "", text)
    return text.lower()


def pick_color() -> tuple[str, str]:
    used = set()
    if USED_COLORS_FILE.exists():
        used.update(c.strip() for c in USED_COLORS_FILE.read_text(encoding="utf-8").splitlines() if c.strip())
    available = [c for c in COLOR_POOL if c not in used]
    if not available:
        # reset
        USED_COLORS_FILE.write_text("", encoding="utf-8")
        available = COLOR_POOL[:]
    bg = random.choice(available)
    with USED_COLORS_FILE.open("a", encoding="utf-8") as f:
        f.write(bg + "\n")
    # luminance
    hx = bg.lstrip('#')
    R, G, B = int(hx[0:2], 16), int(hx[2:4], 16), int(hx[4:6], 16)
    lum = (R*299 + G*587 + B*114) // 1000
    text = "#000000" if lum > 128 else "#FFFFFF"
    return bg, text


def build_post_front_matter(title: str, slug: str, description: str, image: str, category: str, tags_csv: str, draft: bool) -> str:
    # tags as YAML list
    tags_yaml_lines = []
    for t in [t.strip() for t in tags_csv.split(',') if t.strip()]:
        tags_yaml_lines.append(f"  - \"{t}\"")
    tags_yaml = ("\n".join(tags_yaml_lines) + "\n") if tags_yaml_lines else ""
    dt = datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")
    fm = (
        "---\n"
        f"title: \"{title or slug}\"\n"
        f"slug: \"{slug}\"\n"
        f"description: \"{description}\"\n"
        f"image: \"{image}\"\n"
        f"categories: [\"{category}\"]\n"
        f"tags:\n{tags_yaml}"
        f"date: {dt}\n"
        f"draft: {'true' if draft else 'false'}\n"
        "---\n\n"
    )
    return fm


def list_post_files() -> list[Path]:
    return sorted(POSTS_DIR.glob("**/index.md"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts")
def posts():
    files = list_post_files()
    items = []
    for f in files:
        rel = f.relative_to(BASE_DIR)
        items.append({
            "path": str(rel),
            "mtime": datetime.fromtimestamp(f.stat().st_mtime),
        })
    return render_template("list_posts.html", items=items)


@app.route("/posts/new", methods=["GET", "POST"])
def new_post():
    if request.method == "POST":
        slug = slugify(request.form.get("slug", ""))
        if not slug:
            flash("slug 不能为空", "error")
            return redirect(url_for("new_post"))
        title = request.form.get("title", "")
        description = request.form.get("description", "")
        image = request.form.get("image", "")
        category = request.form.get("category", "")
        tags = request.form.get("tags", "")
        draft = request.form.get("draft") == "on"

        year = datetime.now().strftime("%Y")
        file_path = POSTS_DIR / year / slug / "index.md"
        ensure_parent(file_path)
        fm = build_post_front_matter(title, slug, description, image, category, tags, draft)
        with file_path.open("w", encoding="utf-8") as f:
            f.write(fm)
        flash(f"已创建文章: {file_path.relative_to(BASE_DIR)}", "success")
        return redirect(url_for("posts"))

    return render_template("create_post.html")


@app.route("/posts/edit", methods=["GET", "POST"])
def edit_post():
    rel_path = request.args.get("path") if request.method == "GET" else request.form.get("path")
    if not rel_path:
        flash("缺少 path 参数", "error")
        return redirect(url_for("posts"))
    abs_path = BASE_DIR / rel_path
    if request.method == "POST":
        content = request.form.get("content", "")
        ensure_parent(abs_path)
        abs_path.write_text(content, encoding="utf-8")
        flash("已保存", "success")
        return redirect(url_for("posts"))

    try:
        content = abs_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        content = ""
    return render_template("edit_post.html", path=rel_path, content=content)


@app.route("/categories/new", methods=["GET", "POST"])
def new_category():
    if request.method == "POST":
        category = request.form.get("category", "").strip()
        if not category:
            flash("类别名不能为空", "error")
            return redirect(url_for("new_category"))
        bg, text = pick_color()
        file_path = CATEGORIES_DIR / category / "_index.md"
        ensure_parent(file_path)
        fm = (
            "---\n"
            f"title: {category}\n"
            f"slug: {category}\n"
            f"description: \n"
            f"image: \n"
            "style:\n"
            f"    background: \"{bg}\"\n"
            f"    color: \"{text}\"\n"
            "---\n"
        )
        file_path.write_text(fm, encoding="utf-8")
        flash(f"已创建分类: {file_path.relative_to(BASE_DIR)}", "success")
        return redirect(url_for("index"))

    return render_template("create_category.html")


@app.route('/admin/static/<path:filename>')
def static_files(filename):
    return send_from_directory(Path(__file__).parent / 'static', filename)


@app.route("/preview")
def preview():
    # Check if port 1313 is open
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('127.0.0.1', 1313))
    sock.close()

    if result != 0:
        # Port is not open, start Hugo server
        try:
            # Start hugo server in background
            # cwd=BASE_DIR ensures it runs from the repo root
            subprocess.Popen(["hugo", "server", "-D"], cwd=BASE_DIR)
            # Give it a moment to start up
            time.sleep(2)
        except FileNotFoundError:
            flash("未找到 hugo 命令，请确保已安装 hugo 并添加到 PATH。", "error")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"启动预览失败: {e}", "error")
            return redirect(url_for('index'))

    return redirect("http://localhost:1313/")


if __name__ == "__main__":
    app.run(debug=True)
