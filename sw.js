/* Keeps a copy of the conference page on the phone so it still opens without signal.
   Made by tools/build.py from tools/sw-template.js. Edit the template, not sw.js.

   Pages: try the network first so updates show straight away, and fall back to
   the saved copy after a few seconds or when there is no connection.
   Everything else: use the saved copy if there is one, otherwise fetch and keep it. */
"use strict";

var VERSION = "9de19cb04f";
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
  "slides/0068ac314560.webp",
  "slides/02b0aee78018.webp",
  "slides/09fb5c495352.webp",
  "slides/1a6bbc58aa3e.webp",
  "slides/2002c125fd76.webp",
  "slides/267eb14c0b4f.webp",
  "slides/2c4e504da56f.webp",
  "slides/2f36c4983683.webp",
  "slides/2fc6c9b5591f.webp",
  "slides/38f5baf232ee.webp",
  "slides/3e60ea172b5d.webp",
  "slides/41d3bcb1e5cf.webp",
  "slides/43cf2d42d193.webp",
  "slides/5238f0a578e1.webp",
  "slides/53ed106e6a70.webp",
  "slides/5b203136b0e5.webp",
  "slides/5b62eeb1a20c.webp",
  "slides/5c687211d960.webp",
  "slides/5c6ef309e9f6.webp",
  "slides/66a4f2586c57.webp",
  "slides/69d70b40ee44.webp",
  "slides/6f24bd16b44c.webp",
  "slides/755d068d711c.webp",
  "slides/75f3aa4f5c4e.webp",
  "slides/7a9b72f286d1.webp",
  "slides/7f8a30bcaeca.webp",
  "slides/83ec44805110.webp",
  "slides/856dd5df78da.webp",
  "slides/89a66f7a7a90.webp",
  "slides/8c8fd4b5b3b4.webp",
  "slides/9249f2ed365e.webp",
  "slides/927a06161c2a.webp",
  "slides/9587ef6e25bf.webp",
  "slides/95ad332fa1ed.webp",
  "slides/96044c0e2cf9.webp",
  "slides/96d33beb2c0f.webp",
  "slides/9a96df071fb8.webp",
  "slides/a173049d289b.webp",
  "slides/a2ca26e9c431.webp",
  "slides/a9c44b65aa17.webp",
  "slides/b4f12c9c51ab.webp",
  "slides/c164accbe49b.webp",
  "slides/c3301fb1c1b6.webp",
  "slides/c4964d2b03ae.webp",
  "slides/c66cfa5fdc15.webp",
  "slides/c92b3eb8ad1b.webp",
  "slides/cbe538503e1e.webp",
  "slides/cf073d981950.webp",
  "slides/cf1362768d38.webp",
  "slides/d28092c6b341.webp",
  "slides/d341ac47259d.webp",
  "slides/d6b3fea4c85d.webp",
  "slides/da6548536d15.webp",
  "slides/e25e490a8681.webp",
  "slides/e2a859134be9.webp",
  "slides/f38d5eec9b30.webp",
  "slides/f45ccb8422a5.webp",
  "slides/f9d26944ea0f.webp",
  "slides/fc25780e1605.webp",
  "slides/fe59228e9077.webp",
  "slides/feab0f521d25.webp"
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
