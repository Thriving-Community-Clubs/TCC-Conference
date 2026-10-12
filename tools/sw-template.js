/* Keeps a copy of the conference page on the phone so it still opens without signal.
   Made by tools/build.py from tools/sw-template.js. Edit the template, not sw.js.

   Pages: try the network first so updates show straight away, and fall back to
   the saved copy after a few seconds or when there is no connection.
   Everything else: use the saved copy if there is one, otherwise fetch and keep it. */
"use strict";

var VERSION = "__VERSION__";
var CORE = "tcc26-core-" + VERSION;
var EXTRA = "tcc26-extra";
var CORE_FILES = __CORE__;
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
