"""
A Python script that has a list of student names and selects two random names and prints them.
Example: It should print Bob => John.
The names must be hardcoded into the 'names' list
"""

import random

names = ['JP', 'Admas', 'Embelle', 'Dilu', 'Andy', 'Denika', 'Abubakar', 'Jeniffer', 'Victoriya', 'Maryana']

name_choice = random.sample(names, 2)
print(f"{name_choice[0]} => {name_choice[1]}")
