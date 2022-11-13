import argparse
<<<<<<< HEAD


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
    )

parser.add_argument('first_file')
parser.add_argument('second_file')

parser.add_argument('-f', '--format', help='set format of output')
agrs = parser.parse_args()

print(agrs)
=======
from gendiff.generate import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help='set format of output')
    agrs = parser.parse_args()

    # print(agrs)

    print(generate_diff(agrs.first_file, agrs.second_file))


if __name__ == "__main__":
    main()

# puth_file1 = 'path_files/file1.json'
# puth_file2 = 'path_files/file2.json'
# print(gen.generate_diff(puth_file1, puth_file2))
>>>>>>> 0285f83 (Add new project 'gendiff')
