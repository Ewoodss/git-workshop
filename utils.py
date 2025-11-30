def load_people() -> list[dict]:
    import json
    with open("people.json", "r") as f:
        names = json.load(f)
    return names["people"]


def print_name(first_name, last_name):
    print(f"{first_name} {last_name}")