"""Content for the Better Everywhere conference delegate page.

Edit this file, then run:  python3 tools/build.py
Times are local time in Nottingham (British Summer Time, UTC+01:00).
"""

TZ = "+01:00"

# Switch to True once the clubs have confirmed. Adds the three club stories
# to the Day 2 agenda and shortens the sessions before them to match the deck.
SHOW_CLUB_STORIES = False

# Paste the Slido link here when it is ready (leave "" to hide the buttons).
SLIDO_URL = ""
# Paste the feedback survey link here after the conference.
FEEDBACK_URL = ""
# Set to the workbook PDF path (for example "files/delegate-workbook.pdf") after the conference.
WORKBOOK_FILE = ""

LINKS = {
    "parking": "https://nottingham.firstparking.co.uk/Event/Register/hXFbnJEB",
    "choices": "https://app.smartsheet.com/b/form/01a1025ecb13743983210fa2bb6a2f70",
    "venue": "https://www.nottinghamvenues.com/",
    "sports": "https://www.nottinghamvenues.com/david-ross-sports-village-nottingham",
    "directions": "https://www.google.com/maps/search/?api=1&query=East+Midlands+Conference+Centre+NG7+2RJ",
}

CONTACTS = [
    ("Helen Martin", "07970 400458", "+447970400458"),
    ("Tom Lee", "07814 075045", "+447814075045"),
    ("Andy Clay", "07484 929866", "+447484929866"),
]

# People shown on the delegate page.
HOST = {"name": "Charlotte Richardson", "role": "Your host", "photo": "img/charlotte-richardson.webp",
        "alt": "Charlotte Richardson"}

KEYNOTE = {
    "name": "Sue Day MBE", "role": "Director of Women's Football, The FA", "photo": "img/sue-day.webp",
    "alt": "Sue Day",
    "session": "Keynote: Leading the Orchestra. Day 2, 11.10am, Main Room 1.",
    "bio": [
        "Sue joined The FA in December 2024 as Director of Women's Football, where she is responsible for the next phase of development for the women's and girls' game and disability football in England, including delivery of the 2024-28 women's strategy.",
        "She previously spent six years on the board of the Rugby Football Union as Chief Operations Officer and Chief Financial Officer, where she played a leading role in establishing Premiership Women's Rugby as an independent league and in England's successful bid to host the 2025 Women's Rugby World Cup. A chartered accountant, she spent over 20 years at KPMG, becoming a partner in 2015.",
        "A former England captain, Sue won 59 caps between 1997 and 2007, played in three Rugby World Cups, won three Grand Slams and remains England women's record try-scorer with 61 tries. She was the first female President of Wasps FC and is a founding trustee of the Women's Sport Trust. She was awarded an MBE in 2020 for services to gender equality in sport and was named in the World Rugby Hall of Fame class of 2026.",
    ],
}

ILLUSTRATOR = {
    "name": "Tom Bradshaw", "role": "Live illustrator, ScribeYak",
    "about": "Tom is a scribe artist who specialises in live visual capture for conferences, talks and events. He will be drawing the conference as it happens, and you will see his illustrations at the round up on both days.",
    "link": ("See Tom's work at scribeyak.com", "https://scribeyak.com/"),
}

# Name and job title, in the order they first appear on the agenda.
SESSION_LEADS = [
    ("Tom Lee", "National Club Development Manager (Grassroots)"),
    ("Phil Woodward", "Head of Clubs and Facilities"),
    ("Mick Baikie", "Senior Club Development Manager"),
    ("Sarah Cummings", "National Club Development Manager"),
    ("Luke Bailey", "Club and Facilities Officer"),
    ("Richard Neal", "National Club Development Manager (NLS)"),
    ("Andy Clay", "Clubs and Facilities Development Manager"),
    ("Ian Grange", "Senior National Development Manager (Networks & Programmes)"),
]

MR1 = "Main Room 1"
MR2 = "Main Room 2"
CR1 = "Conference Room 1"
CR2 = "Conference Room 2"

