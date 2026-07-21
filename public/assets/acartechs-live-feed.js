/**
 * AcarTechs live feed + son dakika bandı
 * - Does not rebuild page layout
 * - Only updates existing marquee/feed nodes + optional breaking strip above live-strip
 */
(function () {
  if (window.__acarLiveFeed) return;
  window.__acarLiveFeed = true;

  var FEED_URL = "/data/live-feed.json";
  var POLL_MS = 75000;
  var BREAKING_MAX_AGE_H = 12;
  var lastUpdatedAt = "";
  var knownIds = Object.create(null);

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  function relTime(iso) {
    if (!iso) return null;
    var d = new Date(iso);
    if (isNaN(d.getTime())) {
      // date-only fallback
      d = new Date(iso + "T12:00:00");
    }
    if (isNaN(d.getTime())) return null;
    var diff = Math.round((Date.now() - d.getTime()) / 1000);
    if (diff < 0) diff = 0;
    if (diff < 90) return "az önce";
    if (diff < 3600) return Math.floor(diff / 60) + " dk önce";
    if (diff < 86400) return Math.floor(diff / 3600) + " saat önce";
    if (diff < 86400 * 2) return "dün";
    if (diff < 86400 * 7) return Math.floor(diff / 86400) + " gün önce";
    return null;
  }

  function ageHours(iso) {
    var d = new Date(iso);
    if (isNaN(d.getTime())) d = new Date(String(iso).slice(0, 10) + "T12:00:00");
    if (isNaN(d.getTime())) return 9999;
    return (Date.now() - d.getTime()) / 3600000;
  }

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function ensureBreakingShell() {
    var existing = document.querySelector(".acartechs-breaking");
    if (existing) return existing;

    var live = document.querySelector(".acartechs-live-strip");
    if (!live || !live.parentNode) return null;

    var bar = document.createElement("section");
    bar.className = "acartechs-breaking";
    bar.setAttribute("aria-label", "Son dakika");
    bar.innerHTML =
      '<span class="acartechs-breaking-pill">Son dakika</span>' +
      '<div class="acartechs-breaking-track" data-breaking-track></div>';
    live.parentNode.insertBefore(bar, live);
    return bar;
  }

  function ensureUpdatedLabel(liveStrip) {
    if (!liveStrip) return null;
    var el = liveStrip.querySelector(".acartechs-live-updated");
    if (el) return el;
    el = document.createElement("small");
    el.className = "acartechs-live-updated";
    el.setAttribute("aria-live", "polite");
    var strong = liveStrip.querySelector("strong");
    if (strong) {
      strong.appendChild(el);
    } else {
      liveStrip.appendChild(el);
    }
    return el;
  }

  function renderBreaking(items) {
    var bar = ensureBreakingShell();
    if (!bar) return;

    var fresh = (items || []).filter(function (it) {
      return it && it.breaking && ageHours(it.iso || it.date) <= BREAKING_MAX_AGE_H;
    }).slice(0, 3);

    var track = bar.querySelector("[data-breaking-track]");
    if (!fresh.length) {
      bar.classList.remove("is-on");
      if (track) track.innerHTML = "";
      return;
    }

    track.innerHTML = fresh
      .map(function (it) {
        var cat = it.categoryLabel || it.category || "";
        return (
          '<a href="' +
          esc(it.url) +
          '">' +
          (cat ? "<span>" + esc(cat) + "</span>" : "") +
          esc(it.title) +
          "</a>"
        );
      })
      .join("");
    bar.classList.add("is-on");
  }

  function renderMarquee(items) {
    var track = document.querySelector(".acartechs-live-track");
    if (!track || !items || !items.length) return;

    var list = items.slice(0, 10);
    // Keep marquee motion: duplicate content if site CSS expects long track
    var html = list
      .map(function (it) {
        return (
          '<a href="' +
          esc(it.url) +
          '"><span>' +
          esc(it.categoryLabel || it.category || "Haber") +
          "</span> " +
          esc(it.title) +
          "</a>"
        );
      })
      .join("");
    track.innerHTML = html + html;
  }

  function buildArticle(it, isNew) {
    var article = document.createElement("article");
    if (isNew) article.className = "is-live-new";
    var rel = relTime(it.iso || it.date) || it.dateLabel || it.date || "";
    var img = it.image
      ? '<img class="acartechs-feed-image" src="' +
        esc(it.image) +
        '" alt="' +
        esc(it.title) +
        '">'
      : "";
    article.innerHTML =
      '<a href="' +
      esc(it.url) +
      '"><div><h3>' +
      esc(it.title) +
      "</h3>" +
      (it.excerpt ? "<p>" + esc(it.excerpt) + "</p>" : "") +
      "<span>Acartechs Editör <time datetime=\"" +
      esc(it.date || "") +
      '" data-acar-date>' +
      esc(rel) +
      "</time></span></div>" +
      img +
      "</a>";
    return article;
  }

  function renderFeed(items, isFirstPaint) {
    var feed = document.querySelector(".acartechs-news-feed");
    if (!feed || !items || !items.length) return;

    var titleRow = feed.querySelector(".acartechs-section-title");
    var existing = Array.prototype.slice.call(feed.querySelectorAll("article"));
    var existingHrefs = {};
    existing.forEach(function (art) {
      var a = art.querySelector("a[href]");
      if (a) existingHrefs[a.getAttribute("href")] = true;
    });

    // First successful live paint: only sync known ids, don't rebuild whole feed
    // (preserves SSR structure / images already on page)
    if (isFirstPaint) {
      items.forEach(function (it) {
        knownIds[it.id || it.url] = true;
      });
      // Soft-update times only
      existing.forEach(function (art) {
        var time = art.querySelector("time[datetime]");
        if (!time) return;
        var r = relTime(time.getAttribute("datetime"));
        if (r) {
          if (!time.dataset.original) time.dataset.original = time.textContent.trim();
          time.textContent = r;
        }
      });
      return;
    }

    // Subsequent polls: prepend brand-new items only
    var newestFirst = items.slice();
    var toPrepend = [];
    newestFirst.forEach(function (it) {
      var key = it.id || it.url;
      var href = it.url;
      if (knownIds[key] || existingHrefs[href]) {
        knownIds[key] = true;
        return;
      }
      knownIds[key] = true;
      toPrepend.push(it);
    });

    if (!toPrepend.length) return;

    // Insert after section title, newest of the new batch first
    var anchor = titleRow ? titleRow.nextSibling : feed.firstChild;
    toPrepend.reverse().forEach(function (it) {
      var node = buildArticle(it, true);
      feed.insertBefore(node, anchor);
      anchor = node.nextSibling;
      // remove "Yeni" class after a while
      setTimeout(function () {
        node.classList.remove("is-live-new");
      }, 12000);
    });

    // Keep feed from growing unbounded
    var all = feed.querySelectorAll("article");
    for (var i = all.length - 1; i >= 12; i--) {
      all[i].parentNode.removeChild(all[i]);
    }
  }

  function setUpdatedLabel(updatedAt) {
    var live = document.querySelector(".acartechs-live-strip");
    var label = ensureUpdatedLabel(live);
    if (!label) return;
    var r = relTime(updatedAt);
    label.textContent = r ? "Güncellendi · " + r : "Canlı gündem";
  }

  function applyPayload(data, isFirstPaint) {
    if (!data || !Array.isArray(data.items)) return;
    if (data.updatedAt && data.updatedAt === lastUpdatedAt && !isFirstPaint) return;
    lastUpdatedAt = data.updatedAt || lastUpdatedAt;

    renderBreaking(data.items);
    renderMarquee(data.items);
    renderFeed(data.items, isFirstPaint);
    setUpdatedLabel(data.updatedAt || data.items[0] && data.items[0].iso);
  }

  function fetchFeed(isFirstPaint) {
    if (document.hidden && !isFirstPaint) return;
    var url = FEED_URL + (FEED_URL.indexOf("?") >= 0 ? "&" : "?") + "t=" + Date.now();
    fetch(url, { credentials: "same-origin", cache: "no-cache" })
      .then(function (res) {
        if (!res.ok) throw new Error("feed " + res.status);
        return res.json();
      })
      .then(function (data) {
        applyPayload(data, !!isFirstPaint);
      })
      .catch(function () {
        /* silent: keep static SSR content */
      });
  }

  ready(function () {
    // Only run where live strip or news feed exists (homepage primarily)
    if (
      !document.querySelector(".acartechs-live-strip") &&
      !document.querySelector(".acartechs-news-feed")
    ) {
      return;
    }

    fetchFeed(true);
    setInterval(function () {
      fetchFeed(false);
    }, POLL_MS);

    document.addEventListener("visibilitychange", function () {
      if (!document.hidden) fetchFeed(false);
    });
  });
})();
