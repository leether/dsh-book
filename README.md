# 《DeepSeek Harness 入门》

## 从第一次对话到自己的插件

**给 0 基础用户的实用指南**

> **在线阅读**：<https://leether.github.io/dsh-book/>  
> **非官方指南**：本书不代表 DeepSeek 官方；DSH / DeepSeek 名称与商标归其权利人。

版本：2026-10  
参考环境：DeepSeek Harness Desktop 0.2.1-rc.2  
正文：[dsh-book.md](dsh-book.md) · 站点构建脚本：[scripts/build-site.py](scripts/build-site.py)

---

## 这本书写给谁

- 第一次接触 AI Agent，不知道“模型”和“Harness”有什么区别的人；
- 用过聊天机器人，但没让 AI 真正读写文件、跑命令、做项目的人；
- 想给 DSH 装技能、装插件，但被 Profile、Bundle、Preset 这些词吓住的人；
- 想用创造模式做一个小插件，但不知道从哪里开始的人。

前 7 章不需要编程基础。第 8 章开始会接触插件概念，第 9 章会进入“做插件”，但仍然以“描述目标、审查结果”为主。

---

## 读之前需要准备什么

1. 安装好 **DeepSeek Harness Desktop**；
2. 准备一个可用的模型服务（DeepSeek 官方 API，或其他兼容提供方）；
3. 在电脑上建一个**专门给 Agent 用的文件夹**，不要一上来就让它操作整个硬盘；
4. 记住一条：**Agent 会犯错，重要文件先备份，破坏性操作先确认。**

---

## 全书提纲

### 第 1 章　认识 DSH：模型、Harness、Agent

- Agent = Model + Harness
- DSH 是什么，不是什么
- 五个核心词：Agent、Session、Workspace、Tool、Skill
- 为什么需要 Harness
- Desktop / Web / Headless 三种入口

### 第 2 章　第一次启动：桌面、模型、工作区

- 打开 Desktop
- 连接模型与 API Key
- 选择工作区
- 选择标准模式
- 界面地图
- 第一次对话：只读、可观察

### 第 3 章　第一次任务：把需求说清楚

- 好任务的四个要素：目标、输入、约束、验收
- 先计划，再执行
- 看工具调用与文件改动
- 迭代与验收
- 用 `present` 交付文件

### 第 4 章　工作区、文件与权限

- Workspace 到底是什么
- Agent 能读什么、写什么
- `workspace-write` 与 `danger-full-access`
- 破坏性操作与备份
- 密钥、密码、截图
- `AGENTS.md`：给项目立规矩

### 第 5 章　会话、上下文与记忆

- Session 是什么
- Context Window 为什么会满
- DSH 不会自动记住一切
- 新会话 vs 继续会话
- 用文件、`AGENTS.md`、Skill 做“长期记忆”
- 上下文卫生

### 第 6 章　工具与技能：Agent 的手和脑

- 工具的分类：读、写、跑、搜、交付
- 工具调用卡片与审批
- 计划、待办、子代理、工作流
- Skill 是什么，和 Tool / Plugin 的区别
- 如何选择和使用 Skill
- `present` 的准确含义

### 第 7 章　模式与 Preset：同一个模型，不同工作方式

- Preset 是“能力组合”，不是模型
- 标准模式
- 创造模式
- PTC 模式
- 极简模式
- 如何选择
- 自定义 Preset 的正确方式

### 第 8 章　插件、Bundle 与 Profile：给 DSH 装能力

- Plugin 是运行时能力单元
- Bundle 是可分发的补丁包
- Profile 是安装环境
- 三者与 Preset 的关系
- 用 Plugin Manager 安装、启用、卸载
- 第三方插件的信任边界
- 常见故障

### 第 9 章　创造模式：从使用者到扩展者

- 创造模式到底是什么
- 它比标准模式多了什么
- 什么时候该用，什么时候不该用
- 一次完整的“做插件”流程
- 安全边界：代码在 Host 进程执行
- 不会编程的人怎么参与

### 第 10 章　排错、安全与继续学习

- 常见错误对照表
- 怎么读诊断信息
- 安全清单
- 成本与用量
- 继续练习的路线
- 一页纸速查

### 附录

- 术语表
- 10 个可直接套用的提示词模板
- 开始任务前的检查清单
- 一页纸速查表

