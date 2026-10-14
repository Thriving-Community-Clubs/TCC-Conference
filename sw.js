/* Keeps a copy of the conference page on the phone so it still opens without signal.
   Made by tools/build.py from tools/sw-template.js. Edit the template, not sw.js.

   Pages: try the network first so updates show straight away, and fall back to
   the saved copy after a few seconds or when there is no connection.
   Everything else: use the saved copy if there is one, otherwise fetch and keep it. */
"use strict";

var VERSION = "678c9117df";
var CORE = "tcc26-core-" + VERSION;
var EXTRA = "tcc26-extra";
var CORE_FILES = [
  "./",
  "assets/site.css?v=70196c90f7",
  "assets/site.js?v=d53f60fd8a",
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
  "img/charlotte-richardson.webp",
  "img/cover-1600.webp",
  "img/cover-800.webp",
  "img/feedback-qr.png",
  "img/slido-qr.png",
  "img/sue-day.webp",
  "slides/194cd76e9ffb.webp",
  "slides/1a049b2b3766.webp",
  "slides/1a4e91a015a9.webp",
  "slides/1e13b75f912a.webp",
  "slides/2002c125fd76.webp",
  "slides/2570d5d805e8.webp",
  "slides/288a95ac2d27.webp",
  "slides/2c4e504da56f.webp",
  "slides/38f5baf232ee.webp",
  "slides/3b440f9d798f.webp",
  "slides/46e1b60e7718.webp",
  "slides/478e43b8f8f4.webp",
  "slides/4a0685edae47.webp",
  "slides/4b53251493dc.webp",
  "slides/4bbd56c3bf34.webp",
  "slides/4d83a529cdc2.webp",
  "slides/4ee8c506fb05.webp",
  "slides/583ce6afe31f.webp",
  "slides/5c6ef309e9f6.webp",
  "slides/606413281f08.webp",
  "slides/66a4f2586c57.webp",
  "slides/75a15f82369e.webp",
  "slides/7705e34172b5.webp",
  "slides/7cfecbfe6046.webp",
  "slides/8223e093745d.webp",
  "slides/8953b59010cc.webp",
  "slides/8bbf172222bc.webp",
  "slides/95b2557e4e89.webp",
  "slides/96d33beb2c0f.webp",
  "slides/9a96df071fb8.webp",
  "slides/9aab21919ff4.webp",
  "slides/9c4bfa44f384.webp",
  "slides/9ff9603eeeab.webp",
  "slides/a173049d289b.webp",
  "slides/a5b02901ece7.webp",
  "slides/a67f1bcaf1a6.webp",
  "slides/a85c01098774.webp",
  "slides/addcd26d09ba.webp",
  "slides/b3c64c2fb7fa.webp",
  "slides/b432a4d4113d.webp",
  "slides/c0f8de383416.webp",
  "slides/c2f93c9ae21f.webp",
  "slides/c396aeddf288.webp",
  "slides/c3df46daa5f5.webp",
  "slides/c4964d2b03ae.webp",
  "slides/c92b3eb8ad1b.webp",
  "slides/c98c63b11477.webp",
  "slides/cbea19915f2b.webp",
  "slides/ce8aedc42f7b.webp",
  "slides/cf1362768d38.webp",
  "slides/d41edf396442.webp",
  "slides/d530b5c33f2c.webp",
  "slides/ea6e495b4a60.webp",
  "slides/f1f01a8354ae.webp",
  "slides/f45ccb8422a5.webp"
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
