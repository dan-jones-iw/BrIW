from source.files import File
from source.person import Person
from source.drinks import Drink


class ItemList:
    list = []

    def __init__(self, object_type=None, item_list=None):
        self.clear_list()
        if object_type:
            self.load_from_file(object_type)
        else:
            self.list = item_list

    def clear_list(self):
        self.list.clear()

    def append_item(self, item):
        self.list.append(item)

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

    def load_from_file(self, object_type):
        file = File()
        if object_type == "person":
            list_of_people = file.get_people()
            for elm in list_of_people:
                if elm != "":
                    split_line = elm.split(",")
                    new_person = Person(split_line[1], int(split_line[2]))
                    if len(split_line) > 2:
                        new_person.set_preference(int(split_line[2]))
                        if len(split_line) > 3:
                            new_person.set_recent_order(int(split_line[3]))
                    self.list.append(new_person)
        elif object_type == "drink":
            list_of_drinks = file.get_drinks()
            for elm in list_of_drinks:
                if elm != "":
                    split_line = elm.split(",")
                    new_drink = Drink(split_line[1], int(split_line[2]))
                    if len(split_line) > 2:
                        new_drink.set_temp(int(split_line[2]))
                    self.list.append(new_drink)
        elif object_type == "fav":
            fav_list = file.get_favourites()
            for elm in fav_list:
                if elm != "":
                    pass
