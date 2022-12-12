def get_str_from_value(value):
    if isinstance(value, bool):
        value = str(value).lower()
    if value is None:
        value = 'null'
    return value
