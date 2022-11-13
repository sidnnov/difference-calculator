from gendiff import generate_diff

PUTH_FILE1 = 'tests/fixtures/file1.json'
PUTH_FILE2 = 'tests/fixtures/file2.json'


with open('tests/fixtures/expected.txt') as file:
    expected = file.read()


def test_generate_diff():
    assert generate_diff(PUTH_FILE1, PUTH_FILE2) == expected
