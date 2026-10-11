#!/usr/bin/env python3
"""Builds conference/index.html from tools/content.py.

Usage (from the repository root):  python3 tools/build.py
Slide images are made separately by tools/make_slides.py from the master deck PDF.
"""
import hashlib
import html
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import content as C  # noqa: E402

e = html.escape


def version(path):
    """Short fingerprint of a file, added to its address so browsers never pair
    a new page with an older copy of the stylesheet or script."""
    with open(os.path.join(ROOT, path), "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:10]


def slide_name(key, page):
    return hashlib.sha256(f"tcc26-{key}-{page}".encode()).hexdigest()[:12] + ".webp"


def clock(hhmm):
    """'13:00' -> '1.00pm' (the style used in the joining instructions)."""
    h, m = map(int, hhmm.split(":"))
    suffix = "am" if h < 12 else "pm"
    h12 = h % 12 or 12
    return f"{h12}.{m:02d}{suffix}"


def iso(day, hhmm):
    return f"{day}T{hhmm}:00{C.TZ}"


def end_of(s):
    if C.SHOW_CLUB_STORIES and s.get("end_clubs"):
        return s["end_clubs"]
    return s["end"]


def slides_block(day, start, key, label):
    pages = C.SLIDE_PAGES.get(key, [])
    if not pages:
        return ""
    items = [{"f": slide_name(key, p), "a": C.SLIDE_ALT.get(p, "")} for p in pages]
    n = len(items)
    count = "1 slide" if n == 1 else f"{n} slides"
    return (
        f'<div class="slides" data-unlock="{iso(day, start)}" data-label="{e(label)}" '
        f"data-slides='{e(json.dumps(items), quote=True)}'>"
        f'<p class="slides-locked">{count} from this session will appear here when it starts at {clock(start)}.</p>'
        f"</div>"
    )


def slido_button():
    if not C.SLIDO_URL:
        return ""
    return f'<p><a class="button button-outline" href="{e(C.SLIDO_URL)}" rel="noopener">Open Slido</a></p>'


def groups_list(which):
    rows = []
    for g in C.GROUPS:
        d = g[which]
        rows.append(
            f'<li><strong>{e(d["room"])}, {e(d["group"])}</strong> with {e(d["leads"])}'
            f'<span class="counties">{e(", ".join(g["counties"]))}</span></li>'
        )
    return (
        '<h4>Groups</h4><ul class="rooms">' + "".join(rows) + "</ul>"
        '<p class="hint"><a href="#yours">Find your County FA under Your sessions</a>.</p>'
    )


def pillars_list():
    rows = []
    for name, icon, room, leads in C.PILLAR_ROOMS:
        rows.append(
            f'<li class="pillar"><img src="assets/pillar-{icon}.png" alt="" width="44" height="50">'
            f'<div><strong>{e(name)}</strong><span>{e(room)}</span><span class="with">With {e(leads)}</span></div></li>'
        )
    return '<h4>Where each pillar meets</h4><ul class="pillars">' + "".join(rows) + "</ul>"


def session_html(day, s):
    start, end = s["start"], end_of(s)
    attrs = f'id="{s["id"]}" data-start="{iso(day, start)}" data-end="{iso(day, end)}"'
    time = f'<time datetime="{day}T{start}">{clock(start)}</time>'
    if s["kind"] == "pause":
        note = f'<p class="note">{e(s["note"])}</p>' if s.get("note") else ""
        return (
            f'<li class="row pause" {attrs}><div class="when">{time}</div>'
            f'<div class="what"><h3>{e(s["title"])}</h3>{note}</div></li>'
        )

    body = []
    if s.get("about"):
        body.append(f'<p>{e(s["about"])}</p>')
    if s.get("options"):
        for o in s["options"]:
            body.append(
                f'<div class="option"><h4>{e(o["name"])}</h4>'
                f'<p class="where">{e(o["room"])}, with {e(o["who"])}</p>'
                f'<p>{e(o["about"])}</p>'
                + slides_block(day, start, o["slides"], o["name"])
                + "</div>"
            )
    if s.get("groups"):
        body.append(groups_list(s["groups"]))
    if s.get("pillars"):
        body.append(pillars_list())
        body.append('<p class="hint">Your pillar will be listed under <a href="#yours">Your sessions</a> and confirmed at registration.</p>')
    if s.get("more"):
        label, href = s["more"]
        body.append(f'<p><a href="{e(href)}">{e(label)}</a></p>')
    if s.get("workbook"):
        n = s["workbook"]
        if C.WORKBOOK_FILE:
            body.append(f'<p class="workbook"><a href="#workbook-page-{n}">Workbook page {n}</a></p>')
        else:
            body.append(f'<p class="workbook">Workbook page {n}</p>')
    for key in s.get("slides", []):
        body.append(slides_block(day, start, key, s["title"]))
    if s.get("slides") or s.get("options"):
        body.append(slido_button())

    summary = (
        f'<summary><h3>{e(s["title"])}</h3>'
        f'<span class="where">{e(s["room"])}</span>'
        f'<span class="who">{e(s["who"])}</span></summary>'
    )
    inner = "".join(b for b in body if b)
    if inner:
        what = f'<details>{summary}<div class="detail">{inner}</div></details>'
    else:
        what = f'<div class="plain">{summary.replace("<summary>", "").replace("</summary>", "")}</div>'
    return (
        f'<li class="row session" {attrs}><div class="when">{time}'
        f'<span class="until">to {clock(end)}</span></div><div class="what">{what}</div></li>'
    )


def agenda_html():
    out = []
    for d in C.DAYS:
        rows = [
            session_html(d["date"], s)
            for s in d["sessions"]
            if not s.get("club") or C.SHOW_CLUB_STORIES
        ]
        out.append(
            f'<section class="day" id="{d["key"]}" data-date="{d["date"]}" aria-labelledby="{d["key"]}-h">'
            f'<h3 class="day-title" id="{d["key"]}-h">{d["label"]}<span>{d["long"]}</span></h3>'
            f'<ol class="timeline">{"".join(rows)}</ol></section>'
        )
    return "".join(out)


def schedule_json():
    """Compact schedule for the Now and next panel."""
    items = []
    for d in C.DAYS:
        for s in d["sessions"]:
            if s.get("club") and not C.SHOW_CLUB_STORIES:
                continue
            items.append({
                "id": s["id"],
                "t": s["title"],
                "s": iso(d["date"], s["start"]),
                "e": iso(d["date"], end_of(s)),
                "r": s.get("room") or s.get("note", ""),
                "c": clock(s["start"]),
            })
    return json.dumps(items, ensure_ascii=False)


def groups_json():
    out = {}
    for g in C.GROUPS:
        for c in g["counties"]:
            out[c] = {"d1": g["d1"], "d2": g["d2"]}
    return json.dumps(out, ensure_ascii=False)


def county_options():
    names = sorted(c for g in C.GROUPS for c in g["counties"])
    return "".join(f"<option>{e(n)}</option>" for n in names)


def contacts_html():
    return "".join(
        f'<li><span class="name">{e(n)}</span><a href="tel:{tel}">{e(shown)}</a></li>'
        for n, shown, tel in C.CONTACTS
    )


def people_html():
    h, k = C.HOST, C.KEYNOTE
    bio_first = f"<p>{e(k['bio'][0])}</p>"
    bio_rest = "".join(f"<p>{e(par)}</p>" for par in k["bio"][1:])
    leads = "".join(
        f'<li><strong>{e(n)}</strong><span>{e(t)}</span></li>' for n, t in C.SESSION_LEADS
    )
    return (
        '<div class="people">'
        f'<article class="person"><img src="{h["photo"]}" alt="{e(h["alt"])}" width="480" height="480" loading="lazy">'
        f'<div><h3>{e(h["name"])}</h3><p class="role">{e(h["role"])}</p></div></article>'
        f'<article class="person"><img src="{k["photo"]}" alt="{e(k["alt"])}" width="480" height="480" loading="lazy">'
        f'<div><h3>{e(k["name"])}</h3><p class="role">{e(k["role"])}</p>'
        f'<p class="slot">{e(k["session"])}</p></div>'
        f'<div class="bio">{bio_first}'
        f'<details class="fold"><summary>More about Sue</summary><div class="fold-body">{bio_rest}</div></details>'
        '</div></article></div>'
        f'<h3 class="leads-title">Leading your sessions</h3><ul class="leads">{leads}</ul>'
    )


def after_html():
    parts = []
    if C.FEEDBACK_URL:
        parts.append(
            '<p>Tell us what worked and what we should change. It takes a few minutes.</p>'
            f'<p><a class="button" href="{e(C.FEEDBACK_URL)}" rel="noopener">Give your feedback</a></p>'
        )
    else:
        parts.append("<p>The feedback survey will be here shortly.</p>")
    if C.WORKBOOK_FILE:
        parts.append('<p>You can <a href="#workbook">read or download the workbook</a> further down this page.</p>')
    return "".join(parts)


def workbook_html():
    if not C.WORKBOOK_FILE:
        return (
            '<div class="wb"><h3 id="workbook">Delegate workbook</h3>'
            "<p>You will get a printed copy at registration. A digital copy to view and download will be here after the conference.</p></div>"
        )
    size = os.path.getsize(os.path.join(ROOT, C.WORKBOOK_FILE)) / 1e6
    total = len(C.WORKBOOK_PAGES)
    pages = []
    for n, (printed, alt) in enumerate(C.WORKBOOK_PAGES, 1):
        anchor = f' id="workbook-page-{printed}"' if printed else ""
        label = f"Page {printed}" if printed else ""
        cap = f"<figcaption>{label}</figcaption>" if label else ""
        described = f"Workbook page {printed}. {alt}" if printed else alt
        pages.append(
            f'<li{anchor}><figure>{cap}<img src="workbook/page-{n:02d}.webp" alt="{e(described)}" '
            f'width="1200" height="1696" loading="lazy" decoding="async"></figure></li>'
        )
    return (
        '<div class="wb"><h3 id="workbook">Delegate workbook</h3>'
        "<p>You will get a printed copy at registration. You can also read it here or download a copy to keep.</p>"
        f'<p><a class="button button-outline" href="{e(C.WORKBOOK_FILE)}">Download the workbook (PDF, {size:.0f} MB)</a></p>'
        f'<details class="fold" id="workbook-reader"><summary>Read the workbook here ({total} pages)</summary>'
        f'<ol class="wb-pages">{"".join(pages)}</ol></details></div>'
    )


def illustrator_html():
    i = C.ILLUSTRATOR
    return (
        f'<h3>{e(i["name"])}</h3><p class="role">{e(i["role"])}</p>'
        f'<p>{e(i["about"])}</p>'
        f'<p><a href="{e(i["link"][1])}" rel="noopener">{e(i["link"][0])}</a></p>'
    )


def main():
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    updated = date.today().strftime("%-d %B %Y")
    values = {
        "AGENDA": agenda_html(),
        "SCHEDULE_JSON": schedule_json(),
        "GROUPS_JSON": groups_json(),
        "COUNTY_OPTIONS": county_options(),
        "CONTACTS": contacts_html(),
        "AFTER": after_html(),
        "PEOPLE": people_html(),
        "ILLUSTRATOR": illustrator_html(),
        "WORKBOOK": workbook_html(),
        "LINK_PARKING": e(C.LINKS["parking"]),
        "LINK_CHOICES": e(C.LINKS["choices"]),
        "LINK_VENUE": e(C.LINKS["venue"]),
        "LINK_SPORTS": e(C.LINKS["sports"]),
        "LINK_DIRECTIONS": e(C.LINKS["directions"]),
        "FLOORPLAN": open(os.path.join(HERE, "floorplan.svg"), encoding="utf-8").read(),
        "UPDATED": updated,
        "CSS_V": version("assets/site.css"),
        "JS_V": version("assets/site.js"),
    }
    for k, v in values.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    if "{{" in tpl:
        left = sorted(set(part.split("}}")[0] for part in tpl.split("{{")[1:]))
        raise SystemExit(f"Unfilled placeholders: {left}")
    out = os.path.join(ROOT, "index.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(tpl)
    print("wrote", out, len(tpl), "bytes")


if __name__ == "__main__":
    main()