# Group membership is the same on both days. Labels follow the deck slides.
GROUPS = [
    {
        "counties": ["Essex FA", "West Riding FA", "Lancashire FA", "Birmingham FA", "Surrey FA", "Durham FA", "Hampshire FA"],
        "d1": {"room": MR1, "group": "Group 1", "leads": "Steve Maker, Luke Bowles, Jo De Tute and Dominic Foley"},
        "d2": {"room": CR1, "group": "Group 1", "leads": "Luke Bowles, Jo De Tute and Dominic Foley"},
    },
    {
        "counties": ["Berks & Bucks FA", "Kent FA", "Cheshire FA", "Sheffield & Hallamshire FA", "Leicestershire FA", "Manchester FA", "Liverpool FA", "Devon FA"],
        "d1": {"room": MR1, "group": "Group 2", "leads": "Andy Baker and Ash Donovan"},
        "d2": {"room": MR1, "group": "Group 2", "leads": "Ash Donovan"},
    },
    {
        "counties": ["Derbyshire FA", "Northamptonshire FA", "Middlesex FA", "Gloucestershire FA", "Hertfordshire FA", "Lincolnshire FA", "London FA", "Norfolk FA", "Sussex FA"],
        "d1": {"room": MR1, "group": "Group 3", "leads": "Karl Lingham and Jemma Fairey"},
        "d2": {"room": MR1, "group": "Group 3", "leads": "Jemma Fairey"},
    },
    {
        "counties": ["Oxfordshire FA", "Staffordshire FA", "Northumberland FA", "Nottinghamshire FA", "Somerset FA", "Suffolk FA", "Cambridgeshire FA", "Worcestershire FA"],
        "d1": {"room": MR2, "group": "Group 1", "leads": "Chris Smith and Alex Scott"},
        "d2": {"room": CR2, "group": "Group 4", "leads": "Alex Scott"},
    },
    {
        "counties": ["Bedfordshire FA", "Cumberland FA", "Dorset FA", "East Riding FA", "North Riding FA", "Wiltshire FA", "Cornwall FA", "Shropshire FA", "Huntingdonshire FA", "Herefordshire FA", "Westmorland FA"],
        "d1": {"room": MR2, "group": "Group 2", "leads": "Katie Phillipson and Marc Di Carlo"},
        "d2": {"room": MR2, "group": "Group 5", "leads": "Marc Di Carlo"},
    },
]

PILLAR_ROOMS = [
    ("Leadership & Governance", "lg", CR2, "Richard Neal, Frank Bell, Mark Hilton and Tom Lee"),
    ("Coaches", "cv", MR2, "Bex Garlick and Lee Brown"),
    ("Volunteers", "cv", MR2, "Steph Powell, Ellie Reid, Mick Baikie and Laura Smith"),
    ("Facilities", "facilities", CR1, "Ian Grange, Liam Devlin, Mark Pover and Simon Wood"),
    ("Community", "community", MR1, "Sarah Cummings, Andy Baker and Rus Smith"),
]

