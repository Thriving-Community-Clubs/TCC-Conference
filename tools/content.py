"""Content for the Better Everywhere conference delegate page.

Edit this file, then run:  python3 tools/build.py
Times are local time in Nottingham (British Summer Time, UTC+01:00).
"""

TZ = "+01:00"

# Switch to True once the clubs have confirmed. Adds the three club stories
# to the Day 2 agenda and shortens the sessions before them to match the deck.
SHOW_CLUB_STORIES = False

# The Slido event. Set SLIDO_URL to "" to hide the Slido section and buttons.
SLIDO_URL = "https://app.sli.do/event/b9EDPXgxX4wQAkY91z1iSJ"
# The joining code people type at slido.com, without the #.
SLIDO_CODE = "1283463"
# Paste the feedback survey link here after the conference.
FEEDBACK_URL = ""
# The workbook PDF, made by tools/make_workbook.py. Set to "" to take the workbook off the page.
WORKBOOK_FILE = "files/delegate-workbook.pdf"

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
HOST = {
    "name": "Charlotte Richardson", "first": "Charlotte", "role": "Sports broadcaster and conference host",
    "photo": "img/charlotte-richardson.webp", "alt": "Charlotte Richardson",
    "bio": [
        "Charlotte is a freelance presenter, reporter and football commentator who became talkSPORT's first female commentator and covers the whole football pyramid on radio and TV. Her broadcasting career began in BBC local radio before she was chosen to report for Final Score, and she is a regular voice on Times Radio Breakfast and a pitch-side presenter and live host for Charlton TV at The Valley.",
        "Grassroots football runs through her work. She is an FA Club Consultant and travels the country presenting the FA Club Hub podcast, In The Box, and before moving into broadcasting she worked in marketing and communications at Gillingham FC and Kent FA. In 2016 she founded Eighth Wonder, a programme to develop football's future female leaders, aimed at 14 to 20 year olds, which has helped more than 35 women into coaching.",
    ],
}

