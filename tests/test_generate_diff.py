from gendiff import generate_diff
from gendiff.parser import parser
from gendiff.format.plain import plain
from gendiff.format.json_form import json

PUTH_JSON_FILE1 = "tests/fixtures/file1.json"
PUTH_JSON_FILE2 = "tests/fixtures/file2.json"
PUTH_YAML_FILE1 = "tests/fixtures/file1.yaml"
PUTH_YAML_FILE2 = "tests/fixtures/file2.yml"
PUTH_HARD_YAML_FILE1 = "tests/fixtures/hard_file1.yml"
PUTH_HARD_YAML_FILE2 = "tests/fixtures/hard_file2.yml"
PUTH_HARD_JSON_FILE1 = "tests/fixtures/hard_file1.json"
PUTH_HARD_JSON_FILE2 = "tests/fixtures/hard_file2.json"
CORRECT_DICT = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}
HARD_CORRECT_DICT = {
    "common": {
        "setting1": "Value 1",
        "setting2": 200,
        "setting3": True,
        "setting6": {"key": "value", "doge": {"wow": ""}},
    },
    "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
    "group2": {"abc": 12345, "deep": {"id": 45}},
}


with open("tests/fixtures/examples.txt") as file:
    examples = file.read()


expected = examples.split("\n\n\n")


def test_parser():
    assert parser(PUTH_JSON_FILE1) == CORRECT_DICT
    assert parser(PUTH_YAML_FILE1) == CORRECT_DICT
    assert parser(PUTH_HARD_YAML_FILE1) == HARD_CORRECT_DICT
    assert parser(PUTH_HARD_JSON_FILE1) == HARD_CORRECT_DICT


def test_generate_diff():
    assert generate_diff(PUTH_JSON_FILE1, PUTH_JSON_FILE2) == expected[0]
    assert generate_diff(PUTH_YAML_FILE1, PUTH_YAML_FILE2) == expected[0]
    assert generate_diff(
        PUTH_HARD_YAML_FILE1, PUTH_HARD_YAML_FILE2) == expected[1]
    assert generate_diff(
        PUTH_HARD_JSON_FILE1, PUTH_HARD_JSON_FILE2) == expected[1]
    assert generate_diff(
        PUTH_HARD_JSON_FILE1, PUTH_HARD_JSON_FILE2, plain) == expected[2]
    assert generate_diff(
        PUTH_HARD_YAML_FILE1, PUTH_HARD_YAML_FILE2, plain) == expected[2]
    assert generate_diff(
        PUTH_HARD_YAML_FILE1, PUTH_HARD_YAML_FILE2, json) == expected[3]
