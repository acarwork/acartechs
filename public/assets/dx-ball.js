/**
 * AcarTechs Dx Ball — polished breakout mini-game
 */
(function () {
  "use strict";

  var canvas = document.getElementById("acartechs-dxball");
  if (!canvas || !canvas.getContext) return;

  var ctx = canvas.getContext("2d");
  var dpr = Math.min(window.devicePixelRatio || 1, 2);

  var ui = {
    score: document.querySelector("[data-dx-score]"),
    best: document.querySelector("[data-dx-best]"),
    lives: document.querySelector("[data-dx-lives]"),
    level: document.querySelector("[data-dx-level]"),
    status: document.querySelector("[data-dx-status]"),
    start: document.querySelector("[data-dx-start]"),
    pause: document.querySelector("[data-dx-pause]"),
    reset: document.querySelector("[data-dx-reset]"),
  };

  var BASE_W = 520;
  var BASE_H = 680;
  var W = BASE_W;
  var H = BASE_H;

  var state = "ready"; // ready | running | paused | over | clear
  var raf = 0;
  var lastT = 0;
  var score = 0;
  var best = 0;
  var lives = 3;
  var level = 1;
  var combo = 0;
  var particles = [];
  var keys = { left: false, right: false };

  try {
    best = parseInt(localStorage.getItem("acartechs_dxball_best") || "0", 10) || 0;
  } catch (e) {}

  var paddle = { w: 110, h: 14, x: 0, y: 0, targetX: 0 };
  var ball = { r: 8.5, x: 0, y: 0, vx: 0, vy: 0, stuck: true };
  var bricks = [];
  var cols = 11;
  var rows = 7;
  var brickGap = 5;
  var brickTop = 88;
  var brickH = 20;

  var palette = [
    ["#7dd3fc", "#0ea5e9"],
    ["#38bdf8", "#0284c7"],
    ["#22d3ee", "#0891b2"],
    ["#60a5fa", "#2563eb"],
    ["#a78bfa", "#7c3aed"],
    ["#f472b6", "#db2777"],
    ["#fbbf24", "#d97706"],
  ];

    function resizeCanvas() {
    var parent = canvas.parentElement;
    var maxW = parent ? parent.clientWidth : BASE_W;
    var maxH = parent ? parent.clientHeight : BASE_H;
    if (!maxH || maxH < 200) maxH = Math.min(window.innerHeight * 0.72, BASE_H);
    var scale = Math.min(maxW / BASE_W, maxH / BASE_H, 1.15);
    scale = Math.max(0.55, scale);
    var displayW = Math.round(BASE_W * scale);
    var displayH = Math.round(BASE_H * scale);
    canvas.style.width = displayW + "px";
    canvas.style.height = displayH + "px";
    canvas.width = Math.round(BASE_W * dpr);
    canvas.height = Math.round(BASE_H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    W = BASE_W;
    H = BASE_H;
  }

  function brickW() {
    return (W - brickGap * (cols + 1)) / cols;
  }

  function buildBricks() {
    bricks = [];
    var w = brickW();
    var rCount = Math.min(8, rows + Math.floor((level - 1) / 2));
    for (var r = 0; r < rCount; r++) {
      for (var c = 0; c < cols; c++) {
        // mild pattern holes on higher levels
        if (level > 2 && (r + c + level) % 9 === 0) continue;
        var hp = r < 2 ? 2 : 1;
        if (level >= 4 && r === 0) hp = 3;
        bricks.push({
          x: brickGap + c * (w + brickGap),
          y: brickTop + r * (brickH + brickGap),
          w: w,
          h: brickH,
          hp: hp,
          maxHp: hp,
          colors: palette[r % palette.length],
        });
      }
    }
  }

  function resetPaddle() {
    paddle.w = Math.max(78, 110 - (level - 1) * 4);
    paddle.x = W / 2 - paddle.w / 2;
    paddle.targetX = paddle.x;
    paddle.y = H - 42;
  }

  function stickBall() {
    ball.stuck = true;
    ball.x = paddle.x + paddle.w / 2;
    ball.y = paddle.y - ball.r - 2;
    ball.vx = 0;
    ball.vy = 0;
  }

  function launchBall() {
    if (!ball.stuck) return;
    ball.stuck = false;
    var dir = Math.random() > 0.5 ? 1 : -1;
    var speed = 4.6 + level * 0.28;
    ball.vx = dir * speed * 0.72;
    ball.vy = -speed;
  }

  function spawnBurst(x, y, color, n) {
    for (var i = 0; i < (n || 8); i++) {
      var a = Math.random() * Math.PI * 2;
      var s = 1.2 + Math.random() * 3.2;
      particles.push({
        x: x,
        y: y,
        vx: Math.cos(a) * s,
        vy: Math.sin(a) * s,
        life: 0.35 + Math.random() * 0.35,
        max: 0.7,
        color: color,
        r: 1.5 + Math.random() * 2.2,
      });
    }
  }

  function hardReset() {
    score = 0;
    lives = 3;
    level = 1;
    combo = 0;
    particles = [];
    resetPaddle();
    buildBricks();
    stickBall();
    state = "ready";
    updateHud();
    setStatus("Hazır — tıkla veya Space ile başlat");
    draw(0);
  }

  function nextLevel() {
    level += 1;
    combo = 0;
    particles = [];
    resetPaddle();
    buildBricks();
    stickBall();
    state = "clear";
    updateHud();
    setStatus("Seviye " + level + " — devam için tıkla / Space");
  }

  function updateHud() {
    if (ui.score) ui.score.textContent = String(score);
    if (ui.best) ui.best.textContent = String(best);
    if (ui.lives) ui.lives.textContent = String(lives);
    if (ui.level) ui.level.textContent = String(level);
  }

  function setStatus(text) {
    if (ui.status) ui.status.textContent = text;
  }

  function saveBest() {
    if (score > best) {
      best = score;
      try {
        localStorage.setItem("acartechs_dxball_best", String(best));
      } catch (e) {}
      updateHud();
    }
  }

  function setPaddleFromClientX(clientX) {
    var rect = canvas.getBoundingClientRect();
    var x = ((clientX - rect.left) / rect.width) * W;
    paddle.targetX = Math.max(0, Math.min(W - paddle.w, x - paddle.w / 2));
  }

  canvas.addEventListener("mousemove", function (e) {
    setPaddleFromClientX(e.clientX);
  });
  canvas.addEventListener(
    "touchmove",
    function (e) {
      if (!e.touches || !e.touches[0]) return;
      e.preventDefault();
      setPaddleFromClientX(e.touches[0].clientX);
    },
    { passive: false }
  );
  canvas.addEventListener("click", function () {
    if (state === "ready" || state === "clear") startGame();
    else if (state === "over") hardReset();
    else if (state === "running" && ball.stuck) launchBall();
  });

  window.addEventListener("keydown", function (e) {
    if (e.code === "ArrowLeft" || e.code === "KeyA") keys.left = true;
    if (e.code === "ArrowRight" || e.code === "KeyD") keys.right = true;
    if (e.code === "Space") {
      e.preventDefault();
      if (state === "ready" || state === "clear" || state === "over") startGame();
      else if (state === "running" && ball.stuck) launchBall();
      else if (state === "running") pauseGame();
      else if (state === "paused") resumeGame();
    }
    if (e.code === "KeyP") {
      if (state === "running") pauseGame();
      else if (state === "paused") resumeGame();
    }
  });
  window.addEventListener("keyup", function (e) {
    if (e.code === "ArrowLeft" || e.code === "KeyA") keys.left = false;
    if (e.code === "ArrowRight" || e.code === "KeyD") keys.right = false;
  });

  function startGame() {
    if (state === "over") hardReset();
    if (state === "clear") {
      state = "running";
      stickBall();
      setStatus("Raketi hizala, tıkla / Space ile topu fırlat");
      loop(performance.now());
      return;
    }
    state = "running";
    if (ball.stuck) launchBall();
    setStatus("Oynanıyor");
    lastT = 0;
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(loop);
  }

  function pauseGame() {
    if (state !== "running") return;
    state = "paused";
    setStatus("Duraklatıldı — Space / P ile devam");
    cancelAnimationFrame(raf);
    draw(0);
  }

  function resumeGame() {
    if (state !== "paused") return;
    state = "running";
    setStatus("Oynanıyor");
    lastT = 0;
    raf = requestAnimationFrame(loop);
  }

  function loseLife() {
    lives -= 1;
    combo = 0;
    updateHud();
    saveBest();
    if (lives <= 0) {
      state = "over";
      setStatus("Oyun bitti — yeniden başlat");
      cancelAnimationFrame(raf);
      draw(0);
      return;
    }
    stickBall();
    setStatus("Can kaybı — tıkla / Space ile devam");
  }

  function update(dt) {
    // paddle
    if (keys.left) paddle.targetX -= 520 * dt;
    if (keys.right) paddle.targetX += 520 * dt;
    paddle.targetX = Math.max(0, Math.min(W - paddle.w, paddle.targetX));
    paddle.x += (paddle.targetX - paddle.x) * Math.min(1, 18 * dt);

    if (ball.stuck) {
      ball.x = paddle.x + paddle.w / 2;
      ball.y = paddle.y - ball.r - 2;
    } else {
      ball.x += ball.vx * 60 * dt;
      ball.y += ball.vy * 60 * dt;
      collide();
    }

    // particles
    for (var i = particles.length - 1; i >= 0; i--) {
      var p = particles[i];
      p.life -= dt;
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.08;
      if (p.life <= 0) particles.splice(i, 1);
    }
  }

  function collide() {
    if (ball.x - ball.r < 0) {
      ball.x = ball.r;
      ball.vx = Math.abs(ball.vx);
    } else if (ball.x + ball.r > W) {
      ball.x = W - ball.r;
      ball.vx = -Math.abs(ball.vx);
    }
    if (ball.y - ball.r < 0) {
      ball.y = ball.r;
      ball.vy = Math.abs(ball.vy);
    }
    if (ball.y - ball.r > H + 20) {
      loseLife();
      return;
    }

    // paddle
    if (
      ball.vy > 0 &&
      ball.y + ball.r >= paddle.y &&
      ball.y + ball.r <= paddle.y + paddle.h + 10 &&
      ball.x >= paddle.x - 2 &&
      ball.x <= paddle.x + paddle.w + 2
    ) {
      var hit = (ball.x - (paddle.x + paddle.w / 2)) / (paddle.w / 2);
      hit = Math.max(-1, Math.min(1, hit));
      var speed = Math.min(9.5, Math.sqrt(ball.vx * ball.vx + ball.vy * ball.vy) * 1.02);
      var angle = (-Math.PI / 2) + hit * 1.05;
      ball.vx = Math.cos(angle) * speed;
      ball.vy = Math.sin(angle) * speed;
      ball.y = paddle.y - ball.r - 1;
      combo = 0;
      spawnBurst(ball.x, paddle.y, "#26c9f4", 5);
    }

    // bricks
    for (var i = 0; i < bricks.length; i++) {
      var b = bricks[i];
      if (b.hp <= 0) continue;
      if (
        ball.x + ball.r > b.x &&
        ball.x - ball.r < b.x + b.w &&
        ball.y + ball.r > b.y &&
        ball.y - ball.r < b.y + b.h
      ) {
        var overlapL = ball.x + ball.r - b.x;
        var overlapR = b.x + b.w - (ball.x - ball.r);
        var overlapT = ball.y + ball.r - b.y;
        var overlapB = b.y + b.h - (ball.y - ball.r);
        var minX = Math.min(overlapL, overlapR);
        var minY = Math.min(overlapT, overlapB);
        if (minX < minY) {
          ball.vx *= -1;
          ball.x += ball.vx > 0 ? minX : -minX;
        } else {
          ball.vy *= -1;
          ball.y += ball.vy > 0 ? minY : -minY;
        }
        b.hp -= 1;
        combo += 1;
        var gain = 10 * level + Math.min(40, combo * 2);
        if (b.hp <= 0) {
          score += gain;
          spawnBurst(b.x + b.w / 2, b.y + b.h / 2, b.colors[0], 12);
        } else {
          score += Math.floor(gain / 3);
          spawnBurst(b.x + b.w / 2, b.y + b.h / 2, b.colors[1], 5);
        }
        updateHud();
        saveBest();
        break;
      }
    }

    var left = 0;
    for (var j = 0; j < bricks.length; j++) if (bricks[j].hp > 0) left++;
    if (left === 0) {
      score += 100 * level;
      updateHud();
      saveBest();
      nextLevel();
      cancelAnimationFrame(raf);
      draw(0);
    }
  }

  function loop(t) {
    if (state !== "running") return;
    if (!lastT) lastT = t;
    var dt = Math.min(0.033, (t - lastT) / 1000);
    lastT = t;
    update(dt);
    draw(dt);
    raf = requestAnimationFrame(loop);
  }

  function roundRect(x, y, w, h, r) {
    var rr = Math.min(r, w / 2, h / 2);
    ctx.beginPath();
    ctx.moveTo(x + rr, y);
    ctx.arcTo(x + w, y, x + w, y + h, rr);
    ctx.arcTo(x + w, y + h, x, y + h, rr);
    ctx.arcTo(x, y + h, x, y, rr);
    ctx.arcTo(x, y, x + w, y, rr);
    ctx.closePath();
  }

  function draw() {
    // backdrop
    var g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, "#04101f");
    g.addColorStop(0.55, "#072844");
    g.addColorStop(1, "#061b31");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // vignette + grid
    ctx.save();
    ctx.strokeStyle = "rgba(56,189,248,0.05)";
    ctx.lineWidth = 1;
    for (var gx = 0; gx < W; gx += 26) {
      ctx.beginPath();
      ctx.moveTo(gx, 0);
      ctx.lineTo(gx, H);
      ctx.stroke();
    }
    for (var gy = 0; gy < H; gy += 26) {
      ctx.beginPath();
      ctx.moveTo(0, gy);
      ctx.lineTo(W, gy);
      ctx.stroke();
    }
    ctx.restore();

    // top glass bar
    ctx.fillStyle = "rgba(15,23,42,0.55)";
    roundRect(12, 12, W - 24, 52, 12);
    ctx.fill();
    ctx.fillStyle = "rgba(255,255,255,0.92)";
    ctx.font = "700 13px Inter, system-ui, sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("DX BALL", 28, 36);
    ctx.fillStyle = "rgba(148,163,184,0.95)";
    ctx.font = "600 11px Inter, system-ui, sans-serif";
    ctx.fillText("AcarTechs Arcade", 28, 52);
    ctx.textAlign = "right";
    ctx.fillStyle = "#7dd3fc";
    ctx.font = "800 14px Inter, system-ui, sans-serif";
    ctx.fillText("Lv " + level + "  ·  " + score, W - 28, 44);

    // bricks
    for (var i = 0; i < bricks.length; i++) {
      var b = bricks[i];
      if (b.hp <= 0) continue;
      var bg = ctx.createLinearGradient(b.x, b.y, b.x, b.y + b.h);
      var alpha = b.hp / b.maxHp;
      bg.addColorStop(0, b.colors[0]);
      bg.addColorStop(1, b.colors[1]);
      ctx.globalAlpha = 0.55 + alpha * 0.45;
      ctx.fillStyle = bg;
      roundRect(b.x, b.y, b.w, b.h, 5);
      ctx.fill();
      ctx.globalAlpha = 0.25;
      ctx.fillStyle = "#fff";
      roundRect(b.x + 2, b.y + 2, b.w - 4, Math.max(3, b.h * 0.35), 3);
      ctx.fill();
      ctx.globalAlpha = 1;
      if (b.hp > 1) {
        ctx.fillStyle = "rgba(255,255,255,0.85)";
        ctx.font = "800 10px Inter, system-ui, sans-serif";
        ctx.textAlign = "center";
        ctx.fillText(String(b.hp), b.x + b.w / 2, b.y + b.h / 2 + 3);
      }
    }

    // paddle
    var pg = ctx.createLinearGradient(paddle.x, paddle.y, paddle.x, paddle.y + paddle.h);
    pg.addColorStop(0, "#67e8f9");
    pg.addColorStop(0.5, "#22d3ee");
    pg.addColorStop(1, "#0284c7");
    ctx.fillStyle = pg;
    ctx.shadowColor = "rgba(34,211,238,0.55)";
    ctx.shadowBlur = 14;
    roundRect(paddle.x, paddle.y, paddle.w, paddle.h, 8);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = "rgba(255,255,255,0.35)";
    roundRect(paddle.x + 8, paddle.y + 3, paddle.w - 16, 3, 2);
    ctx.fill();

    // ball
    ctx.beginPath();
    ctx.shadowColor = "rgba(125,211,252,0.8)";
    ctx.shadowBlur = 16;
    var bgall = ctx.createRadialGradient(
      ball.x - 2,
      ball.y - 2,
      1,
      ball.x,
      ball.y,
      ball.r
    );
    bgall.addColorStop(0, "#ffffff");
    bgall.addColorStop(0.55, "#e0f2fe");
    bgall.addColorStop(1, "#38bdf8");
    ctx.fillStyle = bgall;
    ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // particles
    for (var p = 0; p < particles.length; p++) {
      var pt = particles[p];
      ctx.globalAlpha = Math.max(0, pt.life / pt.max);
      ctx.fillStyle = pt.color;
      ctx.beginPath();
      ctx.arc(pt.x, pt.y, pt.r, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;

    // overlays
    if (state !== "running") {
      ctx.fillStyle = "rgba(2, 8, 20, 0.52)";
      ctx.fillRect(0, 0, W, H);
      ctx.textAlign = "center";
      ctx.fillStyle = "#fff";
      ctx.font = "800 30px Inter, system-ui, sans-serif";
      var title =
        state === "over"
          ? "Oyun Bitti"
          : state === "paused"
          ? "Duraklatıldı"
          : state === "clear"
          ? "Seviye Tamam"
          : "Dx Ball";
      ctx.fillText(title, W / 2, H / 2 - 18);
      ctx.font = "600 14px Inter, system-ui, sans-serif";
      ctx.fillStyle = "#94a3b8";
      var sub =
        state === "over"
          ? "Skor: " + score + "  ·  En iyi: " + best
          : state === "paused"
          ? "Space veya P ile devam et"
          : state === "clear"
          ? "Sonraki seviye için tıkla"
          : "Space / tıkla ile başla · ← → ile raket";
      ctx.fillText(sub, W / 2, H / 2 + 14);
    }
  }

  if (ui.start) {
    ui.start.addEventListener("click", function () {
      if (state === "paused") resumeGame();
      else startGame();
    });
  }
  if (ui.pause) {
    ui.pause.addEventListener("click", function () {
      if (state === "running") pauseGame();
      else if (state === "paused") resumeGame();
    });
  }
  if (ui.reset) {
    ui.reset.addEventListener("click", function () {
      cancelAnimationFrame(raf);
      hardReset();
    });
  }

  window.addEventListener("resize", function () {
    resizeCanvas();
    draw(0);
  });

  resizeCanvas();
  hardReset();
})();