# kind: "session" opens to show detail; "pause" is a plain row (breaks, meals, arrivals).
# "end_clubs" is the end time used when SHOW_CLUB_STORIES is True.
# "club" marks a club story row that only appears when SHOW_CLUB_STORIES is True.
DAY1 = [
    {"id": "d1-registration", "kind": "pause", "start": "09:30", "end": "10:30",
     "title": "Registration, refreshments and networking"},
    {"id": "d1-welcome", "kind": "session", "start": "10:30", "end": "10:40",
     "title": "Hello and welcome", "room": MR1,
     "who": "Charlotte Richardson, your host, and Tom Lee",
     "slides": ["d1-welcome"]},
    {"id": "d1-scene", "kind": "session", "start": "10:40", "end": "11:00",
     "title": "Setting the scene", "room": MR1,
     "who": "Phil Woodward and Mick Baikie",
     "about": "Where the programme stands today, the route to 1,000 Thriving Community Clubs, and the three things that will get us there: knowing your patch, teamwork and collaboration, and a development mindset.",
     "slides": ["d1-scene"]},
    {"id": "d1-breakout", "kind": "session", "start": "11:00", "end": "12:00",
     "title": "Breakout workshops", "room": "Main Room 1 or Main Room 2",
     "who": "Go to the workshop you have been allocated",
     "workbook": 4,
     "options": [
         {"name": "A Digital Journey (Data and Digital)", "room": MR1,
          "who": "Tom Lee, Sarah Cummings and Luke Bailey",
          "about": "Understand the different data and digital platforms, and build the skills, knowledge and capability to get the best out of them. Turn insight into impact: the right clubs, the right support, at the right time.",
          "slides": "d1-digital"},
         {"name": "National League System", "room": MR2,
          "who": "Richard Neal and Andrew Lomas",
          "about": "Explore what is different about working with clubs with National League System provision, the other expectations these clubs are obliged to meet (such as licensing and stadium accreditation), and why they might be uniquely positioned to help grow football participation in your area.",
          "slides": "d1-nls"},
     ]},
    {"id": "d1-lunch", "kind": "pause", "start": "12:00", "end": "13:00", "title": "Lunch"},
    {"id": "d1-teamwork", "kind": "session", "start": "13:00", "end": "14:00",
     "title": "Teamwork and Collaboration", "room": "Starts in Main Room 1, then your group",
     "who": "Andy Clay",
     "about": "See what great collaboration looks like through real examples from across the network. Tackle a real challenge, see what colleagues elsewhere are doing, and decide what you are taking back. Leave with one thing somebody else is doing that could make your job easier.",
     "workbook": 5, "groups": "d1",
     "slides": ["d1-teamwork"]},
    {"id": "d1-pillar", "kind": "session", "start": "14:00", "end": "15:00",
     "title": "Pillar Networking", "room": "Starts in Main Room 1, then your pillar",
     "who": "Sarah Cummings",
     "about": "Use your own Club Development Review data to get underneath the red and amber ratings on your pillar: the root causes, what is blocking progress, and the tactics and interventions that would fix both.",
     "workbook": 6, "pillars": True,
     "slides": ["d1-pillar"]},
    {"id": "d1-break", "kind": "pause", "start": "15:00", "end": "15:20", "title": "Break"},
    {"id": "d1-progression", "kind": "session", "start": "15:20", "end": "16:10",
     "title": "Accelerating Progression", "room": "Starts in Main Room 1, then find a space in any of the four rooms",
     "who": "Tom Lee",
     "about": "Turn what you learned in Pillar Networking into a two-season plan for your Thriving Community Clubs: what comes first, what comes second, and when FA Club Consultant one-to-one support is deployed.",
     "workbook": 7,
     "slides": ["d1-progression"]},
    {"id": "d1-roundup", "kind": "session", "start": "16:10", "end": "16:30",
     "title": "Day 1 round up and group photo", "room": MR1,
     "who": "Charlotte Richardson and Tom Lee",
     "about": "We pull the day together, Tom Bradshaw shares the illustrations he has drawn so far, and we finish with a group photo.",
     "more": ("About Tom Bradshaw", "#people")},
    {"id": "d1-checkin", "kind": "pause", "start": "16:30", "end": "19:00",
     "title": "Hotel check-in and downtime",
     "note": "Check in at The Orchard Hotel, use the facilities, catch up with colleagues or just relax."},
    {"id": "d1-evening", "kind": "pause", "start": "19:00", "end": "23:00", "hide_end": True,
     "title": "Drinks reception, street food dinner and interactive games",
     "note": "Main Room 1 and Main Room 2. Dress is smart casual."},
]

