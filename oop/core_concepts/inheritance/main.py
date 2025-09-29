class Employee:
    def __init__(self, f_name = "", l_name = "", salary = 0):
        self.first_name = f_name
        self.second_name = l_name
        self.salary = salary

class Programmer (Employee):
    def __init__(self, f_name="", l_name="", salary= 0, programming_lang = ""):
        super().__init__(f_name, l_name, salary)

        self.p_language = programming_lang

    def display_programmer (self):
        print (self.first_name)
        print (self.second_name)
        print (self.salary)
        print (self.p_language)




person = Programmer ("Ahmed", "Mohamed", 50000, "Python")

person.display_programmer ()

print ("-----------------------")

person.first_name = "Rab3ko"

person.display_programmer ()