import csv
import json

with open('usernames.txt', 'r') as csvfile:
    usernames = csvfile.readlines()
    usernames = [name.strip() for name in usernames]

print(len(usernames))
usernames = set(usernames)
print(len(usernames))

'''
with open('usernames2.txt', 'r') as csvfile:
    usernames2 = csvfile.readlines()
    usernames2 = [name.strip() for name in usernames]
    usernames2 = set(usernames2)

usernames = usernames | usernames2
print(len(usernames))
'''
people = {}
for username in usernames:
    people[username] = {}

with open('users_data.json', 'w') as outfile:
    json.dump(people, outfile)