---

## 三条阅读路线

| 你是 | 建议读 |
| --- | --- |
| 只想日常使用 | 第 1–7 章 |
| 想装别人做的插件/技能 | 第 1–8 章 |
| 想自己做插件 | 第 1–9 章 |
| 遇到问题 | 直接看第 10 章，再回头查相关章节 |

---

## 本书约定

- 以 **Desktop** 为主；Web 与 Headless 的差异放在“换一种入口”小栏里。
- “Agent”指正在工作的助手；“模型”指它背后的语言模型；“DSH”指 DeepSeek Harness。
- 示例中的文件名、项目名都是虚构的；不要把自己的 API Key、密码、私人文件贴进对话。
- 界面文字可能随版本变化；如果按钮名称不同，按功能找，不要死记位置。
- 书中的“安全做法”不是可选项。Agent 能执行真实操作，误操作会留下真实后果。


---

## 在线阅读与仓库

- **GitHub Pages**：<https://leether.github.io/dsh-book/>
- **GitHub 仓库**：<https://github.com/leether/dsh-book>
- **问题反馈**：<https://github.com/leether/dsh-book/issues>

GitHub Pages 使用 `main` 分支的 `docs/` 目录，纯静态 HTML，不需要构建服务。  
修改书稿后，运行：

```bash
python3 scripts/build-site.py
git add dsh-book.md docs/index.html
git commit -m "docs: refresh site"
git push
```

Pages 会在一两分钟内自动更新。

## 站点版式

- **封面式 Hero**：标题、副标题、阅读量、封面卡片和“开始阅读”入口；
- **桌面侧边目录**：章节导航随页面滚动保持可见；
- **移动端单列**：目录、正文、章节导航自动堆叠；
- **阅读节奏**：每章显示预计阅读时间、字数和小节数；
- **章节导航**：每章末尾有上一章/下一章；
- **纯 CSS 阅读进度条**：支持的浏览器顶部显示进度，不支持时自动隐藏；
- **明暗主题**：跟随系统 `prefers-color-scheme`；
- **打印样式**：隐藏导航，按章分页。

这些效果不依赖 JavaScript、Cookie、统计或外部字体/图片。

---

## 仓库结构

```text
.
├── README.md            # 本文件：提纲、阅读路线、公开说明
├── dsh-book.md          # 完整正文（10 章 + 附录）
├── 00-front.md          # 标题页与目录
├── part1.md … part4.md  # 分章节源文件
├── scripts/build-site.py # Markdown → 静态站点
├── docs/                # GitHub Pages 站点（main /docs）
│   ├── index.html
│   ├── favicon.svg
│   └── .nojekyll
├── PUBLISHING.md        # 发布与 Pages 设置记录
├── CONTRIBUTING.md      # 纠错与贡献
├── requirements.txt     # 站点构建依赖
└── LICENSE              # MIT
```

`dsh-book.md` 是 `00-front.md` + `part1.md` … `part4.md` 的合并稿。  
改章节时，建议改 `part*.md`，再重新生成合并稿：

```bash
cat 00-front.md part1.md part2.md part3.md part4.md > dsh-book.md
python3 -m pip install -r requirements.txt
python3 scripts/build-site.py
```

---

## 隐私与公开说明

这个仓库是公开的，因此：

- **不包含**任何真实 API Key、密码、Token、私人文件、个人笔记或本机绝对路径；
- 书中的项目名、文件名、对话示例均为虚构；
- 站点是**纯静态 HTML**：无 JavaScript、无 Cookie、无统计、无第三方字体或 CDN 请求；
- 页面只链接到 GitHub 仓库与 Pages 自身，不加载外部追踪资源；
- 本书是**非官方**学习材料，不代表 DeepSeek 官方文档或产品承诺；
- DSH / DeepSeek 的名称与商标归其权利人；本书仅作说明与教学用途；
- 书中的界面、按钮、版本行为可能随 DSH 版本变化，请以实际产品为准。

> 如果你要引用本书，请保留出处与许可证；如果发现内容错误，欢迎开 issue。

---

## 许可证

本书采用 **MIT License**，见 [LICENSE](LICENSE)。  
你可以复制、修改、分发，包括商业用途，但需保留版权与许可声明。  
书中的 DSH / DeepSeek 商标不随本许可证授予。
