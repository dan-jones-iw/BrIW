import os


class Strings:
    menu_option_list = ["List of people", "List of drinks", "Show preferences", "Create Round", "Help", "Exit"]
    welcome_message = ""

    def __init__(self):
        pass

    def main_menu(self):
        os.system('clear')
        print(self.welcome_message)  # print the welcome message
        num = input("Please enter a number. ")  # request user input
        # num = num_check(num)  # check valid number
        return num

    def create_welcome_message(self):
        welcome_message = "Welcome to BrUH v0.4 - class release! \nPlease select from the following options: "

        i = 0
        while i < len(self.menu_option_list):
            self.welcome_message += f"\n    [{i + 1}] {self.menu_option_list[i]}"
            i += 1
