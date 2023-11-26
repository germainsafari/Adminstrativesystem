from users import User

class Doctor(User):
    def __init__(self, speciality, pwz, name, surname, pesel):
        super().__init__(name, surname, pesel)
        self.speciality = speciality
        self.pwz = pwz
        self.duties = []
    def add_duty(self, date):
        self.duties.append(date)



class Cardiologist(Doctor):
    def __init__(self, speciality, pwz, name, surname, pesel):
        super().__init__(speciality, pwz, name, surname, pesel)
class Urologist:
    def __init__(self):
        pass
class Neurologist:
    def __init__(self):
        pass
class Laryngologist:
    def __init__(self):
        pass
