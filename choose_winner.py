import csv
import random

with open('discord_members.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    entries = list(reader)

if entries:
    winner = random.choice(entries)
    print("The winner is:", winner["Discord Name"])
else:
    print("Did not find any entries in the CSV file.")
