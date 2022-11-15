from gendiff import generate_diff
from gendiff.parser import parser


PUTH_JSON_FILE1 = 'tests/fixtures/file1.json'
PUTH_JSON_FILE2 = 'tests/fixtures/file2.json'
PUTH_YAML_FILE1 = 'tests/fixtures/file1.yaml'
PUTH_YAML_FILE2 = 'tests/fixtures/file2.yml'
CORRECT_DICT = {
    'follow': 'false',
    'host': 'hexlet.io',
    'proxy': '123.234.53.22',
    'timeout': 50
}


with open('tests/fixtures/expected.txt') as file:
    expected = file.read()


def test_generate_diff():
    assert generate_diff(PUTH_JSON_FILE1, PUTH_JSON_FILE2) == expected
    assert generate_diff(PUTH_YAML_FILE1, PUTH_YAML_FILE2) == expected


def test_parser():
    assert parser(PUTH_JSON_FILE1) == CORRECT_DICT
    assert parser(PUTH_YAML_FILE1) == CORRECT_DICT
