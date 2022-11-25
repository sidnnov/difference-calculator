from gendiff.parser import parser


INDENT = 4


def stringify(data, replacer=" ", spases_count=1):
    depth = spases_count

    def walk(data, replacer, spases_count):
        result = ""
        if not isinstance(data, dict):
            return str(data)
        for key, val in data.items():
            if isinstance(val, dict):
                val = walk(val, replacer, spases_count + depth)
            result += f"    {replacer * spases_count}{key}: {val}\n"
        result = "{\n" + result + replacer * spases_count + "}"
        return result

    return walk(data, replacer, spases_count)


def stylish(data):
    def walk(data, depth=0):
        result = []
        for value in data:
            if value["action"] == "nested":
                result.append(
                    f"{depth * ' '}    {value['key']}: {'{'}\n"
                    f"{walk(value['children'], depth + INDENT)}\n"
                    f"{(depth + INDENT) * ' ' + '}'}"
                )
            elif value["action"] == "added":
                result.append(
                    f"{depth * ' '}  + {value['key']}: "
                    f"{stringify(value['val'], ' ', depth + INDENT)}"
                )
            elif value["action"] == "unchanged":
                result.append(
                    f"{depth * ' '}    {value['key']}: "
                    f"{stringify(value['val'], ' ', depth + INDENT)}"
                )
            elif value["action"] == "deleted":
                result.append(
                    f"{depth * ' '}  - {value['key']}: "
                    f"{stringify(value['val'], ' ', depth + INDENT)}"
                )
            elif value["action"] == "changed":
                result.append(
                    f"{depth * ' '}  - {value['key']}: "
                    f"{stringify(value['old'], ' ', depth + INDENT)}"
                )
                result.append(
                    f"{depth * ' '}  + {value['key']}: "
                    f"{stringify(value['new'], ' ', depth + INDENT)}"
                )
        return "\n".join(result)

    return "{\n" + walk(data) + "\n}"


def get_str_from_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    if value is None:
        value = "null"
    return value


def constructing_diff(dict_1, dict_2):
    keys = dict_1.keys() | dict_2.keys()
    result = []
    for key in sorted(keys):
        if key not in dict_2:
            result.append(
                {
                    "key": key,
                    "action": "deleted",
                    "val": get_str_from_value(dict_1[key]),
                }
            )
        elif key not in dict_1:
            result.append(
                {
                    "key": key,
                    "action": "added",
                    "val": get_str_from_value(dict_2[key])
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
                    "val": get_str_from_value(dict_1[key]),
                }
            )
        else:
            result.append(
                {
                    "key": key,
                    "action": "changed",
                    "old": get_str_from_value(dict_1[key]),
                    "new": get_str_from_value(dict_2[key]),
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
