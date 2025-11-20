本地 Hugo 管理页面（Flask）

用法：

1. 进入 admin 目录并创建虚拟环境

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. 运行

   python app.py

3. 打开浏览器访问 http://127.0.0.1:5000

功能：
- 新建文章：自动在 content/post/{year}/{slug}/index.md 生成 FrontMatter（与脚本一致）。
- 列表/编辑文章：扫描所有 content/post/**/index.md，在线编辑后保存。
- 新建分类：在 content/categories/{category}/_index.md 生成文件，并自动分配背景色与前景色。

注意：
- 该工具只在本地修改仓库文件，不会发布网站。仍需按你的原流程运行 hugo 构建与部署。
- 如果你已有 .used_colors，该工具会复用并扩展颜色使用记录。
