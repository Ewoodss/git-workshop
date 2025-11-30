from utils import print_name,load_people


if __name__ == "__main__":
    people = load_people()
    
    for person in people:
        print_name(person["first_name"], person["last_name"])