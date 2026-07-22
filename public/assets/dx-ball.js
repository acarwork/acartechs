(function () {
  var canvas = document.getElementById("acartechs-dxball");
  if (!canvas) return;
  var ctx = canvas.getContext("2d");
  var scoreEl = document.querySelector("[data-dx-score]");
  var livesEl = document.querySelector("[data-dx-lives]");
  var levelEl = document.querySelector("[data-dx-level]");
  var startBtn = document.querySelector("[data-dx-start]");
  var resetBtn = document.querySelector("[data-dx-reset]");

  var W = canvas.width;
  var H = canvas.height;
  var running = false;
  var raf = 0;
  var score = 0;
  var lives = 3;
  var level = 1;

  var paddle = { w: 96, h: 14, x: W / 2 - 48, y: H - 36, speed: 9 };
  var ball = { r: 8, x: W / 2, y: H - 60, vx: 3.2, vy: -4.2 };
  var bricks = [];
  var cols = 10;
  var rows = 6;
  var brickGap = 4;
  var brickTop = 70;
  var brickH = 18;

  function brickW() {
    return (W - brickGap * (cols + 1)) / cols;
  }

  function colors() {
    return ["#26c9f4", "#2188f6", "#38bdf8", "#60a5fa", "#22d3ee", "#0ea5e9"];
  }

  function buildBricks() {
    bricks = [];
    var w = brickW();
    var c = colors();
    for (var r = 0; r < rows; r++) {
      for (var col = 0; col < cols; col++) {
        bricks.push({
          x: brickGap + col * (w + brickGap),
          y: brickTop + r * (brickH + brickGap),
          w: w,
          h: brickH,
          alive: true,
          color: c[r % c.length]
        });
      }
    }
  }

  function resetBall() {
    ball.x = paddle.x + paddle.w / 2;
    ball.y = paddle.y - ball.r - 2;
    var dir = Math.random() > 0.5 ? 1 : -1;
    ball.vx = dir * (3 + level * 0.35);
    ball.vy = -(4 + level * 0.25);
  }

  function hardReset() {
    score = 0;
    lives = 3;
    level = 1;
    paddle.w = 96;
    buildBricks();
    resetBall();
    running = false;
    updateHud();
    draw();
  }

  function updateHud() {
    if (scoreEl) scoreEl.textContent = "Skor: " + score;
    if (livesEl) livesEl.textContent = "Can: " + lives;
    if (levelEl) levelEl.textContent = "Seviye: " + level;
  }

  function setPaddleFromClientX(clientX) {
    var rect = canvas.getBoundingClientRect();
    var x = ((clientX - rect.left) / rect.width) * W;
    paddle.x = Math.max(0, Math.min(W - paddle.w, x - paddle.w / 2));
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

  function collide() {
    // walls
    if (ball.x - ball.r < 0) {
      ball.x = ball.r;
      ball.vx *= -1;
    }
    if (ball.x + ball.r > W) {
      ball.x = W - ball.r;
      ball.vx *= -1;
    }
    if (ball.y - ball.r < 0) {
      ball.y = ball.r;
      ball.vy *= -1;
    }
    // bottom
    if (ball.y - ball.r > H) {
      lives -= 1;
      updateHud();
      if (lives <= 0) {
        running = false;
        draw(true);
        return;
      }
      resetBall();
      return;
    }
    // paddle
    if (
      ball.vy > 0 &&
      ball.y + ball.r >= paddle.y &&
      ball.y + ball.r <= paddle.y + paddle.h + 8 &&
      ball.x >= paddle.x &&
      ball.x <= paddle.x + paddle.w
    ) {
      var hit = (ball.x - (paddle.x + paddle.w / 2)) / (paddle.w / 2);
      ball.vx = hit * 5.2;
      ball.vy = -Math.abs(ball.vy);
      ball.y = paddle.y - ball.r - 1;
    }
    // bricks
    for (var i = 0; i < bricks.length; i++) {
      var b = bricks[i];
      if (!b.alive) continue;
      if (
        ball.x + ball.r > b.x &&
        ball.x - ball.r < b.x + b.w &&
        ball.y + ball.r > b.y &&
        ball.y - ball.r < b.y + b.h
      ) {
        b.alive = false;
        score += 10 * level;
        // bounce direction
        var overlapL = ball.x + ball.r - b.x;
        var overlapR = b.x + b.w - (ball.x - ball.r);
        var overlapT = ball.y + ball.r - b.y;
        var overlapB = b.y + b.h - (ball.y - ball.r);
        var minX = Math.min(overlapL, overlapR);
        var minY = Math.min(overlapT, overlapB);
        if (minX < minY) ball.vx *= -1;
        else ball.vy *= -1;
        updateHud();
        break;
      }
    }
    // level clear
    var left = 0;
    for (var j = 0; j < bricks.length; j++) if (bricks[j].alive) left++;
    if (left === 0) {
      level += 1;
      if (paddle.w > 64) paddle.w -= 6;
      rows = Math.min(8, rows);
      buildBricks();
      resetBall();
      updateHud();
    }
  }

  function step() {
    if (!running) return;
    ball.x += ball.vx;
    ball.y += ball.vy;
    // slight speed clamp
    var sp = Math.sqrt(ball.vx * ball.vx + ball.vy * ball.vy);
    var max = 8.5 + level * 0.3;
    if (sp > max) {
      ball.vx = (ball.vx / sp) * max;
      ball.vy = (ball.vy / sp) * max;
    }
    collide();
    draw();
    raf = requestAnimationFrame(step);
  }

  function draw(gameOver) {
    // bg
    var g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, "#061b31");
    g.addColorStop(1, "#0b2a4a");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // grid dots
    ctx.fillStyle = "rgba(38,201,244,0.08)";
    for (var y = 20; y < H; y += 28) {
      for (var x = 16; x < W; x += 28) {
        ctx.beginPath();
        ctx.arc(x, y, 1.2, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    // bricks
    for (var i = 0; i < bricks.length; i++) {
      var b = bricks[i];
      if (!b.alive) continue;
      ctx.fillStyle = b.color;
      roundRect(b.x, b.y, b.w, b.h, 4);
      ctx.fill();
    }

    // paddle
    ctx.fillStyle = "#26c9f4";
    roundRect(paddle.x, paddle.y, paddle.w, paddle.h, 8);
    ctx.fill();
    ctx.fillStyle = "#2188f6";
    roundRect(paddle.x + 4, paddle.y + 3, paddle.w - 8, 4, 3);
    ctx.fill();

    // ball
    ctx.beginPath();
    ctx.fillStyle = "#ffffff";
    ctx.shadowColor = "rgba(38,201,244,0.7)";
    ctx.shadowBlur = 12;
    ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // overlays
    if (!running) {
      ctx.fillStyle = "rgba(2,8,20,0.45)";
      ctx.fillRect(0, 0, W, H);
      ctx.fillStyle = "#fff";
      ctx.font = "bold 28px Inter, Arial, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(gameOver || lives <= 0 ? "Oyun Bitti" : "Dx Ball", W / 2, H / 2 - 10);
      ctx.font = "16px Inter, Arial, sans-serif";
      ctx.fillStyle = "#9fb2c8";
      ctx.fillText(lives <= 0 ? "Sifirla veya Baslat" : "Baslat ile oyna", W / 2, H / 2 + 22);
    }
  }

  function roundRect(x, y, w, h, r) {
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.arcTo(x + w, y, x + w, y + h, r);
    ctx.arcTo(x + w, y + h, x, y + h, r);
    ctx.arcTo(x, y + h, x, y, r);
    ctx.arcTo(x, y, x + w, y, r);
    ctx.closePath();
  }

  if (startBtn) {
    startBtn.addEventListener("click", function () {
      if (lives <= 0) hardReset();
      if (!running) {
        running = true;
        cancelAnimationFrame(raf);
        raf = requestAnimationFrame(step);
      }
    });
  }
  if (resetBtn) {
    resetBtn.addEventListener("click", function () {
      cancelAnimationFrame(raf);
      hardReset();
    });
  }

  buildBricks();
  resetBall();
  updateHud();
  draw();
})();