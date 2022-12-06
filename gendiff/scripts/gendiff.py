#!/usr/bin/env python3
import argparse
from gendiff.generate import generate_diff


def main():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] [format] <filepath1> <filepath2>',
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f",
        "--format",
        choices=['stylish', 'plain', 'json'],
        help="set format of output",
        default='stylish',
    )
    agrs = parser.parse_args()
    print(generate_diff(agrs.first_file, agrs.second_file, agrs.format))


if __name__ == "__main__":
    main()
