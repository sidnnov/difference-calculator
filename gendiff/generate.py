from gendiff.parser import parser
from gendiff.format.stylish import stylish


def constructing_diff(dict_1, dict_2):
    keys = dict_1.keys() | dict_2.keys()
    result = []
    for key in sorted(keys):
        if key not in dict_2:
            result.append(
                {
                    "key": key,
                    "action": "deleted",
                    "val": dict_1[key],
                }
            )
        elif key not in dict_1:
            result.append(
                {
                    "key": key,
                    "action": "added",
                    "val": dict_2[key],
                }
            )
        elif isinstance(dict_1[key], dict) and isinstance(dict_2[key], dict):
            result.append(
                {
                    "key": key,
                    "action": "nested",
                    "children": constructing_diff(dict_1[key], dict_2[key]),
                }
            )
        elif dict_1[key] == dict_2[key]:
            result.append(
                {
                    "key": key,
                    "action": "unchanged",
                    "val": dict_1[key],
                }
            )
        else:
            result.append(
                {
                    "key": key,
                    "action": "changed",
                    "old": dict_1[key],
                    "new": dict_2[key],
                }
            )
    return result


def generate_diff(puth_file1, puth_file2, format=stylish):
    dict_1 = parser(puth_file1)
    dict_2 = parser(puth_file2)
    return format(constructing_diff(dict_1, dict_2))


# puth_file1 = "tests/fixtures/hard_file1.json"
# puth_file2 = "tests/fixtures/hard_file2.json"
# print(stylish(generate_diff(puth_file1, puth_file2)))
# # print(generate_diff(puth_file1, puth_file2))
