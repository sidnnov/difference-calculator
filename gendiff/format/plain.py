from gendiff.format.get_str import get_str_from_value


def conversion(value):
    if isinstance(value, str):
        value = f"'{value}'"
    elif isinstance(value, dict):
        value = "[complex value]"
    else:
        value = get_str_from_value(value)
    return value


def plain(data, key=""):
    result = []

    for value in data:
        path = f"{key}{value.get('key')}"
        if value["action"] == "nested":
            result.append(plain(value["children"], path + "."))
        elif value["action"] == "added":
            result.append(
                f"Property '{path}' was added with value: "
                f"{conversion(value['val'])}"
            )
        elif value["action"] == "deleted":
            result.append(f"Property '{path}' was removed")
        elif value["action"] == "changed":
            result.append(
                f"Property '{path}' was updated. "
                f"From {conversion(value['old'])} "
                f"to {conversion(value['new'])}"
            )
    return "\n".join(result)
