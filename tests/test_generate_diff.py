import pytest
from gendiff import generate_diff
from gendiff.parser import read_file, parse


FILE_JSON_PATH1 = 'tests/fixtures/file1.json'
FILE_JSON_PATH2 = 'tests/fixtures/file2.json'
FILE_YAML_PATH1 = 'tests/fixtures/file1.yaml'
FILE_YAML_PATH2 = 'tests/fixtures/file2.yml'
FILE_NESTED_YAML_PATH1 = 'tests/fixtures/hard_file1.yml'
FILE_NESTED_YAML_PATH2 = 'tests/fixtures/hard_file2.yml'
FILE_NESTED_JSON_PATH1 = 'tests/fixtures/hard_file1.json'
FILE_NESTED_JSON_PATH2 = 'tests/fixtures/hard_file2.json'
CORRECT_JSON_PATH = 'tests/fixtures/correct_json.txt'
CORRECT_NESTED_PATH = 'tests/fixtures/correct_nested.txt'
CORRECT_PLAIN_PATH = 'tests/fixtures/correct_plain.txt'
CORRECT_SIMPLE_PATH = 'tests/fixtures/correct_simple.txt'
SIMPLE_CORRECT_DICT = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}
NESTED_CORRECT_DICT = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}


testdata = {
    'parse': [
        (FILE_JSON_PATH1, SIMPLE_CORRECT_DICT),
        (FILE_YAML_PATH1, SIMPLE_CORRECT_DICT),
        (FILE_NESTED_YAML_PATH1, NESTED_CORRECT_DICT),
        (FILE_NESTED_JSON_PATH1, NESTED_CORRECT_DICT),
    ],
    'generate_diff': [
        (FILE_JSON_PATH1, FILE_JSON_PATH2,
            'stylish', CORRECT_SIMPLE_PATH),
        (FILE_YAML_PATH1, FILE_YAML_PATH2,
            'stylish', CORRECT_SIMPLE_PATH),
        (FILE_NESTED_YAML_PATH1, FILE_NESTED_YAML_PATH2,
            'stylish', CORRECT_NESTED_PATH),
        (FILE_NESTED_JSON_PATH1, FILE_NESTED_JSON_PATH2,
            'stylish', CORRECT_NESTED_PATH),
        (FILE_NESTED_JSON_PATH1, FILE_NESTED_JSON_PATH2,
            'plain', CORRECT_PLAIN_PATH),
        (FILE_NESTED_YAML_PATH1, FILE_NESTED_YAML_PATH2,
            'plain', CORRECT_PLAIN_PATH),
        (FILE_NESTED_JSON_PATH1, FILE_NESTED_JSON_PATH2,
            'json', CORRECT_JSON_PATH),
        (FILE_NESTED_YAML_PATH1, FILE_NESTED_YAML_PATH2,
            'json', CORRECT_JSON_PATH),
    ],
}


@pytest.mark.parametrize('file_path,expected', testdata['parse'])
def test_parser(file_path, expected):
    content, file_format = read_file(file_path)
    with open(file_path) as file:
        content = file.read()
    assert parse(content, file_format) == expected


@pytest.mark.parametrize(
    'file_path1,file_path2,format,expected', testdata['generate_diff']
)
def test_generate_diff(file_path1, file_path2, format, expected):
    with open(expected) as file:
        correct_date = file.read()
    assert generate_diff(file_path1, file_path2, format) == correct_date
