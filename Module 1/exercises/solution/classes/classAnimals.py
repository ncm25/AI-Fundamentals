import numpy as np

class Animals:
    def __init__(self, name, age, gender, color, species):
        self.name = name
        self.age = age
        self.gender = gender
        self.color = color
        self.species = species
        self.weight_kg = None  # Add weight attribute (default None)

    def set_weight_from_pounds(self, pounds):
        """Sets the weight in kilograms, given the weight in pounds."""
        self.weight_kg = pounds * 0.453592
        return self.weight_kg

    def get_weight_kg(self):
        """Returns the animal's weight in kilograms."""
        return self.weight_kg

    # (The rest of your methods remain unchanged)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_color(self):
        return self.color

    def get_species(self):
        return self.species

    def update_info(self, name=None, age=None, gender=None, color=None, species=None):
        if name: self.name = name
        if age: self.age = age
        if gender: self.gender = gender
        if color: self.color = color
        if species: self.species = species

    def is_adult(self):
        return self.age >= 3

    def make_sound(self):
        return "Some generic animal sound."

    def get_info(self):
        info = (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Color: {self.color}\n"
            f"Species: {self.species}"
        )
        if self.weight_kg is not None:
            info += f"\nWeight: {self.weight_kg:.2f} kg"
        return info
