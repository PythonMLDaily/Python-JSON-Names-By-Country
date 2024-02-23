import json
import random
from names_dataset import NameDataset
from langcodes import *

names = NameDataset()

voices = json.load(open('all-tts-voices.json'))
print(f'Total voices: {len(voices)}')

found = 0
for i, item in enumerate(voices):
    print(f'Processing voice no.{i+1}')
    try:
        gender = item['gender'].split('-')[0].title()
        item['name'] = ''

        language = Language.get(item['languageCode'])
        country = language.territory

        if country:
            random_names = names.get_top_names(n=5,
                                               gender=gender,
                                               country_alpha2=country)

            if len(random_names) > 0:
                item['name'] = random.choice(random_names[country][gender[0]])
                found += 1
        else:
            print('=' * 50)
            print('[EXCEPTION] Country not found by languageCode: ' + item['languageCode'])
            print(item)
            print('=' * 50)
    except BaseException as e:
        print('=' * 50)
        print('[EXCEPTION] Unplanned error: ' + str(e))
        print(item)
        print('=' * 50)

with open('result.json', 'w') as f:
    json.dump(voices, f, indent=4)

print(found)