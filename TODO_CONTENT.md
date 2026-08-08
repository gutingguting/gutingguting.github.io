# TODO — Public Content Confirmation

以下项目在获得用户明确确认前保持空白或占位，不阻塞网站构建：

- [ ] Institution and department
- [ ] Public email address
- [ ] GitHub profile URL
- [ ] Google Scholar profile
- [ ] ORCID
- [ ] Education institutions and dates
- [ ] Research and employment timeline
- [ ] Verified publications and author ordering
- [ ] Awards and professional activities
- [ ] Final public CV PDF
- [ ] Approved profile photograph
- [ ] Approved project and research figures
- [ ] Approved performance metrics with test conditions
- [ ] Public project repositories or document links
- [ ] Collaboration attribution and release permissions

## Replacement rule

不要把真实内容直接写死在组件中。个人资料更新 `src/data/`；项目、研究和笔记更新 `src/content/`。每次公开前重新执行 README 中的 Privacy / Public Release Checklist。
