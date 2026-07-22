(function () {
  var pad = document.querySelector("[data-rx-pad]");
  if (!pad) return;
  var label = document.querySelector("[data-rx-label]");
  var hint = document.querySelector("[data-rx-hint]");
  var roundEl = document.querySelector("[data-rx-round]");
  var lastEl = document.querySelector("[data-rx-last]");
  var avgEl = document.querySelector("[data-rx-avg]");
  var bestEl = document.querySelector("[data-rx-best]");
  var startBtn = document.querySelector("[data-rx-start]");

  var state = "idle"; // idle | wait | go | done
  var timer = null;
  var goAt = 0;
  var round = 0;
  var times = [];
  var best = null;
  try {
    var b = localStorage.getItem("acartechs_reflex_best");
    if (b) best = parseInt(b, 10);
  } catch (e) {}

  function fmt(ms) {
    if (ms == null || isNaN(ms)) return "—";
    return Math.round(ms) + " ms";
  }
  function hud() {
    if (roundEl) roundEl.textContent = round + " / 10";
    if (lastEl) lastEl.textContent = times.length ? fmt(times[times.length - 1]) : "—";
    if (avgEl) {
      if (!times.length) avgEl.textContent = "—";
      else {
        var s = 0;
        for (var i = 0; i < times.length; i++) s += times[i];
        avgEl.textContent = fmt(s / times.length);
      }
    }
    if (bestEl) bestEl.textContent = best == null ? "—" : fmt(best);
  }
  function setPad(mode, text) {
    pad.className = "acartechs-reflex-pad is-" + mode;
    if (label) label.textContent = text;
  }
  function clearT() {
    if (timer) {
      clearTimeout(timer);
      timer = null;
    }
  }
  function beginWait() {
    if (round >= 10) {
      state = "done";
      setPad("done", "Bitti");
      if (hint) hint.textContent = "10 tur tamam. Yeni tur ile tekrar dene.";
      return;
    }
    state = "wait";
    setPad("wait", "Bekle…");
    if (hint) hint.textContent = "Yeşili bekle. Erken basarsan tur yanar.";
    clearT();
    var delay = 900 + Math.random() * 2400;
    timer = setTimeout(function () {
      state = "go";
      goAt = performance.now();
      setPad("go", "ŞİMDİ!");
      if (hint) hint.textContent = "Hemen bas!";
    }, delay);
  }
  function onPad() {
    if (state === "idle" || state === "done") {
      times = [];
      round = 0;
      hud();
      beginWait();
      return;
    }
    if (state === "wait") {
      clearT();
      state = "idle";
      setPad("fail", "Erken!");
      if (hint) hint.textContent = "Çok erken bastın. Yeni tur ile tekrar dene.";
      return;
    }
    if (state === "go") {
      var ms = performance.now() - goAt;
      times.push(ms);
      round += 1;
      if (best == null || ms < best) {
        best = Math.round(ms);
        try {
          localStorage.setItem("acartechs_reflex_best", String(best));
        } catch (e) {}
      }
      hud();
      if (round >= 10) {
        state = "done";
        setPad("done", "Bitti");
        var s = 0;
        for (var i = 0; i < times.length; i++) s += times[i];
        if (hint) hint.textContent = "Ortalama " + fmt(s / times.length) + ". Harika.";
        return;
      }
      beginWait();
    }
  }
  pad.addEventListener("click", onPad);
  if (startBtn) {
    startBtn.addEventListener("click", function () {
      clearT();
      times = [];
      round = 0;
      hud();
      beginWait();
    });
  }
  hud();
  setPad("idle", "Başlat");
})();