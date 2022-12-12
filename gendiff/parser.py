import os
import json
import yaml


def get_file_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format


def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content


def parse(content, file_format):
    if file_format == '.json':
        dictionary = json.loads(content)
    if file_format in ('.yaml', '.yml'):
        dictionary = yaml.load(content, Loader=yaml.Loader)
    return dictionary
