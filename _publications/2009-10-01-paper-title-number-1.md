---
title: "角色介绍"  # 页面标题
layout: single    # 模板布局（必须保留）
---

<!-- 角色展示容器 -->
<div style="max-width: 1000px; margin: 20px auto; display: flex; gap: 30px; align-items: flex-start; flex-wrap: wrap;">
  <!-- 角色立绘 -->
  <div>
    <img src="images/you.png" 
         alt="YOU" 
         style="width: 300px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.15);">
  </div>

  <!-- 右侧内容区 -->
  <div style="flex: 1; min-width: 300px; position: relative;">
    <!-- 提问气泡按钮 -->
    <button id="questionBtn" 
            style="position: absolute; top: 0; right: 0; background: #ff7e67; color: white; border: none; border-radius: 50px; padding: 10px 20px; cursor: pointer; font-size: 14px; box-shadow: 0 2px 8px rgba(255,126,103,0.3);">
      对角色提问💬
    </button>

    <!-- 角色简介卡片 -->
    <div style="background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); margin-bottom: 20px;">
      <h2>角色名称</h2>
      <p>年龄：XX岁</p>
      <p>性格：活泼开朗</p>
      <p>背景：来自某个奇幻世界的冒险者...</p>
    </div>

    <!-- 提问输入框（默认隐藏） -->
    <div id="questionBox" style="display: none; background: white; padding: 18px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
      <input type="text" id="questionInput" placeholder="输入你的提问..." style="width: 80%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px;">
      <button id="submitQuestion" style="padding: 10px 20px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor: pointer; margin-left: 10px;">发送提问</button>
    </div>

    <!-- 提问&回复展示区 -->
    <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08);">
      <h3>大家的提问</h3>
      <div id="commentsList" style="margin-top: 15px;"></div>
    </div>
  </div>
</div>

<!-- 交互功能JS -->
<script>
  // 显示/隐藏提问框
  document.getElementById('questionBtn').onclick = function() {
    const box = document.getElementById('questionBox');
    box.style.display = box.style.display === 'none' ? 'block' : 'none';
  };

  // 提交提问
  document.getElementById('submitQuestion').onclick = function() {
    const question = document.getElementById('questionInput').value.trim();
    if (!question) { alert('请输入提问内容~'); return; }

    // 添加提问到列表
    const list = document.getElementById('commentsList');
    const item = document.createElement('div');
    item.style = "margin: 15px 0; padding: 12px; border-left: 3px solid #ff7e67; background: #fafafa; border-radius: 0 6px 6px 0;";
    item.innerHTML = `
      <strong>访客：</strong>${question}
      <button onclick="reply(this)" style="margin-left: 10px; background: #2196F3; color: white; border: none; border-radius: 4px; padding: 5px 10px; cursor: pointer; font-size: 12px;">回复</button>
      <div class="reply-area" style="display: none; margin-top: 8px; padding-left: 20px;"></div>
    `;
    list.appendChild(item);

    // 清空输入框
    document.getElementById('questionInput').value = '';
    document.getElementById('questionBox').style.display = 'none';
  };

  // 回复功能
  function reply(btn) {
    const area = btn.nextElementSibling;
    area.style.display = 'block';
    area.innerHTML = `
      <input type="text" placeholder="输入回复..." style="width: 70%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; font-size: 13px;">
      <button onclick="sendReply(this)" style="padding: 8px 15px; background: #4CAF50; color: white; border: none; border-radius: 4px; cursor: pointer; margin-left: 8px; font-size: 13px;">发送</button>
    `;
  }

  // 发送回复
  function sendReply(btn) {
    const reply = btn.previousElementSibling.value.trim();
    if (!reply) { alert('请输入回复内容~'); return; }

    const text = document.createElement('div');
    text.style = "margin-top: 8px;";
    text.innerHTML = `<strong>我：</strong>${reply}`;
    btn.parentElement.replaceWith(text);
  }
</script>
