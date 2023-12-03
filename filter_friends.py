"""
This file is used to create a filtered dataset of users who have friends.
"""

# Run this script to create the filtered friends dataset.
# Delete the "yelp_academic_dataset_user_friends.json" file before running this
#   script (if it exists),

import json


def main() -> None:
    """Main function to create the filtered friends dataset."""

    with (
        open(
            "data/yelp_academic_dataset_user.json", "r", encoding="utf-8"
        ) as input_file,
        open(
            "data/yelp_academic_dataset_user_friends.json", "a", encoding="utf-8"
        ) as output,
    ):
        for line in input_file.readlines():
            row = json.loads(line)
            if row["friends"] != "None":
                output.write(line)


if __name__ == "__main__":
    main()
