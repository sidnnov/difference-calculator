from gendiff.parser import parse, read_file
from gendiff.format.stylish import stylish
from gendiff.format.plain import plain
from gendiff.format.json import json


FORMAT = {'stylish': stylish, 'plain': plain, 'json': json}


def build_diff(dict_1, dict_2):
    keys = dict_1.keys() | dict_2.keys()
    result = []
    for key in sorted(keys):
        if key not in dict_2:
            result.append(
                {
                    'key': key,
                    'action': 'deleted',
                    'val': dict_1[key],
                }
            )
        elif key not in dict_1:
            result.append(
                {
                    'key': key,
                    'action': 'added',
                    'val': dict_2[key],
                }
            )
        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            result.append(
                {
                    'key': key,
                    'action': 'nested',
                    'children': build_diff(dict_1[key], dict_2[key]),
                }
            )
        elif dict_1[key] == dict_2[key]:
            result.append(
                {
                    'key': key,
                    'action': 'unchanged',
                    'val': dict_1[key],
                }
            )
        else:
            result.append(
                {
                    'key': key,
                    'action': 'changed',
                    'old': dict_1[key],
                    'new': dict_2[key],
                }
            )
    return result


def generate_diff(file_path1, file_path2, format='stylish'):
    file_content1, file_format1 = read_file(file_path1)
    file_content2, file_format2 = read_file(file_path2)
    dict_1 = parse(file_content1, file_format1)
    dict_2 = parse(file_content2, file_format2)
    return FORMAT[format](build_diff(dict_1, dict_2))
