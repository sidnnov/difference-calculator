import json as origin_json


INDENT = 2


def json(data):
    return origin_json.dumps(data, indent=INDENT)
