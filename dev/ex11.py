print("What year were you born?", end=' ')
birth_year = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

age = 2022 - int(birth_year)

print(f"So, you are {age} years old, {height} tall and {weight} heavy.")
