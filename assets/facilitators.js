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

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (input.value.trim()) attempt(input.value, false);
  });

  var earlier = saved();
  if (earlier) attempt(earlier, true);
})();
