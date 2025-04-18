class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):  # Getter
        return self.__name

    @name.setter
    def name(self, value):  # Setter
        if value != "":
            self.__name = value

p = Person("Alex")
print(p.name)     # ✅ Uses getter
p.name = "Jordan" # ✅ Uses setter
print(p.name)     # Output: Jordan
