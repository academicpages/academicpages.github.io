---
title: '学术主页使用指南(Academicpages usage guide in Chinese)'
date: 2022-02-06
permalink: /posts/2022/02/academicpages-usage-guide/
tags:
  - Guide
  - Chinese
---

这是中文版学术主页使用指南，旨在搭建一个托管在 [Github](http://github.com) 的学术主页。通过开源项目 [Academicpages](https://github.com/academicpages/academicpages.github.io) 和 Github 的 Github Pages 服务我们可以搭建一个**免费**、**简约**和**高度定制**的学术主页。

# 入门

1. 如果没有 [Github](http://github.com) 帐户，请注册一个 GitHub 帐户并确认电子邮件。
2. 通过单击右上角的“fork”按钮来创建[此存储库](https://github.com/academicpages/academicpages.github.io)的分叉。
3. 转到存储库的设置（以“代码”开头的选项卡中最右边的项目，应位于“取消监视”下方）。将存储库重命名为“[您的 GitHub 用户名].github.io”，这也是您网站的 URL。
4. 设置站点范围的配置并创建内容和元数据。
5. 将任何文件（如 PDF、.zip 文件等）上传到 files/ 目录。它们将出现在 https://[你的 GitHub 用户名].github.io/files/example.pdf。
6. 通过转到“GitHub 页面”部分中的存储库设置来检查状态。
7. （可选）使用 markdown_generator 文件夹中的 Jupyter 笔记本或 python 脚本从 TSV 文件生成用于出版物和讨论的 markdown 文件。

在 https://academicpages.github.io/ 上查看更多信息。

## 在本地运行

1. 克隆存储库并进行更新，如上所述。
2. 确保安装了 ruby-dev、bundler 和 nodejs：`sudo apt install ruby-dev ruby-bundler nodejs`。
3. 运行 `bundle clean` 清理目录（无需运行 `--force`）。
4. 运行 `bundle install` 来安装 ruby 依赖项。 如果出现错误，请删除 Gemfile.lock 并重试。
5. 运行 `bundle exec jekyll liveserve` 生成 HTML 并在 `localhost:4000` 提供服务，本地服务器将在更改时自动重建和刷新页面。

# 站点范围的配置

站点的主要配置文件 _config.yml 位于基本目录中，它定义了侧边栏中的内容和其他站点范围的功能。 您需要将默认变量替换为关于您自己和您网站的 github 存储库的变量。 顶部菜单的配置文件在 _data/navigation.yml 中。 例如，如果您没有文件夹或博客文章，则可以从该 navigation.yml 文件中删除这些项目，以将它们从标题中删除。

# 创建内容和元数据

对于网站内容，每种类型的内容都有一个 markdown 文件，这些文件存储在 _publications、_talks、_posts、_teaching 或 _pages 等目录中。 例如，每个演讲都是 _talks 目录中的一个 markdown 文件。 每个 markdown 文件的顶部是 YAML 中关于演讲的结构化数据，主题将解析这些数据以做很多很酷的事情。 有关演讲的相同结构化数据用于生成演讲页面上的演讲列表、特定演讲的每个单独页面、简历页面的演讲部分以及您进行演讲的地点地图（如果您运行 /talkmap.py 这个 python 文件或 /talkmap.ipynb 这个 Jupyter notebook 文件，它根据 _talks 目录的内容为地图创建 HTML）。

## markdown 生成器

创建了一组 Jupyter notebook 文件，可将包含有关演讲或演示的结构化数据的 CSV 转换为单独的 markdown 文件，这些文件将针对学术页面模板进行正确格式化。 该目录中的示例 CSV 是用来在 stuartgeiger.com 创建个人网站的那些。 通常的工作流程是保存出版物和演讲的 CSV，然后在这些notebook 中运行代码以生成 markdown 文件，然后提交并将它们推送到 GitHub 存储库。

# 如何编辑网站的 GitHub 存储库

许多人使用 git 客户端在本地计算机上创建文件，然后将它们推送到 GitHub 的服务器。 如果对 git 不熟悉，可以直接在 github.com 界面直接编辑这些配置和 markdown 文件。 导航到一个文件（像这个文件，然后单击内容预览右上角的铅笔图标（在“原始\|责任\|历史”按钮的右侧）。可以通过单击右侧的垃圾桶图标来删除文件 您还可以通过导航到目录并单击“创建新文件”或“上传文件”按钮来创建新文件或上传文件。

示例：为演讲编辑 Markdown 文件
![为演讲编辑 Markdown 文件](/images/editing-talk.png)

# 关键文件/目录的位置

* 基本配置选项: _config.yml
* 顶部导航栏配置: _data/navigation.yml
* 单页: _pages/
* 页面集合是 .md 或 .html 文件，位于:
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* 页脚: _includes/footer.html
* 静态文件（如 PDF）: /files/
* 个人资料图片（可以在_config.yml中设置）: images/profile.png

# 提示

* 将文件命名为“.md”以使其在 Markdown 中呈现，将其命名为“.html”以在 HTML 中呈现。
* 转到提交列表（在您的 repo 上）以找到使用 Jekyll 构建的最新版本的 Github。
  * 绿色对勾：成功构建
  * 橙色圆圈：建筑
  * 红色 X：错误
  * 无图标：未构建

# Markdown 指南

# 标题一

```
# 标题一
```

## 标题二

```
## 标题二
```

### 标题三

```
### 标题三
```

## 块引用

单行块引用：

```
> 引用很酷。
```

## 表

| 标题1 | 标题2 | 标题3 |
|:--------|:-------:|--------:|
| 项目1   | 项目2   | 项目3   |
| 项目4   | 项目5   | 项目6   |

```
| 标题1 | 标题2 | 标题3 |
|:--------|:-------:|--------:|
| 项目1   | 项目2   | 项目3   |
| 项目4   | 项目5   | 项目6   |
```

## 定义列表

定义列表一标题
:   定义列表一

定义列表二标题
:   定义列表二

```
定义列表一标题
:   定义列表一

定义列表二标题
:   定义列表二
```

## 无序列表（嵌套）

  * 列表项目一 
      * 列表项目一 
          * 列表项目一 
          * 列表项目二
      * 列表项目二
  * 列表项目二

```
  * 列表项目一 
      * 列表项目一 
          * 列表项目一 
          * 列表项目二
      * 列表项目二
  * 列表项目二
```

## 有序列表（嵌套）

  1. 列表项目一 
      1. 列表项目一 
          1. 列表项目一
          2. 列表项目二
      2. 列表项目二
  2. 列表项目二