DAY2 = [
    {"id": "d2-registration", "kind": "pause", "start": "09:00", "end": "09:30",
     "title": "Registration, refreshments, networking and hotel check-out"},
    {"id": "d2-welcome", "kind": "session", "start": "09:30", "end": "09:40",
     "title": "Hello and welcome", "room": MR1,
     "who": "Charlotte Richardson, your host, and Tom Lee",
     "slides": ["d2-welcome"]},
    {"id": "d2-workforce", "kind": "session", "start": "09:40", "end": "10:50", "end_clubs": "10:30",
     "title": "Empowering the Club Workforce", "room": MR1,
     "who": "Steph Powell, Ellie Reid, Mick Baikie and Laura Smith",
     "about": "Understand the volunteer development framework and find practical ways to support off-pitch volunteers. By the end you will have the makings of a County FA plan and a club-based plan covering growth, development, diversification and celebration.",
     "workbook": 8,
     "slides": ["d2-workforce"]},
    {"id": "d2-club1", "kind": "session", "club": True, "start": "10:30", "end": "10:50",
     "title": "Club story: AFC Pogmoor", "room": MR1,
     "who": "In conversation with Charlotte Richardson"},
    {"id": "d2-break", "kind": "pause", "start": "10:50", "end": "11:10", "title": "Break"},
    {"id": "d2-keynote", "kind": "session", "start": "11:10", "end": "12:00",
     "title": "Keynote: Leading the Orchestra", "room": MR1,
     "who": "Sue Day MBE, Director of Women's Football at The FA, with Charlotte Richardson",
     "about": "Our keynote from Sue Day. There is space for your notes in the workbook.",
     "more": ("About Sue Day", "#people"),
     "workbook": 9},
    {"id": "d2-lmd", "kind": "session", "start": "12:00", "end": "12:30",
     "title": "Lead, Manage, Do", "room": "Starts in Main Room 1, then your group",
     "who": "Andy Clay",
     "about": "Are we actually putting it into practice? Peer-to-peer conversations built on real examples and three questions: what needs to happen, who have I got around me, and what is my role?",
     "workbook": 9, "groups": "d2",
     "slides": ["d2-lmd"]},
    {"id": "d2-lunch", "kind": "pause", "start": "12:30", "end": "13:30", "title": "Lunch"},
    {"id": "d2-growing", "kind": "session", "start": "13:30", "end": "14:30", "end_clubs": "14:10",
     "title": "Growing Pains", "room": MR1,
     "who": "Richard Neal, Frank Bell and Mark Pover",
     "about": "Get ready for the growth pressures that come with Thriving Community Clubs, with real examples. Leave knowing the pressures clubs face when they grow quickly, how to spot them on the horizon, and what to have ready.",
     "workbook": 10},
    {"id": "d2-club2", "kind": "session", "club": True, "start": "14:10", "end": "14:30",
     "title": "Club story: Knowle FC", "room": MR1,
     "who": "In conversation with Charlotte Richardson"},
    {"id": "d2-impact", "kind": "session", "start": "14:30", "end": "15:00", "end_clubs": "14:40",
     "title": "Demonstrating Impact", "room": MR1,
     "who": "Sarah Cummings and Luke Bailey",
     "about": "How we demonstrate real impact through Club Development Reviews, what those reviews look like, and what to expect for your clubs and your county.",
     "workbook": 11,
     "slides": ["d2-impact"]},
    {"id": "d2-club3", "kind": "session", "club": True, "start": "14:40", "end": "15:00",
     "title": "Club story: Brereton FC", "room": MR1,
     "who": "In conversation with Charlotte Richardson"},
    {"id": "d2-vision", "kind": "session", "start": "15:00", "end": "15:15",
     "title": "Future Vision", "room": MR1,
     "who": "Phil Woodward and Mick Baikie",
     "about": "What the Board told us, the ambition beyond 2028, and our shared task: national ambition, local leadership, lasting impact.",
     "slides": ["d2-vision"]},
    {"id": "d2-roundup", "kind": "session", "start": "15:15", "end": "15:45",
     "title": "Day 2 round up and conference reflections", "room": MR1,
     "who": "Charlotte Richardson and Tom Lee",
     "about": "Bring the two days together in your Better Everywhere Gameplan, with Tom Bradshaw's illustrations of the conference. Write your pledge in your workbook, then share a short version on Slido.",
     "workbook": 12,
     "slides": ["d2-roundup"]},
    {"id": "d2-depart", "kind": "pause", "start": "15:45", "end": "15:45", "hide_end": True,
     "title": "Conference closes"},
]

