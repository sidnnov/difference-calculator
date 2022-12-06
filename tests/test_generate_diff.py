import pytest
from gendiff import generate_diff
from gendiff.parser import parser


FILE_JSON_PATH1 = "tests/fixtures/file1.json"
FILE_JSON_PATH2 = "tests/fixtures/file2.json"
FILE_YAML_PATH1 = "tests/fixtures/file1.yaml"
FILE_YAML_PATH2 = "tests/fixtures/file2.yml"
FILE_HARD_YAML_PATH1 = "tests/fixtures/hard_file1.yml"
FILE_HARD_YAML_PATH2 = "tests/fixtures/hard_file2.yml"
FILE_HARD_JSON_PATH1 = "tests/fixtures/hard_file1.json"
FILE_HARD_JSON_PATH2 = "tests/fixtures/hard_file2.json"
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

testdata = {
    "parser": [
        (FILE_JSON_PATH1, CORRECT_DICT),
        (FILE_YAML_PATH1, CORRECT_DICT),
        (FILE_HARD_YAML_PATH1, HARD_CORRECT_DICT),
        (FILE_HARD_JSON_PATH1, HARD_CORRECT_DICT),
    ],
    "generate_diff": [
        (FILE_JSON_PATH1, FILE_JSON_PATH2, "stylish", expected[0]),
        (FILE_YAML_PATH1, FILE_YAML_PATH2, "stylish", expected[0]),
        (FILE_HARD_YAML_PATH1, FILE_HARD_YAML_PATH2, "stylish", expected[1]),
        (FILE_HARD_JSON_PATH1, FILE_HARD_JSON_PATH2, "stylish", expected[1]),
        (FILE_HARD_JSON_PATH1, FILE_HARD_JSON_PATH2, "plain", expected[2]),
        (FILE_HARD_YAML_PATH1, FILE_HARD_YAML_PATH2, "plain", expected[2]),
        (FILE_HARD_JSON_PATH1, FILE_HARD_JSON_PATH2, "json", expected[3]),
        (FILE_HARD_YAML_PATH1, FILE_HARD_YAML_PATH2, "json", expected[3]),
    ],
}


@pytest.mark.parametrize("file_path,expected", testdata["parser"])
def test_parser(file_path, expected):
    assert parser(file_path) == expected


@pytest.mark.parametrize(
    "file_path1,file_path2,format,expected", testdata["generate_diff"]
)
def test_generate_diff(file_path1, file_path2, format, expected):
    assert generate_diff(file_path1, file_path2, format) == expected
