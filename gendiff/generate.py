import json


# def generate_diff(puth_file1, puth_file2):
#     dict_1 = make_sorted_dict_from_file(puth_file1)
#     dict_2 = make_sorted_dict_from_file(puth_file2)
#     result = ''

#     for key, val in dict_1.items():
#         if key in dict_2:
#             if val == dict_2[key]:
#                 result += f'    {key}: {val}\n'
#             else:
#                 result += f'  - {key}: {val}\n'
#                 result += f'  + {key}: {dict_2[key]}\n'
#         if key not in dict_2:
#             result += f'  - {key}: {val}\n'

#     for key, val in dict_2.items():
#         if key not in dict_1:
#             result += f'  + {key}: {val}\n'
#     result = '{\n' + result + '}'

def generate_diff(puth_file1, puth_file2):
    dict_1 = make_sorted_dict_from_file(puth_file1)
    dict_2 = make_sorted_dict_from_file(puth_file2)
    keys = dict_1.keys() | dict_2.keys()
    result = ''

    for key in sorted(keys):
        if key not in dict_2:
            result += f'  - {key}: {dict_1[key]}\n'
        elif key not in dict_1:
            result += f'  + {key}: {dict_2[key]}\n'
        elif dict_1[key] == dict_2[key]:
            result += f'    {key}: {dict_1[key]}\n'
        else:
            result += f'  - {key}: {dict_1[key]}\n'
            result += f'  + {key}: {dict_2[key]}\n'
    result = '{\n' + result + '}'

    return result

    # list1 = []
    # with open(puth_file1) as file1:
    #     dict_1 = json.loads(file1.read())
    # # print(dict(sorted(dict_1.items())))
    #
    # for key, val in dict_1.items():
    #     if type(val) == bool:
    #         dict_1[key] = str(val).lower()
    #
    # list1 = [': '.join([str(key), str(val)]) for key, val in dict_1.items()]
    #
    # with open(puth_file2) as file2:
    #     dict_2 = json.loads(file2.read())
    # for key, val in dict_2.items():
    #     if type(val) == bool:
    #         dict_2[key] = str(val).lower()
    # return sorted(list1), dict_2


def make_sorted_dict_from_file(puth_file):
    with open(puth_file) as file:
        dictionary = json.loads(file.read())
    sorted_dict = dict(sorted(dictionary.items()))

    for key, val in sorted_dict.items():
        if type(val) == bool:
            sorted_dict[key] = str(val).lower()

    # for key, val in dict.items():
    #     if type(val) == bool:
    #         dict[key] = str(val).lower()
    # list_values = [
    #     ': '.join([str(key), str(val)]) for key, val in dict.items()
    #     ]

    return sorted_dict


# puth_file1 = 'path_files/file1.json'
# puth_file2 = 'path_files/file2.json'
# print(generate_diff(puth_file1, puth_file2))
