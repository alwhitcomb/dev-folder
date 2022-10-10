from sys import argv

script, user_name, user_last_name = argv
Q = '> '

print(f"Hi {user_name} {user_last_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name} {user_last_name}?")
likes = input(Q)

print(f"Where do you live, {user_name} {user_last_name}?")
lives = input(Q)

print("What kind of computer do you have?")
computer = input(Q)

print(f"""
Alright, so you have said you {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
