#!python

import os
import argparse


def create(day: int):
    def create_file(file):
        if not os.path.exists(file):
            open(file, "w", encoding="utf-8").close()

    # Python file
    create_file(f"day{day}.py")
    create_file(f"inputs/day{day}.txt")
    create_file(f"inputs/day{day}ex.txt")


def create_folders():
    if not os.path.exists("inputs/"):
        os.mkdir("inputs/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", nargs="+", type=int, help="The days to create.")

    args = parser.parse_args()

    create_folders()
    for day in args.day:
        create(day)