KEYNOTE = {
    "name": "Sue Day MBE", "first": "Sue", "role": "Director of Women's Football, The FA", "photo": "img/sue-day.webp",
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

# The workbook as shown on the page: (page number or None, description for people who cannot see the image).
# The numbers printed in the workbook match the PDF's own page count (the cover is page 1).
# One entry per page of the PDF, in order. Images are made by tools/make_workbook.py.
WORKBOOK_PAGES = [
    (None, "Front cover: Better Everywhere, Thriving Community Clubs Conference 2026."),
    (None, "Photograph of a player with a football, framed by a white star."),
    (3, "Welcome message."),
    (4, "Your name and County FA, then starter questions on knowing my patch, teamwork and collaboration, and development mindset."),
    (5, "Breakout workshops: space for notes on the workshop you attended."),
    (6, "Teamwork and Collaboration: connect, share, steal or adapt, act, and a score from 1 to 10 for four challenges."),
    (7, "Pillar Networking: root causes, barriers blocking progress, and tactics and interventions."),
    (8, "Accelerating Progression: the Pyramid of Progression and a two-season plan by quarter."),
    (9, "Empowering the Club Workforce: five questions on volunteer growth, development pathways and paid roles."),
    (10, "Lead, Manage, Do: notes from the keynote and the three questions."),
    (11, "Growing Pains: common pressures, common threads and how to spot them coming."),
    (12, "Demonstrating Impact: the clubs you have supported and your approach to reviews."),
    (13, "My Better Everywhere Gameplan and my commitment."),
    (14, "Notes."),
    (None, "Photograph of a young player smiling, framed by a white star."),
    (None, "Back cover."),
]

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

# Group membership is the same on both days. Taken from the attendee session allocation
# spreadsheet (13 Oct): County FAs listed are those with staff attending.
# Day 1 rooms for groups 3 to 5 changed on 13 Oct to match the deck.
# County FAs whose staff attend Day 1 only (no Lead, Manage, Do group).
DAY1_ONLY = {"Westmorland FA"}

GROUPS = [
    {
        "counties": ["Essex FA", "West Riding FA", "Lancashire FA", "Birmingham FA", "Surrey FA", "Durham FA", "Hampshire FA"],
        "d1": {"room": MR1, "group": "Group 1", "leads": "Steve Maker, Luke Bowles, Jo de Tute and Dominic Foley"},
        "d2": {"room": CR1, "group": "Group 1", "leads": "Luke Bowles, Jo de Tute and Dominic Foley"},
    },
    {
        "counties": ["Berks & Bucks FA", "Kent FA", "Cheshire FA", "Sheffield & Hallamshire FA", "Leicestershire FA", "Manchester FA", "Liverpool FA", "Devon FA"],
        "d1": {"room": MR1, "group": "Group 2", "leads": "Andy Baker and Ashley Donovan"},
        "d2": {"room": MR1, "group": "Group 2", "leads": "Ashley Donovan"},
    },
    {
        "counties": ["Derbyshire FA", "Northamptonshire FA", "Middlesex FA", "Gloucestershire FA", "Hertfordshire FA", "Lincolnshire FA", "London FA", "Norfolk FA", "Sussex FA"],
        "d1": {"room": MR2, "group": "Group 3", "leads": "Karl Lingham and Jemma Fairey"},
        "d2": {"room": MR1, "group": "Group 3", "leads": "Jemma Fairey"},
    },
    {
        "counties": ["Oxfordshire FA", "Staffordshire FA", "Northumberland FA", "Nottinghamshire FA", "Somerset FA", "Suffolk FA", "Cambridgeshire FA"],
        "d1": {"room": CR1, "group": "Group 4", "leads": "Chris Smith and Alex Scott"},
        "d2": {"room": CR2, "group": "Group 4", "leads": "Alex Scott"},
    },
    {
        "counties": ["Bedfordshire FA", "Cumberland FA", "Dorset FA", "East Riding FA", "North Riding FA", "Wiltshire FA", "Cornwall FA", "Huntingdonshire FA", "Herefordshire FA", "Westmorland FA"],
        "d1": {"room": CR2, "group": "Group 5", "leads": "Katie Phillipson and Marc Di Carlo"},
        "d2": {"room": MR2, "group": "Group 5", "leads": "Marc Di Carlo"},
    },
]

PILLAR_ROOMS = [
    ("Leadership & Governance", "lg", CR2, "Richard Neal, Frank Bell, Mark Hilton and Tom Lee"),
    ("Coaches", "cv", MR2, "Rebecca Garlick, Lee Brown and Andy Somers"),
    ("Volunteers", "cv", MR2, "Steph Powell, Ellie Reid, Mick Baikie and Laura Smith"),
    ("Facilities", "facilities", CR1, "Ian Grange, Liam Devlin, Mark Pover and Simon Wood"),
    ("Community", "community", MR1, "Sarah Cummings, Andy Baker and Rus Smith"),
]

# Resources shown inside a session in the agenda, keyed by session id.
SESSION_RESOURCES = {
    "d1-teamwork": [
        {
            "title": "Steal & Adapt: good practice from your band",
            "pdf": "files/steal-and-adapt.pdf",
            "pages": [
                ("resources/steal-and-adapt/page-1.webp", 1400, 990, "Steal and Adapt, Band A. Examples of good practice around collaboration within County FA teams, FA Club Consultants and other County FA support staff from counties in Band A. What could you steal and adapt for your County?", "Band A"),
                ("resources/steal-and-adapt/page-2.webp", 1400, 990, "Steal and Adapt, Band B. Examples of good practice around collaboration from counties in Band B. What could you steal and adapt for your County?", "Band B"),
                ("resources/steal-and-adapt/page-3.webp", 1400, 990, "Steal and Adapt, Band C. Examples of good practice around collaboration from counties in Band C. What could you steal and adapt for your County?", "Band C"),
                ("resources/steal-and-adapt/page-4.webp", 1400, 990, "Steal and Adapt, Band D. Examples of good practice around collaboration from counties in Band D. What could you steal and adapt for your County?", "Band D"),
            ],
        },
    ],
}

# Resources shown under a pillar in the Pillar Networking session.
# Keyed by the pillar name used in PILLAR_ROOMS. Prepare files with tools/add_resource.py.
# Each page is (image path, width, height, description for people who cannot see it[, caption]).
# Each link is (label, address[, note shown beside it]).
# The caption defaults to "Page n of N".
PILLAR_RESOURCES = {
    "Leadership & Governance": [
        {
            "title": "Leadership & Governance: help and support guide",
            "pdf": "files/leadership-governance-support-guide.pdf",
            "pages": [
                ("resources/leadership-governance-support-guide/page-1.webp", 1240, 1752,
                 "Leadership & Governance help and support guide, page 1. Everything currently available under this pillar, and where to find it. One, the Club Leadership Programme with UCFB. Two, Financial Controls from England Football. Three, legal and governance support from The FA and Muckle LLP, with FA Bitesize Guides and guidance on data protection and club structures. Four, video guides on The Club Hub on YouTube. The links are listed below the pages."),
                ("resources/leadership-governance-support-guide/page-2.webp", 1240, 1752,
                 "Leadership & Governance help and support guide, page 2. Five, tools and guidance in the PlayBook: VAT assessment information, VAT guidance, a VAT flow chart and a VAT case study toolkit for clubs, the Club Structures Assistant and the Resource Sharing Agreement. Six, workshops for 2026 in the PlayBook: Financial Controls and VAT, and Club Legal Structures and Governance."),
            ],
            # The guide's links, so they can be opened from the page. The image of the guide cannot be clicked.
            "links": [
                ("Club Leadership Programme, with UCFB", [
                    ("View the Club Leadership Programme", "https://www.ucfb.ac.uk/your-degree/executive-education/fa-club-leadership-programme/"),
                ]),
                ("Financial Controls, England Football", [
                    ("Read the Financial Controls guidance", "https://www.englandfootball.com/participate/leagues-and-clubs/Financial-Control"),
                ]),
                ("Legal and governance support, The FA and Muckle LLP", [
                    ("The FA and Muckle LLP hub", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/"),
                    ("FA Bitesize Guide: Financial Controls", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-financial-controls/"),
                    ("FA Bitesize Guide: Governance Standards", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-governance/"),
                    ("FA Bitesize Guide: Incorporation & Legal Structures", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-incorporation-legal-structures/"),
                    ("FA Bitesize Guide: Leadership", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-leadership/"),
                    ("FA Bitesize Guide: Risk Management", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-risk-management/"),
                    ("FA Bitesize Guide: Special Tax Status & Trading", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-bitesize-guides/fa-bitesize-special-tax-status-trading/"),
                    ("FA Data Protection Factsheets", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/gdpr-factsheets/"),
                    ("FA Data Protection Templates", "https://www.muckle-llp.com/what-we-do/sectors/sports/the-football-association/fa-template-documents/"),
                    ("The FA's Guide to Club Structures (PDF)", "https://www.muckle-llp.com/files/pdf/19799_THE_FA_REMAKE-OF-THE-CLUB-STRUCTURES_L.pdf"),
                ]),
                ("Video guides, The Club Hub on YouTube", [
                    ("Football Club Governance with Muckle LLP: the full playlist", "https://youtube.com/playlist?list=PLlPyxLEijGBoCmdjykakE8KbtfOgV3Z_-"),
                    ("Managing data & risk at your football club", "https://youtu.be/OFaBeM8kZic"),
                    ("Which legal structure should your football club have?", "https://youtu.be/MpzkJFACpzg"),
                    ("How leadership can help shape a successful football club", "https://youtu.be/XZxDjCfL4pM"),
                    ("How to optimise your football club's finances", "https://youtu.be/03nZvOi0XpM"),
                ]),
                ("Tools, guidance and workshops, in the PlayBook", [
                    ("Open the PlayBook (log in needed)", "https://theplaybook.thefa.com/dashboard"),
                    ("Open the Club Structures Assistant", "https://club-structures.muckle-llp.com/",
                     "Signpost only to eligible clubs you are directly supporting."),
                ]),
            ],
        },
    ],
    "Volunteers": [
        {
            "title": "Volunteers: help and support guide",
            "pdf": "files/volunteers-support-guide.pdf",
            "pages": [
                ("resources/volunteers-support-guide/page-1.webp", 1241, 1754,
                 "Volunteers help and support guide, page 1. Everything currently available to help clubs and leagues recruit, develop, keep and celebrate their volunteers. One, learning and development from England Football Learning: The FA Club Maker, Run Football Club Edition, Run Football League Edition, EE Playmaker, the Personal Development Compass and England Football Learning. Two, Growing Volunteers from England Football, with resources to download: Volunteer Planning Toolkit, Volunteer Welcome Pack, Volunteer Roles and Tasks guide, Football Volunteer Agreement, volunteer profile videos and editable role profiles. The links are listed below the pages."),
                ("resources/volunteers-support-guide/page-2.webp", 1241, 1754,
                 "Volunteers help and support guide, page 2. Three, celebrating volunteers with The England Football Family: membership, the Grassroots Football Awards, thank-you films and finding volunteering opportunities. Four, volunteer planning in the PlayBook: the Volunteer Planning Toolkit for clubs and leagues, the Volunteer Planning Workshop for workshop delivery, and the Volunteer Planning Checklist for County FAs."),
            ],
            # The guide's links, so they can be opened from the page. The image of the guide cannot be clicked.
            "links": [
                ("Learning and development, England Football Learning", [
                    ("See all volunteer courses", "https://www.englandfootball.com/participate/volunteer/Learning-and-Development-for-Volunteers"),
                    ("The FA Club Maker", "https://learn.englandfootball.com/mylearning?courseUrl=https://mylearning.englandfootball.com/learn/courses/232/club-maker"),
                    ("Run Football: Club Edition", "https://learn.englandfootball.com/mylearning?courseUrl=https://mylearning.englandfootball.com/learn/courses/233/run-football-club-edition/"),
                    ("Run Football: League Edition", "https://mylearning.englandfootball.com/learn/courses/390/run-football-league-edition/lessons"),
                    ("EE Playmaker", "https://learn.englandfootball.com/courses/football/ee-playmaker"),
                    ("Personal Development Compass", "https://mylearning.englandfootball.com/learn/courses/388/personal-development-compass-building-personal-capability/lessons"),
                    ("Personal Development Compass workbooks", "https://community.thefa.com/youth-leadership-volunteering/b/latest-news/posts/england-football-personal-development-compass-workbooks"),
                    ("England Football Learning", "https://learn.englandfootball.com/"),
                ]),
                ("Growing volunteers, England Football", [
                    ("Go to Growing Volunteers", "https://www.englandfootball.com/participate/volunteer/Growing-Volunteers"),
                    ("Find volunteering opportunities on Find Football", "https://find.englandfootball.com/onboarding/volunteer"),
                ]),
                ("Celebrating volunteers, The England Football Family", [
                    ("Go to Celebrating Volunteers and the Volunteer Video Hub", "https://www.englandfootball.com/participate/volunteer/Celebrating-Volunteers"),
                    ("Join the England Football Family", "https://www.englandfootball.com/participate/volunteer/Volunteer-Membership-Registration"),
                    ("Grassroots Football Awards", "https://www.englandfootball.com/participate/Grassroots-Football-Awards"),
                ]),
                ("Volunteer planning, in the PlayBook", [
                    ("Open the PlayBook (log in needed)", "https://theplaybook.thefa.com/dashboard"),
                ]),
            ],
        },
        {
            "title": "FA Volunteer Development Framework",
            "pdf": "files/volunteer-development-framework.pdf",
            "pages": [
                ("resources/volunteer-development-framework/page-1.webp", 1400, 991,
                 "FA Volunteer Development Framework, overview. The FA Volunteering Development Team and the FA Club Development Team support volunteers across four areas. Grow: Volunteer Planning Toolkit and Workshops, National Strategic Partnerships, Local Strategic Partnerships, National Recruitment Campaigns. Diversify: Youth Voice and Leadership Ecosystem, FA funded casual workforce of EDI, Equal Game and Disability Football ambassadors, FA funded volunteer coordinators for female and disability growth, FA Volunteer Conferences. Learning and development, from unaware to interested, involved and invested: Your Game, BBC Bitesize Follow Your Passion, Club Maker, FA Leadership Academy, Rising Leaders, Emerging Club Leaders, Run Football Club and League Editions, Personal Development Compass, Equal Game, Journey to Inclusion, TCC Pillar Workshops, Operational and Strategic Leaders. Celebrate: The England Football Family, the Grassroots Football Awards, the Volunteer Thank You Campaign, in-club celebration resources. Links to the FA Volunteering Hub, the Volunteer Development Dashboard and the Find Volunteering tool. The links are listed below the pages.", "Overview"),
                ("resources/volunteer-development-framework/page-2.webp", 1241, 1754,
                 "Grow. Volunteer Planning Toolkit and Workshops: guidance, templates and role profiles for clubs and leagues, online and in County FA workshops. National Strategic Partnerships such as Access Sport, Women in Football and the Duke of Edinburgh Award. Local Strategic Partnerships such as the Council for Voluntary Service, faith groups and disability charities. National Recruitment Campaigns such as Made For This Game and the Disability Volunteering Marketing Campaign.", "Grow"),
                ("resources/volunteer-development-framework/page-3.webp", 1241, 1754,
                 "Diversify. Youth Voice and Leadership Ecosystem for young volunteers aged 16 to 24: FA National Youth Council, FA Leadership Academy, FA Youth Leadership Network, FA Rising Leaders and County FA Youth Councils. FA funded casual workforce: EDI Community of Practice, Equal Game and Disability Football ambassadors. 13 part-time FA funded volunteer coordinators to grow female and disabled volunteers. FA Volunteer Conferences for prospective volunteers.", "Diversify"),
                ("resources/volunteer-development-framework/page-4.webp", 1241, 1754,
                 "Learning and development. Your Game (ages 14 to 24), Club Maker (ages 18 to 25), FA Leadership Academy (ages 16 to 24), Rising Leaders (ethnically diverse young women aged 16 to 19), the Personal Development Compass (ages 14 to 24) and Run Football: Club Edition for new club committee volunteers, each with its audience and how it is delivered.", "Learning and development"),
                ("resources/volunteer-development-framework/page-5.webp", 1241, 1754,
                 "Learning and development, continued. Run Football: League Edition, Equal Game workshops, Journey to Inclusion workshops, TCC Pillar Workshops, Emerging Club Leaders, Operational Club Leaders and Strategic Club Leaders through UCFB. Training for County FAs in volunteer development interventions is on The Training Ground.", "Learning and development, continued"),
                ("resources/volunteer-development-framework/page-6.webp", 1241, 1754,
                 "Celebrate. The England Football Family membership and rewards for any volunteer, the Grassroots Football Awards with nominations in March and April, and the Volunteer Thank You Campaign from September to December.", "Celebrate"),
            ],
            "links": [
                ("Across the framework", [
                    ("FA Volunteering Hub", "https://www.englandfootball.com/participate/volunteer/growing-volunteers"),
                    ("Volunteer Development Dashboard", "https://app.smartsheet.com/dashboards/HqPgqhXR7Vg2vMp6Qc9mGgfqHFj3h5c6GpMFrMP1", "Opens in Smartsheet"),
                    ("Find Volunteering tool", "https://find.englandfootball.com/onboarding/volunteer"),
                ]),
                ("Grow", [
                    ("Volunteer Planning Toolkit and Workshops", "https://www.englandfootball.com/participate/volunteer/growing-volunteers"),
                    ("National Strategic Partnerships: Access Sport disability volunteering pathway", "https://www.accesssport.org.uk/news/access-sport-and-the-fa-launch-new-disability-volunteering-pathway-in-grassroots-football"),
                    ("Local Strategic Partnerships", "https://englishfa.sharepoint.com/:w:/s/AValuedNetwork/IQDOoc7I9ghmQqOVqnWVrCU3AeAg5J-RsVJXIWXlAbA8wEQ?e=qaZkay", "Opens in FA SharePoint; sign-in needed"),
                    ("National Recruitment Campaigns", "https://englishfa.sharepoint.com/:f:/r/sites/AValuedNetwork/Shared%20Documents/1.%20Volunteers?d=w06a7bb7e752943c08468aa9f5a7fc806&csf=1&web=1&e=FRsVPs", "Opens in FA SharePoint; sign-in needed"),
                ]),
                ("Diversify", [
                    ("Youth Voice and Leadership Ecosystem", "https://www.englandfootball.com/participate/volunteer/Young-Volunteers"),
                    ("Equal Game", "https://www.englandfootball.com/participate/leagues-and-clubs/female-football-at-your-club?tab=EQUALGAME"),
                    ("Disability Football training", "https://www.englandfootball.com/play/Disability-Football/Training"),
                    ("FA Volunteer Conferences", "https://www.englandfootball.com/participate/volunteer/Volunteer-Conferences"),
                ]),
                ("Learning and development", [
                    ("Your Game", "https://englishfa.sharepoint.com/:f:/s/AValuedNetwork/IgCqXPwyos1LT61cy2IoPZhGAWBRO8kBSBUIfXruZFCvoR0?e=LFS4uy", "Opens in FA SharePoint; sign-in needed"),
                    ("BBC Bitesize: Follow Your Passion", "https://www.bbc.co.uk/bitesize/groups/c1e1leepl00t"),
                    ("Club Maker, Run Football and the Personal Development Compass", "https://www.englandfootball.com/participate/volunteer/learning-and-development-for-volunteers"),
                    ("FA Leadership Academy", "https://www.englandfootball.com/participate/volunteer/young-volunteers"),
                    ("Rising Leaders", "https://www.englandfootball.com/participate/women-and-girls/rising-leaders"),
                    ("Emerging Club Leaders (UCFB)", "https://www.ucfb.ac.uk/your-degree/executive-education/?courseType=executive&search=#degree-results"),
                    ("Journey to Inclusion", "https://www.englandfootball.com/disability-training-for-clubs"),
                    ("TCC Pillar Workshops, in the PlayBook", "https://theplaybook.thefa.com/", "Log in needed"),
                    ("Operational Club Leaders (UCFB)", "https://www.ucfb.ac.uk/your-degree/executive-education/fa-club-leadership-programme-operational-leaders/"),
                    ("Strategic Club Leaders (UCFB)", "https://www.ucfb.ac.uk/your-degree/executive-education/fa-club-leadership-programme/"),
                    ("The Training Ground, for County FA staff", "https://thetrainingground.curatr3.com/login", "Log in needed"),
                ]),
                ("Celebrate", [
                    ("The England Football Family and the Volunteer Thank You Campaign", "https://www.englandfootball.com/participate/volunteer/Celebrating-Volunteers"),
                    ("The Grassroots Football Awards", "https://www.englandfootball.com/participate/Grassroots-Football-Awards"),
                    ("In-club celebration resources", "https://englishfa.sharepoint.com/:b:/r/sites/AValuedNetwork/Shared%20Documents/1.%20Volunteers/CFA%20Support/Volunteer%20Celebration%20Tactics.pdf?d=w8c1623a82684470ab408b865c743397d&csf=1&web=1&e=8kddZP", "Opens in FA SharePoint; sign-in needed"),
                ]),
            ],
        },
    ],
    "Facilities": [
        {
            "title": "Facilities: help and support guide",
            "pdf": "files/facilities-support-guide.pdf",
            "pages": [
                ("resources/facilities-support-guide/page-1.webp", 1241, 1754,
                 "Facilities help and support guide, page 1. Everything currently available to help clubs improve, fund, run and look after their pitches and facilities. One, facilities guidance from England Football: pavilion and changing room guidance, pitch and goalpost safety, grass pitch use during drought, and hosting an InPost locker. Two, funding for facilities from the Football Foundation, covering pitches, buildings and site, equipment and safety, and programmes, with a note of what is not funded. The links are listed below the pages."),
                ("resources/facilities-support-guide/page-2.webp", 1241, 1754,
                 "Facilities help and support guide, page 2. Three, the Community Engagement Toolkit from the Football Foundation and its five stages of engagement. Four, The Greener Game with E.ON Next. Five, saving energy. Six, workshops and guides in the PlayBook: the 3G Pitch Activation Workshop, the Facilities Grass Pitches Workshop, the Home Advantage Programme guide and the Facilities and Investment Technical Expertise reference guide."),
            ],
            "links": [
                ("Facilities guidance, England Football", [
                    ("Go to Facilities Guidance", "https://www.englandfootball.com/participate/leagues-and-clubs/Facilities-Guidance"),
                    ("Pavilion and Changing Room Guidance (PDF)", "https://cdn.englandfootball.com/-/media/EnglandFootball/Files/run/leagues-and-clubs/PAVILION-AND-CHANGING-ROOM-GUIDANCE.pdf?rev=b4684735da3749419418d492815cc66f"),
                    ("Pitch and Goalpost Safety (PDF)", "https://cdn.englandfootball.com/-/media/EnglandFootball/Files/run/leagues-and-clubs/FA-Guide-to-pitch-and-goalpost-safety.pdf?rev=47beadcc779549a4a54604f49cb4c345"),
                    ("Grass Pitch Use During Drought (PDF)", "https://cdn.englandfootball.com/-/media/EnglandFootball/Files/run/leagues-and-clubs/Grass-Pitch-Usage-During-Drought---Guidance-for-Clubs-Leagues-and-Match-Officials.pdf?rev=b399d4fa79734f51af52ace0298d0572"),
                    ("Host an InPost locker", "https://www.englandfootball.com/participate/leagues-and-clubs/InPost"),
                ]),
                ("Funding for facilities, Football Foundation", [
                    ("See all funding", "https://footballfoundation.org.uk/looking-for-funding"),
                    ("3G Pitches", "https://footballfoundation.org.uk/grant/3g-pitch"),
                    ("Grass Pitch improvement", "https://footballfoundation.org.uk/get-your-pitch-match-fit"),
                    ("Creation of new grass pitches", "https://footballfoundation.org.uk/grant/new-grass-pitch"),
                    ("Grass Pitch Drainage", "https://footballfoundation.org.uk/grant/grass-pitch-drainage"),
                    ("Small-sided facility improvements", "https://footballfoundation.org.uk/grant/playing-surface-improvement"),
                    ("Changing Pavilions & Clubhouses", "https://footballfoundation.org.uk/grant/changing-pavilions-and-clubhouses"),
                    ("Catering Units", "https://footballfoundation.org.uk/grant/Catering-Unit"),
                    ("Storage Containers", "https://footballfoundation.org.uk/grant/storage-containers"),
                    ("Fencing", "https://footballfoundation.org.uk/grant/fencing"),
                    ("Goalposts", "https://footballfoundation.org.uk/grant/goalposts"),
                    ("3G Pitch Maintenance Machinery & Equipment", "https://footballfoundation.org.uk/grant/3g-maintenance"),
                    ("Grass Pitch Maintenance Machinery & Equipment", "https://footballfoundation.org.uk/grant/grass-pitch-maintenance-machinery-and-equipment"),
                    ("Premier League Defibrillator Fund", "https://footballfoundation.org.uk/grant/premier-league-defibrillator-fund"),
                    ("PlayZones", "https://footballfoundation.org.uk/playzones-programme"),
                    ("Hubs", "https://footballfoundation.org.uk/hubs-programme"),
                    ("Active Through Football", "https://footballfoundation.org.uk/active-through-football"),
                    ("Lionesses HERe to Play Fund", "https://footballfoundation.org.uk/lionesses-here-to-play"),
                    ("Premier League Stadium Fund", "https://premierleaguestadiumfund.co.uk/"),
                ]),
                ("Community Engagement Toolkit, Football Foundation", [
                    ("Open the toolkit", "https://footballfoundation.org.uk/Community-Engagement-Toolkit"),
                    ("Guidance by facility type", "https://footballfoundation.org.uk/cet-home-page/facility-types"),
                    ("Guidance by priority group", "https://footballfoundation.org.uk/cet-home-page/under-represented-audiences"),
                ]),
                ("The Greener Game, with E.ON Next", [
                    ("About the Greener Game", "https://www.englandfootball.com/participate/leagues-and-clubs/Greener-Game"),
                    ("Join the programme", "https://app.smartsheet.com/b/form/072c1176827c4c209d776ad83d66383e"),
                    ("Request the free energy support pack", "https://app.smartsheet.com/b/form/d16b72b54a1a4e9384e097523fa42f2d"),
                    ("Email greenergame@thefa.com", "mailto:greenergame@thefa.com?subject=Greener%20Game"),
                ]),
                ("Saving energy, Football Foundation", [
                    ("Read all the energy-saving tips", "https://footballfoundation.org.uk/energy-saving-hints-tips"),
                ]),
                ("Workshops and guides, in the PlayBook", [
                    ("Open the PlayBook (log in needed)", "https://theplaybook.thefa.com/dashboard"),
                ]),
            ],
        },
        {
            "title": "Howdens Game Changer Programme: application guidance for clubs",
            "pdf": "files/howdens-game-changer-application-guidance.pdf",
            "links_label": "Links from this guidance",
            "pages": [
                ("resources/howdens-game-changer-application-guidance/page-1.webp", 1241, 1241,
                 "Front cover: Howdens Game Changer Programme, application guidance for clubs.", "Page 1 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-2.webp", 1400, 700,
                 "Transforming kitchens for clubs and communities.", "Pages 2 and 3 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-3.webp", 1240, 1241,
                 "Photograph of a newly fitted club kitchen.", "Page 4 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-4.webp", 1241, 1241,
                 "Welcome. Howdens and The FA have extended their partnership for another year to offer more grassroots clubs the opportunity to apply for a Howdens kitchen. Applications for the 2026 programme open on 1 September 2026 and close on 31 October 2026. From James Kendall, Director of Football Development, The FA.", "Page 5 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-5.webp", 1240, 1241,
                 "Photograph of a Howdens Game Changer Programme sign.", "Page 6 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-6.webp", 1241, 1241,
                 "About the programme. Howdens partnered with The FA in 2023 to invest 3 million pounds in improving grassroots club kitchens, with a further 1 million pounds now secured.", "Page 7 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-7.webp", 1240, 1241,
                 "Who can apply? England Football Accredited clubs that are 2 or 3 star, or 1 star with at least six teams, including National League Pyramid clubs. The club must own its facilities, or have a lease or licence of five years or longer with the landlord's consent.", "Page 8 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-8.webp", 1241, 1241,
                 "Who can't apply? Clubs outside those accreditation levels, individuals and sole traders, national governing bodies, Premier League and Football League clubs, educational establishments providing facilities solely for their students, local authorities and professional club community organisations.", "Page 9 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-9.webp", 1240, 1241,
                 "What we will support: Howdens supplies the kitchen, including cabinets, worktops, sinks, taps and appliances. What we will not support: plumbing and electrical work, flooring, decoration, furniture, small freestanding appliances and structural works.", "Page 10 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-10.webp", 1241, 1241,
                 "Photograph of a football in front of a goal.", "Page 11 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-11.webp", 1240, 1241,
                 "Photograph of a club kitchen with a coffee machine and drinks fridge.", "Page 12 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-12.webp", 1241, 1241,
                 "What do you need to consider before getting started on your application? Things to consider, and the types of projects the programme wants to fund.", "Page 13 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-13.webp", 1240, 1241,
                 "A hand-drawn sketch plan of a kitchen and servery, with measurements.", "Page 14 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-14.webp", 1241, 1241,
                 "Getting started with your application: the form must be completed in one go, and what to include with it, such as a dimensioned sketch plan, photos, evidence of security of tenure, landlord's consent and insurance.", "Page 15 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-15.webp", 1240, 1241,
                 "Getting started with your application, continued. How your application will be assessed: during November and December 2026, with decisions in February 2027, and the criteria used to prioritise.", "Page 16 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-16.webp", 1241, 1241,
                 "If you are successful, what happens next: the award pack, the on-site meeting with your local Howdens depot and fitter, design, sign-off and installation.", "Page 17 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-17.webp", 1240, 1241,
                 "Frequently asked questions: what the award can be used for, refurbishment and redecoration, accepting the award, and how the project is monitored.", "Page 18 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-18.webp", 1241, 1241,
                 "Frequently asked questions on eligibility and the application process: when the window is open, how long the form takes, bid consultants, and who is eligible.", "Page 19 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-19.webp", 1240, 1241,
                 "Frequently asked questions, continued: security of tenure, not nominating a fitter, and clubs with more than one site.", "Page 20 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-20.webp", 1241, 1241,
                 "Photograph of a circular saw cutting a worktop, with the words Crafted at the heart of your community.", "Page 21 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-21.webp", 1240, 1241,
                 "Frequently asked questions, continued: how to apply, previous Football Foundation funding, when you will hear, installation timing, work already started, reapplying and why an application might be rejected.", "Page 22 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-22.webp", 1241, 1241,
                 "Frequently asked questions, continued: funding for other works, who to contact, who funds the programme, its aim, and other Football Foundation grants.", "Page 23 of 24"),
                ("resources/howdens-game-changer-application-guidance/page-23.webp", 1241, 1241,
                 "Back cover.", "Page 24 of 24"),
            ],
            "links": [
                ("Applying", [
                    ("Open the application form", "https://app.smartsheet.com/b/form/019fced56c2c7dc6bfcba19ca698bea7"),
                    ("Email howdens@footballfoundation.org.uk", "mailto:howdens@footballfoundation.org.uk"),
                ]),
                ("Related", [
                    ("View the Howdens kitchen range", "https://eng.football/dINMCN"),
                    ("Premier League Stadium Fund: clubhouses grant information", "https://premierleaguestadiumfund.co.uk/clubhouses-grant-information"),
                ]),
            ],
        },
    ],
    "Coaches": [
        {
            "title": "County FA Coach Development Lead: role purpose",
            "pages": [
                ("resources/coach-development-lead-role-purpose/page-1.webp", 1400, 787,
                 "County FA Coach Development Lead role purpose. One, support sustainable clubs: support England Football Accredited Clubs to become more sustainable by embedding the Thriving Community Club framework, aligning support services and facilitating collaboration between stakeholders. Two, grow coaching and coach development: lead the growth and sustainability of high-quality coaching and coach development in England Football Accredited Clubs, working with Coaching Leads on people-centred programmes aligned with the FA Learning Coach Development Framework. Three, create meaningful learning opportunities: ensure all coaches have access to meaningful learning, mentoring and development that helps them create positive experiences for every player. Question: how could you collaborate to overcome some of the coach and volunteer challenges faced by your clubs?"),
            ],
        },
        {
            "title": "Club Coaching Leads Development Programme: what, so what, now what?",
            "pages": [
                ("resources/club-coaching-leads-development-programme/page-1.webp", 1086, 1448,
                 "Club Coaching Leads Development Programme. Purpose: support the coaching pillar of the Thriving Community Club framework; 4,000 trained club coaching leads deployed within 2 and 3 star England Accredited clubs; 25% of coaches attending local CPD. To date: pilot programmes, consultation, content build, consultation, content design, consultation, roll out. Build considerations: FA Learning principles, adult learning principles, FA coach developer framework, enquiry-based learning, prior mentor developer series. Delivered by County FA coach development leads; Band 1 counties can nominate a casual coach developer to support, and Band 2 to 5 counties can propose one based on capacity, approved at the discretion of the regional manager. Coming next: training and familiarisation, monitoring and evaluation, ongoing support and development, retaining FA Club Coaching Lead status, alignment with England Accredited Clubs renewal, reward and recognition, scope of delivery, and a blended approach."),
            ],
        },
        {
            "title": "Game plan for grassroots coaching",
            "pdf": "files/game-plan-for-grassroots-coaching.pdf",
            "pages": [
                ("resources/game-plan-for-grassroots-coaching/page-1.webp", 1400, 788,
                 "Game plan for grassroots coaching: developing coaches, inspiring players, strengthening communities. At the centre: developers, delivery and diversity. Around them: connect learning, engage people, recognise progress and build partnerships."),
                ("resources/game-plan-for-grassroots-coaching/page-2.webp", 1400, 788,
                 "Developer workforce pyramid: 17 in the full-time coach development team, 40 County FA Coach Development Leads, 200 in the casual coach development workforce, and 4,000 Club Coaching Leads in Thriving Community Clubs."),
                ("resources/game-plan-for-grassroots-coaching/page-3.webp", 1400, 788,
                 "The learning offer. Live, strategic priorities with same month delivery: Know Your Format in September, Coaching fundamentals in November, Volume and variety in May. Super Library, equality, diversity and inclusion priorities with anytime delivery: Football without limits and Coaching Female Players. Library, always on: Getting Started, Enjoy and Participate, Lead and Manage Teams, and Helping Individuals."),
            ],
        },
    ],
    "Community": [
        {
            "title": "Community: help and support guide",
            "pdf": "files/community-support-guide.pdf",
            "pages": [
                ("resources/community-support-guide/page-1.webp", 1241, 1754,
                 "Community help and support guide, page 1. Everything currently available to help clubs connect with their community, evidence their impact, secure funding and tell their story. One, the Stakeholder Cribsheet, an online publication. Two, Building Common-Unity in your club, a workshop on Asset Based Community Development. Three, Build My Bid, a funding support service in the PlayBook. Four, the Club Impact Calculator in the PlayBook, which produces a Club Impact Report. The links are listed below the pages."),
                ("resources/community-support-guide/page-2.webp", 1241, 1754,
                 "Community help and support guide, page 2. Five, communications and marketing: the Effective Communications and Marketing workshop, covering the basics, the tools and the people, with three resources to use afterwards: the Club Communications and Social Media Planner, 10 Things Your Website Should Have, and the Effective Communications 11-a-side Team."),
            ],
            "links": [
                ("Stakeholder Cribsheet, online publication", [
                    ("Read the Stakeholder Cribsheet", "https://www.calameo.com/esports-media/read/001230235c30c3517ad02?authid=x8qk1vVkmvAs"),
                ]),
                ("Build My Bid, funding support service", [
                    ("Complete the Build My Bid expression of interest form", "https://app.smartsheet.com/b/form/019d1ab14e687d73ab6ad61108b97c2f"),
                ]),
                ("Everything else, in the PlayBook", [
                    ("Open the PlayBook (log in needed)", "https://theplaybook.thefa.com/dashboard"),
                ]),
            ],
        },
    ],
}

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
     "workbook": 5,
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
     "who": "Steve Maker",
     "about": "See what great collaboration looks like through real examples from across the network. Tackle a real challenge, see what colleagues elsewhere are doing, and decide what you are taking back. Leave with one thing somebody else is doing that could make your job easier.",
     "workbook": 6, "groups": "d1",
     "slides": ["d1-teamwork"]},
    {"id": "d1-pillar", "kind": "session", "start": "14:00", "end": "15:00",
     "title": "Pillar Networking", "room": "Starts in Main Room 1, then your pillar",
     "who": "Sarah Cummings",
     "about": "Use your own Club Development Review data to get underneath the red and amber ratings on your pillar: the root causes, what is blocking progress, and the tactics and interventions that would fix both.",
     "workbook": 7, "pillars": True,
     "slides": ["d1-pillar"]},
    {"id": "d1-break", "kind": "pause", "start": "15:00", "end": "15:20", "title": "Break"},
    {"id": "d1-progression", "kind": "session", "start": "15:20", "end": "16:10",
     "title": "Accelerating Progression", "room": "Starts in Main Room 1, then find a space in any of the four rooms",
     "who": "Tom Lee",
     "about": "Turn what you learned in Pillar Networking into a two-season plan for your Thriving Community Clubs: what comes first, what comes second, and when FA Club Consultant one-to-one support is deployed.",
     "workbook": 8,
     "slides": ["d1-progression"]},
    {"id": "d1-roundup", "kind": "session", "start": "16:10", "end": "16:30",
     "title": "Day 1 round up and group photo", "room": MR1,
     "who": "Charlotte Richardson and Tom Lee",
     "about": "We pull the day together, Tom Bradshaw shares the illustrations he has drawn so far, and we finish with a group photo.",
     "more": ("About Tom Bradshaw", "#illustrator")},
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
     "workbook": 9,
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
     "workbook": 10},
    {"id": "d2-lmd", "kind": "session", "start": "12:00", "end": "12:30",
     "title": "Lead, Manage, Do", "room": "Starts in Main Room 1, then your group",
     "who": "Andy Clay",
     "about": "Are we actually putting it into practice? Peer-to-peer conversations built on real examples and three questions: what needs to happen, who have I got around me, and what is my role?",
     "workbook": 10, "groups": "d2",
     "slides": ["d2-lmd"]},
    {"id": "d2-lunch", "kind": "pause", "start": "12:30", "end": "13:30", "title": "Lunch"},
    {"id": "d2-growing", "kind": "session", "start": "13:30", "end": "14:30", "end_clubs": "14:10",
     "title": "Growing Pains", "room": MR1,
     "who": "Richard Neal, Frank Bell and Mark Pover",
     "about": "Get ready for the growth pressures that come with Thriving Community Clubs, with real examples. Leave knowing the pressures clubs face when they grow quickly, how to spot them on the horizon, and what to have ready.",
     "workbook": 11},
    {"id": "d2-club2", "kind": "session", "club": True, "start": "14:10", "end": "14:30",
     "title": "Club story: Knowle FC", "room": MR1,
     "who": "In conversation with Charlotte Richardson"},
    {"id": "d2-impact", "kind": "session", "start": "14:30", "end": "15:00", "end_clubs": "14:40",
     "title": "Demonstrating Impact", "room": MR1,
     "who": "Sarah Cummings and Luke Bailey",
     "about": "How we demonstrate real impact through Club Development Reviews, what those reviews look like, and what to expect for your clubs and your county.",
     "workbook": 12,
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
     "workbook": 13,
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
