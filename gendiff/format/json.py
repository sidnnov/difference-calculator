import json as origin_json


INDENT = 4


def json(data):
    return origin_json.dumps(data, indent=INDENT)
