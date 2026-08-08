# Research & Engineering Portfolio

WANG Haoxin 的个人学术与工程主页源码，面向博士后申请、科研合作、科研机构及 FPGA / DAQ / 数字电子学研发岗位。网站坚持“科学问题 → 工程系统 → 测量 → 定量结果 → 技术输出”的叙事，并默认不公开未经确认的信息。

正式站点：<https://gutingguting.github.io>

## Tech Stack

- Astro + strict TypeScript
- Markdown / MDX Content Collections
- Native CSS
- KaTeX math rendering
- GitHub Pages + GitHub Actions

## Local Development

```bash
npm install
npm run dev
```

构建与检查：

```bash
npm run check
npm run build
npm run preview
```

## Project Structure

- `src/content/projects/`：工程项目 Markdown。
- `src/content/research/`：研究主题 Markdown。
- `src/content/notes/`：技术笔记 Markdown。
- `src/data/`：个人资料、教育、技能、论文和链接。
- `src/pages/`：网站路由。
- `public/`：CV、图片、favicon、robots 和社交分享图。
- `reports/site_delivery/`：中文交付与维护报告。

## Content Model

`src/content.config.ts` 定义 projects、research、notes 三个集合及 frontmatter 校验。构建阶段会拒绝不符合 schema 的内容，避免静默丢失。

## Daily Maintenance

1. 修改 `src/data/profile.ts` 更新姓名、简介、Current Focus 和公开链接。
2. 在相应 content 目录复制一个现有 Markdown 文件，修改 frontmatter 和正文。
3. 执行 `npm run check && npm run build`。
4. 提交并推送到 `main`，GitHub Pages 会自动更新。

## Add a Project

复制 `src/content/projects/full-data-readout.md`，使用新的英文 slug 文件名，填写 title、summary、role、status、tags、metrics 和正文十个标准章节。任何未验证指标必须留空或写为 `To be confirmed`。

## Add a Research Topic

复制 `src/content/research/recovered-clock-phase-uncertainty.md`，保持 Research Question、Method、Measurement Definition、Results、Interpretation、Limitations 等科学结构。

## Add a Publication

在 `src/data/publications.ts` 中添加经过核验的条目。DOI、PDF、Code、Slides 为空时不会显示按钮；确认前不得删除 `placeholder: true`。

## Add a Technical Note

在 `src/content/notes/` 新建 Markdown，选择 schema 允许的分类，并填写日期、阅读时间、摘要和标签。

## Replace CV

将批准公开的 PDF 放到 `public/documents/cv.pdf`，然后把 `src/pages/cv.astro` 中的 `cvAvailable` 改为 `true`。不要上传含私人电话、住址或不宜公开信息的版本。

## Add Images

图片按内容类型放入 `public/images/` 子目录。页面引用必须提供准确 alt；科研图发布前需要确认数据、版权和合作组授权。

## GitHub Pages Deployment

`.github/workflows/deploy.yml` 在 `main` 推送后执行 Astro 构建并部署。仓库 Settings → Pages 的 Source 应为 **GitHub Actions**。

## Privacy / Public Release Checklist

- [ ] Remove private IP addresses and server names
- [ ] Remove credentials, tokens, keys, and internal repository URLs
- [ ] Remove unpublished collaboration data and raw experiment data
- [ ] Verify image and PDF publication permissions
- [ ] Verify code ownership and third-party licenses
- [ ] Verify all publication claims and performance metrics
- [ ] Check external and internal links
- [ ] Run `npm run check`
- [ ] Run `npm run build`

详细使用、维护、发布、回滚与故障排查见：[交付与维护报告](reports/site_delivery/20260808_个人科研工程主页交付与维护报告.md)。

No open-source license is granted. All rights reserved.
