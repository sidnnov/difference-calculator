import json
import yaml


def parser(puth_file):
    with open(puth_file) as file:
        if puth_file.endswith('.json'):
            dictionary = json.loads(file.read())
        if puth_file.endswith('.yaml') or puth_file.endswith('.yml'):
            dictionary = yaml.load(file, Loader=yaml.Loader)
    sorted_dict = dict(sorted(dictionary.items()))
    for key, val in sorted_dict.items():
        if type(val) == bool:
            sorted_dict[key] = str(val).lower()
    return sorted_dict
