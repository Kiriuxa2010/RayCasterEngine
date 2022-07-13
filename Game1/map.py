from settings import *

text_map = [
    'WWWWWWWWWWWWWW',
    'W..W...W.....W',
    'W......www...W',
    'W....W..WW...W',
    'W..W....W....W',
    'W..W...W.W...W',
    'W....W.......W',
    'WWWWWWWWWWWWWW',
]

world_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))