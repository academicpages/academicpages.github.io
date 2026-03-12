---
permalink: /
layout: splash        # use the splash layout for a hero image
title: "Shaofeng Guo"
author_profile: true
header:
  overlay_image: /images/hero.jpg   # replace with your hero photo
  overlay_color: "#000000"
  overlay_opacity: 0.5
redirect_from: 
  - /about/
  - /about.html
---

欢迎来到我的个人网站！我是来自合肥工业大学的计算机科学博士研究生，
研究方向为图像取证和视觉推理。这里展示我的论文、报告、教程以及
与多媒体安全分析相关的项目。

## 📬 联系方式
- email: [1kingto1top@gmail.com](mailto:1kingto1top@gmail.com)
- Google Scholar: [我的主页](https://scholar.google.com/citations?hl=en&user=UBCS-zsAAAAJ&scilu=&scisig=ACUpqDcAAAAAaLsDrdC3shQ3rrUcQRgOmDFymqA&gmla=AH8HC4yIMt86aRUoS4xW8WS_nOh5v8Y57XYbVi_PusYdCqmy2dQ6fM2YppnuAA3TuedBpNqTl6CWV7AVn9KkUNUoRuhafY2NzrJRVTU&sciund=6415130130695938645)
- GitHub: [battle1king](https://github.com/battle1king)

下面是一份中文使用指南，帮助你日后修改和维护本站。

## 📌 站点配置
- 全局设置在根目录的 `_config.yml`。
- 修改站点标题(`title`)、描述(`description`)、URL、仓库名等。
- 在 `author:` 部分填写个人信息：头像(`avatar`)、邮箱(`email`)、简历(`bio`)、所在地(`location`)等。
- 添加或删除社交链接；不使用的平台可以删掉对应行（已删除 Bluesky）。
- 导航菜单可通过 `_data/navigation.yml` 调整顺序和显隐。

## 🛠 内容编辑
- 各类内容放在固定文件夹：
  - 博客：`_posts/`（文件名 `YYYY-MM-DD-title.md`）。
  - 论文：`_publications/`。
  - 报告/演讲：`_talks/`。
  - 教学资料：`_teaching/`。
  - 作品集：`_portfolio/`。
- 每个 Markdown 文件首部有 YAML 元数据，例如 `title`、`date`、`tags`。
- 可以用 `markdown_generator/` 里的 Jupyter 笔记本从表格批量生成。

## 📂 图片和附件
- 上传图片到 `images/`，引用路径 `/images/xxx.jpg`。
- 文件如 PDF、压缩包放 `files/`，访问路径 `/files/yourfile.pdf`。

## 🎨 自定义样式
- 在 `_sass/_custom.scss` 写 Sass/CSS 覆盖默认主题。
  ```scss
  $color-accent: #e91e63;
  @import "minimal-mistakes";
  ```
- 主题变量详见 Minimal Mistakes 文档。

## 🔍 本地预览和部署
1. 安装 Ruby 和 Bundler，然后执行：
   ```sh
   bundle install
   bundle exec jekyll serve -l -H localhost
   ```
2. 打开 `http://localhost:4000` 查看效果，保存后页面会自动刷新。
3. 修改完成后 `git commit` 并推送到 GitHub，Pages 会自动构建并上线。

希望这份中文指南能帮你管理未来的内容。欢迎随时在主页加新文章或更新设置！
