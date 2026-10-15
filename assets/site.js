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
    before: ["before", "agenda", "yours", "slido", "people", "venue", "getting", "help", "resources", "illustrator"],
    during: ["agenda", "yours", "slido", "people", "venue", "help", "getting", "before", "resources", "illustrator"],
    after: ["after", "agenda", "yours", "slido", "people", "venue", "getting", "help", "resources", "illustrator"]
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
    var named = ORDER[s];
    var unnamed = $all("#sections > section").filter(function (node) {
      return named.indexOf(node.id) === -1 && node.id !== "after";
    });
    named.forEach(function (id) {
      var node = doc.getElementById(id);
      if (node) holder.appendChild(node);
    });
    // Anything the list above does not name stays at the foot of the page.
    unnamed.forEach(function (node) { holder.appendChild(node); });
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

  function buildFilm(box) {
    var frame = doc.createElement("iframe");
    frame.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(box.dataset.id) + "?rel=0";
    frame.title = box.dataset.title;
    frame.allow = "accelerometer; encrypted-media; picture-in-picture; fullscreen";
    frame.allowFullscreen = true;
    frame.loading = "lazy";
    box.textContent = "";
    box.appendChild(frame);
    var p = el("p", "hint");
    var a = el("a", null, "Watch on YouTube");
    a.href = "https://youtu.be/" + encodeURIComponent(box.dataset.id);
    a.rel = "noopener";
    p.appendChild(a);
    box.appendChild(p);
    box.dataset.open = "true";
  }

  function updateSlides() {
    var n = now();
    $all(".yt").forEach(function (box) {
      if (!box.dataset.open && n >= Date.parse(box.dataset.unlock)) buildFilm(box);
    });
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
    if (g.d2) slot(dl, "Day 2, Wednesday at 12.00pm", "Lead, Manage, Do", g.d2);
    else {
      var wrap = el("div", "slot");
      wrap.appendChild(el("dt", null, "Day 2"));
      wrap.appendChild(el("dd", null, "Your County FA is booked for Day 1 only. If that has changed, ask at registration for your Lead, Manage, Do group."));
      dl.appendChild(wrap);
    }
    result.appendChild(dl);
    result.hidden = false;
  }

  /* By name: breakout workshop and pillar */

  var peopleEl = doc.getElementById("people-data");
  var people = peopleEl ? JSON.parse(peopleEl.textContent) : {};
  var personSelect = doc.getElementById("person");
  var personResult = doc.getElementById("person-result");

  function personSlot(dl, when, title, x) {
    var wrap = el("div", "slot");
    wrap.appendChild(el("dt", null, when));
    var dd = el("dd");
    dd.appendChild(el("strong", null, x.r));
    var line = title;
    if (x.role === "lead") line += ". You are leading this session";
    else if (x.role === "facilitator") line += ". You are facilitating";
    else if (x.l) line += " with " + x.l;
    dd.appendChild(doc.createTextNode(line));
    wrap.appendChild(dd);
    dl.appendChild(wrap);
  }

  function showPerson(name) {
    var p = people[name];
    personResult.textContent = "";
    if (!p) { personResult.hidden = true; return; }
    personResult.appendChild(el("h3", null, name));
    var dl = el("dl");
    if (p.w) personSlot(dl, "Day 1, Tuesday at 11.00am, breakout workshop", p.w.t, p.w);
    if (p.p) personSlot(dl, "Day 1, Tuesday at 2.00pm, Pillar Networking", p.p.t, p.p);
    personResult.appendChild(dl);
    personResult.hidden = false;
  }

  if (personSelect) {
    var savedPerson = null;
    try { savedPerson = localStorage.getItem("tcc26-person"); } catch (err) { /* private browsing */ }
    if (savedPerson && people[savedPerson]) { personSelect.value = savedPerson; showPerson(savedPerson); }
    personSelect.addEventListener("change", function () {
      showPerson(personSelect.value);
      try { localStorage.setItem("tcc26-person", personSelect.value); } catch (err) { /* ignore */ }
      // Fill in the County FA too, when we know it.
      var c = people[personSelect.value] && people[personSelect.value].c;
      if (c && select && groups[c] && !select.value) {
        select.value = c;
        showCounty(c);
        try { localStorage.setItem("tcc26-county", c); } catch (err) { /* ignore */ }
      }
    });
  }

  /* By County FA: group sessions */

  if (select) {
    var saved = null;
    try { saved = localStorage.getItem("tcc26-county"); } catch (err) { /* private browsing */ }
    if (saved && groups[saved]) { select.value = saved; showCounty(saved); }
    select.addEventListener("change", function () {
      showCounty(select.value);
      try { localStorage.setItem("tcc26-county", select.value); } catch (err) { /* ignore */ }
    });
  }

  /* ----- Without signal ----- */

  // Keep a copy of the page on the phone (see sw.js).
  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("sw.js").catch(function () { /* the page works without it */ });
    });
  }

  var offline = el("div", "offline");
  offline.setAttribute("role", "status");
  offline.appendChild(el("div", "wrap", "No signal. You are seeing the copy saved on this device. Times and slides still work."));
  var jump = $(".jump");
  if (jump && jump.parentNode) jump.parentNode.insertBefore(offline, jump.nextSibling);
  function updateOffline() { offline.hidden = navigator.onLine !== false; }
  window.addEventListener("online", updateOffline);
  window.addEventListener("offline", updateOffline);
  updateOffline();

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
