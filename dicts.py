from pprint import pprint
from copy import deepcopy
from collections import defaultdict

d = {
    'a': 23,
    'b': 52,
    'c': 12
}

pprint(d)
pprint(d.keys())
pprint(d.values())
d.update({'d': 345})
pprint(d)
pprint(d['a'])
pprint(d.get('f', 'DOES NOT EXIST'))

e = {
    'foo': 'bar',
    **d,
    'another': 'entry'
}
pprint(e)

# iterate over the keys by default
for elem in d:
    print(f'{type(elem)}: {elem}')

# .items() returns key/value tuples
for elem in d.items():
    print(f'{type(elem)}: {elem}')

# you can implicitly break them up into locally scoped variables
for k, v in d.items():
    print(f'{type(k)},{k}: {type(v)},{v}')

list_map = {
    'one': [],
    'two': [1, 2, 3],
    'three': [10, 20, 30]
}

# Shallow copy of
copy_of_list_map = list_map.copy()
deepcopy_of_list_map = deepcopy(list_map)

copy_of_list_map['four'] = [100, 200, 300]

pprint(list_map)
pprint(copy_of_list_map)
pprint(deepcopy_of_list_map)

copy_of_list_map['one'].append(0)

pprint(list_map)
pprint(copy_of_list_map)
pprint(deepcopy_of_list_map)

listdict = defaultdict(list)
print(listdict['something'])
listdict['else'].append(10)
pprint(listdict)


def nesteddict():
    """A recursive defaultdict """
    return defaultdict(nesteddict)


recursive_dict = nesteddict()
recursive_dict['a']['b']['c'] = 100
pprint(recursive_dict)
