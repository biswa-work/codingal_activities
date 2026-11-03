class FamilyMember:
    def __init__(self, name, family_trait):
        self.name = name
        self.family_trait = family_trait

    def show_traits(self):
        print(f"{self.name} shares the family trait: {self.family_trait}")


class Child(FamilyMember):
    def __init__(self, name, family_trait, personal_trait):
        super().__init__(name, family_trait)
        self.personal_trait = personal_trait

    def show_traits(self):
        print(f"{self.name} shares the family trait: {self.family_trait}")
        print(f"{self.name}'s personal trait: {self.personal_trait}")


member = Child("Riya", "Kindness", "Curiosity")
member.show_traits()
print("Is Child a subclass of FamilyMember?", issubclass(Child, FamilyMember))
