from gendiff.parser import parser


def generate_diff(puth_file1, puth_file2):
    dict_1 = parser(puth_file1)
    dict_2 = parser(puth_file2)
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
