from utils import print_name_random_style,load_people


if __name__ == "__main__":
    people = load_people()
    
    for person in people:
        print_name_random_style(person["first_name"], person["last_name"])