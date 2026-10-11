/* Better Everywhere conference page.
   Everything here is an enhancement: without it the page still shows the full
   agenda for both days, and slides stay hidden.

   To see the page as it will look at another time, add ?preview= to the address,
   for example ?preview=2026-10-20T13:05 (Nottingham time). */
(function () {
  "use strict";

  var TZ = "+01:00";
  var doc = document;
  doc.documentElement.classList.add("js");

  var params = new URLSearchParams(location.search);
  var preview = params.get("preview");
  var offset = 0;
  if (preview) {
    var stamp = /[zZ]|[+-]\d\d:\d\d$/.test(preview) ? preview : preview + (preview.length <= 16 ? ":00" : "") + TZ;
    var t = Date.parse(stamp);
    if (!isNaN(t)) offset = t - Date.now();
  }
  function now() { return Date.now() + offset; }

  var schedule = JSON.parse(doc.getElementById("schedule").textContent).map(function (s) {
    return { id: s.id, title: s.t, start: Date.parse(s.s), end: Date.parse(s.e), room: s.r, clock: s.c };
  });
  var groups = JSON.parse(doc.getElementById("groups").textContent);

  var first = schedule[0].start;
  var last = schedule[schedule.length - 1].end;
  var day2 = Date.parse("2026-10-21T00:00:00" + TZ);

  function $(sel, root) { return (root || doc).querySelector(sel); }
  function $all(sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); }
  function el(tag, cls, text) {
    var n = doc.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  /* ----- Stage: before, during, after ----- */

  var ORDER = {
    before: ["before", "agenda", "yours", "people", "venue", "getting", "help", "resources", "illustrator"],
    during: ["agenda", "yours", "venue", "help", "people", "getting", "before", "resources", "illustrator"],
    after: ["after", "agenda", "people", "help", "yours", "venue", "getting", "resources", "illustrator"]
  };
  var currentStage = null;

  function stage() {
    var n = now();
    // "During" starts the evening before so the agenda leads as people travel.
    if (n < first - 14 * 3600 * 1000) return "before";
    if (n <= last) return "during";
    return "after";
  }

  function applyStage() {
    var s = stage();
    if (s === currentStage) return;
    currentStage = s;
    doc.body.dataset.stage = s;
    var holder = doc.getElementById("sections");
    var after = doc.getElementById("after");
    var before = doc.getElementById("before");
    after.hidden = s !== "after";
    before.hidden = s === "after";
    ORDER[s].forEach(function (id) {
      var node = doc.getElementById(id);
      if (node) holder.appendChild(node);
    });
  }

  /* ----- Day tabs ----- */

  var tabs = $(".tabs");
  var days = $all(".day");
  var chosenDay = null;

  function showDay(key, byUser) {
    if (byUser) chosenDay = key;
    days.forEach(function (d) { d.hidden = d.id !== key; });
    $all("button", tabs).forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.dataset.day === key));
    });
  }

  if (tabs) {
    tabs.hidden = false;
    $all("button", tabs).forEach(function (b) {
      b.addEventListener("click", function () { showDay(b.dataset.day, true); });
    });
  }

  function autoDay() {
    if (chosenDay) return;
    showDay(now() >= day2 ? "day2" : "day1", false);
  }

  /* Open the right day and session when a link points at one. */
  function revealTarget() {
    var id = location.hash.slice(1);
    if (!id) return;
    var target = doc.getElementById(id);
    if (!target) return;
    var day = target.closest(".day");
    if (day) showDay(day.id, true);
    var d = target.matches("details") ? target : $("details", target);
    if (d && target.classList.contains("row")) d.open = true;
    // Open anything folded away around the target, such as a workbook page.
    for (var up = target.parentElement; up; up = up.parentElement) {
      if (up.tagName === "DETAILS") up.open = true;
    }
    target.scrollIntoView();
  }
  window.addEventListener("hashchange", revealTarget);

  /* ----- Now and next ----- */

  var nowBox = doc.getElementById("now");
  var nowHead = doc.getElementById("now-h");
  var nowLead = $(".now-lead", nowBox);
  var nowNext = $(".now-next", nowBox);

  function link(session) {
    var a = el("a", null, session.title);
    a.href = "#" + session.id;
    return a;
  }

  function updateNow() {
    var n = now();
    var current = null, next = null;
    schedule.forEach(function (s) {
      if (s.end > s.start && n >= s.start && n < s.end) current = s;
      if (!next && s.start > n) next = s;
    });

    $all(".row").forEach(function (row) {
      var st = Date.parse(row.dataset.start), en = Date.parse(row.dataset.end);
      row.classList.toggle("is-now", en > st && n >= st && n < en);
      row.classList.toggle("is-past", n >= en);
    });

    nowLead.textContent = "";
    nowNext.textContent = "";

    if (n > last) {
      nowHead.textContent = "The conference has finished";
      nowLead.textContent = "Slides from every session are in the agenda below.";
      return;
    }
    if (n < first) {
      nowHead.textContent = "Starts Tuesday 20 October";
      nowLead.textContent = "Registration opens at 9.30am and we start at 10.30am.";
      return;
    }
    if (current) {
      nowHead.textContent = "";
      nowHead.appendChild(el("span", "tag", "Now"));
      nowHead.appendChild(doc.createElement("br"));
      nowHead.appendChild(link(current));
      if (current.room) nowLead.textContent = current.room;
    } else {
      nowHead.textContent = n >= day2 ? "Day 2" : "Day 1";
    }
    if (next) {
      nowNext.appendChild(doc.createTextNode("Next at " + next.clock + ": "));
      nowNext.appendChild(link(next));
    }
  }

  /* ----- Slides: appear when the session starts ----- */

  function buildSlides(box) {
    var items = JSON.parse(box.dataset.slides);
    var label = box.dataset.label;
    var total = items.length;
    box.textContent = "";

    var strip = el("ul", "slides-strip");
    strip.tabIndex = 0;
    strip.setAttribute("role", "group");
    strip.setAttribute("aria-label", "Slides from " + label);
    items.forEach(function (it, i) {
      var li = el("li");
      var a = el("a");
      a.href = "slides/" + it.f;
      a.target = "_blank";
      a.rel = "noopener";
      var img = new Image();
      if (i > 0) img.loading = "lazy";
      img.decoding = "async";
      img.width = 1280;
      img.height = 720;
      img.src = "slides/" + it.f;
      img.alt = "Slide " + (i + 1) + " of " + total + ". " + (it.a || label);
      a.appendChild(img);
      li.appendChild(a);
      strip.appendChild(li);
    });
    box.appendChild(strip);

    if (total > 1) {
      var bar = el("div", "slides-bar");
      var prev = el("button", null, "Previous");
      var count = el("span", null, "1 of " + total);
      var next = el("button", null, "Next");
      prev.type = next.type = "button";
      prev.disabled = true;
      function index() { return Math.round(strip.scrollLeft / Math.max(1, strip.clientWidth)); }
      function go(i) {
        var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
        strip.scrollTo({ left: i * strip.clientWidth, behavior: reduce ? "auto" : "smooth" });
      }
      function sync() {
        var i = index();
        count.textContent = (i + 1) + " of " + total;
        prev.disabled = i <= 0;
        next.disabled = i >= total - 1;
      }
      prev.addEventListener("click", function () { go(index() - 1); });
      next.addEventListener("click", function () { go(index() + 1); });
      strip.addEventListener("scroll", function () { window.requestAnimationFrame(sync); }, { passive: true });
      bar.appendChild(prev);
      bar.appendChild(count);
      bar.appendChild(next);
      box.appendChild(bar);
    }
    box.dataset.open = "true";
  }

  function updateSlides() {
    var n = now();
    $all(".slides").forEach(function (box) {
      if (box.dataset.open) return;
      if (n >= Date.parse(box.dataset.unlock)) buildSlides(box);
    });
  }

  /* ----- Timed notes (for example the session choice deadline) ----- */

  function updateTimed() {
    var n = now();
    $all("[data-until]").forEach(function (x) { x.hidden = n > Date.parse(x.dataset.until); });
    $all("[data-from]").forEach(function (x) { x.hidden = n <= Date.parse(x.dataset.from); });
  }

  /* ----- Your sessions ----- */

  var select = doc.getElementById("county");
  var result = doc.getElementById("county-result");

  function slot(dl, when, title, where) {
    var wrap = el("div", "slot");
    wrap.appendChild(el("dt", null, when));
    var dd = el("dd");
    dd.appendChild(el("strong", null, where.room + ", " + where.group));
    dd.appendChild(doc.createTextNode(title + " with " + where.leads));
    wrap.appendChild(dd);
    dl.appendChild(wrap);
  }

  function showCounty(name) {
    var g = groups[name];
    result.textContent = "";
    if (!g) { result.hidden = true; return; }
    result.appendChild(el("h3", null, name));
    var dl = el("dl");
    slot(dl, "Day 1, Tuesday at 1.00pm", "Teamwork and Collaboration", g.d1);
    slot(dl, "Day 2, Wednesday at 12.00pm", "Lead, Manage, Do", g.d2);
    result.appendChild(dl);
    result.hidden = false;
  }

  if (select) {
    var saved = null;
    try { saved = localStorage.getItem("tcc26-county"); } catch (err) { /* private browsing */ }
    if (saved && groups[saved]) { select.value = saved; showCounty(saved); }
    select.addEventListener("change", function () {
      showCounty(select.value);
      try { localStorage.setItem("tcc26-county", select.value); } catch (err) { /* ignore */ }
    });
  }

  /* ----- Run ----- */

  function tick() {
    applyStage();
    autoDay();
    updateNow();
    updateSlides();
    updateTimed();
  }

  tick();
  revealTarget();
  setInterval(tick, 30000);
  doc.addEventListener("visibilitychange", function () { if (!doc.hidden) tick(); });
})();
