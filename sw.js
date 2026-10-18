/* Keeps a copy of the conference page on the phone so it still opens without signal.
   Made by tools/build.py from tools/sw-template.js. Edit the template, not sw.js.

   Pages: try the network first so updates show straight away, and fall back to
   the saved copy after a few seconds or when there is no connection.
   Everything else: use the saved copy if there is one, otherwise fetch and keep it. */
"use strict";

var VERSION = "dccf918491";
var CORE = "tcc26-core-" + VERSION;
var EXTRA = "tcc26-extra";
var CORE_FILES = [
  "./",
  "assets/site.css?v=41714afb20",
  "assets/site.js?v=962bf69347",
  "files/tcc-conference-2026.ics",
  "files/tcc-conference-2026-sessions.ics",
  "assets/accredited-club-programme-red.png",
  "assets/accredited-club-programme-white.png",
  "assets/better-everywhere-red.png",
  "assets/better-everywhere-white.png",
  "assets/pillar-community.png",
  "assets/pillar-cv.png",
  "assets/pillar-facilities.png",
  "assets/pillar-lg.png",
  "assets/pillar-po.png",
  "img/animation-poster.webp",
  "img/charlotte-richardson.webp",
  "img/cover-1600.webp",
  "img/cover-800.webp",
  "img/feedback-qr.png",
  "img/slido-qr.png",
  "img/sue-day.webp",
  "slides/02ba715c6588.webp",
  "slides/0a8289558403.webp",
  "slides/0af329ce386b.webp",
  "slides/0b763246eda5.webp",
  "slides/0f9a02c4164a.webp",
  "slides/1131191d22f6.webp",
  "slides/148bcb4f5d2b.webp",
  "slides/14c011012dbb.webp",
  "slides/194cd76e9ffb.webp",
  "slides/1a049b2b3766.webp",
  "slides/1a4e91a015a9.webp",
  "slides/1e13b75f912a.webp",
  "slides/2395bf4ca0af.webp",
  "slides/249179cb9bb3.webp",
  "slides/2570d5d805e8.webp",
  "slides/288a95ac2d27.webp",
  "slides/2999373fc38b.webp",
  "slides/2af502bee7d6.webp",
  "slides/2c9248ef41b9.webp",
  "slides/2f390152ecbe.webp",
  "slides/324b70859b69.webp",
  "slides/324c42344375.webp",
  "slides/32cb89e6cb4b.webp",
  "slides/337d399e15d6.webp",
  "slides/36eab4b8f033.webp",
  "slides/3b440f9d798f.webp",
  "slides/3df64d5fc845.webp",
  "slides/3e91710a4003.webp",
  "slides/41d272d24805.webp",
  "slides/440265c33959.webp",
  "slides/46a4af3bc17f.webp",
  "slides/46e1b60e7718.webp",
  "slides/478e43b8f8f4.webp",
  "slides/47c39ac4f89e.webp",
  "slides/48482d609474.webp",
  "slides/4a0685edae47.webp",
  "slides/4b53251493dc.webp",
  "slides/4bbd56c3bf34.webp",
  "slides/4d83a529cdc2.webp",
  "slides/4ee8c506fb05.webp",
  "slides/4f66393065b7.webp",
  "slides/51b2209159e2.webp",
  "slides/535d0f3be9e4.webp",
  "slides/57155d722223.webp",
  "slides/5822fcbaa95c.webp",
  "slides/583ce6afe31f.webp",
  "slides/5f21500a4ed2.webp",
  "slides/606413281f08.webp",
  "slides/64cd40ff2e94.webp",
  "slides/660711302053.webp",
  "slides/6a6dff17c822.webp",
  "slides/730172bdce9a.webp",
  "slides/75a15f82369e.webp",
  "slides/7705e34172b5.webp",
  "slides/7a200c87bbd8.webp",
  "slides/7a62f1fc871b.webp",
  "slides/7c7e865e9b7d.webp",
  "slides/7cfecbfe6046.webp",
  "slides/80ba53f186cb.webp",
  "slides/817133305b13.webp",
  "slides/8223e093745d.webp",
  "slides/869601e6650d.webp",
  "slides/87d26dc5300b.webp",
  "slides/87ecc9d4e1e6.webp",
  "slides/8953b59010cc.webp",
  "slides/89ad465d6c85.webp",
  "slides/8bbf172222bc.webp",
  "slides/8edc8d0b3a9b.webp",
  "slides/95b2557e4e89.webp",
  "slides/9633bdfe568d.webp",
  "slides/9a2b71166b93.webp",
  "slides/9aab21919ff4.webp",
  "slides/9aec65072f1f.webp",
  "slides/9c4bfa44f384.webp",
  "slides/9da439f74a72.webp",
  "slides/9ff9603eeeab.webp",
  "slides/a49f6a907af6.webp",
  "slides/a5b02901ece7.webp",
  "slides/a67f1bcaf1a6.webp",
  "slides/a85c01098774.webp",
  "slides/acae37af37df.webp",
  "slides/addcd26d09ba.webp",
  "slides/b0a9490a387a.webp",
  "slides/b0ca7cf57491.webp",
  "slides/b0e8fc5e6e73.webp",
  "slides/b1ff927d5294.webp",
  "slides/b2c161baa5d1.webp",
  "slides/b3c64c2fb7fa.webp",
  "slides/b432a4d4113d.webp",
  "slides/b50b05fe7a68.webp",
  "slides/b6b3cda1beb3.webp",
  "slides/bcc67e0ebf7a.webp",
  "slides/c0f8de383416.webp",
  "slides/c2f93c9ae21f.webp",
  "slides/c396aeddf288.webp",
  "slides/c3df46daa5f5.webp",
  "slides/c53c20472ecc.webp",
  "slides/c616ad542037.webp",
  "slides/c98c63b11477.webp",
  "slides/cbea19915f2b.webp",
  "slides/ce7ec7ede7cc.webp",
  "slides/ce8aedc42f7b.webp",
  "slides/d41edf396442.webp",
  "slides/d530b5c33f2c.webp",
  "slides/d5468002cfb1.webp",
  "slides/d85dc3f235e5.webp",
  "slides/ddf0fade06d6.webp",
  "slides/ded8c190065d.webp",
  "slides/e0f7a0bec49b.webp",
  "slides/e3ff97cdb4d9.webp",
  "slides/e5f271f431ab.webp",
  "slides/e6afc3e54cc6.webp",
  "slides/ea6e495b4a60.webp",
  "slides/ef710089b7ed.webp",
  "slides/f11341a3d089.webp",
  "slides/f1f01a8354ae.webp",
  "slides/f50c0d2da97d.webp",
  "slides/f5a10db5af36.webp",
  "slides/fa08317a2a2c.webp",
  "slides/faebf70908b3.webp",
  "slides/fd252cec2077.webp"
];
var WAIT = 4000;

