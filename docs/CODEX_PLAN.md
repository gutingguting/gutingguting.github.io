# `_research_engineering_portfolio` 实施基线

## 目标

建立可长期维护的 Research & Engineering Portfolio，采用 Astro、TypeScript、Markdown/MDX 和 GitHub Pages。网站面向博士后导师、科研机构、FPGA / DAQ / 数字电子研发岗位及技术同行。

## 决策

- 本地唯一源码：`D:\upgrade file\obsidian\obsidian_ori\codex\report\codex_projects\_research_engineering_portfolio`。
- GitHub 用户主页仓库：`gutingguting/gutingguting.github.io`。
- 视觉：白底、黑灰文字、浅灰边框、极少强调色，无 3D、粒子、技能条、Logo 墙或自动动画。
- 内容：组件和内容分离；未确认内容使用明显占位符；不虚构论文、指标、奖项或结果。
- 功能：纯静态站点，无数据库、后端、登录、CMS、分析、评论或自动抓取。
- 发布：`main` 推送触发 GitHub Actions 和 GitHub Pages。

## 第一版页面

Home、Research、Research detail、Projects、Project detail、Publications、Notes、Note detail、About、CV、404。

## 第一版内容

3 个项目占位、2 个研究主题、5 个技术笔记、论文数据模型、个人资料数据模型和集中式 TODO。

## 完成标准

类型检查与静态构建通过；主要页面在 375 / 768 / 1024 / 1440 px 可用；无凭据和内部信息；GitHub Actions 成功；正式站点可访问。
