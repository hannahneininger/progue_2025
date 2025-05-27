import json

# Paket zum anzeigen der Bilder
from PIL import Image

def get_person_data():
    """
    Returns the person data loaded from the JSON file.
    """
    # Opening JSON file
    file = open("data/person_db.json")

    # Loading the JSON File in a dictionary
    person_data = json.load(file)

    return person_data

def get_person_names():
    """
    Returns a list of person names from the loaded person data.
    """
    person_names = []

    
    # gib mir die lsite mit allen Personen
    persons_dicts = get_person_data()
    #gehe durch die liste durch von den Personen
    for person_dict in persons_dicts:
            # jeder Einttrag ist ein dict mit dne felern (firstname und lastname)
            person_dict["firstname"]
            person_names.append(f"{person_dict['lastname']}, {person_dict['firstname']}")
    
    return person_names
            # hänge das an die namensliste an



def get_person_data_by_name(personname):
    all_persons = get_person_data()
    firstname = personname.split(", ")[1]
    lastname = personname.split(", ")[0]
    

    for person_dict in all_persons:
        if person_dict["firstname"] == firstname and person_dict["lastname"] == lastname:
            return person_dict



def get_person_image_by_name(personname):
     # Laden eines Bilds
    image = Image.open(get_person_data_by_name(personname)["picture_path"])
    
    return image





if __name__ == "__main__":
    # Example usage
    person_data = get_person_data()
    print(person_data)

    person_names = get_person_names()
    print(person_names)

    person_name = "Huber, Julian"
    person_dict = get_person_data_by_name(person_name)
    print(person_dict)





