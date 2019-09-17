from files import File


class Person:
    name = ""
    id = None
    fav_drink_id = None
    recent_drink_id = None
    error_present = False

    def __init__(self, name, id_num):
        if name == "":
            self.errors(1)
        else:
            self.name = name
        if id_num < 0:
            self.errors(2)
        else:
            self.id = id_num

    def rename(self, new_name):
        if new_name == "":
            print("Empty name dummy. ")
            return False
        else:
            self.name = new_name
            return True

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def set_preference(self, fav_id):
        self.fav_drink_id = fav_id

    def set_recent_order(self, drink_id):
        self.recent_drink_id = drink_id

    # how to present errors
    def errors(self, error_code):
        self.error_present = True
        if error_code == 1:  # bad name
            print("Empty name dummy. ")
        if error_code == 2:  # bad id
            print("ID must be greater than 0. ")

    def to_string(self):
        string = f"""Name - {self.name}
Drink Preference - {self.fav_drink_id} 
Recent Drink - {self.recent_drink_id}"""
        return string


class PeopleList:
    list = []

    def __init__(self, from_file, people_list=None):
        if from_file:
            self.load_from_file()
        else:
            self.list = people_list

    def append_person(self, person):
        self.list.append(person)

    def get_name_list(self):
        string_list = []
        for elm in self.list:
            string_list.append(elm.get_name())
        return string_list

    def get_id_list(self):
        id_list = []
        for elm in self.list:
            id_list.append(elm.get_id())
        return id_list

    def load_from_file(self):
        file = File()
        list_of_people = file.get_people()
        for elm in list_of_people:
            if elm != "":
                split_line = elm.split(",")
                new_person = Person(split_line[0], split_line[1])
                if len(split_line) > 2:
                    new_person.set_preference(split_line[2])
                    if len(split_line) > 3:
                        new_person.set_recent_order(split_line[3])
            self.list += new_person
