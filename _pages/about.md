---
permalink: /
title: "关于我"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<section class="home-hero">
  <p class="home-eyebrow">Academic homepage</p>
  <h1>投入产出技术、企业供应链与碳排放研究</h1>
  <p class="home-hero__lead">
    我是张欣洋，目前关注投入产出技术、微观企业供应链与碳排放相关问题。我的研究尝试连接宏观产业关联与微观企业行为，刻画供应链网络中的依赖结构、风险传导和环境影响。
  </p>
  <div class="home-actions">
    <a class="btn btn--large" href="{{ '/research/' | relative_url }}">查看研究方向</a>
    <a class="btn btn--large btn--inverse" href="{{ '/publications/' | relative_url }}">浏览论文</a>
  </div>
</section>

<section class="home-section">
  <div class="home-section__head">
    <p class="home-eyebrow">Research focus</p>
    <h2>研究方向</h2>
  </div>

  <div class="home-card-grid">
    <article class="home-card">
      <span class="home-card__icon"><i class="fas fa-diagram-project" aria-hidden="true"></i></span>
      <h3>投入产出与产业关联</h3>
      <p>利用投入产出表、供给使用表和产业链数据，识别部门间生产依赖、关键路径与冲击传导机制。</p>
    </article>
    <article class="home-card">
      <span class="home-card__icon"><i class="fas fa-network-wired" aria-hidden="true"></i></span>
      <h3>微观企业供应链网络</h3>
      <p>结合企业层面的交易、生产和经营信息，分析供应链网络结构、关键节点和风险扩散路径。</p>
    </article>
    <article class="home-card">
      <span class="home-card__icon"><i class="fas fa-leaf" aria-hidden="true"></i></span>
      <h3>碳排放核算与绿色转型</h3>
      <p>从生产网络视角追踪隐含碳排放，评估减排政策对企业、行业和区域的异质性影响。</p>
    </article>
  </div>
</section>

<section class="home-section home-section--split">
  <div>
    <p class="home-eyebrow">Questions</p>
    <h2>当前关注的问题</h2>
  </div>
  <ul class="home-checklist">
    <li>如何将投入产出模型与企业微观供应链数据结合，刻画更细粒度的产业关联结构？</li>
    <li>供应链冲击如何沿企业网络和产业链条传导，并影响产出、价格和排放？</li>
    <li>企业和行业的碳排放责任如何在生产链条中分解和追踪？</li>
    <li>在“双碳”目标下，如何评估不同减排政策对企业、行业和区域的异质性影响？</li>
  </ul>
</section>

<section class="home-section">
  <div class="home-section__head">
    <p class="home-eyebrow">Methods</p>
    <h2>研究方法</h2>
  </div>
  <div class="home-chip-list">
    <span>投入产出分析</span>
    <span>结构分解分析</span>
    <span>生产网络模型</span>
    <span>企业微观数据处理</span>
    <span>复杂网络分析</span>
    <span>碳排放核算</span>
    <span>政策情景模拟</span>
    <span>数据可视化</span>
  </div>
</section>

<section class="home-section home-updates">
  <div class="home-section__head">
    <p class="home-eyebrow">Updates</p>
    <h2>近期更新</h2>
  </div>

  <div class="home-update-grid">
    <article class="home-update-card">
      <h3>近期论文</h3>
      {% if site.publications.size > 0 %}
        <ul>
          {% for post in site.publications reversed limit:3 %}
            <li>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              {% if post.venue %}<span>{{ post.venue }}</span>{% endif %}
              {% if post.date %}<time>{{ post.date | date: "%Y" }}</time>{% endif %}
            </li>
          {% endfor %}
        </ul>
        <a class="home-more-link" href="{{ '/publications/' | relative_url }}">查看更多论文</a>
      {% else %}
        <p>论文与工作论文将陆续更新。</p>
      {% endif %}
    </article>

    <article class="home-update-card">
      <h3>最新文章</h3>
      {% if site.posts.size > 0 %}
        <ul>
          {% for post in site.posts limit:3 %}
            <li>
              <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
              {% if post.date %}<time>{{ post.date | date: "%Y-%m-%d" }}</time>{% endif %}
            </li>
          {% endfor %}
        </ul>
        <a class="home-more-link" href="{{ '/year-archive/' | relative_url }}">查看全部文章</a>
      {% else %}
        <p>研究笔记与文章将陆续更新。</p>
      {% endif %}
    </article>
  </div>
</section>

<section class="home-section">
  <div class="home-callout">
    <div>
      <p class="home-eyebrow">Contact</p>
      <h2>欢迎交流与合作</h2>
      <p>如果你对投入产出技术、企业供应链网络、碳排放核算或相关数据方法感兴趣，欢迎通过邮件联系我。</p>
    </div>
    <a class="btn btn--large" href="mailto:zhangxinyang@amss.ac.cn">zhangxinyang@amss.ac.cn</a>
  </div>
</section>
