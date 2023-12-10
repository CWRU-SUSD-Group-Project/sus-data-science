"""This file creates a sample of each JSON file in the "data" folder."""

import os
import random


def find_json_files(directory) -> list:
    """
    Finds all JSON files in the specified directory.
    """

    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))
    return json_files


def num_lines(file_path) -> int:
    """
    Returns the number of lines in a file.
    """
    with open(file_path, "rb") as f:
        return sum(1 for _ in f) # TODO check on this

def main() -> None:
    """
    This function finds all data files in "data" and creates a sample of each one
    in the "sample" folder.
    """
    data_directory = "data"
    sample_directory = os.path.join(data_directory, "sample")
    json_files = find_json_files(data_directory)

    # Create the "sample" directory if it doesn't exist
    if not os.path.exists(sample_directory):
        os.makedirs(sample_directory)

    for file in json_files:
        filename = os.path.basename(file)
        sample_file = os.path.join(sample_directory, filename)
        line_count = num_lines(file)
        sample_lines = random.sample(range(0, line_count), line_count // 100)
        with (
            open(file, "r", encoding="utf-8") as input_file,
            open(sample_file, "a", encoding="utf-8") as output_file,
        ):
            for index, line in enumerate(input_file.readlines()):
                if index in sample_lines:
                    output_file.write(line)

if __name__ == "__main__":
    main()
