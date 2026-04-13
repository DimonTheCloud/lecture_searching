from pathlib import Path
import json


def read_data(file_name, field):
    with open(file_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    allowed_fields = {"unordered_numbers", "ordered_numbers", "dna_sequence"}

    if field not in allowed_fields:
        return None

    return data[field]


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == "__main__":
    main()
