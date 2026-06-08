---
layout: blog
title: Blog
permalink: /blog/
---

<div class="blog-header">
  <h1>Blog</h1>
  <p>记录研究感悟 · 技术思考 · 日常随笔</p>
</div>

<div class="tags-bar">
  <span class="tag-filter active" data-tag="all">全部</span>
  <span class="tag-filter" data-tag="研究感悟">研究感悟</span>
  <span class="tag-filter" data-tag="技术思考">技术思考</span>
  <span class="tag-filter" data-tag="日常随笔">日常随笔</span>
</div>

<div class="posts-grid" id="posts-grid">
  {%- for post in site.posts -%}
    <a href="{{ post.url | relative_url }}" class="post-card"
       data-tags="{{ post.tags | join: ',' }}">
      {%- if post.tags and post.tags.size > 0 -%}
        <span class="card-tag">{{ post.tags[0] }}</span>
      {%- endif -%}
      <h3>{{ post.title }}</h3>
      {%- if post.excerpt -%}
        <p class="card-excerpt">{{ post.excerpt | strip_html | truncate: 100 }}</p>
      {%- endif -%}
      <div class="card-meta">
        <span>{{ post.date | date: "%Y-%m-%d" }}</span>
        <span class="read-more">阅读 →</span>
      </div>
    </a>
  {%- endfor -%}
</div>

<script>
document.querySelectorAll('.tag-filter').forEach(function(btn) {
  btn.addEventListener('click', function() {
    document.querySelectorAll('.tag-filter').forEach(function(b) { b.classList.remove('active'); });
    btn.classList.add('active');
    var tag = btn.dataset.tag;
    document.querySelectorAll('.post-card').forEach(function(card) {
      if (tag === 'all') {
        card.style.display = '';
      } else {
        var tags = card.dataset.tags ? card.dataset.tags.split(',') : [];
        card.style.display = tags.indexOf(tag) !== -1 ? '' : 'none';
      }
    });
  });
});
</script>
