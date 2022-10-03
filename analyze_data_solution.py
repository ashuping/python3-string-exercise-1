'''
    Python String Exercise - Example Solution
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



def cleanup_responses(data):
    clean_data = []    

    '''
        Write code here to clean up the input data, removing excess whitespace
        and changing all letters to lowercase. The cleaned-up data should go
        in the variable `clean_data`
    '''
    clean = lambda x: x.lower().strip()
    for entry in data:
        clean_data.append((clean(entry[0]), clean(entry[1]), clean(entry[2])))

    return clean_data



def get_insights(data):
    vanilla_fans, mint_choco_fans, strawberry_fans, meat_fans = 0, 0, 0, 0

    '''
        Go through the input data and count up how many dragons liked each
        flavor of ice cream. Save the results in the variables defined above.
    '''
    for result in data:
        if result[1] == 'vanilla':
            vanilla_fans += 1
        elif result[1] == 'mint choco':
            mint_choco_fans += 1
        elif result[1] == 'strawberry':
            strawberry_fans += 1
        elif result[1] == 'meat':
            meat_fans += 1

    return {'vanilla':vanilla_fans,'mint_choco':mint_choco_fans,"strawberry":strawberry_fans,'meat':meat_fans}



def get_advanced_insights(data):
    vanilla_fan_list, mint_choco_fan_list, strawberry_fan_list, meat_fan_list = [], [], [], []

    '''
        This time, instead of just counting up the number of fans for each type,
        you will make a list of human-readable strings that give information on
        each fan. For example, instead of ending up with

        strawberry_fans = 2

        You would end up with

        strawberry_fan_list = ['lannirth, champion of the green likes strawberry ice cream with gummy dragons on top.', 'lamme, lady of the white likes strawberry ice cream with chocolate chips on top']

        The exact format for each string should be:

        "DRAGON_NAME_HERE likes FLAVOR_HERE ice cream with TOPPING_HERE on top."
    '''
    for result in data:
        if result[1] == 'vanilla':
            vanilla_fan_list.append(f'{result[0]} likes {result[1]} ice cream with {result[2]} on top.')
        elif result[1] == 'mint choco':
            mint_choco_fan_list.append(f'{result[0]} likes {result[1]} ice cream with {result[2]} on top.')
        elif result[1] == 'strawberry':
            strawberry_fan_list.append(f'{result[0]} likes {result[1]} ice cream with {result[2]} on top.')
        elif result[1] == 'meat':
            meat_fan_list.append(f'{result[0]} likes {result[1]} ice cream with {result[2]} on top.')

    return {'vanilla':vanilla_fan_list,'mint_choco':mint_choco_fan_list,"strawberry":strawberry_fan_list,'meat':meat_fan_list}




'''
    ===========================================================================
    ================= Don't change anything below this line ===================
    ===========================================================================
'''

def print_insights(insights, adv_insights):
    for key, val in adv_insights.items():
        print(f'\n===== {key} =====')
        for dragon in val:
            print(f'  {dragon}')

    print('\n\n======== OVERVIEW ========')
    for dex, x in enumerate(sorted(insights.items(), key=lambda x:x[1], reverse=True)):
        if dex == 0:
            print(f'The most popular flavor was {x[0]}, with {x[1]} responses.')
        else:
            print(f'Rank {dex+1}: {x[0]} with {x[1]} responses')

def main():
    print(f'Reading survey responses from inputs.json...')

    data = []
    with open('inputs.json') as input_file:
        data = json.load(input_file)

    print(f'Read {len(data)} survey responses.')

    print('Processing...')
    data = cleanup_responses(data)

    print_insights(get_insights(data), get_advanced_insights(data))


if __name__ == '__main__':
    main()
