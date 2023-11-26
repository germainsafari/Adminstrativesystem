from users import User
class Nurse(User):
    def __init__(self, name, surname, pesel):
        super().__init__(name, surname, pesel)

    def add_patient(self, patient):
        self.patients.append(patient)
