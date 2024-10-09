---
permalink: /
title: "Academic Pages is a ready-to-fork GitHub Pages template for academic personal websites"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>奢华星空爱情语</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: radial-gradient(
            circle at center,
            rgba(30, 30, 50, 0.5),
            rgba(10, 10, 20, 0.8)
          ),
          url("https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80")
            no-repeat center center fixed;
        background-size: cover;
        font-family: "Lato", sans-serif;
        overflow: hidden;
        filter: brightness(0.7);
      }

      #love-messages-container {
        background: linear-gradient(
          to bottom right,
          rgba(128, 128, 255, 0.1),
          rgba(255, 128, 128, 0.1)
        );
        backdrop-filter: blur(50px);
        border-radius: 60px;
        padding: 80px;
        box-shadow: 0 50px 100px rgba(0, 0, 0, 0.6);
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 80%;
        text-align: center;
      }

      p.love-message {
        font-size: 32px;
        color: #fff;
        text-shadow: 3px 3px 8px rgba(0, 0, 0, 0.7);
        margin: 40px 0;
        letter-spacing: 2px;
        line-height: 1.8;
        opacity: 0;
        animation: fadeIn 1.5s ease forwards;
      }

      p.love-message:hover {
        transform: scale(1.1);
        text-shadow: 5px 5px 12px rgba(0, 0, 0, 0.8);
      }

      #refresh-button {
        position: fixed;
        bottom: 50px;
        right: 120px;
        background-color: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(30px);
        border: none;
        border-radius: 50%;
        width: 80px;
        height: 80px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.6);
        font-size: 36px;
        color: #fff;
        text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.7);
      }

      .love-heart {
        position: absolute;
        font-size: 60px;
        opacity: 0;
        transition: all 0.7s ease;
        animation: fallDown 5s linear forwards;
      }

      @keyframes fadeIn {
        from {
          opacity: 0;
          transform: translateY(40px);
        }

        to {
          opacity: 1;
          transform: translateY(0);
        }
      }

      @keyframes fallDown {
        from {
          top: -70px;
          opacity: 0.8;
        }

        to {
          top: 130%;
          opacity: 0;
        }
      }
    </style>
  </head>

  <body>
    <div id="love-messages-container"></div>
    <button id="refresh-button">&#10084;</button>
    <script>
      let clickCount = 0;
      document
        .getElementById("refresh-button")
        .addEventListener("click", function () {
          generateRandomLoveMessages();
          const heartContainer = document.body;
          let heartContent;
          if (clickCount % 2 === 0) {
            heartContent = "M💖";
          } else {
            heartContent = "Y💖";
          }
          const heart = document.createElement("div");
          heart.classList.add("love-heart");
          heart.textContent = heartContent;
          heart.style.top = Math.random() * 75 + "%";
          heart.style.left = Math.random() * 75 + "%";
          // 确保新生成的爱心不与已有爱心位置重叠
          const existingHearts = document.querySelectorAll(".love-heart");
          for (const existingHeart of existingHearts) {
            if (
              Math.abs(existingHeart.offsetTop - heart.offsetTop) < 70 &&
              Math.abs(existingHeart.offsetLeft - heart.offsetLeft) < 70
            ) {
              heart.style.top = Math.random() * 75 + "%";
              heart.style.left = Math.random() * 75 + "%";
              break;
            }
          }
          heartContainer.appendChild(heart);
          heart.style.opacity = 1;
          clickCount++;
        });

      function generateRandomLoveMessages() {
        const loveMessagesContainer = document.getElementById(
          "love-messages-container"
        );
        loveMessagesContainer.innerHTML = "";
        const allLoveMessages = [
          "Always by your side.（永远在你身边。）",
          "Be mine forever.（永远属于我。）",
          "Cherish every moment.（珍惜每一刻。）",
          "Deep love endures.（深爱持久。）",
          "Embrace our love.（拥抱我们的爱。）",
          "Forever in love.（永远相爱。）",
          "Gentle love shines.（温柔的爱闪耀。）",
          "Hold me tight.（紧紧抱住我。）",
          "Infinite love.（无尽的爱。）",
          "Joyful love grows.（快乐的爱成长。）",
          "Kindness in love.（爱中的善良。）",
          "Love lasts forever.（爱永恒。）",
          "My heart is yours.（我的心属于你。）",
          "Never let go.（永不放手。）",
          "Our love is strong.（我们的爱很强烈。）",
          "Passionate love burns.（激情的爱燃烧。）",
          "Quiet love endures.（安静的爱持久。）",
          "Radiant love shines.（灿烂的爱闪耀。）",
          "Sweet love endures.（甜蜜的爱持久。）",
          "True love conquers.（真爱征服一切。）",
          "United by love.（因爱而团结。）",
          "Vibrant love lives.（充满活力的爱存在。）",
          "Warm love surrounds.（温暖的爱围绕。）",
          "XOXO, love you.（亲亲抱抱，爱你。）",
          "Yearning for you.（渴望你。）",
          "Zealous love burns.（热情的爱燃烧。）",
          "Adore and cherish.（崇拜和珍惜。）",
          "Affection blooms.（爱意绽放。）",
          "Always connected.（永远相连。）",
          "Admire your love.（钦佩你的爱。）",
          "Allure of love.（爱的诱惑。）",
          "Affectionate touch.（深情的触摸。）",
          "Always glowing.（永远发光。）",
          "Admiring hugs.（令人羡慕的拥抱。）",
          "Alluring eyes.（迷人的眼睛。）",
          "Adorable kisses.（可爱的吻。）",
          "Always kind.（永远善良。）",
          "Alluring love.（迷人的爱。）",
          "Admired moments.（令人钦佩的时刻。）",
          "Affectionate nights.（深情的夜晚。）",
          "Always on my mind.（永远在我心中。）",
          "Affectionate promise.（深情的承诺。）",
          "Always quiet.（永远安静。）",
          "Admiring rays.（令人钦佩的光芒。）",
          "Affectionate smile.（深情的微笑。）",
          "Always true.（永远真实。）",
          "Adorable union.（可爱的结合。）",
          "Alluring view.（迷人的景色。）",
          "Always warm.（永远温暖。）",
          "Always xoxo.（永远亲亲抱抱。）",
          "Always yearning.（永远渴望。）",
          "Always zealous.（永远热情。）",
          "Beautiful affection.（美丽的感情。）",
          "Blissful bond.（幸福的纽带。）",
          "Brilliant connection.（辉煌的联系。）",
          "Beloved devotion.（心爱的奉献。）",
          "Bright eyes.（明亮的眼睛。）",
          "Beautiful forever.（永远美丽。）",
          "Blissful glow.（幸福的光芒。）",
          "Beautiful hugs.（美丽的拥抱。）",
          "Brilliant illumination.（辉煌的照明。）",
          "Beautiful joy.（美丽的喜悦。）",
          "Blissful kindness.（幸福的善良。）",
          "Beautiful love.（美丽的爱。）",
          "Beloved memories.（心爱的回忆。）",
          "Blissful nights.（幸福的夜晚。）",
          "Beautifully one.（美丽地合一。）",
          "Blissful promise.（幸福的承诺。）",
          "Beautifully quiet.（美丽地安静。）",
          "Beautiful rays.（美丽的光芒。）",
          "Blissful smile.（幸福的微笑。）",
          "Beautifully true.（美丽地真实。）",
          "Beautiful union.（美丽的结合。）",
          "Brilliant view.（辉煌的景色。）",
          "Beautifully warm.（美丽地温暖。）",
          "Beautiful xoxo.（美丽的亲亲抱抱。）",
          "Beautiful yearning.（美丽的渴望。）",
          "Beautifully zealous.（美丽地热情。）",
          "Captivating affection.（迷人的感情。）",
          "Cherished bond.（珍贵的纽带。）",
          "Compassionate connection.（富有同情心的联系。）",
          "Constant devotion.（始终如一的奉献。）",
          "Charming eyes.（迷人的眼睛。）",
          "Cherished forever.（永远珍惜。）",
          "Comforting glow.（令人安慰的光芒。）",
          "Caring hugs.（关怀的拥抱。）",
          "Captivating illumination.（迷人的照明。）",
          "Charming joy.（迷人的喜悦。）",
          "Compassionate kindness.（富有同情心的善良。）",
          "Captivating love.（迷人的爱。）",
          "Cherished moments.（珍贵的时刻。）",
          "Comforting nights.（令人安慰的夜晚。）",
          "Compassionately one.（富有同情心地合一。）",
          "Cherished promise.（珍贵的承诺。）",
          "Comfortingly quiet.（令人安慰地安静。）",
          "Captivating rays.（迷人的光芒。）",
          "Charming smile.（迷人的微笑。）",
          "Compassionately true.（富有同情心地真实。）",
          "Captivating union.（迷人的结合。）",
          "Charming view.（迷人的景色。）",
          "Comfortingly warm.（令人安慰地温暖。）",
          "Captivating xoxo.（迷人的亲亲抱抱。）",
          "Charming yearning.（迷人的渴望。）",
          "Captivating zealous.（迷人地热情。）",
          "Enchanting love.（迷人的爱。）",
          "Faithful devotion.（忠诚的奉献。）",
          "Glorious love.（光荣的爱。）",
          "Heavenly affection.（天堂般的感情。）",
          "Innocent love.（纯真的爱。）",
          "Loyal love.（忠诚的爱。）",
          "Magical love.（神奇的爱。）",
          "Nurturing love.（培育的爱。）",
          "Optimistic love.（乐观的爱。）",
          "Passionate embrace.（激情的拥抱。）",
          "Romantic love.（浪漫的爱。）",
          "Serene love.（宁静的爱。）",
          "Tender love.（温柔的爱。）",
          "Unique love.（独特的爱。）",
          "Vivid love.（生动的爱。）",
          "Whimsical love.（异想天开的爱。）",
          "Yearning embrace.（渴望的拥抱。）",
          "Zestful love.（充满热情的爱。）",
        ];
        const selectedMessages = [];
        while (selectedMessages.length < 6) {
          const randomIndex = Math.floor(
            Math.random() * allLoveMessages.length
          );
          const message = allLoveMessages[randomIndex];
          if (!selectedMessages.includes(message)) {
            selectedMessages.push(message);
          }
        }
        selectedMessages.forEach((message) => {
          const lovePhrase = document.createElement("p");
          lovePhrase.classList.add("love-message");
          lovePhrase.textContent = message;
          loveMessagesContainer.appendChild(lovePhrase);
        });
      }

      generateRandomLoveMessages();
    </script>
  </body>
</html>

------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
