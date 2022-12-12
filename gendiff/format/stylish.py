from gendiff.format.get_str import get_str_from_value


INDENT = 4
ACTION = {'added': ' + ', 'deleted': ' - ', 'unchanged': '   '}


def stringify(data, replacer=' ', spaces_count=1):
    depth = spaces_count

    def walk(data, replacer, spaces_count):
        result = ''
        if not isinstance(data, dict):
            return str(data)
        for key, val in data.items():
            if isinstance(val, dict):
                val = walk(val, replacer, spaces_count + depth)
            result += f"{INDENT * ' '}{replacer * spaces_count}{key}: {val}\n"
        result = '{\n' + result + replacer * spaces_count + '}'
        return result

    return walk(data, replacer, spaces_count)


def get_branch_str(value, depth):
    return stringify(get_str_from_value(value), ' ', (depth + INDENT))


def get_key_str(depth, action, key):
    indent = (depth + INDENT - len(action)) * ' '
    return f"{indent}{action}{key}: "


def build_stylish(data, depth=0):
    result = []
    for value in data:
        if value['action'] == 'nested':
            result.append(
                f"{get_key_str(depth, ACTION['unchanged'], value['key'])}"
                f"{'{'}\n"
                f"{build_stylish(value['children'], (depth + INDENT))}\n"
                f"{((depth + INDENT)) * ' ' + '}'}"
            )
        elif value['action'] == 'added':
            result.append(
                f"{get_key_str(depth, ACTION['added'], value['key'])}"
                f"{get_branch_str(value['val'], depth)}"
            )
        elif value['action'] == 'unchanged':
            result.append(
                f"{get_key_str(depth, ACTION['unchanged'], value['key'])}"
                f"{get_branch_str(value['val'], depth)}"
            )
        elif value['action'] == 'deleted':
            result.append(
                f"{get_key_str(depth, ACTION['deleted'], value['key'])}"
                f"{get_branch_str(value['val'], depth)}"
            )
        elif value['action'] == 'changed':
            result.append(
                f"{get_key_str(depth, ACTION['deleted'], value['key'])}"
                f"{get_branch_str(value['old'], depth)}"
            )
            result.append(
                f"{get_key_str(depth, ACTION['added'], value['key'])}"
                f"{get_branch_str(value['new'], depth)}"
            )
    return '\n'.join(result)


def stylish(data):
    return '{\n' + build_stylish(data) + '\n}'
