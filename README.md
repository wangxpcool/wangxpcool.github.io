# wangxp 的个人博客

纯静态 HTML / CSS / JavaScript，适用于现有 GitHub Pages 根目录部署。页面无需 Node.js、第三方 CDN 或运行时服务；旧文章 URL 保留。

## 本地预览

```sh
python -m http.server 4173 --bind 127.0.0.1
```

打开 http://127.0.0.1:4173 。

## 更新内容

- `data/posts.json`：首页文章顺序、标题、链接、分类、日期、摘要。日期沿用原文；未知日期留空。支持分类：技术、算法、随笔。
- `scripts/build.py`：首页、关于页、笔记目录的模板和共享导航。
- `css/site.css`、`js/site.js`：新版目录页样式与搜索筛选。禁用 JavaScript 时仍能阅读完整文章列表。
- `blogs/`、`notes/`：历史正文；`css/article.css` 为共享阅读样式，旧文章暂保留 Bootstrap。
- `Theme/`、`myResume.html`：历史简历，独立保留。

更新文章索引或模板后运行：

```sh
python scripts/build.py
```

将生成的 HTML 与源文件一起提交，GitHub Pages 直接提供静态文件，无需新增构建配置。部署仍使用仓库原有的 Pages 分支和目录设置。

本轮移除了目录页的旧音乐、IP 城市脚本和动画依赖，修复了文章页缺失脚本引用与 HTTP jQuery 加载；历史正文中的外部链接及现有文章统计脚本仍保留。
