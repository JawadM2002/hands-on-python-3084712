NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name) # prints the names on the lists

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}") # prints name and age

for name in reversed(NAMES):
    print(name) # prints list in reverse

for i in range(5):
    print(i) # prints numbers from range

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}") # enumerates the names in order from 0, has iteration with index