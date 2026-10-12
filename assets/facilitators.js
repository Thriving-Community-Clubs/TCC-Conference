/* Opens the facilitator page. The content is stored encrypted in the page
   (AES-GCM, key derived from the passcode with PBKDF2) and is only readable
   with the right passcode. */
(function () {
  "use strict";

  var KEY = "tcc26-facilitator-passcode";
  var payload = JSON.parse(document.getElementById("payload").textContent);
  var form = document.getElementById("unlock");
  var input = document.getElementById("code");
  var remember = document.getElementById("remember");
  var msg = document.getElementById("lock-msg");
  var lock = document.getElementById("lock");
  var content = document.getElementById("content");
  var button = form.querySelector("button");

  function bytes(b64) {
    var bin = atob(b64), out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }

  /* Forgiving about capitals, spaces and stray punctuation between words. */
  function tidy(code) {
    return code.trim().toLowerCase().replace(/[\s_.,]+/g, "-").replace(/-+/g, "-");
  }

  function decrypt(code) {
    var enc = new TextEncoder();
    return crypto.subtle.importKey("raw", enc.encode(tidy(code)), "PBKDF2", false, ["deriveKey"])
      .then(function (base) {
        return crypto.subtle.deriveKey(
          { name: "PBKDF2", salt: bytes(payload.salt), iterations: payload.iter, hash: "SHA-256" },
          base, { name: "AES-GCM", length: 256 }, false, ["decrypt"]);
      })
      .then(function (key) {
        return crypto.subtle.decrypt({ name: "AES-GCM", iv: bytes(payload.iv) }, key, bytes(payload.data));
      })
      .then(function (plain) { return new TextDecoder().decode(plain); });
  }

  function store(code) {
    try { localStorage.setItem(KEY, code); } catch (err) { /* private browsing */ }
  }
  function forget() {
    try { localStorage.removeItem(KEY); } catch (err) { /* ignore */ }
  }
  function saved() {
    try { return localStorage.getItem(KEY); } catch (err) { return null; }
  }

  function show(html) {
    content.innerHTML = html;
    content.hidden = false;
    lock.hidden = true;
    try { enhance(); } catch (err) { /* the page still reads without these extras */ }
    var id = location.hash.slice(1);
    var target = id && document.getElementById(id);
    if (target) target.scrollIntoView();
  }

  function attempt(code, quiet) {
    if (!window.crypto || !crypto.subtle) {
      msg.textContent = "This browser can't open the page. Try a current version of Safari, Chrome or Edge.";
      return;
    }
    button.disabled = true;
    if (!quiet) msg.textContent = "Opening…";
    decrypt(code).then(function (html) {
      if (remember.checked || quiet) store(code); else forget();
      msg.textContent = "";
      show(html);
    }).catch(function () {
      button.disabled = false;
      if (quiet) { forget(); msg.textContent = ""; return; }
      msg.textContent = "That passcode didn't open the page. Check it and try again.";
      input.focus();
      input.select();
    });
  }

  /* ----- Extras that work on the opened page ----- */

  var NAME_KEY = "tcc26-facilitator-name";
  var DAYS = { "2026-10-19": "Monday 19 October", "2026-10-20": "Day 1, Tuesday 20 October", "2026-10-21": "Day 2, Wednesday 21 October" };
  var VENUE = "East Midlands Conference Centre, Beeston Lane, Nottingham NG7 2RJ";

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function clock(hhmm) {
    var p = hhmm.split(":"), h = +p[0];
    return (h % 12 || 12) + "." + p[1] + (h < 12 ? "am" : "pm");
  }
  function joinNames(list) {
    if (list.length < 2) return list.join("");
    return list.slice(0, -1).join(", ") + " and " + list[list.length - 1];
  }

  /* Calendar file, built on the phone so nothing leaves the locked page. */
  function utc(day, hhmm) {
    return new Date(day + "T" + hhmm + ":00+01:00").toISOString().replace(/[-:]/g, "").replace(/\.\d+/, "");
  }
  function esc(v) { return String(v).replace(/\\/g, "\\\\").replace(/;/g, "\;").replace(/,/g, "\\,").replace(/\n/g, "\\n"); }
  function calendar(name, events) {
    var stamp = utc(new Date().toISOString().slice(0, 10), "00:00");
    var lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Thriving Community Clubs//Facilitators 2026//EN", "METHOD:PUBLISH", "X-WR-CALNAME:" + esc(name)];
    events.forEach(function (ev) {
      lines.push("BEGIN:VEVENT", "UID:" + ev.uid + "@thriving-community-clubs.github.io", "DTSTAMP:" + stamp,
        "DTSTART:" + utc(ev.d, ev.s), "DTEND:" + utc(ev.d, ev.e), "SUMMARY:" + esc(ev.t),
        "LOCATION:" + esc(ev.room + ", " + VENUE), "DESCRIPTION:" + esc(ev.about || ""), "END:VEVENT");
    });
    lines.push("END:VCALENDAR");
    return lines.join("\r\n") + "\r\n";
  }
  function download(filename, text) {
    var a = document.createElement("a");
    a.href = "data:text/calendar;charset=utf-8," + encodeURIComponent(text);
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
  }
  function slug(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, ""); }

  function briefingEvents(data) {
    return data.briefings.map(function (b) {
      return { uid: "tcc26-briefing-" + b.d + "-" + b.s.replace(":", ""), d: b.d, s: b.s, e: b.e,
        t: "Conference team briefing: " + b.t, room: b.room };
    });
  }

  function jobsFor(data, name) {
    var out = [];
    data.sessions.forEach(function (s) {
      s.jobs.forEach(function (j) {
        if (j.who.indexOf(name) === -1) return;
        var others = j.who.filter(function (n) { return n !== name; });
        var role = j.role + (others.length ? ", with " + joinNames(others) : "");
        var last = out[out.length - 1];
        if (last && last.session === s) {
          // Two jobs in one session, such as introducing it and then facilitating a room.
          last.role += (j.room !== last.room ? " in " + last.room : "") + ". Then " + role.charAt(0).toLowerCase() + role.slice(1);
          last.room = j.room;
          return;
        }
        out.push({ session: s, role: role, room: j.room });
      });
    });
    return out;
  }

  function showPerson(data, name, box) {
    box.textContent = "";
    if (!name) { box.hidden = true; return; }
    var jobs = jobsFor(data, name);
    box.appendChild(el("h3", null, name));
    var day = null, list = null;
    jobs.forEach(function (j) {
      var s = j.session;
      if (s.d !== day) {
        day = s.d;
        box.appendChild(el("h4", "fac-day", DAYS[day]));
        list = el("ul", "fac-list");
        box.appendChild(list);
      }
      var li = el("li");
      li.appendChild(el("time", null, clock(s.s) + " to " + clock(s.e)));
      var what = el("div");
      what.appendChild(el("strong", null, s.t));
      what.appendChild(el("span", null, j.role + ". " + j.room + "."));
      if (s.tbc) { what.appendChild(document.createElement("br")); what.appendChild(el("span", "tbc", "Club to be confirmed")); }
      li.appendChild(what);
      list.appendChild(li);
    });
    var note = el("p", "fac-check");
    note.appendChild(document.createTextNode("Plus the five "));
    var a = el("a", null, "team briefings");
    a.href = "#briefings";
    note.appendChild(a);
    note.appendChild(document.createTextNode(" at the venue."));
    box.appendChild(note);
    var btn = el("button", "button", "Add my sessions and the briefings to my calendar");
    btn.type = "button";
    btn.addEventListener("click", function () {
      var events = jobs.map(function (j) {
        var s = j.session;
        return { uid: "tcc26-" + slug(name) + "-" + s.d + "-" + s.s.replace(":", "") + "-" + slug(j.role).slice(0, 20),
          d: s.d, s: s.s, e: s.e, t: s.t, room: j.room, about: j.role + (s.tbc ? ". Club to be confirmed." : ".") };
      }).concat(briefingEvents(data));
      download("tcc26-" + slug(name) + ".ics", calendar("Conference 2026: " + name, events));
    });
    box.appendChild(btn);
    box.hidden = false;
  }

  function enhance() {
    var holder = document.getElementById("fac-data");
    if (!holder) return;
    var data = JSON.parse(holder.textContent);
    var select = document.getElementById("fac-name");
    var box = document.getElementById("fac-result");
    var names = {};
    data.sessions.forEach(function (s) { s.jobs.forEach(function (j) { j.who.forEach(function (n) { names[n] = true; }); }); });
    Object.keys(names).sort().forEach(function (n) {
      var o = el("option", null, n);
      o.value = n;
      select.appendChild(o);
    });
    var saved = null;
    try { saved = localStorage.getItem(NAME_KEY); } catch (err) { /* private browsing */ }
    if (saved && names[saved]) { select.value = saved; showPerson(data, saved, box); }
    select.addEventListener("change", function () {
      showPerson(data, select.value, box);
      try { localStorage.setItem(NAME_KEY, select.value); } catch (err) { /* ignore */ }
    });
    Array.prototype.forEach.call(document.querySelectorAll('[data-ics="briefings"]'), function (b) {
      b.addEventListener("click", function () {
        download("tcc26-team-briefings.ics", calendar("Conference 2026: team briefings", briefingEvents(data)));
      });
    });
  }

  // Keep a copy for use without signal (see sw.js at the site root).
  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
    window.addEventListener("load", function () {
      navigator.serviceWorker.register("../sw.js", { scope: "../" }).catch(function () { /* fine without it */ });
    });
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (input.value.trim()) attempt(input.value, false);
  });

  var earlier = saved();
  if (earlier) attempt(earlier, true);
})();
