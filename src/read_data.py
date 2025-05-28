import json
from PIL import Image
#open json file
file= open('data/person_db.json')

#loading json file in a dict
person_data= json.load(file)

#print(person_data)

def get_person_data():
    file= open('data/person_db.json')
    #loading json file in a dict
    person_data= json.load(file)

    return person_data


def get_person_names():
    names_list= []
    #gib mir eine Liste mit allen Persons
    person_dict= get_person_data()

    #geh durch Liste
    for person_dict in person_dict:
    #jeder Eintrag ist ein dict mit den Feldern 'fristname' und 'lastname'
        #person_dict['firstname']
    # hänge Namen an die Liste an
        names_list.append(person_dict['firstname'] + " " + person_dict['lastname'])
    print(names_list)
    return names_list

def get_person_data_by_name(personname):
    all_persons= get_person_data()
    firstname= personname.split(" ")[0]
    lastname= personname.split(' ')[1]

    for person_dict in all_persons:
        if person_dict['firstname']== firstname and person_dict['lastname'] == lastname:
            return person_dict

def get_image_by_name(personname):
    person_dict = get_person_data_by_name(personname)
    path = person_dict["picture_path"]
    image= Image.open(path)
    return image


if __name__ == "__name__":
    person_data= get_person_data()
    #print(person_data)
    print(names_list)

person_names= get_person_names()