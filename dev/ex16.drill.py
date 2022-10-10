from sys import argv

script, filename = argv

print("We are going to display {filename}.")
print("Opening the file...")

target = open(filename, 'r+')

print(target.read())

target.close()
