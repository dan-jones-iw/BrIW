from source.strings import Strings
from source.files import File
from source.person import Person
from source.itemlist import ItemList
string = Strings()
file = File()

# MAIN BODY OF PROGRAM
# execute main loop
while True:
    num_selection = string.main_menu()  # print main menu screen and get user selection
    if num_selection == 1:  # list of people
        while True:  # run until user decides against it
            people_list = ItemList("person")  # get the list of people
            string.create_table(["id", "PEOPLE"], [people_list.get_id_list(), people_list.get_name_list()])  # show table to user
            input("")
    #         choice = choose("people")  # ask if user wants to amend the list
    #         if choice in yes:
    #             amend_people()  # amend people on file
    #         elif choice == "rm":  # cheeky remove person
    #             remove_person()
    #         else:
    #             break
    #     return_to_menu()
    elif num_selection == 2:  # list of drinks
        while True:  # run until user stops
            drinks_list = ItemList("drinks")  # get the drinks dictionary
            string.create_table(["id", "DRINKS"], [drinks_list.get_id_list(), drinks_list.get_name_list()])  # show table to user
            input("")
    #         choice = choose("drinks")  # ask user if they want to amend
    #         if choice in yes:
    #             amend_drinks()  # add to file
    #         elif choice == "rm":
    #             remove_drink()
    #         else:
    #             break
    #     return_to_menu()
    elif num_selection == 3:  # update preferences
        while True:  # run until user stops
            fav_list = ItemList("fav")  # update pref dictionary
            print_preferences()  # print preferences
    #         choice = choose("preferences")  # ask user if they want to amend
    #         if choice in yes:
    #             pref_amend()  # add to file
    #         else:
    #             break
    #     return_to_menu()
    # elif num_selection == 4:  # orders
    #     while True:
    #         order = Round()
    #         order.print_current_order()
    #         choice = choose("orders")
    #         if choice in yes:
    #             order.add_to_order()
    #         else:
    #             break
    #     return_to_menu()
    # elif num_selection == 5:  # help menu
    #     help_menu()
    #     return_to_menu()
    elif num_selection == 6:  # exit
        exit()
    else:
        print("You shouldn't really see this tbh. ")
