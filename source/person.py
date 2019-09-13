

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

    def set_preference(self, fav_id):
        self.fav_drink_id = fav_id

    def set_recent_order(self, drink_id):
        self.recent_drink_id = drink_id

    def errors(self, error_code):
        self.error_present = True
        if error_code == 1:  # bad name
            print("Empty name dummy. ")
        if error_code == 2:  # bad id
            print("ID must be greater than 0. ")
