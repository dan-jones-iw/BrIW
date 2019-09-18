from source.item import *


class Drink(Item):
    temperature = ""

    def set_temp(self, new_temp):
        self.temperature = new_temp

    def get_temp(self):
        return self.temperature

# class DrinkList(ItemList):
#     list = []
#
#     def __init__(self, from_file, drink_list=None):
#         super().__init__()
#         if from_file:
#             self.load_from_file()
#         else:
#             self.list = drink_list
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
