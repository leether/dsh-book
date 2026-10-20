# 发布与 GitHub Pages 设置

## 仓库

- 仓库：`https://github.com/leether/dsh-book`
- 站点（中文）：`https://leether.github.io/dsh-book/`
- 站点（English）：`https://leether.github.io/dsh-book/en/`
- 默认分支：`main`
- Pages 来源：`main` 分支的 `/docs` 目录
- 站点类型：纯静态 HTML 双语站点，无服务端、无 JavaScript、无第三方资源

---

## 首次发布

```bash
cd ~/workspace/dsh-book

# 1. 生成正文与站点
cat 00-front.md part1.md part2.md part3.md part4.md > dsh-book.md
cat en/00-front.md en/part1.md en/part2.md en/part3.md en/part4.md > en/dsh-book.md
python3 scripts/build-site.py

# 2. 本地检查
python3 - <<'PY'
from pathlib import Path
html = Path('docs/index.html').read_text()
assert '<script' not in html.lower(), 'site must not include JavaScript'
assert 'google-analytics' not in html.lower()
assert 'googletagmanager' not in html.lower()
print('site check ok:', len(html), 'chars')
PY

# 3. 提交
git add -A
git commit -m "docs: publish DeepSeek Harness beginner book"

# 4. 建公开仓库并推送
gh repo create leether/dsh-book \
  --public \
  --description "《DeepSeek Harness 入门》—— 给 0 基础用户的 DSH 使用指南" \
  --source . \
  --remote origin \
  --push
```

---

## 开启 GitHub Pages

仓库已有 `main` 分支和 `docs/index.html` 后，用 API 设置 Pages：

```bash
gh api --method POST repos/leether/dsh-book/pages \
  -H "Accept: application/vnd.github+json" \
  --input - <<'JSON'
{
  "source": {
    "branch": "main",
    "path": "/docs"
  }
}
JSON
```

如果已经开通过，接口会返回 409；改用 PUT：

```bash
gh api --method PUT repos/leether/dsh-book/pages \
  -H "Accept: application/vnd.github+json" \
  --input - <<'JSON'
{
  "source": {
    "branch": "main",
    "path": "/docs"
  }
}
JSON
```

也可以用网页操作：

```text
GitHub 仓库 → Settings → Pages
Source: Deploy from a branch
Branch: main
Folder: /docs
Save
```

---

## 确认部署

```bash
gh api repos/leether/dsh-book/pages \
  --jq '{status, html_url, source, build_type}'

curl -I https://leether.github.io/dsh-book/
```

- 首次启用通常需要 1–3 分钟；
- 如果返回 404，先等一分钟，再查 Pages 状态；
- `status: built` 表示构建完成；
- 中文入口 `/`，英文入口 `/en/`，右上角可切换；
- 页面内容来自 `docs/index.html` 与 `docs/en/index.html`，不需要 Jekyll 构建。

`docs/.nojekyll` 已存在，用于跳过 Jekyll 处理。

---

## 更新流程

```bash
# 改章节
vim part2.md

# 重新合并 + 生成站点
cat 00-front.md part1.md part2.md part3.md part4.md > dsh-book.md
cat en/00-front.md en/part1.md en/part2.md en/part3.md en/part4.md > en/dsh-book.md
python3 scripts/build-site.py

# 本地打开检查
open docs/index.html

# 提交并推送
git add -A
git commit -m "docs: update chapter 4"
git push
```

Pages 会在推送后自动更新；通常 1–2 分钟。

---

## 公开仓库的隐私与合规检查

发布前逐项确认：

```text
[ ] 没有真实 API Key、Token、密码、Cookie
[ ] 没有个人邮箱、电话、住址、账号截图
[ ] 没有本机绝对路径、用户名、私有仓库地址
[ ] 没有真实笔记、客户资料、聊天记录
[ ] 没有未授权的图片、字体、长段引用
[ ] 没有把 DeepSeek/DSH 说成“官方”
[ ] 示例中的项目名、文件名、对话均为虚构
[ ] 站点无 JavaScript、无统计、无外部字体/CDN
[ ] 中英页面可互相切换，hreflang / canonical 正确
[ ] 英文页除语言切换外没有残留中文
[ ] LICENSE 已包含，商标声明已写清
```

当前仓库的公开说明在 [README.md](README.md) 的“隐私与公开说明”。

---

## GitHub Pages 的限制

- 只能托管静态内容；没有服务端代码、数据库、私密 API；
- 站点是公开的，即使仓库以后改为 private，已发布的 Pages 仍可能可访问；
- 不要用 Pages 托管密钥、内部文档、客户数据；
- 大文件/大量流量受 GitHub 的软限制约束；
- 自定义域名需要额外配置 `CNAME` 与 DNS，本项目暂不需要。

---

## 常见问题

### 404

- 确认 Pages Source 是 `main` / `/docs`；
- 确认 `docs/index.html` 已提交；
- 等待 1–3 分钟；
- 看 `gh api repos/leether/dsh-book/pages` 的 `status`。

### 页面是旧内容

- 确认改完 `dsh-book.md` 后运行了 `scripts/build-site.py`；
- 确认提交的是 `docs/index.html`，不是只改 Markdown；
- 强制刷新浏览器。

### 页面样式丢失

- 样式内嵌在 `docs/index.html`，不应依赖外部 CSS；
- 检查生成脚本是否覆盖了模板；
- 本地打开 `docs/index.html` 对比。

### 想换主题/加目录

改 `scripts/build-site.py` 里的模板与 CSS，重新生成，不要直接手改 `docs/index.html`（会被覆盖）。