self.addEventListener("install", function (event) {
  event.waitUntil(
    caches.open(CORE)
      .then(function (cache) { return cache.addAll(CORE_FILES); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (event) {
  event.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (key) {
        if (key.indexOf("tcc26-core-") === 0 && key !== CORE) return caches.delete(key);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

function keep(cacheName, request, response) {
  if (response && response.ok && response.type === "basic") {
    var copy = response.clone();
    caches.open(cacheName).then(function (cache) { cache.put(request, copy); });
  }
  return response;
}

function page(request) {
  var url = new URL(request.url);
  // Save each page under its plain address, so ?preview= links share one copy.
  var plain = url.origin + url.pathname;
  var saved = function () {
    return caches.match(plain).then(function (hit) {
      return hit || caches.match(request, { ignoreSearch: true });
    });
  };
  var network = fetch(request).then(function (response) {
    if (response && response.ok) {
      var copy = response.clone();
      caches.open(CORE).then(function (cache) { cache.put(plain, copy); });
    }
    return response;
  });
  var timeout = new Promise(function (resolve) {
    setTimeout(function () { saved().then(resolve); }, WAIT);
  });
  return Promise.race([network.catch(saved), timeout.then(function (hit) { return hit || network; })])
    .then(function (response) { return response || saved(); })
    .catch(saved);
}

self.addEventListener("fetch", function (event) {
  var request = event.request;
  if (request.method !== "GET") return;
  var url = new URL(request.url);
  if (url.origin !== self.location.origin) return;
  if (request.headers.has("range")) return;

  if (request.mode === "navigate") {
    event.respondWith(page(request));
    return;
  }
  event.respondWith(
    caches.match(request).then(function (hit) {
      return hit || fetch(request).then(function (response) { return keep(EXTRA, request, response); });
    })
  );
});
