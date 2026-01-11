import random as rn

COUNTRY_GROUPS = {
    "north_america": [
        "United States",
        "Canada",
        "Mexico"
    ],

    "europe_west": [
        "United Kingdom",
        "Germany",
        "France",
        "Netherlands",
        "Belgium",
        "Switzerland",
        "Austria",
        "Ireland"
    ],

    "europe_east": [
        "Poland",
        "Czech Republic",
        "Slovakia",
        "Hungary",
        "Romania",
        "Ukraine",
        "Russia"
    ],

    "nordic": [
        "Sweden",
        "Norway",
        "Finland",
        "Denmark"
    ],

    "caucasus": [
        "Azerbaijan",
        "Georgia",
        "Armenia"
    ],

    "middle_east": [
        "Turkey",
        "Israel",
        "United Arab Emirates",
        "Saudi Arabia"
    ],

    "asia": [
        "China",
        "India",
        "Japan",
        "South Korea",
        "Indonesia",
        "Vietnam"
    ],

    "oceania": [
        "Australia",
        "New Zealand"
    ],

    "south_america": [
        "Brazil",
        "Argentina",
        "Chile",
        "Colombia"
    ]
}

def generate_country() -> str:
    group = rn.choice(list(COUNTRY_GROUPS.values()))
    return rn.choice(group)
