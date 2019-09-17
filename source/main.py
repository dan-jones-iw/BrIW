from strings import Strings
from files import File
from person import Person, PeopleList
string = Strings()
file = File()

print("Initialise list with Dan and Greg: ")
dan = Person("Dan", 1)
greg = Person("Greg", 2)
list_of_people = [dan, greg]
people_list = PeopleList(False, list_of_people)
print(people_list.get_name_list())

print("Adding Giles: ")
giles = Person("Giles", 3)
people_list.append_person(giles)
print(people_list.get_name_list())

print("Renaming Giles to Adam: ")
giles.rename("Adam")
print(people_list.get_name_list())

print("Acquire Adam info: ")
print(people_list.list[2].to_string())

string.create_table("People", people_list.get_name_list())

# MAIN BODY OF PROGRAM
# execute main loop
# while True:
#     num_selection = string.main_menu()  # print main menu screen and get user selection
#     if num_selection == 1:  # list of people
#         while True:  # run until user decides against it
#             people_list = PeopleList(True)  # get the list of people
#             make_table("people", people_dict)  # show table to user
#             choice = choose("people")  # ask if user wants to amend the list
#             if choice in yes:
#                 amend_people()  # amend people on file
#             elif choice == "rm":  # cheeky remove person
#                 remove_person()
#             else:
#                 break
#         return_to_menu()
#     elif num_selection == 2:  # list of drinks
#         while True:  # run until user stops
#             drinks_dict = get_drinks()  # get the drinks dictionary
#             make_table("drinks", drinks_dict)  # show table to user
#             choice = choose("drinks")  # ask user if they want to amend
#             if choice in yes:
#                 amend_drinks()  # add to file
#             elif choice == "rm":
#                 remove_drink()
#             else:
#                 break
#         return_to_menu()
#     elif num_selection == 3:  # update preferences
#         while True:  # run until user stops
#             id_dict = get_id()  # update pref dictionary
#             print_preferences()  # print preferences
#             choice = choose("preferences")  # ask user if they want to amend
#             if choice in yes:
#                 pref_amend()  # add to file
#             else:
#                 break
#         return_to_menu()
#     elif num_selection == 4:  # orders
#         while True:
#             order = Round()
#             order.print_current_order()
#             choice = choose("orders")
#             if choice in yes:
#                 order.add_to_order()
#             else:
#                 break
#         return_to_menu()
#     elif num_selection == 5:  # help menu
#         help_menu()
#         return_to_menu()
#     elif num_selection == 6:  # exit
#         exit()
#     else:
#         print("You shouldn't really see this tbh. ")
