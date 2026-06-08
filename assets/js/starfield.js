(function () {
  const canvas = document.getElementById('stars');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, stars = [];
  const mouse = { x: 0, y: 0 };

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function initStars() {
    stars = [];
    for (let i = 0; i < 280; i++) {
      const x = Math.random() * W;
      const y = Math.random() * H;
      stars.push({
        ox: x, oy: y,
        r: Math.random() * 1.5 + 0.3,
        alpha: Math.random() * 0.7 + 0.2,
        depth: Math.random() * 3 + 1,
        twinkle: Math.random() * Math.PI * 2,
        twinkleSpeed: 0.01 + Math.random() * 0.02,
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // Nebula glow — indigo
    const g1 = ctx.createRadialGradient(W * 0.3, H * 0.25, 0, W * 0.3, H * 0.25, W * 0.45);
    g1.addColorStop(0, 'rgba(67,56,202,0.12)');
    g1.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g1;
    ctx.fillRect(0, 0, W, H);

    // Nebula glow — sky blue
    const g2 = ctx.createRadialGradient(W * 0.75, H * 0.65, 0, W * 0.75, H * 0.65, W * 0.35);
    g2.addColorStop(0, 'rgba(14,165,233,0.08)');
    g2.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = g2;
    ctx.fillRect(0, 0, W, H);

    const cx = W / 2, cy = H / 2;
    const dx = (mouse.x - cx) / cx;
    const dy = (mouse.y - cy) / cy;

    for (const s of stars) {
      s.twinkle += s.twinkleSpeed;
      const a = s.alpha * (0.75 + 0.25 * Math.sin(s.twinkle));
      const px = s.ox + dx * s.depth * 18;
      const py = s.oy + dy * s.depth * 18;
      ctx.beginPath();
      ctx.arc(px, py, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${a})`;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  window.addEventListener('mousemove', (e) => { mouse.x = e.clientX; mouse.y = e.clientY; });
  window.addEventListener('resize', () => { resize(); initStars(); });

  resize();
  initStars();
  draw();
})();
