from gendiff.format.get_str import get_str_from_value


def check_composite(value):
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
        puth = f"{key}{value.get('key')}"
        if value["action"] == "nested":
            result.append(plain(value["children"], puth + "."))
        elif value["action"] == "added":
            result.append(
                f"Property '{puth}' was added with value: "
                f"{check_composite(value['val'])}"
            )
        elif value["action"] == "deleted":
            result.append(f"Property '{puth}' was removed")
        elif value["action"] == "changed":
            result.append(
                f"Property '{puth}' was updated. "
                f"From {check_composite(value['old'])} "
                f"to {check_composite(value['new'])}"
            )
    return "\n".join(result)
