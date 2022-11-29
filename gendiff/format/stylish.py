from gendiff.format.get_str import get_str_from_value


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

    def get_branch_str(value, depth):
        return stringify(get_str_from_value(value), ' ', depth + INDENT)

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
                    f"{get_branch_str(value['val'], depth)}"
                )
            elif value["action"] == "unchanged":
                result.append(
                    f"{depth * ' '}    {value['key']}: "
                    f"{get_branch_str(value['val'], depth)}"
                )
            elif value["action"] == "deleted":
                result.append(
                    f"{depth * ' '}  - {value['key']}: "
                    f"{get_branch_str(value['val'], depth)}"
                )
            elif value["action"] == "changed":
                result.append(
                    f"{depth * ' '}  - {value['key']}: "
                    f"{get_branch_str(value['old'], depth)}"
                )
                result.append(
                    f"{depth * ' '}  + {value['key']}: "
                    f"{get_branch_str(value['new'], depth)}"
                )
        return "\n".join(result)

    return "{\n" + walk(data) + "\n}"
