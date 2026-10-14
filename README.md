# Better Everywhere: Thriving Community Clubs Conference 2026

The delegate page for the conference on 20 and 21 October 2026 at the East Midlands Conference Centre, Nottingham.

The page is `index.html` at the top of this repository. It is built from the files in `tools/`, so change the content there and rebuild; do not edit `index.html` by hand.

## Changing the content

Everything delegates read comes from two files:

- `tools/content.py` holds the agenda, rooms, session leads, groups, contact numbers, links and the list of slides shown for each session.
- `tools/template.html` holds the fixed wording: travel, hotel, venue and resources.

After a change, run this from the top of the repository:

    python3 tools/build.py

### Common updates

| To do this | Change this in `tools/content.py` |
| --- | --- |
| Add the Slido link | `SLIDO_URL` |
| Add the feedback survey after the conference | `FEEDBACK_URL` |
| Replace the workbook | run `python3 tools/make_workbook.py "/path/to/workbook.pdf"`, check `WORKBOOK_PAGES`, rebuild |
| Take the workbook off the page | set `WORKBOOK_FILE = ""` |
| Add a resource under a pillar | run `python3 tools/add_resource.py <short-name> "/path/to/file"`, paste what it prints into `PILLAR_RESOURCES`, add a title and descriptions, rebuild |
| Update who goes to which breakout and pillar ("Choose your name") | run `python3 tools/import_allocations.py "/path/to/Attendee Session Allocation.xlsx"`, then rebuild. It stops if a County FA's groups in the sheet disagree with `GROUPS` |
| Add files to a session in the agenda | `SESSION_RESOURCES`, keyed by session id |
| Show the three club stories on Day 2 | `SHOW_CLUB_STORIES = True` |
| Use a session's own final deck | list its pages as "f1", "f2"... in `SLIDE_PAGES`, run `python3 tools/make_session_slides.py <session-id> "/path/to/deck.pdf"`, then rebuild |
| Change which slides delegates see | `SLIDE_PAGES` (page numbers of the master deck PDF), then re-run `make_slides.py` |

### Refreshing the slides from a new deck

    python3 tools/make_slides.py "/path/to/MASTER content slides.pdf"
    python3 tools/build.py

Each slide also has a short description in `SLIDE_ALT` for people who cannot see the images. Update it when a slide changes.

## How the page behaves

- **Before, during and after.** The page reorders itself: joining information leads beforehand, the agenda leads from the evening before Day 1, and the feedback survey leads once the conference closes.
- **Now and next.** On the two days, the dark panel at the top shows the current session and the next one.
- **Slides.** Each session's slides appear when the session starts and stay up afterwards. The image files are in this public repository from the moment they are added, so the timing hides them from the page; it does not secure them. Do not add a slide that must stay private.
- **Without signal.** `sw.js` keeps a copy of the page, its stylesheet and script, logos, photos and every slide on the phone after the first visit, so the page opens with no connection. Pages are fetched fresh when there is signal (after 4 seconds the saved copy is shown instead). Workbook pages, resources and PDFs are kept once opened. `sw.js` is written by `tools/build.py` from `tools/sw-template.js`; edit the template, never `sw.js`.
- **Calendar files.** `tools/build.py` also writes `files/tcc-conference-2026.ics` (both days) and `files/tcc-conference-2026-sessions.ics` (every session) from the agenda, so rebuild after any time change.
- **Preview another time.** Add `?preview=2026-10-20T13:05` to the page address to see it as it will look at that moment (Nottingham time).

## Design

The page follows the England Football Thriving design system: England Football red and white lead, navy for body copy, square corners, hairlines, no shadows or gradients. Arial stands in for FS Dillon. Logos and pillar icons in `assets/` are the supplied files, resized and never redrawn.

## The facilitator page

`facilitators/index.html` is for facilitators and the conference team. Its content is encrypted, and the page only opens with the passcode.

- The readable source and the passcode are kept outside this repository. Never commit either.
- To rebuild the page after a change to the source, or to change the passcode:

      node tools/encrypt-facilitators.mjs /path/outside/this/repo/facilitators-source.html "the passcode"

- The "Your sessions" picker on the facilitator page reads a JSON block (`id="fac-data"`) inside the source, listing every session, who is doing what and where, and the team briefings. Update it when roles change. Calendar files on that page are built in the browser, so nothing readable is published.
- The passcode is forgiving about capitals and about spaces in place of hyphens.
- Anyone can download the encrypted page, so the passcode is the only protection. It keeps casual visitors out. Do not put anything on the page that would be a real problem if it became public.

| To do this | Change this in `tools/content.py` |
| --- | --- |
| Update the host, keynote or session leads | `HOST`, `KEYNOTE`, `SESSION_LEADS` |
