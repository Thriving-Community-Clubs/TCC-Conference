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
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urlencode

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


def file_size(path):
    """A file's size as people expect to read it: '290 KB' or '11 MB'."""
    size = os.path.getsize(os.path.join(ROOT, path))
    if size < 950_000:
        return f"{max(1, round(size / 1000))} KB"
    return f"{size / 1e6:.0f} MB"


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


def resources_fold(pillar):
    """Resources for one pillar, folded away under its name. Nothing when there are none."""
    items = getattr(C, "PILLAR_RESOURCES", {}).get(pillar, [])
    if not items:
        return ""
    out = []
    for item in items:
        pages = item["pages"]
        many = len(pages) > 1
        figures = []
        for n, page in enumerate(pages, 1):
            src, w, h, alt = page[:4]
            label = page[4] if len(page) > 4 else f"Page {n} of {len(pages)}"
            cap = f'<span class="res-count">{e(label)}</span>' if many else ""
            figures.append(
                f'{cap}<a href="{e(src)}" target="_blank" rel="noopener">'
                f'<img src="{e(src)}" alt="{e(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a>'
            )
        if item.get("pdf"):
            link = f'<a href="{e(item["pdf"])}">Download the PDF ({file_size(item["pdf"])})</a>'
        else:
            link = f'<a href="{e(pages[0][0])}" target="_blank" rel="noopener">Open full size</a>'
        links_html = ""
        if item.get("links"):
            total = sum(len(group) for _, group in item["links"])

            def one(link):
                label, url = link[0], link[1]
                note = f'<span class="res-note">{e(link[2])}</span>' if len(link) > 2 else ""
                return f'<li><a href="{e(url)}" rel="noopener">{e(label)}</a>{note}</li>'

            groups = "".join(
                f'<p class="res-group">{e(heading)}</p><ul>' + "".join(one(link) for link in group) + "</ul>"
                for heading, group in item["links"]
            )
            links_html = (
                f'<details class="fold res-links"><summary>{e(item.get("links_label", "Links from this guide"))} ({total})</summary>'
                f'<div class="fold-body">{groups}</div></details>'
            )
        tip = "Tap a page to enlarge it." if many else "Tap the image to enlarge it."
        # A long document shows its first page, with the rest folded away.
        if len(figures) > 4:
            shown = figures[0] + (
                f'<details class="fold res-more"><summary>Show the other {len(figures) - 1} pages</summary>'
                f'<div class="fold-body">{"".join(figures[1:])}</div></details>'
            )
        else:
            shown = "".join(figures)
        out.append(
            f'<figure class="res-item"><figcaption>{e(item["title"])}</figcaption>'
            f'{shown}<p class="hint">{tip} {link}</p>{links_html}</figure>'
        )
    return (
        f'<details class="fold res"><summary>Resources for {e(pillar)} ({len(items)})</summary>'
        f'<div class="fold-body">{"".join(out)}</div></details>'
    )


