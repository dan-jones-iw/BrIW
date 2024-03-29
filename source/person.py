from source.item import *
# TODO  refactor so that Person and Drink are subclasses of ITEM
#       item contains _name and _id values
#       it has get_name, get_id and rename methods


class Person(Item):
    fav_drink_id = None
    recent_drink_id = None

    def set_preference(self, fav_id):
        self.fav_drink_id = fav_id

    def set_recent_order(self, drink_id):
        self.recent_drink_id = drink_id

    def to_string(self):
        string = f"""Name - {self.name}
Drink Preference - {self.fav_drink_id} 
Recent Drink - {self.recent_drink_id}"""
        return string

#
# class PeopleList(ItemList):
#     list = []
#
#     def __init__(self, from_file, people_list=None):
#         super().__init__()
#         if from_file:
#             self.load_from_file()
#         else:
#             self.list = people_list
#
#     def load_from_file(self):
#         file = File()
#         list_of_people = file.get_people()
#         for elm in list_of_people:
#             if elm != "":
#                 split_line = elm.split(",")
#                 new_person = Person(split_line[0], int(split_line[1]))
#                 if len(split_line) > 2:
#                     new_person.set_preference(int(split_line[2]))
#                     if len(split_line) > 3:
#                         new_person.set_recent_order(int(split_line[3]))
#                 self.list.append(new_person)