DAYS = [
    {"key": "day1", "date": "2026-10-20", "label": "Day 1", "long": "Tuesday 20 October", "sessions": DAY1},
    {"key": "day2", "date": "2026-10-21", "label": "Day 2", "long": "Wednesday 21 October", "sessions": DAY2},
]

# Slides shown to delegates, by page number of the master deck PDF.
# Each set unlocks on the page when its session starts.
SLIDE_PAGES = {
    "d1-welcome": [4],
    "d1-scene": list(range(13, 23)),
    "d1-digital": [25, 26, 27, 28, 30, 34],
    "d1-nls": [35],
    "d1-teamwork": list(range(42, 49)),
    "d1-pillar": [53, 54, 55, 56, 57, 58, 59, 60],
    "d1-progression": [65, 66, 67, 68],
    "d2-welcome": [77],
    "d2-workforce": [85, 86, 87, 89, 90, 91, 92],
    "d2-lmd": list(range(102, 110)),
    "d2-impact": [120, 121],
    "d2-vision": [127, 128, 129, 130, 131],
    "d2-roundup": [141],
}

# Short descriptions for people who cannot see the slide images.
SLIDE_ALT = {
    4: "Day 1 agenda, from Hello and welcome at 10.30am to the evening reception at 7.00pm.",
    13: "Setting the scene.",
    14: "We've made a strong start: foundations in 2024-25, practice in 2025-26, impact in 2026-28.",
    15: "Proof it's working: 93% stronger relationships, 76% more proactive, 88% long-term mindset, 98% intervention support, 95% positive difference.",
    16: "The next 2 years: stronger clubs, opportunities and system.",
    17: "The route to 1,000 is clear.",
    18: "Success factors: know your patch gives insight, teamwork and collaboration gives capability, and a development mindset joins the two.",
    19: "Understand the club.",
    20: "Tailor the support: understand, support, progress.",
    21: "Progress that lasts: trusted relationships, continuous learning, generational impact.",
    22: "National ambition, local progress: which clubs, what commitment, what support?",
    25: "A Digital Journey, in Main Room 1 with Tom Lee, Sarah Cummings and Luke Bailey.",
    26: "A Digital Journey: Power BI answers which clubs, the Club Programme Platform answers what support, and The Playbook answers what next step.",
    27: "The aim: turn insight into impact. Use the digital journey to make better decisions and provide the right clubs, the right support, at the right time.",
    28: "Slido question: what are your unanswered questions about the platforms in our Digital Journey?",
    30: "Which clubs? Build your Thriving Community Clubs pipeline: identify 5 clubs that are strategically important in your County FA, looking at strong pathways, the National League System and Women's Football Pyramid, and facility investment.",
    34: "Slido discussion: future insights from the Power BI dashboards, future functionality for the Club Programme Platform and The Playbook, and the resources and support to push directly to clubs.",
    35: "National League System workshop, in Main Room 2 with Richard Neal and Andrew Lomas.",
    42: "Teamwork and Collaboration groupings by room, group lead and County FA. The same information is under Your sessions on this page.",
    43: "The activity: challenge, move and steal, act.",
    44: "You told us: workforce capacity, accessing the right expertise, Club Consultant relationships, stretched volunteers, working across teams.",
    45: "The aim: leave with one thing somebody else is doing that could make your job easier.",
    46: "Challenge: pick one card, flip it, tackle it.",
    47: "Move and steal: find your station, get underneath why it worked, what could you steal?",
    48: "Act: what's the one thing you're stealing, who will you stay connected with? Capture it in your workbook.",
    53: "The activity: root causes, blocking progress, tactics and interventions.",
    54: "Pillar groupings: Leadership & Governance, Coaches, Volunteers, Facilities, Community.",
    55: "Leadership & Governance themes: outdated legal structures, limited understanding of liability and incorporation, poor succession planning, reliance on 3 or 4 volunteers, weak operational structures, no clear long-term vision.",
    56: "Coaches themes: recruitment and retention, burnout, low engagement with coach development, travel barriers, workforce diversity.",
    57: "Volunteers themes: recruitment and retention, burnout, difficulty recruiting off-pitch volunteers, travel barriers for courses, workforce diversity.",
    58: "Facilities themes: demand for 3G pitches, pitch availability, wet winters, few clubs owning facilities, varied funding awareness, need for inclusive facilities.",
    59: "Slido question: if The FA, Football Foundation and County FAs could do one thing to help clubs maximise the use and quality of their facilities, what would it be?",
    60: "Community themes: clubs disconnected from communities, little data collection, weak marketing and communications, few external partnerships, Club Impact Calculator well received, appetite for wellbeing workshops.",
    65: "Pyramid of Progression: red at risk, amber developing, green strong, gold thriving, each with its focus and tools.",
    66: "The activity: sequencing, tactics and practices, accelerating progress.",
    67: "Accelerating Progress template with three columns: sequencing activity, tactics and practices, accelerating progress.",
    68: "Slido question: what is the one single resource or intervention we have missing that can accelerate progression?",
    77: "Day 2 agenda, from Hello and welcome at 9.30am to depart at 3.45pm.",
    85: "The activity: club challenges, understanding the current offer, creating a Thriving Community Club workforce plan.",
    86: "Setting the scene: 70% of club administrators and officials are satisfied in their role, workload is landing on a few key officials, and over half of Thriving Community Clubs want to evolve their volunteer structure but have no plan.",
    87: "Growth and capacity mapped to the Pyramid of Progression, from role profiles and operational structure up to the strategic development of volunteers.",
    89: "FA Volunteer Development Framework: grow, diversify, learning and development, celebrate.",
    90: "70-20-10 learning model: in club and in action, networking and on action, formal learning.",
    91: "Activity: create a support plan for an example club's off-pitch volunteers covering growth, development, diversification and celebration, and consider how a County FA plan can support it.",
    92: "Empowering the Club Workforce template: a club-based plan beside a County FA approach plan.",
    102: "Lead, Manage, Do groupings by room, group lead and County FA. The same information is under Your sessions on this page.",
    103: "The journey: Development Mindset asks what does this club need next; Lead, Manage, Do asks what is my role in making that happen.",
    104: "The aim: are we actually putting it into practice?",
    105: "The activity: what needs to happen, who have I got around me, what is my role?",
    106: "What needs to happen? Start with a real club, priority or challenge. Ask what actually needs to change here.",
    107: "Who have I got around me? Within your County FA, FA support and Club Consultants, partners and the wider network.",
    108: "What is my role? Lead: create direction, prioritise, influence. Manage: bring the right people together and coordinate. Do: step in where your own expertise adds value.",
    109: "The challenge: what am I currently doing that somebody else might be better equipped to do?",
    120: "Your impact so far: 1,800 clubs named around a star, with one success story of a club that set up its legal structure, upgraded facilities, introduced disability provision and achieved 3-star accreditation.",
    121: "Club Development Reviews plus success stories equals impact demonstrated.",
    127: "What the board told us: backed, challenged, looking ahead.",
    128: "Ambition: 1,000, stronger.",
    129: "Why stronger clubs matter: more football, inclusion, value.",
    130: "Beyond 2028: better facilities, more opportunities, community connection, stronger people, stronger leadership.",
    131: "Our shared task: national ambition, local leadership, lasting impact.",
    141: "Illustration of a football pitch full of conference themes, titled Let's make the pledge.",
}
