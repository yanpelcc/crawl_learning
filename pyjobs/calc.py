import json
from collections import Counter

with open('pyjobs.json', 'r') as f:
    data = json.load(f)

l_area = []
for job in data:
    area = job['area']
    if len(area) > 4:
        new_area = ''
        for i in range(2):
            new_area += area[i]
        job['area'] = new_area

    l_area.append(job['area'])

print(Counter(l_area).most_common(5))
