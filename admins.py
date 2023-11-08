from users import User
class Admin(User):
    def __init__(self, name, surname, pesel):
        super().__init__(name, surname, pesel)

