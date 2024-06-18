NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23] # lists

JOHN = NAMES[0]
PAUL = NAMES[1]

JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES)) # total sum of ages
print(min(AGES)) # youngest
print(max(AGES)) # oldest

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
