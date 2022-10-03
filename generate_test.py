'''
    Python String Exercise - Test Case Generator
    Copyright (C) 2022 Alexis Maya-Isabelle Shuping

    This program is free software: you can redistribute it and/or modify it
    under the terms of the GNU Lesser General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
    for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import json
import random
import sys

NUM_INPUTS = 16
OUT_FILE_NAME = 'inputs.json'

DIRTY_SPACE_PROBABILITY = 0.4
DIRTY_CAPS_PROBABILITY = 0.4

def dirtify(s:str) -> str:
    space_chars     = [' ', '\t', '\n', '\r']
    space_c_weights = [ 0.9, 0.04, 0.04,  0.02 ]
    if random.random() < DIRTY_SPACE_PROBABILITY:
        chars_before = random.randint(0, 2)
        chars_after = random.randint(0, 2)
        s = ''.join(random.choices(space_chars, weights=space_c_weights, k=chars_before)) + s + ''.join(random.choices(space_chars, weights=space_c_weights, k=chars_after))
    
    if random.random() < DIRTY_CAPS_PROBABILITY:
        x:str = ''
        for c in s:
            x += (c.lower() if random.random() < 0.5 else c.upper())
        s = x
    
    return s

def main():
    names = []
    flavors = []
    toppings = []

    with open('names.json') as name_file:
        names = json.load(name_file)

    if len(names) < NUM_INPUTS:
        print(f'ERROR: requested {NUM_INPUTS} input lines, but only {len(names)} names were read from the name-file. Add more names or decrease NUM_INPUTS.', file=sys.stderr)
        sys.exit(1)

    with open('flavors.json') as flavors_file:
        flavors = json.load(flavors_file)

    with open('toppings.json') as toppings_file:
        toppings = json.load(toppings_file)

    inputs = []
    random.shuffle(names)
    for i in range(NUM_INPUTS):
        inputs.append((dirtify(names[i]), dirtify(random.choice(flavors)), dirtify(random.choice(toppings))))

    with open(OUT_FILE_NAME, 'w') as out_file:
        json.dump(inputs, out_file, indent=4)

if __name__ == '__main__':
    main()