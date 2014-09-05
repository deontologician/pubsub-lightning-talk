import random
import re

import blessings

t = blessings.Terminal()

def random_topic_key():
    '''Returns a random topic key with a corresponding payload'''
    topics = random_topic()
    payload = random_payload(topics[0])
    topic_key = '.'.join(topics)
    return topic_key, payload

def random_tags():
    '''Returns random topic tags with corresponding payload'''
    topic_tags = set(random_topic() + random_topic())
    payload = random_payload(*tuple({'teamups', 'fights', 'events'} & topic_tags))
    return ['#' + tag for tag in sorted(topic_tags)], payload

def random_topic():
    '''Returns the pieces of a random topic'''
    category = random.choice(CATEGORIES.keys())    
    chartype = random.choice(CHARACTERS.keys())
    character = random.choice(CHARACTERS[chartype])
    return category, chartype, character


def random_payload(*categories):
    '''Selects a random payload from among the categories passed in'''
    payloads = [payload for cat in categories for payload in CATEGORIES[cat]]
    return random.choice(payloads)

def highlight_matching_tags(tags, results):
    '''Highlights in red matching tags'''
    colors = [196, 
    chunks = []
    for i, result in enumerate(results):
        if result in tags:
            chunks.append(t.color(colors[hash(result) % len(colors)])(result))
        else:
            chunks.append(result)
    return ' '.join(chunks)


def point_in_region(point, region):
    return region[0] <= point < region[1]

def skip_out(region):
    return region[1]

def skip_before(region):
    return region[0]

def regex_colorize(string, regex):
    '''Colorize a string based on which groups in a regex match it'''
    chunks = []
    index = 0
    colors = (t.color(x) for x in [160, 166, 172, 178, 184])
    for color, region in zip(colors, re.match(regex, string).regs[1:]):
        if not point_in_region(index, region):
            chunks.append(string[index:skip_before(region)])
        index = skip_out(region)
        chunks.append(color(string[slice(*region)]))
    if index != len(string) - 1:
        chunks.append(string[index:len(string)])
    return ''.join(chunks)

green = t.green

def get_speed(argv):
    '''Returns the speed in seconds for sleeping'''
    if len(argv) == 1:
        return 0.1
    elif argv[1] == 'fast':
        return 0
    else:
        return 0.5 


# These are used in the demos
CHARACTERS = {
    'superheroes': [
        'Batman',
        'Superman',
        'CaptainAmerica',
        'Thor',
        'Hulk',
        'Spiderman',
        'Deadpool',
        'Wolverine',
    ],
    'supervillains': [
        'Joker',
        'Lex Luthor',
        'RedSkull',
        'Loki',
        'Apocalypse',
        'GreenGoblin',
        'DrDoom',
        'Magneto',
    ],
    'sidekicks': [
        'Robin',
        'JimmyOlsen',
        'BuckyBarnes',
        'BatGirl',
        'Aqualad',
        'Jubilee',
        'Speedy',
        'WoozyWinks',
    ],
}

TEAMUPS = [
    "You'll never guess who's teaming up",
    'A completely one-sided fight between superheroes',
    'Sidekick goes on rampage. Hundreds given parking tickets',
    'Local politician warns of pairing between villains',
    'Unexpected coalition teams up to take on opponents',
    'Seemingly random heroes band together for the first time',
    'Unfortunately for everybody, a partnership is formed',
    'At long last, the old team is back together fighting crime',
]

FIGHTS = [
    'A fight rages between combatants',
    'Tussle between mighty foes continues',
    'All out war in the streets between battling heroes',
    "City's greatest hero defeated!",
    "Villain locked in minimum security prison after defeat",
    "Most of downtown destroyed in battle between mortal foes",
    "Car alarms going off in the night. Who's fighting now?",
    "Stock exchange remains closed after battle royale demolishes it",
]

EVENTS = [
    "Scientists accidentally thaw a T-Rex and release it",
    "Time vortex opens over downtown.",
    "EMP turns out the lights. You'll never guess who turned them back on",
    "Inter-dimensional sludge released. Who can contain it?",
    "Super computer-virus disables all police cars. City helpless.",
    "Mechanical spiders invade! Cancel your weekend plans.",
    "Ancient evil crawling around in the sewers. Why that's bad at 11",
    "Fractions of cents hoarded by eccentric hacker!",
]

CATEGORIES = {
    'teamups': TEAMUPS,
    'fights': FIGHTS,
    'events': EVENTS,
}
