from random import Random
rnd = Random()

def load_people() -> list[dict]:
    import json
    with open("people.json", "r") as f:
        names = json.load(f)
    return names["people"]

def randomize_list(list: list) -> list:
    rnd.shuffle(list)
    return list

def print_name(first_name, last_name):
    print(f"{first_name} {last_name}")

def print_name_reversed(first_name, last_name):
    first_name_rev = first_name[::-1]
    last_name_rev = last_name[::-1]
    print(f"{last_name_rev} {first_name_rev}")

def print_name_uppercase(first_name, last_name):
    print(f"{first_name.upper()} {last_name.upper()}")

def print_name_shuffle_letters(first_name, last_name):
    first_name_shuffled = "".join(rnd.sample(first_name, len(first_name)))
    last_name_shuffled = "".join(rnd.sample(last_name, len(last_name)))
    print(f"{first_name_shuffled} {last_name_shuffled}")

def print_name_colored(first_name, last_name):
    print(f"\033[91m{first_name}\03 \033[94m{last_name}\033[0m")

def get_random_color():
    return rnd.choice(["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"])

def print_name_rnd_color(first_name, last_name):
    first_name_color = get_random_color()
    last_name_color = get_random_color()
    print(f"{first_name_color}{first_name}\033[0m {last_name_color}{last_name}\033[0m")  # Reset color after print
    
    


print_styles = [print_name, print_name_reversed, print_name_uppercase,print_name_shuffle_letters,print_name_colored,print_name_rnd_color]

def print_name_random_style(first_name, last_name):
    rnd.choice(print_styles)(first_name, last_name)