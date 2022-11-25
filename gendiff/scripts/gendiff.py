#!/usr/bin/env python3
import argparse
from gendiff.generate import generate_diff, stylish


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        default=stylish
    )
    agrs = parser.parse_args()
    if agrs.format == 'something':
        agrs.format = 'something'
    print(generate_diff(agrs.first_file, agrs.second_file, agrs.format))


if __name__ == "__main__":
    main()
