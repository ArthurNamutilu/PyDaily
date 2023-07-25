#!/usr/bin/python3
members = {
	"Arthur": "Present",
	"Erickson": "Absent",
	"Gg": "Present",
	"Fred": "Absent",
	"Programmer": "Present",
}

active_members = {}
for user, status in members.copy().items():
    if status == 'Absent':
        del members[user]
    if user in members:
        active_members[user] = status

print(active_members)