def pillars_list():
    rows = []
    for name, icon, room, leads in C.PILLAR_ROOMS:
        rows.append(
            f'<li class="pillar"><img src="assets/pillar-{icon}.png" alt="" width="44" height="50">'
            f'<div><strong>{e(name)}</strong><span>{e(room)}</span><span class="with">With {e(leads)}</span></div>'
            f'{resources_fold(name)}</li>'
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
            out[c] = {"d1": g["d1"], "d2": None if c in C.DAY1_ONLY else g["d2"]}
    return json.dumps(out, ensure_ascii=False)


def county_options():
    names = sorted(c for g in C.GROUPS for c in g["counties"])
    return "".join(f"<option>{e(n)}</option>" for n in names)


def contacts_html():
    return "".join(
        f'<li><span class="name">{e(n)}</span><a href="tel:{tel}">{e(shown)}</a></li>'
        for n, shown, tel in C.CONTACTS
    )


def person_card(d):
    """Photo, name and role, then the first paragraph of the bio with the rest folded away."""
    slot = f'<p class="slot">{e(d["session"])}</p>' if d.get("session") else ""
    bio = d.get("bio") or []
    bio_html = ""
    if bio:
        rest = "".join(f"<p>{e(par)}</p>" for par in bio[1:])
        fold = (
            f'<details class="fold"><summary>More about {e(d["first"])}</summary>'
            f'<div class="fold-body">{rest}</div></details>'
        ) if rest else ""
        bio_html = f'<div class="bio"><p>{e(bio[0])}</p>{fold}</div>'
    return (
        f'<article class="person"><img src="{d["photo"]}" alt="{e(d["alt"])}" width="480" height="480" loading="lazy">'
        f'<div><h3>{e(d["name"])}</h3><p class="role">{e(d["role"])}</p>{slot}</div>{bio_html}</article>'
    )


def people_html():
    leads = "".join(
        f'<li><strong>{e(n)}</strong><span>{e(t)}</span></li>' for n, t in C.SESSION_LEADS
    )
    return (
        f'<div class="people">{person_card(C.HOST)}{person_card(C.KEYNOTE)}</div>'
        f'<h3 class="leads-title">Leading your sessions</h3><ul class="leads">{leads}</ul>'
    )


def slido_html():
    """The Slido section, or nothing when no link is set."""
    if not C.SLIDO_URL:
        return ""
    code = e(C.SLIDO_CODE)
    return (
        '<section class="block" id="slido" aria-labelledby="slido-h"><div class="wrap">'
        '<h2 id="slido-h">Slido</h2>'
        '<div class="person slido">'
        '<a href="img/slido-qr.png" aria-label="Open the Slido QR code at full size">'
        '<img src="img/slido-qr.png" alt="QR code to join the conference Slido" width="700" height="700"></a>'
        '<div><h3>Join in on your phone</h3>'
        f'<p class="role">Joining code #{code}</p></div>'
        '<div class="bio"><p>We use Slido for your questions, polls and pledges across both days.</p>'
        f'<p><a class="button" href="{e(C.SLIDO_URL)}" rel="noopener">Open Slido</a></p>'
        f'<p class="hint">On another device, scan the code, or go to slido.com and enter #{code}.</p></div>'
        '</div></div></section>'
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
        f'<p><a class="button button-outline" href="{e(C.WORKBOOK_FILE)}">Download the workbook (PDF, {file_size(C.WORKBOOK_FILE)})</a></p>'
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


# ----- Calendar files -----

VENUE = "East Midlands Conference Centre, Beeston Lane, Nottingham NG7 2RJ"
PAGE_URL = "https://thriving-community-clubs.github.io/TCC-Conference/"
CAL_BOTH = "files/tcc-conference-2026.ics"
CAL_SESSIONS = "files/tcc-conference-2026-sessions.ics"

# The whole of each day, for people who want one entry per day.
CAL_DAYS = [
    ("tcc26-day1", "2026-10-20", "09:30", "16:30",
     "Thriving Community Clubs Conference 2026: Day 1",
     "Registration opens at 9.30am and we start at 10.30am in Main Room 1. "
     "The drinks reception, street food dinner and games start at 7.00pm in Main Room 1 and Main Room 2. "
     "Agenda, slides and venue plan: " + PAGE_URL),
    ("tcc26-day2", "2026-10-21", "09:00", "15:45",
     "Thriving Community Clubs Conference 2026: Day 2",
     "Registration and hotel check-out from 9.00am. We start at 9.30am in Main Room 1 and close at 3.45pm. "
     "Agenda, slides and venue plan: " + PAGE_URL),
]


def utc(day, hhmm):
    local = datetime.fromisoformat(f"{day}T{hhmm}:00{C.TZ}")
    return local.astimezone(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def ics_text(value):
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def ics_fold(line):
    """Lines in a calendar file must be under 75 bytes; longer ones continue with a space."""
    out, raw = [], line.encode("utf-8")
    while len(raw) > 73:
        cut = 73
        while (raw[cut] & 0xC0) == 0x80:  # do not split a character
            cut -= 1
        out.append(raw[:cut].decode("utf-8"))
        raw = b" " + raw[cut:]
    out.append(raw.decode("utf-8"))
    return "\r\n".join(out)


def ics(name, events, stamp):
    lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Thriving Community Clubs//Conference 2026//EN",
             "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:" + ics_text(name)]
    for uid, day, start, end, title, where, about in events:
        lines += ["BEGIN:VEVENT", f"UID:{uid}@thriving-community-clubs.github.io", f"DTSTAMP:{stamp}",
                  f"DTSTART:{utc(day, start)}", f"DTEND:{utc(day, end)}",
                  "SUMMARY:" + ics_text(title), "LOCATION:" + ics_text(where),
                  "DESCRIPTION:" + ics_text(about), "URL:" + PAGE_URL, "END:VEVENT"]
    lines.append("END:VCALENDAR")
    return "\r\n".join(ics_fold(x) for x in lines) + "\r\n"


def write_calendars():
    stamp = date.today().strftime("%Y%m%dT000000Z")
    days = [(uid, d, a, b, t, VENUE, about) for uid, d, a, b, t, about in CAL_DAYS]
    sessions = []
    for d in C.DAYS:
        for s in d["sessions"]:
            if s.get("club") and not C.SHOW_CLUB_STORIES:
                continue
            if end_of(s) <= s["start"]:
                continue
            where = s.get("room") or s.get("note") or ""
            about = (s.get("who") + ". " if s.get("who") else "") + "Agenda and slides: " + PAGE_URL + "#" + s["id"]
            sessions.append((s["id"], d["date"], s["start"], end_of(s), "Conference: " + s["title"],
                             f"{where}, {VENUE}" if where else VENUE, about))
    for path, name, events in [(CAL_BOTH, "Thriving Community Clubs Conference 2026", days),
                               (CAL_SESSIONS, "Thriving Community Clubs Conference 2026, every session", sessions)]:
        with open(os.path.join(ROOT, path), "w", encoding="utf-8", newline="") as f:
            f.write(ics(name, events, stamp))


def google_link(uid, day, start, end, title, about):
    query = urlencode({"action": "TEMPLATE", "text": title, "dates": f"{utc(day, start)}/{utc(day, end)}",
                       "details": about, "location": VENUE, "ctz": "Europe/London"})
    return "https://calendar.google.com/calendar/render?" + query


def calendar_html():
    google = "".join(
        f'<li><a href="{e(google_link(*d))}" rel="noopener">{"Day 1" if d[0].endswith("1") else "Day 2"} in Google Calendar</a></li>'
        for d in CAL_DAYS
    )
    return (
        f'<p><a class="button" href="{CAL_BOTH}" download>Add both days to your calendar</a></p>'
        '<p class="hint">Opens in Outlook, Apple Calendar and most phone calendars. It adds two entries, one for each day.</p>'
        f'<ul class="cal-more"><li><a href="{CAL_SESSIONS}" download>Add every session instead</a></li>{google}</ul>'
    )


# ----- Saved copy for when there is no signal -----

def write_service_worker():
    """Lists what a phone keeps for use without signal, and fingerprints it so
    phones fetch a fresh copy whenever any of it changes."""
    core = ["./", f"assets/site.css?v={version('assets/site.css')}", f"assets/site.js?v={version('assets/site.js')}",
            CAL_BOTH, CAL_SESSIONS]
    for folder, ext in [("assets", ".png"), ("img", ""), ("slides", ".webp")]:
        for name in sorted(os.listdir(os.path.join(ROOT, folder))):
            if name.endswith(ext) and not name.startswith("."):
                core.append(f"{folder}/{name}")
    h = hashlib.sha256()
    for item in ["index.html"] + core[1:]:
        h.update(item.encode())
        with open(os.path.join(ROOT, item.split("?")[0]), "rb") as f:
            h.update(f.read())
    tpl = open(os.path.join(HERE, "sw-template.js"), encoding="utf-8").read()
    out = tpl.replace("__VERSION__", h.hexdigest()[:10]).replace("__CORE__", json.dumps(core, indent=2))
    with open(os.path.join(ROOT, "sw.js"), "w", encoding="utf-8") as f:
        f.write(out)
    return len(core)


def main():
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    write_calendars()
    updated = date.today().strftime("%-d %B %Y")
    values = {
        "AGENDA": agenda_html(),
        "SCHEDULE_JSON": schedule_json(),
        "GROUPS_JSON": groups_json(),
        "COUNTY_OPTIONS": county_options(),
        "CONTACTS": contacts_html(),
        "AFTER": after_html(),
        "SLIDO": slido_html(),
        "SLIDO_NAV": '<li><a href="#slido">Slido</a></li>' if C.SLIDO_URL else "",
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
        "CALENDAR": calendar_html(),
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
    print("saved for use without signal:", write_service_worker(), "files")


if __name__ == "__main__":
    main()
