import json
import yaml


def read_file(file_path):
    with open(file_path) as file:
        line = file.read()
    if file_path.endswith('.json'):
        format = 'json'
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        format = 'yaml'
    return format, line


def parser(file_path):
    format, line = read_file(file_path)
    if format == 'json':
        dictionary = json.loads(line)
    if format == 'yaml':
        dictionary = yaml.load(line, Loader=yaml.Loader)
    return dictionary
