import os


class Strings:
    menu_option_list = ["List of people", "List of drinks", "Show preferences", "Create Round", "Help", "Exit"]
    welcome_message = ""

    def __init__(self):
        self.create_welcome_message()

    def main_menu(self):
        os.system('clear')
        print(self.welcome_message)  # print the welcome message
        num = input("Please enter a number. ")  # request user input
        # num = num_check(num)  # check valid number
        return int(num)

    def create_welcome_message(self):
        welcome_message = "Welcome to BrUH v0.4 - class release! \nPlease select from the following options: "

        i = 0
        while i < len(self.menu_option_list):
            welcome_message += f"\n    [{i + 1}] {self.menu_option_list[i]}"
            i += 1
        self.welcome_message = welcome_message

    # need convert list of strings into nice table
    # takes a list of titles and a list of lists of body texts and creates a table string
    # I'M SORRY ABOUT THIS CODE IT WORKS SO DON'T QUESTION IT
    def create_table(self, title_text_list, body_texts_list):
        table_string = ""
        os.system('clear')

        # ensure lists are same length
        if len(title_text_list) != len(body_texts_list):
            print("Screwed up. ")
            return

        # ensure other lists are same length
        for item in body_texts_list:
            if len(item) != len(body_texts_list[0]):
                print("You're dumb. ")
                return

        # find longest line for each list of body texts
        lengths = []  # this holds the longest lengths of strings per column text
        iterator = 0
        for item in body_texts_list:
            lengths.append(self.find_longest_line(item))
            if len(title_text_list[iterator]) > lengths[iterator]:
                lengths[iterator] = len(title_text_list[iterator])
            iterator += 1

        # sort barrier stuff
        barrier = "+"
        for i in range(0, len(title_text_list)):
            barrier += "-"*(lengths[i]+2) + "+"

        # sort out title section
        title_str = "| "
        for i in range(0,len(title_text_list)):
            number_of_spaces = lengths[i] - len(title_text_list[i])
            title_str += title_text_list[i] + " "*number_of_spaces + " | "
        table_string += barrier + "\n"
        table_string += title_str + "\n"
        table_string += barrier + "\n"
        for i in range(0, len(body_texts_list[0])):
            row_str = "| "
            for j in range(0, len(body_texts_list)):
                number_of_spaces = lengths[j] - len(str(body_texts_list[j][i]))
                row_str += str(body_texts_list[j][i]) + " "*number_of_spaces + " | "
            table_string += row_str + "\n"
        table_string += barrier + "\n"

        print(table_string)
        return table_string

    def find_longest_line(self, data):
        length = 0
        for item in data:
            if len(str(item)) > length:
                length = len(str(item))
        return length

