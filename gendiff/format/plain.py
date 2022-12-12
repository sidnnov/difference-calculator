from gendiff.format.get_str import get_str_from_value


def convert(value):
    if isinstance(value, str):
        value = f"'{value}'"
    elif isinstance(value, dict):
        value = '[complex value]'
    else:
        value = get_str_from_value(value)
    return value


def build_plain(data, key=''):
    result = []

    for value in data:
        path = f"{key}{value.get('key')}"
        if value['action'] == 'nested':
            result.append(build_plain(value['children'], path + '.'))
        elif value['action'] == 'added':
            result.append(
                f"Property '{path}' was added with value: "
                f"{convert(value['val'])}"
            )
        elif value['action'] == 'deleted':
            result.append(f"Property '{path}' was removed")
        elif value['action'] == 'changed':
            result.append(
                f"Property '{path}' was updated. "
                f"From {convert(value['old'])} "
                f"to {convert(value['new'])}"
            )
    return '\n'.join(result)


def plain(data):
    return build_plain(data, key='')
