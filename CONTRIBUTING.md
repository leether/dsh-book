# 纠错与贡献

这是一本公开的非官方 DSH 入门书。欢迎指出错误、补充例子、改进表达。

## 提交 issue

请尽量包含：

- 章节与小节标题；
- 你使用的 DSH 版本与平台（Desktop / Web / Headless）；
- 实际看到的现象；
- 你期望的正确说法；
- 如涉及界面，附上**脱敏后的**截图或步骤。

不要在 issue 里贴 API Key、Token、密码、私人文件、客户资料或本机绝对路径。

## 修改书稿

1. 章节源文件是 `part1.md` … `part4.md`，标题页是 `00-front.md`；
2. 修改后重新合并正文：
   ```bash
   cat 00-front.md part1.md part2.md part3.md part4.md > dsh-book.md
   ```
3. 重新生成站点：
   ```bash
   python3 -m pip install -r requirements.txt
   python3 scripts/build-site.py
   ```
4. 本地打开 `docs/index.html` 检查；
5. 不要直接手改 `docs/index.html`，它会被生成脚本覆盖；
6. 提交 PR，并在描述里说明改了哪一章、为什么。

## 内容边界

- 不收录真实个人数据、密钥、私有仓库内容；
- 不复制未授权的图片、字体或长段受版权保护的文本；
- 明确标注“非官方”，不要把本书写成 DeepSeek 官方文档；
- 示例使用虚构的文件名、项目名和对话。

## License

文字贡献默认按 CC BY-NC-ND 4.0 发布；代码贡献默认按 MIT 发布。商业出版需另行取得书面授权。
