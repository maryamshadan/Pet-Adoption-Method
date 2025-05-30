"""
# -*- coding: utf-8 -*-
Pet Adoption Method

Original file is located at
    https://colab.research.google.com/drive/1WpuAWzj65mCZEbYMfeP1ecQqaISthvPa
"""

import random

# Parent class
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}")

# Child class for Dogs
class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color
        self.preferences = ("Bones", "Walk")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}")
        print(f"Preferences: {self.preferences}")

# Child class for Cats
class Cat(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.color = color
        self.preferences = ("Fish", "Nap")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.color}")
        print(f"Preferences: {self.preferences}")

# Dictionary to store pets
pet_store = {}

# Generate unique pet ID
def generate_pet_id():
    while True:
        pet_id = random.randint(1000, 9999)
        if pet_id not in pet_store:
            return pet_id

# Add a pet
def add_pet():
    species = input("Enter species (Dog/Cat): ").capitalize()
    name = input("Enter pet name: ")
    age = int(input("Enter pet age: "))
    breed = input("Enter breed: ")
    color = input("Enter color: ")

    if species == "Dog":
        pet = Dog(name, age, breed, color)
    elif species == "Cat":
        pet = Cat(name, age, breed, color)
    else:
        print("\nUnsupported species.")
        return

    pet_id = generate_pet_id()
    pet_store[pet_id] = pet
    print(f"{species} added with ID: {pet_id}")

# View all pets
def view_pets():
    if not pet_store:
        print("\n\nNo pets available.")
        return
    for pet_id, pet in pet_store.items():
        print(f"\nPet ID: {pet_id}")
        pet.display_info()

# Adopt a pet
def adopt_pet():
    pet_id = int(input("\nEnter the Pet ID to adopt: "))
    if pet_id in pet_store:
        print("\nYou have adopted the following pet:")
        pet_store[pet_id].display_info()
        del pet_store[pet_id]
    else:
        print("Invalid Pet ID.")

# Main menu
def main():
    while True:
        print("\n--- Pet Adoption Menu ---")
        print("1. View Pets")
        print("2. Add Pet")
        print("3. Adopt Pet")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_pets()
        elif choice == '2':
            add_pet()
        elif choice == '3':
            adopt_pet()
        elif choice == '4':
            print("Exiting Pet Adoption System. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()

git remote add origin https://github.com/maryamshadan/Pet-Adoption-Method.git

