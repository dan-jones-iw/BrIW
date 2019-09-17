import os


class Strings:
    menu_option_list = ["List of people", "List of drinks", "Show preferences", "Create Round", "Help", "Exit"]
    welcome_message = ""
    barrier = "+" + "= " * 12

    def __init__(self):
        self.create_welcome_message()

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
            welcome_message += f"\n    [{i + 1}] {self.menu_option_list[i]}"
            i += 1
        self.welcome_message = welcome_message

    # need convert list of people strings into nice table
    def create_table(self, title_text, body_text_list):
        os.system('clear')
        print(f"{self.barrier}")
        print(f"| {title_text.title()}")
        print(f"{self.barrier}")
        for item in body_text_list:
            print(f"| {item} ")
        print(f"{self.barrier}")
