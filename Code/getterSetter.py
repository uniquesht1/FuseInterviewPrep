class Person:
    def __init__(self, name):
        self.__name = name  # private

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self, new_name):
        if new_name != "":
            self.__name = new_name

p = Person("Alex")
print(p.get_name())   # ✅ Output: Alex
p.set_name("Jordan")  # ✅ Updating the name
print(p.get_name())   # ✅ Output: Jordan
