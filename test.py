from collections import MutableMapping

dict = {'John': '21', 'Tim': '19', 'Pets': {'Chewy': 'dead', 'doggo': 'coming soon'}}
 
# code to convert ini_dict to flattened dictionary
# default separator '_'
def convert_flatten(d, parent_key ='', sep ='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
 
        if isinstance(v, MutableMapping):
            items.extend(convert_flatten(v, new_key, sep = sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

print(str(convert_flatten(dict)))