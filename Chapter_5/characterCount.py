#! /usr/bin/python3

massage = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Veniam, asperiores sunt debitis molestias neque magni ad praesentium incidunt voluptate qui aut, expedita voluptates sit perspiciatis, amet illum impedit nesciunt beatae?'
count = {}

for character in massage:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

input()
